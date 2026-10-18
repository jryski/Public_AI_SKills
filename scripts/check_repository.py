#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Structural, link and license checks for Public AI Skills.

These checks prove that the published files are consistent and reachable:
the manifest resolves, each skill's front matter matches it, every relative
Markdown link and in-repository anchor resolves, the license and notices say
CC BY 4.0, no current file revives the withdrawn personal-use restrictions, and
a portable package keeps its license and attribution notices.

They do NOT measure whether a skill improves any model's results. Cross-model
effectiveness has not been qualified, and passing these checks is not a claim
that it has.

Usage: python scripts/check_repository.py [--root DIR]   (exit 0 = all pass)
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import tempfile
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import package_skill  # noqa: E402

# History may describe the old terms; current files must not reintroduce them.
HISTORY_FILES = {"CHANGELOG.md"}
WITHDRAWN = [
    re.compile(r"Personal Use License", re.I),
    re.compile(r"license[-_ ]required", re.I),
    re.compile(r"COMMERCIAL-LICENSING", re.I),
    re.compile(r"\bnot authorized\b", re.I),
    re.compile(r"organizational(?: and|,)? (?:or )?commercial use (?:is|are|remains?) (?:subject|restricted|not)", re.I),
    re.compile(r"stop_and_direct_to_licensing", re.I),
    re.compile(r"\]\(LICENSE\.md\)"),
    re.compile(r"subject to this repository's explicit usage gate", re.I),
]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP_SCHEMES = ("http://", "https://", "mailto:")


def slug(heading: str) -> str:
    text = re.sub(r"[`*_]", "", heading.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    found: set[str] = set()
    seen: dict[str, int] = {}
    in_code = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        match = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if match:
            base = slug(match.group(1))
            count = seen.get(base, 0)
            seen[base] = count + 1
            found.add(base if count == 0 else f"{base}-{count}")
    return found


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts and "dist" not in p.parts)


def check_links(root: Path) -> list[str]:
    errors = []
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in LINK.findall(text):
            if target.startswith(SKIP_SCHEMES):
                continue
            file_part, _, anchor = target.partition("#")
            destination = (path.parent / file_part).resolve() if file_part else path
            rel = path.relative_to(root)
            if not destination.exists():
                errors.append(f"{rel}: broken link {target}")
                continue
            if root.resolve() not in destination.parents and destination != root.resolve():
                errors.append(f"{rel}: link leaves repository {target}")
                continue
            if anchor and destination.suffix == ".md" and anchor not in anchors(destination):
                errors.append(f"{rel}: missing anchor {target}")
    return errors


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^(\w+):\s*(.*)$", line)
        if field:
            fields[field.group(1)] = field.group(2).strip()
    return fields


def check_skills(root: Path) -> list[str]:
    errors = []
    skills = package_skill.manifest_skills(root)
    if not skills:
        return ["skills/manifest.yaml: no skills listed"]
    for name, entry in skills.items():
        path = root / entry.get("path", "")
        if not entry.get("path") or not path.is_file():
            errors.append(f"manifest: {name} path does not resolve")
            continue
        fields = front_matter(path)
        if fields.get("name") != name:
            errors.append(f"{entry['path']}: front matter name {fields.get('name')!r} != manifest {name!r}")
        if fields.get("version") != entry.get("version"):
            errors.append(f"{entry['path']}: front matter version != manifest version")
        if not fields.get("description"):
            errors.append(f"{entry['path']}: missing description (trigger)")
        if not re.search(rf"^# .+\(v{re.escape(entry.get('version', ''))}\)\s*$",
                         path.read_text(encoding="utf-8"), re.M):
            errors.append(f"{entry['path']}: title does not carry (v{entry.get('version')})")
        parent = entry.get("parent")
        if parent and parent not in skills:
            errors.append(f"manifest: {name} parent {parent} is not listed")
    readme = (root / "README.md").read_text(encoding="utf-8")
    for name, entry in skills.items():
        if entry.get("path") and entry["path"] not in readme:
            errors.append(f"README.md: does not link {entry['path']}")
    return errors


