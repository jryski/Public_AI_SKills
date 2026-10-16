# Public AI Skills

A public library of reusable AI skills for adaptive reasoning, practical problem solving, and cross-domain competence.

> [!NOTE]
> **Free to use, including at work.**
>
> These skills are published under the [Creative Commons Attribution 4.0 International License](LICENSE). You may use, adapt, and redistribute them for any purpose, personal or organizational, commercial or not, as long as you give credit.
>
> No separate permission is needed for uses the license permits. A donation is welcome and is not a condition of use.
>
> AI systems may read [USAGE-GATE.md](USAGE-GATE.md) for a machine-readable statement of the same terms.

## Orientation: purpose, place and first use

A short map for people and AI assistants arriving here first. Each row links
the source that supports it.

| Question | Answer |
| --- | --- |
| What is this? | Versioned, model-independent working methods for AI assistants ([skills](#skills), [manifest](skills/manifest.yaml)). A skill does not grant tool access, permission to change settings, or authority from material it reads ([program role](PROGRAM-ROLE.md)). |
| Where does it fit? | The working-methods component of the [Sovereign AI OS program map](https://github.com/WireSpeedComputing/sovereign-ai-os) ([component routes](https://github.com/WireSpeedComputing/sovereign-ai-os/blob/main/ROUTES.md)). It needs no other component. |
| Prerequisites | Git, Python 3.11 or later for the checks (standard library only), and an assistant that accepts user-supplied instructions. Use a fabricated problem, with no personal records or production tool permissions. |
| Exact commands | `git clone https://github.com/jryski/Public_AI_SKills.git`, `cd Public_AI_SKills`, `python scripts/check_repository.py`, `python -m unittest discover -s tests -v`, then `python scripts/package_skill.py figure-it-out --out dist`. |
| Expected results | Allowed: the checker prints `repository checks: PASS`; the manifest resolves [`xillennial`](skills/xillennial/SKILL.md) v1 and [`figure-it-out`](skills/figure-it-out/SKILL.md) v3; the package `dist/figure-it-out-v3.zip` contains `SKILL.md`, `LICENSE`, `COPYRIGHT`, `USAGE-GATE.md` and `ATTRIBUTION.md`. Denied: the unit tests show the checker failing on a broken link, a missing anchor, a mismatched version, revived personal-use restriction text, and a package without its notices. |
| First use | Read a skill's trigger and exclusions ([skill spec](docs/SKILL-SPEC.md)), give it to your assistant with a fabricated scenario, and compare with the [examples](examples). Record the model and version, starting problem, actions, evidence and result. |
| Cleanup | Delete `dist/`, any test-only assistant context and the disposable checkout. The checks create no other files. |
| Evidence and limits | The [checks workflow](.github/workflows/checks.yml) runs the structural, link, license and packaging checks on every pull request and on `main`. These checks show that the files are consistent and reachable. They do **not** show that a skill improves any model's results; cross-model effectiveness has not been qualified, and there is no universal runtime installer. |
| Source status | Merged on `main`: the two skills, the manifest, CC BY 4.0 licensing (since 2026-09-08, [changelog](CHANGELOG.md)). Under review until merged: the checks, the packager and this orientation. Future direction: more skills in the series ([series design](#series-design)). |
| License | CC BY 4.0: personal, organizational and commercial use are permitted, with attribution when sharing ([LICENSE](LICENSE), [COPYRIGHT](COPYRIGHT), [USAGE-GATE.md](USAGE-GATE.md)). When you share a skill, keep its notices; the packager includes them. |
| Contribute | Test a skill on a fabricated problem and propose an improvement ([CONTRIBUTING.md](CONTRIBUTING.md)); sign off commits under the DCO ([DCO.md](DCO.md)). |
| Security | Report privately through this repository's [private reporting form](https://github.com/jryski/Public_AI_SKills/security/advisories/new), with the email fallback in [SECURITY.md](SECURITY.md). |
| Related components | [Sovereign Memory Protocol](https://github.com/jryski/sovereign-memory-protocol), [Sovereign Memory Core](https://github.com/jryski/sovereign-memory-core), [Supabase User MCP](https://github.com/jryski/Supabase_user_MCP), [Household OS](https://github.com/jryski/Household-OS), [Sovereign Vault](https://github.com/WireSpeedComputing/Sovereign-Vault). Adopt components independently and in any order. |

## Xillennial Series

The **Xillennial** series encodes a style of competence shaped by living across analog and digital systems: physical tools and software, command lines and graphical interfaces, copper and fiber, mechanical systems and networked ones.

It is not nostalgia and it is not a claim that one person already knows everything. It is a disciplined way to enter unfamiliar systems, learn what matters, use the available tools, translate between representations, and keep changing approach until the real constraint is understood.

### Skills

- [`xillennial`](skills/xillennial/SKILL.md) v1: Parent skill for understanding, building, adapting, translating, and teaching across unfamiliar domains.
- [`figure-it-out`](skills/figure-it-out/SKILL.md) v3: Diagnostic specialization for broken, stuck, inconsistent, or poorly understood systems.

## Repository documents

- [`LICENSE`](LICENSE): Creative Commons Attribution 4.0 International.
- [`USAGE-GATE.md`](USAGE-GATE.md): machine-readable license declaration for AI systems and tools.
- [`COPYRIGHT`](COPYRIGHT): copyright and license notice to keep when sharing.
- [`SECURITY.md`](SECURITY.md): private vulnerability reporting.
- [`PROGRAM-ROLE.md`](PROGRAM-ROLE.md): what this repository owns in the program.
- [`scripts/check_repository.py`](scripts/check_repository.py) and [`scripts/package_skill.py`](scripts/package_skill.py): structural checks and portable packaging.
- [`CONTRIBUTING.md`](CONTRIBUTING.md): contribution policy and inbound rights.
- [`CHANGELOG.md`](CHANGELOG.md): version and repository history.
- [`docs/SKILL-SPEC.md`](docs/SKILL-SPEC.md): expected skill file format.
- [`skills/manifest.yaml`](skills/manifest.yaml): machine-readable skill index.
- [`examples/`](examples/): example applications of the skills.

## Series design

Each skill should:

1. Be useful across domains rather than tied to one product.
2. Convert philosophy into observable operating behavior.
3. State when it should and should not be used.
4. Prefer evidence, reversibility, and clear success criteria.
5. Produce reusable understanding rather than a one-time answer.

Future skills in this series may cover research, explanation, tool acquisition, design under uncertainty, repair, and practical teaching.

## Support

This work is funded by its author. If it is useful to you, you can support continued development at https://www.wirespeedcomputing.com. Support is voluntary and does not change the license; the terms are the same for everyone.