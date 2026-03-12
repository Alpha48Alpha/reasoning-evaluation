# Narrative Engine

## Role

The Narrative Engine is responsible for the **story layer** of a generated film. It produces and structures all text-based cinematic content, including:

- **Story structure** — Three-act framework, plot points, turning points, and resolution
- **Character arcs** — Motivation, transformation, and relationship dynamics
- **Scene logic** — Scene objectives, conflict, and how scenes chain together
- **Dialogue** — Character voice, subtext, and spoken lines formatted as screenplay

---

## Inputs

The Narrative Engine accepts the following parameters:

| Input | Type | Description |
|---|---|---|
| `genre` | string | Film genre (e.g., drama, thriller, sci-fi, comedy) |
| `logline` | string | One-sentence premise of the story |
| `characters` | list | Named characters with brief role descriptions |
| `tone` | string | Emotional register (e.g., dark, hopeful, comedic, tense) |
| `target_length` | string | Short film / Feature / Mini-series |

---

## Outputs

The Narrative Engine produces:

| Output | Format | Description |
|---|---|---|
| Story outline | Structured text | Three-act breakdown with scene-level summaries |
| Character profiles | Structured text | Arc, motivation, and relationships for each character |
| Scene cards | Structured text | Scene number, location, time, objective, conflict, outcome |
| Dialogue | Screenplay format | Character cue lines formatted as INT./EXT. scenes |

---

## Evaluation

Narrative Engine outputs are scored on:

- **Narrative Coherence (NC)** — Does the story hold together across all scenes?
- **Chain Completeness (CC)** — Are setup, conflict, and resolution all present?
- **Clarity (CL)** — Is the screenplay formatting correct and readable?
- **Creative Quality (CQ)** — Does the story demonstrate thematic depth and originality?

See [`../evaluation/metrics.md`](../evaluation/metrics.md) for scoring definitions.

---

## Design Notes

The Narrative Engine is the **foundation layer** of the cinema pipeline. Visual, Audio, and Render engines all derive their inputs from the Narrative Engine's outputs. A scene card produced by the Narrative Engine becomes the source of truth for what the Visual Engine must render and what the Audio Engine must score.
