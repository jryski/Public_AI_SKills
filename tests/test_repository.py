# SPDX-License-Identifier: CC-BY-4.0
"""Positive and negative controls for scripts/check_repository.py and the packager."""
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import check_repository  # noqa: E402
import package_skill  # noqa: E402


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "dist", "__pycache__"))

    def edit(self, rel, old, new):
        path = self.root / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_current_repository_passes(self):
        self.assertEqual(check_repository.run(self.root), [])

    def test_broken_link_fails(self):
        self.edit("PROGRAM-ROLE.md", "[`LICENSE`](LICENSE)", "[`LICENSE`](LICENSE.md)")
        errors = check_repository.run(self.root)
        self.assertTrue(any("broken link LICENSE.md" in e for e in errors), errors)

    def test_missing_anchor_fails(self):
        self.edit("README.md", "([series design](#series-design))", "([series design](#no-such-section))")
        self.assertTrue(any("missing anchor" in e for e in check_repository.run(self.root)))

    def test_version_mismatch_fails(self):
        self.edit("skills/figure-it-out/SKILL.md", "version: 3", "version: 4")
        self.assertTrue(any("version" in e for e in check_repository.run(self.root)))

    def test_revived_personal_use_restriction_fails(self):
        self.edit("README.md", "## Support", "## Support\n\nXillennial Personal Use License 1.0 applies.\n")
        self.assertTrue(any("withdrawn restriction" in e for e in check_repository.run(self.root)))

    def test_manifest_license_restriction_fails(self):
        self.edit("skills/manifest.yaml", "      commercial_use: permitted", "      commercial_use: license-required")
        self.assertTrue(check_repository.run(self.root))

    def test_history_may_describe_old_terms(self):
        self.assertIn("Personal Use License", (self.root / "CHANGELOG.md").read_text(encoding="utf-8"))
        self.assertEqual(check_repository.check_license(self.root), [])

    def test_package_keeps_license_and_attribution(self):
        out = Path(self.temp.name) / "dist"
        archive = package_skill.build("figure-it-out", out, commit="a" * 40, root=self.root)
        self.assertEqual(archive.name, "figure-it-out-v3.zip")
        with zipfile.ZipFile(archive) as package:
            names = set(package.namelist())
            for member in ("SKILL.md", "LICENSE", "COPYRIGHT", "USAGE-GATE.md", "ATTRIBUTION.md"):
                self.assertIn("figure-it-out/" + member, names)
            attribution = package.read("figure-it-out/ATTRIBUTION.md").decode()
            self.assertIn("/blob/" + "a" * 40 + "/skills/figure-it-out/SKILL.md", attribution)
            self.assertIn("commercial use are permitted", attribution)
            self.assertIn("https://creativecommons.org/licenses/by/4.0/legalcode", attribution)
            self.assertEqual(package.read("figure-it-out/SKILL.md"),
                             (self.root / "skills/figure-it-out/SKILL.md").read_bytes())

    def test_effectiveness_claim_fails(self):
        self.edit("README.md", "## Support", "## Support\n\nThis skill works across all models.\n")
        self.assertTrue(any("effectiveness claim" in e for e in check_repository.run(self.root)))

    def test_attribution_without_legal_code_fails(self):
        self.edit("scripts/package_skill.py", " (legal code: {LEGALCODE_URL})", "")
        import importlib.util
        spec = importlib.util.spec_from_file_location("pkg_copy", self.root / "scripts/package_skill.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        archive = module.build("xillennial", Path(self.temp.name) / "d", commit="d" * 40, root=self.root)
        with zipfile.ZipFile(archive) as package:
            self.assertNotIn("/legalcode", package.read("xillennial/ATTRIBUTION.md").decode())

    def test_package_is_deterministic(self):
        first = package_skill.build("xillennial", Path(self.temp.name) / "a", commit="b" * 40, root=self.root)
        second = package_skill.build("xillennial", Path(self.temp.name) / "b", commit="b" * 40, root=self.root)
        self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_missing_notice_fails_packaging(self):
        (self.root / "COPYRIGHT").unlink()
        with self.assertRaises(SystemExit):
            package_skill.build("xillennial", Path(self.temp.name) / "c", commit="c" * 40, root=self.root)


if __name__ == "__main__":
    unittest.main()
