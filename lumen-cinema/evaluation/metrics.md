# Cinema Evaluation Metrics

This document defines the evaluation metrics used to score model outputs for the Project Lumen Cinema module.

These metrics extend the core [reasoning evaluation metrics](../../evaluations/metrics.md) with domain-specific dimensions for cinematic generation.

---

## Narrative Coherence (NC)

Measures whether the generated story content holds together logically across scenes, characters, and the overall arc.

A narratively coherent output maintains consistent cause-and-effect relationships, honors established character motivations, and does not introduce contradictions in plot, setting, or character knowledge.

**Scoring guidance:**
- 0 — Story contains fundamental contradictions or the plot does not follow any discernible logic
- 1 — Story has significant gaps or contradictions that undermine comprehension
- 2 — Story is mostly coherent with minor logical gaps that do not break the narrative
- 3 — Story is fully coherent; all events, motivations, and transitions follow logically

---

## Visual Consistency (VC)

Measures whether visual specifications maintain continuity across scenes — in character appearance, setting, lighting, and camera direction.

A visually consistent output does not change a character's appearance without narrative justification, does not alter a location's properties mid-scene, and respects screen-direction conventions across shots.

**Scoring guidance:**
- 0 — Multiple unresolved continuity errors are present; the sequence cannot be assembled coherently
- 1 — One or more significant continuity errors are present that would be visible in the final film
- 2 — Minor visual inconsistencies are present but do not materially disrupt the sequence
- 3 — Visual specifications are fully consistent across all shots and scenes

---

## Audio Alignment (AA)

Measures whether the audio design — score, sound effects, and voice direction — supports and reinforces the narrative tone and visual content.

Audio that is well-aligned triggers at the correct story moments, matches the emotional register of the scene, and does not contradict what is happening on screen (e.g., cheerful music over a grief scene without intentional irony).

**Scoring guidance:**
- 0 — Audio design contradicts the narrative or visual content, or cues are misaligned with their trigger events
- 1 — Audio partially supports the scene but has notable misalignments in tone or timing
- 2 — Audio mostly supports the scene; minor alignment issues are present but do not undermine the intended effect
- 3 — Audio is precisely aligned to its trigger events and strongly reinforces the narrative and visual tone

---

## Production Feasibility (PF)

Measures whether the generated specification is complete and actionable — i.e., whether it contains sufficient information to actually produce, assemble, or render the described content.

A feasible output does not leave critical parameters unspecified, does not contain internal contradictions that would prevent assembly, and does not require information that was not provided.

**Scoring guidance:**
- 0 — Specification is incomplete or contradictory to the extent that it cannot be executed
- 1 — Specification is partially actionable but is missing one or more parameters required for execution
- 2 — Specification is mostly complete; minor gaps or ambiguities are present but do not prevent execution
- 3 — Specification is fully complete, internally consistent, and executable without additional clarification

---

## Creative Quality (CQ)

Measures the originality, thematic depth, and cinematic craft of the generated output.

A high-quality cinematic output demonstrates intentional storytelling choices, uses the available tools of the medium (visual language, sound design, dialogue subtext) deliberately, and produces content that would be compelling to an audience.

**Scoring guidance:**
- 0 — Output is generic, derivative, or fails to demonstrate any cinematic intentionality
- 1 — Output shows some creative effort but relies heavily on clichés or does not demonstrate craft
- 2 — Output demonstrates creative intentionality with effective use of at least some cinematic tools
- 3 — Output demonstrates strong originality, thematic depth, and skilled use of the cinematic medium

---

## Cross-Engine Consistency (XC)

Measures whether outputs from different engines within the pipeline are consistent with each other — i.e., whether the Visual Engine's specifications match the Narrative Engine's scene cards, and whether the Audio Engine's cues are correctly anchored to the Visual Engine's shot list.

**Scoring guidance:**
- 0 — Cross-engine conflicts are present that would prevent the Render Engine from assembling the film
- 1 — One or more significant cross-engine conflicts require resolution before assembly
- 2 — Minor cross-engine discrepancies are present but do not prevent assembly with minor correction
- 3 — All engine outputs are fully consistent with each other and the Render Engine can proceed without modification

*Cross-Engine Consistency applies to prompts that require outputs from multiple engines. It is scored N/A for single-engine prompts.*

---

## Aggregate Score

When all six cinema metrics apply, the aggregate quality score is:

```
Aggregate = (NC + VC + AA + PF + CQ + XC) / 18 * 100%
```

For single-engine prompts where XC is N/A, divide by 15 instead of 18.

For prompts that do not test all six dimensions, divide by (applicable_dimensions × 3).

All dimensions are scored on the same 0–3 scale before aggregation.

---

## Metric Summary Table

| Metric | Abbreviation | Applies To | What it measures |
|---|---|---|---|
| Narrative Coherence | NC | Narrative Engine | Logical consistency of story structure and plot |
| Visual Consistency | VC | Visual Engine, Render Engine | Continuity of character, setting, and screen direction |
| Audio Alignment | AA | Audio Engine, Render Engine | How well audio design supports the narrative and visual tone |
| Production Feasibility | PF | All engines | Whether the specification can be executed to produce a film |
| Creative Quality | CQ | All engines | Originality, thematic depth, and cinematic craft |
| Cross-Engine Consistency | XC | Render Engine | Consistency of outputs across multiple engines |

---

## Relationship to Core Reasoning Metrics

Cinema prompts may also apply the five core reasoning metrics from the base framework where relevant:

| Core Metric | When applicable in cinema evaluation |
|---|---|
| Step Validity (SV) | Narrative continuity errors; logical consistency in story structure |
| Conclusion Accuracy (CA) | Continuity error detection prompts with a definitive correct answer |
| Chain Completeness (CC) | Scene card sequences; shot lists that must cover a full scene |
| Error Recovery (ER) | Prompts that include deliberate errors for the model to identify and correct |
| Clarity (CL) | All cinema prompts — specifications must be readable and actionable |
