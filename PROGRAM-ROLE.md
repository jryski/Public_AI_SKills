# Program role: Public AI Skills

> **Program:** Sovereign AI OS ecosystem  
> **Role class:** reusable model- and runtime-independent behavior packages  
> **Program context:** [`Sovereign AI OS`](https://github.com/jryski/sovereign-memory-core/blob/main/docs/ecosystem/SOVEREIGN_AI_OS.md)  
> **Usage authority:** [`USAGE-GATE.md`](USAGE-GATE.md) and [`LICENSE.md`](LICENSE.md)

## Mission

Public AI Skills packages reusable reasoning and operating behavior separately from any one model, runtime, deployment, or fact store.

Skills make useful behavior portable. They do not make the model authoritative, grant tool access, or replace deployment policy.

## This repository owns

- skill specifications and manifests;
- reusable behavioral procedures;
- examples and evaluation guidance;
- versioning, licensing, and usage gates;
- generic techniques that remain useful across models and runtimes.

## This repository does not own

- household or business data;
- planning-card state;
- user or agent identity;
- database authorization or RLS;
- model qualification;
- runtime tool wiring;
- permission to use a skill in an organizational or commercial context contrary to the repository license.

## Planning and work-plane relationship

A planning card may require a named skill or behavioral capability. That requirement helps route work but does not prove the selected model possesses the skill, grant access to the card, or authorize the requested action.

A runtime should combine:

```text
accepted card and scope
+ trusted identity and capability
+ qualified model route
+ licensed skill behavior
+ bounded integrations
+ review and evidence requirements
```

The skill remains replaceable and versioned. The durable result and evidence belong to the appropriate deployment store or repository.

## Business use

Organizational, commercial, employer, client, team, school, government, nonprofit, and enterprise use remains subject to this repository's explicit usage gate and licensing terms. Inclusion in the Sovereign AI OS ecosystem does not waive those terms.

## Data boundary

Use synthetic examples. Never commit private prompts, household or company records, credentials, provider logs, or deployment-specific secrets as skill content.

## Agent handoff rule

Before applying a skill, inspect its version, trigger conditions, exclusions, evidence expectations, and usage license. Do not treat model familiarity with a similar technique as evidence that the accepted skill contract was followed.