# Cinema Evaluation Framework

This document describes the methodology for evaluating model responses to Project Lumen Cinema prompts.

For full metric definitions, see [metrics.md](metrics.md).

---

## Scoring Rubric

Each prompt response is scored on a scale of **0–3** for each applicable cinema metric:

| Score | Meaning |
|---|---|
| 0 | Fails to meet the criterion |
| 1 | Partially meets the criterion |
| 2 | Mostly meets the criterion |
| 3 | Fully meets the criterion |

---

## Applicable Metrics by Engine

Each engine has a primary set of metrics:

| Engine | Primary Metrics | Notes |
|---|---|---|
| Narrative Engine | NC, CC, CL, CQ | SV and CA may apply for continuity error detection prompts |
| Visual Engine | VC, PF, CL, CQ | VC is primary; CC applies when full shot sequences are required |
| Audio Engine | AA, PF, CL, CQ | ER applies for prompts that include deliberate audio design errors |
| Render Engine | PF, VC, AA, CL | XC applies for cross-engine integration prompts |

---

## Evaluation Procedure

1. Submit the prompt to the model without modification.
2. Record the full response.
3. Score each applicable dimension independently using the 0–3 rubric.
4. Compute the aggregate score using the formula in [metrics.md](metrics.md).
5. Record scores in the appropriate evaluation results file.

---

## Prompt Types

Cinema prompts fall into three categories:

### Type 1 — Generation Prompts
The model is asked to produce a cinematic artifact (story outline, shot list, music cue sheet, etc.).

Evaluated on: the quality, completeness, and correctness of the generated artifact.

Primary metrics: NC or VC or AA (depending on engine), PF, CL, CQ.

### Type 2 — Error Detection Prompts
The model is given a cinematic specification that contains one or more deliberate errors and is asked to identify them.

Evaluated on: whether the model correctly identifies all errors and proposes valid corrections.

Primary metrics: SV, CA, CL. NC or VC or AA may apply depending on the error type.

### Type 3 — Integration Prompts
The model is given outputs from multiple engines and asked to perform cross-engine reasoning — assembling a timeline, identifying conflicts, or verifying consistency.

Evaluated on: whether cross-engine relationships are correctly handled.

Primary metrics: XC, PF, AA or VC, CL.

---

## Ground Truth

For error-detection prompts, a specific correct answer exists and is used when scoring Conclusion Accuracy.

For generation prompts, quality is evaluated against the **Reference Solution** provided with each prompt. Reference solutions define the characteristics of a high-quality response rather than a single correct answer — they are used to anchor scores of 3 and to calibrate the 0–2 range.

A response that differs from the reference solution is not automatically penalized, provided it satisfies the same underlying criteria.

---

## Results Summary

| Engine | Prompts | Primary Metrics |
|---|---|---|
| Narrative Engine | NE-001 to NE-006 | NC, CC, CL, CQ |
| Visual Engine | VE-001 to VE-005 | VC, PF, CL, CQ |
| Audio Engine | AE-001 to AE-005 | AA, PF, CL, CQ |
| Render Engine | RE-001 to RE-005 | PF, VC, AA, CL, XC |
| **Total** | **20** | — |

---

## Integration with Core Framework

The cinema evaluation framework extends the core reasoning framework described in [`../../evaluations/framework.md`](../../evaluations/framework.md). The same 0–3 scoring rubric and aggregate calculation methodology apply.

Cinema prompts are stored in their respective engine `prompts.md` files and follow the same structural format as prompts in the core `prompts/` directory.
