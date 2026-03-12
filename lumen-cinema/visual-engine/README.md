# Visual Engine

## Role

The Visual Engine is responsible for the **image and camera layer** of a generated film. It translates narrative scene cards into structured visual specifications that describe what the camera sees, how it moves, and what each frame looks like.

The Visual Engine produces:

- **Scene descriptions** — Detailed depictions of setting, lighting, and atmosphere
- **Character appearance** — Costume, physical state, and expression per scene
- **Shot lists** — Camera angle, lens type, movement, and framing for each shot
- **Visual continuity rules** — Constraints that must hold across scenes to avoid inconsistencies

---

## Inputs

The Visual Engine receives its primary input from the Narrative Engine's scene cards and character profiles.

| Input | Type | Description |
|---|---|---|
| Scene card | Structured text | Location, time, objective, conflict, outcome from Narrative Engine |
| Character profile | Structured text | Character name, role, and arc from Narrative Engine |
| Visual style | string | Cinematographic reference (e.g., high-contrast noir, warm naturalist, cold desaturated) |
| Aspect ratio | string | Film format (e.g., 2.39:1 anamorphic, 1.85:1 flat, 1.33:1 academy) |

---

## Outputs

| Output | Format | Description |
|---|---|---|
| Scene visual spec | Structured text | Environment, lighting, atmosphere, and color palette for a scene |
| Character visual spec | Structured text | Appearance, costume, and physical state for a character in a scene |
| Shot list | Structured list | Numbered shots with angle, framing, movement, and duration |
| Continuity notes | Structured text | Flags for visual elements that must persist across scenes |

---

## Evaluation

Visual Engine outputs are scored on:

- **Visual Consistency (VC)** — Do character appearances and environments remain coherent across scenes?
- **Production Feasibility (PF)** — Can the described shots be assembled into a coherent sequence?
- **Clarity (CL)** — Are the visual descriptions specific enough to guide rendering?
- **Creative Quality (CQ)** — Does the visual design serve the narrative tone?

See [`../evaluation/metrics.md`](../evaluation/metrics.md) for scoring definitions.

---

## Design Notes

The Visual Engine transforms abstract scene descriptions into **renderable specifications**. A shot list produced by the Visual Engine is the direct input to the Render Engine. Visual continuity notes must be respected by all downstream engines to maintain film coherence across scenes.
