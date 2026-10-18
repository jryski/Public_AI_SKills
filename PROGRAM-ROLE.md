# Program role: Public AI Skills

> **Program:** Sovereign AI OS ecosystem  
> **Role class:** reusable behavior packages not tied to one model or runtime  
> **Program context:** [`Sovereign AI OS program map`](https://github.com/WireSpeedComputing/sovereign-ai-os)  
> **Usage terms:** [`LICENSE`](LICENSE) (CC BY 4.0, controlling) and [`USAGE-GATE.md`](USAGE-GATE.md) (machine-readable summary)

## Mission

Public AI Skills packages reusable reasoning and operating behavior separately from any one model, runtime, deployment, or fact store.

Skills make useful behavior portable. They do not make the model authoritative, grant tool access, or replace deployment policy.

## This repository owns

- skill specifications and manifests;
- reusable behavioral procedures;
- examples and evaluation guidance;
- versioning, licensing notices, and the machine-readable usage statement;
- generic techniques written without dependence on one model or runtime (their effect on any given model is not qualified).

## This repository does not own

- household or business data;
- planning-card state;
- user or agent identity;
- database authorization or RLS;
- model qualification or cross-model effectiveness claims;
- runtime tool wiring or tool permissions.

## Planning and work-plane relationship

A planning card may require a named skill or behavioral capability. That requirement helps route work but does not prove the selected model possesses the skill, grant access to the card, or authorize the requested action.

A runtime should combine:

```text
accepted card and scope
+ trusted identity and capability
+ qualified model route
+ selected skill behavior
+ bounded integrations
+ review and evidence requirements
```

The skill remains replaceable and versioned. The durable result and evidence belong to the appropriate deployment store or repository.

## Use and sharing

All skills are licensed under CC BY 4.0. Personal, organizational and commercial use are permitted, including employer, client, team, school, government, nonprofit and enterprise use, with no separate permission. When sharing a skill or an adaptation, keep the supplied attribution and notices, link the license and indicate changes; [`scripts/package_skill.py`](scripts/package_skill.py) builds a portable package that carries `LICENSE`, `COPYRIGHT`, `USAGE-GATE.md` and an `ATTRIBUTION.md`. [`LICENSE`](LICENSE) controls.

## Data boundary

Use synthetic examples. Never commit private prompts, household or company records, credentials, provider logs, or deployment-specific secrets as skill content.

## Agent handoff rule

Before applying a skill, inspect its version, trigger conditions, exclusions and evidence expectations. Do not treat model familiarity with a similar technique as evidence that the accepted skill contract was followed.