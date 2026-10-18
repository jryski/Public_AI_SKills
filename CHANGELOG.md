# Changelog

## Unreleased

- Added `scripts/check_repository.py` (structural, link, license and packaging checks), `scripts/package_skill.py` (portable skill packages that keep `LICENSE`, `COPYRIGHT`, `USAGE-GATE.md` and an `ATTRIBUTION.md`), their tests and a checks workflow. These are structural checks, not a model-effectiveness qualification.
- Fixed the `PROGRAM-ROLE.md` link to the removed `LICENSE.md`, pointed program context at the program map, and replaced its obsolete business-use restriction with the CC BY 4.0 terms.
- Added the CC BY 4.0 legal-code link (https://creativecommons.org/licenses/by/4.0/legalcode) to the usage gate, manifest, skill spec and package `ATTRIBUTION.md`; the checker now requires it in packages.
- Added `CURRENT-STATUS.md` (rebuilt from the earlier status draft) and removed wording that implied skills work equally across models.
- Added `SECURITY.md` (this repository's private reporting form, email fallback) and a README orientation table.

## 2026-09-08

- Relicensed the repository from the Xillennial Personal Use License 1.0 to Creative Commons Attribution 4.0 International. All organizational, commercial, and professional restrictions are withdrawn.
- Copyright notice added.
- Replaced `LICENSE.md` with `LICENSE` so GitHub detects the license.
- Rewrote `USAGE-GATE.md` as a permissive machine-readable declaration.
- Removed `COMMERCIAL-LICENSING.md`; there is no commercial licensing route.
- Replaced the inbound contributor grant in `CONTRIBUTING.md` with the Developer Certificate of Origin; added `DCO.md`.
- Updated `skills/manifest.yaml` and `docs/SKILL-SPEC.md` license fields to match.

## 2026-07-06

### Added

- Added `LICENSE.md` with the Xillennial Personal Use License 1.0.
- Added `USAGE-GATE.md` with an AI-readable personal-use and organizational-license gate.
- Added README licensing banner and Wirespeed Computing licensing pointer.
- Added `CONTRIBUTING.md` with inbound contribution terms.

## 2026-07-05

### Added

- Initialized the Xillennial skill series.
- Added `skills/xillennial/SKILL.md` v1 as the parent skill for cross-domain systems reasoning, tool acquisition, representation switching, validation, and teaching.
- Added `skills/figure-it-out/SKILL.md` v3 as the troubleshooting specialization for broken, stuck, inconsistent, or poorly understood systems.
- Added initial repository README.

## Versioning notes

Skill versions are semantic at the skill level, not necessarily repository-wide.

- Patch changes clarify wording without changing behavior.
- Minor changes add sections, examples, metadata, or operational guidance.
- Major changes alter invocation rules, safety boundaries, or required behavior.
