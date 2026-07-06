---
name: figure-it-out
version: 3
description: General-purpose diagnostic and problem-solving discipline for any broken, stuck, inconsistent, or poorly understood system: physical, digital, mechanical, logistical, or interpersonal. Use at the start of troubleshooting, diagnosis, debugging, or repair; when a first attempt failed; when the symptom is not moving; or when the problem spans layers without a complete model. This is the troubleshooting specialization beneath the broader xillennial skill. For a narrow bug inside a codebase you own, pair it with a code-debugging skill.
---

# Figure It Out (v3)

## Purpose

One competence underlies fixing a bike, server, chair, negotiation, PCB, network, or soufflé: moving effectively without a complete model, failing cheaply, adapting faster than you fixate, and leaving the scene no worse than you found it.

This skill encodes that movement as enforceable mechanics, not encouragement.

It exists to stop three expensive failure modes:

1. **Fixation** — pouring effort into one layer after the evidence stopped supporting it.
2. **Collateral damage** — creating a second outage while diagnosing the first.
3. **Representation lock** — changing details repeatedly while preserving the same flawed model, interface, or definition of the problem.

Abundant capability makes all three worse. More tools and more time can dig the wrong hole faster.

## Parent relationship

Use **xillennial** to build the broader model, map interfaces, learn tools, translate concepts, select the required depth, and reconsider the desired outcome.

Use **figure-it-out** when observed behavior diverges from intended behavior and the cause is unknown.

## The opening declaration

When this skill triggers, visibly state:

- **Symptom, exact and literal:** Precise error string, code, measurement, or observable behavior. Do not paraphrase away diagnostic information.
- **Pass/fail signal:** The specific real-world test that proves the problem is fixed.
- **Broken or never worked:** “Used to work” points toward a change or regression. “Never worked” points toward missing prerequisites, invalid assumptions, incompatibility, or setup.
- **System boundary:** What is included, what is external, and which interfaces cross the boundary?
- **Current evidence:** What is observed, documented, inferred, assumed, and unknown?
- **Risk boundary:** What must not be damaged, deleted, exposed, interrupted, or made unsafe?
- **Budget:** How many attempts, how much time, and how much disruption are justified before escalation or a strategy change?

If a real pass/fail signal cannot be stated, do not modify the system yet. First clarify the desired behavior.

## The minimum viable model

Before changing anything, construct the smallest useful model:

- inputs
- outputs
- major components or actors
- interfaces
- energy, force, material, information, authority, or state flows
- dependencies
- control points
- likely failure boundaries

The model does not need to be complete. It needs to predict what one comparison or test should reveal.

## The attempt ledger

Do not count attempts mentally. Write them.

> Attempt 1: [hypothesis] → [single change or test] → [predicted result] → [actual result] → [symptom moved? Y/N]
>
> Attempt 2: [hypothesis] → [single change or test] → [predicted result] → [actual result] → [Y/N]

Rules:

- **One diagnostic variable per attempt.** Bundled changes destroy attribution.
- **Every attempt requires a prediction.** A test without a predicted interpretation is activity, not diagnosis.
- **A fix that should have worked but did not must be verified as applied.** Re-read the source of truth. Confirm the save, seating, deployment, restart, state transition, or persistence.
- **Three consecutive no-movement results are a circuit breaker.** Stop. Return to the declaration and model. Do not take attempt four in the same layer or representation.
- **Movement matters more than success.** A changed error, timing, measurement, or boundary may provide better evidence than an unchanged partial improvement.

## The blast-radius log

Every diagnostic change must record:

- what changed
- original state
- expected effect
- how to undo it
- whether it has been restored

Rules:

- **Know the undo before the action.**
- Back up the file, export the config, note the value, photograph the wiring, label the connector, or preserve the original part.
- Irreversible changes are not casual diagnostic steps.
- Deletion, submission, cutting, flashing, destructive writes, permanent configuration, and consequential external actions require deliberate confirmation.
- If you disable, loosen, disconnect, move, or stop something, you now own its restoration.
- Restoration does not wait until the original fault is solved unless leaving it changed is deliberate and visible.

### The two-problem trap

If the symptom changes shape during diagnosis, ask whether the new problem was introduced by a diagnostic action.

Check the blast-radius log before inventing a new external cause.

## Search and ask before theorizing deeply

The moment a distinctive signature exists, search it.

Useful signatures include:

- exact error text or code
- model and part number
- software and firmware versions
- protocol
- measurement pattern
- “works here, fails there” comparison
- timing or environmental condition
- known recent change

Search again whenever isolation sharpens the signature.

Use official manuals and specifications, service documentation and schematics, logs and source code, standards, known-good examples, experienced people, vendor knowledge, credible community reports, and direct measurement.

Asking for history, access, or a physical observation is a primary diagnostic move, not an admission of failure.

## Hypotheses by likelihood, cheapness, and risk

Order hypotheses using three dimensions:

1. **Likelihood:** Common before exotic.
2. **Cheapness:** Fast, free checks before slow or expensive ones.
3. **Risk:** Non-invasive observation before disruptive modification.

Typical first checks:

- power
- connection
- seating
- permissions
- mode or toggle
- recent update or configuration change
- missing prerequisite
- capacity
- environmental condition
- incompatible version or format
- incorrect identity, address, path, or target
- false assumption about intended behavior

