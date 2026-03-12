# Render Engine

## Role

The Render Engine is responsible for **assembling all engine outputs into a coherent film**. It operates as the final stage in the pipeline, taking structured specifications from the Narrative, Visual, and Audio engines and combining them into a timeline-ordered sequence of frames and tracks.

The Render Engine governs:

- **Frame sequencing** — Ordering shots according to the shot list and scene card sequence
- **Timeline assembly** — Aligning audio cues and video cuts on a unified timeline
- **Cut logic** — Determining how transitions between shots are executed (cut, fade, dissolve)
- **Export specification** — Defining output format, resolution, frame rate, and audio mix

---

## Inputs

The Render Engine receives structured outputs from all three upstream engines.

| Input | Source Engine | Description |
|---|---|---|
| Scene cards (ordered) | Narrative Engine | Ordered sequence of scenes with locations and objectives |
| Shot list | Visual Engine | Numbered shots with type, movement, and duration per scene |
| Character visual specs | Visual Engine | Appearance specs for continuity verification |
| Music cue sheet | Audio Engine | Cue triggers, durations, and instrumentation |
| Sound design spec | Audio Engine | Diegetic and non-diegetic audio per scene |
| Voice direction notes | Audio Engine | Delivery notes per line, cross-referenced to scene cards |

---

## Outputs

| Output | Format | Description |
|---|---|---|
| Assembled timeline | Structured list | Ordered sequence of shots with in/out points and audio layer assignments |
| Transition specification | Structured list | Cut type and duration for each transition between shots |
| Export parameters | Structured text | Resolution, frame rate, codec, audio channels, and delivery format |
| Continuity verification report | Structured text | Cross-engine consistency check — flags any conflicts before final output |

---

## Evaluation

Render Engine outputs are scored on:

- **Production Feasibility (PF)** — Is the assembled timeline complete and executable?
- **Visual Consistency (VC)** — Does the assembled sequence preserve continuity from the Visual Engine specs?
- **Audio Alignment (AA)** — Are audio cues correctly synchronized to their visual trigger points?
- **Clarity (CL)** — Is the timeline specification specific enough for a renderer to execute without ambiguity?

See [`../evaluation/metrics.md`](../evaluation/metrics.md) for scoring definitions.

---

## Design Notes

The Render Engine is the **integration layer** of the pipeline. Its primary function is not to generate creative content but to **verify and assemble** the outputs of the other three engines. A Render Engine failure — a missing cue, a mis-sequenced shot, an unresolved continuity conflict — will manifest as a visible or audible error in the final film.

The Render Engine must resolve any conflicts between engines before assembly. If the Audio Engine specifies a cue that references a shot that does not exist in the Visual Engine's shot list, the Render Engine must flag the conflict rather than proceeding.
