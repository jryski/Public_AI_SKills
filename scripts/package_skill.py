#!/usr/bin/env python3
# SPDX-License-Identifier: CC-BY-4.0
"""Build a portable package for one skill, with its license and notices.

The package is a deterministic zip containing:

  <name>/SKILL.md        the skill, unchanged
  <name>/LICENSE         the full CC BY 4.0 text
  <name>/COPYRIGHT       the copyright and license notice
  <name>/USAGE-GATE.md   the machine-readable terms
  <name>/ATTRIBUTION.md  source, version, commit and license, for re-sharing

CC BY 4.0 lets anyone use, adapt and share the skill, including commercially,
when shared copies keep the supplied attribution and notices, link the license
and indicate changes. Packaging the notices with the skill is how a copy that
travels without this repository keeps them.

Usage: python scripts/package_skill.py <skill-name> [--out DIR] [--commit SHA]
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_URL = "https://github.com/jryski/Public_AI_SKills"
LICENSE_URL = "https://creativecommons.org/licenses/by/4.0/"
LEGALCODE_URL = "https://creativecommons.org/licenses/by/4.0/legalcode"
NOTICE_FILES = ("LICENSE", "COPYRIGHT", "USAGE-GATE.md")
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def manifest_skills(root: Path = ROOT) -> dict[str, dict[str, str]]:
    """Parse the skills list of skills/manifest.yaml (a small, fixed subset of YAML)."""
    skills: dict[str, dict[str, str]] = {}
    current: dict[str, str] | None = None
    in_skills = False
    for line in (root / "skills/manifest.yaml").read_text(encoding="utf-8").splitlines():
        if re.match(r"^skills:\s*$", line):
            in_skills = True
            continue
        if in_skills and re.match(r"^\S", line):
            in_skills = False
        if not in_skills:
            continue
        item = re.match(r"^  - name:\s*(\S+)\s*$", line)
        if item:
            current = {"name": item.group(1)}
            skills[current["name"]] = current
            continue
        field = re.match(r"^    (version|path|role|parent|series):\s*(\S+)\s*$", line)
        if field and current is not None:
            current[field.group(1)] = field.group(2)
    return skills


def head_commit(root: Path = ROOT) -> str:
    try:
        result = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True,
                                text=True, check=True)
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def attribution(name: str, version: str, path: str, commit: str) -> str:
    return f"""# Attribution

- Work: `{name}` skill, version {version}
- Source: {REPOSITORY_URL}/blob/{commit}/{path}
- Authors: The Sovereign AI OS Authors (see COPYRIGHT)
- License: Creative Commons Attribution 4.0 International (CC BY 4.0), {LICENSE_URL} (legal code: {LEGALCODE_URL})
- Changes: none. This package contains the file unchanged from the source commit above.

Personal, organizational and commercial use are permitted. If you share this
skill or an adaptation, keep this file, COPYRIGHT and LICENSE (or a link to the
license), credit the authors, and state your changes. Do not imply endorsement.
"""


def build(name: str, out: Path, commit: str | None = None, root: Path = ROOT) -> Path:
    skills = manifest_skills(root)
    if name not in skills:
        raise SystemExit(f"unknown skill: {name}")
    entry = skills[name]
    skill_path = root / entry["path"]
    for notice in NOTICE_FILES:
        if not (root / notice).is_file():
            raise SystemExit(f"missing notice file: {notice}")
    commit = commit or head_commit(root)
    out.mkdir(parents=True, exist_ok=True)
    target = out / f"{name}-v{entry['version']}.zip"
    members = [(f"{name}/SKILL.md", skill_path.read_bytes())]
    members += [(f"{name}/{notice}", (root / notice).read_bytes()) for notice in NOTICE_FILES]
    members.append((f"{name}/ATTRIBUTION.md",
                    attribution(name, entry["version"], entry["path"], commit).encode("utf-8")))
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for member, data in members:
            info = zipfile.ZipInfo(member, date_time=FIXED_TIME)
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data)
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("skill")
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    parser.add_argument("--commit")
    args = parser.parse_args(argv)
    print(build(args.skill, args.out, args.commit))
    return 0


if __name__ == "__main__":
    sys.exit(main())
