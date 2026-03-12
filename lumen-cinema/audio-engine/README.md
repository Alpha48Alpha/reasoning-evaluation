# Audio Engine

## Role

The Audio Engine is responsible for the **sound layer** of a generated film. It designs the complete audio landscape that accompanies the visual and narrative content, working across three sub-domains:

- **Music / Score** — Original score direction, motif assignment, and cue timing
- **Sound effects** — Diegetic and non-diegetic sound design, ambient textures
- **Voice direction** — Delivery notes, tone, pacing, and accent for each line of dialogue

---

## Inputs

The Audio Engine receives inputs from both the Narrative Engine (scene cards, dialogue) and the Visual Engine (shot lists, visual specs).

| Input | Type | Description |
|---|---|---|
| Scene card | Structured text | Location, time, objective, conflict, outcome from Narrative Engine |
| Dialogue | Screenplay text | Character lines from Narrative Engine |
| Shot list | Structured list | Camera sequence from Visual Engine |
| Tone | string | Emotional register of the scene (from Narrative Engine) |

---

## Outputs

| Output | Format | Description |
|---|---|---|
| Music cue sheet | Structured list | Cue name, trigger point, duration, instrumentation, emotional direction |
| Sound design spec | Structured text | Ambient layers, effects, and their relationship to on-screen events |
| Voice direction notes | Structured text | Delivery guidance per character and line, including pace, pitch, and emphasis |

---

## Evaluation

Audio Engine outputs are scored on:

- **Audio Alignment (AA)** — Does the audio design reinforce the narrative tone and visual mood?
- **Production Feasibility (PF)** — Is the audio specification complete and actionable?
- **Clarity (CL)** — Are direction notes specific enough for a performer or composer to execute?
- **Creative Quality (CQ)** — Does the audio design demonstrate craft and intentionality?

See [`../evaluation/metrics.md`](../evaluation/metrics.md) for scoring definitions.

---

## Design Notes

The Audio Engine operates in parallel with the Visual Engine but must maintain **synchronization** — audio cues are tied to specific visual moments defined in the shot list. The Render Engine uses the Audio Engine's cue sheet to align audio tracks with the video timeline.

Sound design separates into:
- **Diegetic sound** — Sounds that exist within the story world (footsteps, rain, a ringing phone)
- **Non-diegetic sound** — Sounds added for the audience only (score, voice-over narration)

Both must be specified explicitly so the Render Engine can assemble them correctly.