def check_license(root: Path) -> list[str]:
    errors = []
    license_text = (root / "LICENSE").read_text(encoding="utf-8") if (root / "LICENSE").is_file() else ""
    if not license_text.lstrip().startswith("Attribution 4.0 International"):
        errors.append("LICENSE: not the CC BY 4.0 legal code")
    copyright_text = (root / "COPYRIGHT").read_text(encoding="utf-8") if (root / "COPYRIGHT").is_file() else ""
    if "Creative Commons Attribution 4.0" not in copyright_text:
        errors.append("COPYRIGHT: missing CC BY 4.0 notice")
    gate = (root / "USAGE-GATE.md").read_text(encoding="utf-8")
    for key in ("personal_use", "organizational_use", "commercial_use"):
        if not re.search(rf"^\s*{key}:\s*permitted\s*$", gate, re.M):
            errors.append(f"USAGE-GATE.md: {key} is not 'permitted'")
    manifest = (root / "skills/manifest.yaml").read_text(encoding="utf-8")
    if not re.search(r"^license:\s*CC-BY-4.0\s*$", manifest, re.M):
        errors.append("skills/manifest.yaml: license is not CC-BY-4.0")
    for key in ("organizational_use", "commercial_use"):
        for value in re.findall(rf"^\s*{key}:\s*(\S+)", manifest, re.M):
            if value != "permitted":
                errors.append(f"skills/manifest.yaml: {key}: {value}")
    for path in markdown_files(root) + [root / "skills/manifest.yaml"]:
        rel = str(path.relative_to(root))
        if rel in HISTORY_FILES:
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in WITHDRAWN:
            if pattern.search(text):
                errors.append(f"{rel}: withdrawn restriction language ({pattern.pattern})")
    return errors


def check_packages(root: Path) -> list[str]:
    errors = []
    with tempfile.TemporaryDirectory() as directory:
        for name in package_skill.manifest_skills(root):
            archive = package_skill.build(name, Path(directory), commit="0" * 40, root=root)
            with zipfile.ZipFile(archive) as package:
                names = set(package.namelist())
                for member in ("SKILL.md", "LICENSE", "COPYRIGHT", "USAGE-GATE.md", "ATTRIBUTION.md"):
                    if f"{name}/{member}" not in names:
                        errors.append(f"package {name}: missing {member}")
                if f"{name}/ATTRIBUTION.md" in names:
                    text = package.read(f"{name}/ATTRIBUTION.md").decode("utf-8")
                    if "CC BY 4.0" not in text or "creativecommons.org/licenses/by/4.0" not in text or "/legalcode" not in text:
                        errors.append(f"package {name}: attribution lacks license name, deed link or legal-code link")
                if f"{name}/LICENSE" in names and package.read(f"{name}/LICENSE") != (root / "LICENSE").read_bytes():
                    errors.append(f"package {name}: LICENSE differs from repository LICENSE")
    return errors


# Wording that would assert unqualified model effectiveness. History files may
# quote it; current documents and skills may not.
EFFECTIVENESS_CLAIMS = (
    "model-independent",
    "works with any model",
    "works on any model",
    "works across models",
    "works across all models",
    "useful across models",
    "proven across models",
)


def check_claims(root: Path) -> list[str]:
    errors = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel.startswith((".git/", "dist/")) or rel == "CHANGELOG.md":
            continue
        text = path.read_text(encoding="utf-8").lower()
        for phrase in EFFECTIVENESS_CLAIMS:
            if phrase in text:
                errors.append(f"{rel}: unqualified effectiveness claim '{phrase}'")
    return errors


def run(root: Path) -> list[str]:
    return check_skills(root) + check_links(root) + check_license(root) + check_packages(root) + check_claims(root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors = run(args.root.resolve())
    for error in errors:
        print("FAIL", error)
    print(f"repository checks: {'PASS' if not errors else 'FAIL'} ({len(errors)} problem(s)); "
          "structural only, not a model-effectiveness qualification")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