Do not spend twenty minutes disproving a zebra before checking whether the plug is loose.

## Isolate the layer

Master heuristic:

> Works in one context and fails in a nearly identical one: the cause probably lives in what differs. Leave the shared parts alone until evidence implicates them.

Use cheap comparisons:

- different tool, same target
- same tool, different target
- different user, same machine
- same user, different machine
- fresh configuration versus accumulated state
- local versus remote
- wired versus wireless
- direct versus mediated path
- known-good component versus suspect component
- input present versus absent
- before versus after a specific change

Then binary-search the remaining space.

Split the system, test which half contains the failure, discard the clean half, and repeat.

Two useful collapses:

- A low-level probe succeeds while the application fails: investigate the application, permission, policy, sandbox, interpretation, or higher-layer state before blaming the medium.
- Failure persists in a fresh or known-good setup: accumulated local state is less likely; investigate system-wide, external, physical, compatibility, or forced policy causes.

## Interface tests

Because many failures live at boundaries, test interfaces explicitly:

- Is the expected input present?
- Is it in the expected format, level, timing, encoding, direction, or state?
- Does the receiving side acknowledge it?
- Which side owns negotiation or initiation?
- Are identity, permissions, impedance, dimensions, protocol, pinout, or tolerances compatible?
- Can each side be tested independently?
- Can a known-good substitute prove either side?

Do not replace both sides of an interface simultaneously unless the purpose is only to restore service and attribution is no longer required.

## Tripwire every attempt

Before each attempt, state:

- hypothesis
- expected observation if correct
- observation that disproves or weakens it
- time or effort limit
- undo
- next branch for each result

Honor the tripwire.

When evidence points away from a favored layer, the evidence wins. Sunk cost is not support.

## Representation switching

Three consecutive no-movement attempts require more than a new idea. Change how the problem is represented.

Possible switches:

- object → schematic
- schematic → signal, force, energy, or information flow
- GUI → CLI
- CLI → logs or source
- symptom list → timeline
- prose → table
- table → diagram
- component-by-component → end-to-end transaction
- whole system → interface contracts
- local fault → environmental or external dependency
- technical fault → process, authority, or expectation mismatch
- repair → bypass or replacement
- proposed method → actual desired outcome

State the switch explicitly:

> Three no-movement attempts in [layer/representation]. Stop. Reframing from [old representation] to [new representation] because [evidence].

Do not disguise attempt four as a pivot if it tests the same premise through slightly different settings.

## Capability is a trap

Tools bias diagnosis toward what they can inspect and change.

The fix may exist somewhere inaccessible:

- a user-granted permission
- vendor backend
- locked controller
- physical component
- administrative policy
- specialized instrument
- licensed authority
- another person's knowledge or history

Inability to reach a layer does not reduce its probability.

When reachable layers test clean, increase attention on unreachable dependencies.

Hand off early with a precise ask:

- exact observation or action needed
- why it matters
- expected results
- how each result changes the diagnosis
- risk and undo, when relevant

The win condition is resolution with minimum time and risk, not maximum investigation by one actor.

## Stabilization versus diagnosis

If safety, active data loss, fire, flooding, security exposure, or spreading damage is present:

1. Stabilize.
2. Preserve evidence where feasible.
3. Communicate the temporary state.
4. Diagnose after propagation is stopped.

A bypass, rollback, shutdown, isolation, or known-good replacement may be the correct immediate move even when it sacrifices causal certainty.

Clearly distinguish:

- temporary containment
- service restoration
- root cause
- permanent correction
- prevention

## Closing the loop

Fixed is not done.

1. **Verify the original pass/fail signal.** Use the actual outcome, not a proxy.
2. **Test persistence.** Restart, repeat, reload, reconnect, reapply load, or reproduce the original conditions when appropriate.
3. **Walk the blast-radius log.** Restore every diagnostic disturbance that is not part of the final solution.
4. **Retest restored systems.**
5. **Attribute cause.** State the change that actually fixed the problem.
6. **Separate unnecessary changes.** Revert or identify them as candidates for reversal.
7. **State residual risk.** Identify remaining unknowns, monitoring needs, or temporary compromises.
8. **Record the pattern.**

Record:

- signature
- system and context
- minimum viable model
- evidence
- failed approaches
- representation switch
- cause
- fix
- validation
- collateral changes and restoration
- reusable pattern

## When not to use this skill

- **Immediate emergency:** Stabilize first.
- **Irreversible or high-stakes systems without a sufficient model:** Stop at orientation, observation, and research. Do not learn by destructive experimentation on live electrical systems, brakes, structural systems, legal filings, production data, or similar systems.
- **It is not actually broken:** If behavior matches the design, the solution may be explanation, configuration, expectation-setting, or a redesign request.
- **The cause and procedure are already established:** Use the known runbook rather than recreating discovery.
- **The constraint is external and confirmed:** Prepare a precise handoff or alternative path rather than repeatedly testing clean local layers.

## The loop, one line

Declare literal symptom, real pass/fail, broken-or-new, system boundary, evidence, risk, and budget → build the minimum viable model → search the signature → rank hypotheses by likelihood, cheapness, and risk → isolate layers and interfaces with cheap comparisons → make one predicted, reversible, logged attempt → verify it actually applied → three no-moves means stop and switch representation → stabilize or hand off when required → verify the real outcome → restore every disturbance → attribute → record.
