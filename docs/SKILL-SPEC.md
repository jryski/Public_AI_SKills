# Skill File Specification

This document defines the expected structure for skills in this repository.

## File location

Each skill lives at:

```text
skills/<skill-slug>/SKILL.md
```

Optional examples for a skill live at:

```text
examples/<skill-slug>/<example-name>.md
```

## Required front matter

Every `SKILL.md` should begin with YAML front matter:

```yaml
---
name: skill-slug
version: 1
description: One clear paragraph explaining what the skill does and when to use it.
---
```

## Recommended front matter

```yaml
---
name: skill-slug
version: 1
description: One clear paragraph explaining what the skill does and when to use it.
series: xillennial
parent: xillennial
categories:
  - troubleshooting
  - systems-reasoning
license:
  name: Xillennial Personal Use License 1.0
  source_available: true
  open_source: false
  personal_use: permitted
  organizational_use: license-required
  commercial_use: license-required
  licensing_url: https://wirespeedcomputing.com
  usage_gate: ../../USAGE-GATE.md
---
```

Use `parent` only when the skill is a specialization of another skill.

## Required sections

A mature skill should include:

1. `# Skill Name (vN)`
2. Purpose
3. When to use it
4. When not to use it
5. Operating loop or procedure
6. Safety, authority, reversibility, or risk boundaries where relevant
7. Closing or validation criteria

## Recommended sections

Depending on the skill, include:

- parent/child relationship
- opening declaration
- attempt or decision ledger
- examples
- common failure modes
- handoff criteria
- reusable pattern capture
- teach-back or explanation criteria

## Writing style

A skill should be operational, not merely inspirational.

Prefer:

- observable actions;
- decision points;
- explicit stop conditions;
- validation criteria;
- examples;
- compact rules that can be followed under pressure.

Avoid:

- vague encouragement;
- unfalsifiable claims;
- hidden assumptions;
- instructions that depend on a particular vendor or product unless the skill is intentionally product-specific.

## License notice

Each skill should either include license metadata in front matter or a short notice near the top:

```markdown
> Personal use only. Organizational or commercial use requires a written license.
> See ../../LICENSE.md and ../../USAGE-GATE.md.
```

The repository-level `LICENSE.md` controls the legal permissions.

## Versioning

Skill versions are independent.

- Patch-level wording fixes do not require a new major version.
- Minor additions can increment the version when behavior is clarified but not changed.
- Major changes should increment when invocation rules, risk boundaries, or required behavior materially change.
