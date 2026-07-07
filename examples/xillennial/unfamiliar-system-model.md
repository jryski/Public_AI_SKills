# Example: Building a Minimum Viable Model of an Unfamiliar System

This example shows how `xillennial` approaches an unfamiliar system before deciding whether to troubleshoot, repair, replace, bypass, or redesign it.

## Situation

A person is asked to help with a small CNC machine they have never used before. The machine powers on, but the operator says, “It does not cut correctly.”

The goal is not to become a CNC expert immediately. The goal is to build enough model to ask good questions, avoid damage, and choose a safe next step.

## Real outcome versus requested method

- **Requested method:** “Fix the CNC.”
- **Real outcome:** Produce accurate cuts safely and repeatedly.
- **Required depth:** Diagnose first. Modify only after the control points and risks are understood.

## Minimum viable model

```text
job file → controller/software → motion commands → stepper motors → spindle/router → bit → material → finished cut
```

Inputs:

- design file
- toolpath
- machine settings
- bit geometry
- material
- power
- operator setup

Outputs:

- actual cut path
- cut depth
- edge quality
- dimensional accuracy
- machine noise/vibration

Control points:

- software settings
- origin/zeroing
- bit selection
- feed rate
- spindle speed
- material clamping
- machine calibration

Risk boundary:

- do not run an unverified job at full depth;
- do not put hands near moving parts;
- do not alter firmware or calibration until simpler causes are checked;
- preserve current settings before modifying.

## Interface-first reasoning

Important interfaces:

| Interface | Contract to verify |
|---|---|
| Design file → CAM/toolpath | Units, scale, bit diameter, cut depth |
| CAM → controller | File format, coordinate system, origin |
| Controller → motors | Motion follows expected axes and direction |
| Bit → material | Correct bit, speed, feed, depth, clamping |
| Operator → machine | Setup procedure, zeroing, safety steps |

## Representation switch

Instead of asking only “what is broken,” switch representations:

1. physical machine
2. job file
3. toolpath preview
4. coordinate system
5. motion test without cutting
6. shallow test cut on scrap

## Cheap safe test

Before changing calibration, run a dry motion test or shallow cut on scrap.

Prediction examples:

- If the preview is wrong, the problem is upstream in the design/CAM stage.
- If the preview is correct but dry motion is wrong, inspect controller settings or axes.
- If dry motion is correct but cutting is poor, inspect bit, speed, feed, depth, material, and clamping.

## Teach-back

One sentence:

> The CNC is a chain that turns a digital path into controlled physical motion and then into a cut in material.

One minute:

> A design becomes a toolpath, the controller turns that into motion commands, motors move the bit through material, and cut quality depends on both the digital instructions and the physical setup.

Where the analogy breaks:

> It is not just a printer for wood or metal. Cutting forces, bit geometry, material behavior, vibration, and safety risks matter in ways a paper printer does not.

## Reusable pattern

When a digital system controls a physical process, separate:

- file correctness;
- command interpretation;
- actuator behavior;
- physical interaction;
- operator setup;
- safety boundary.

Do not recalibrate the machine before proving whether the bad output originates in the digital file, control interface, or physical cutting conditions.
