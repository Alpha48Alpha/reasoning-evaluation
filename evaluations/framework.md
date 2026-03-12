# Evaluation Framework

This document describes the methodology used to evaluate reasoning prompts in this repository.

For the full definition of each metric, see [metrics.md](metrics.md).

---

## Scoring Rubric

Each prompt response is scored on a scale of **0–3** for each applicable dimension:

| Score | Meaning |
|---|---|
| 0 | Fails to meet the criterion |
| 1 | Partially meets the criterion |
| 2 | Mostly meets the criterion |
| 3 | Fully meets the criterion |

---

## Dimensions

### 1. Step Validity (SV)
- Is each reasoning step logically or mathematically sound?
- Are intermediate calculations performed correctly?
- Are inferences drawn from valid premises?

### 2. Conclusion Accuracy (CA)
- Does the final answer match the ground truth?
- Is the answer consistent with the reasoning shown?
- For open-ended reasoning, does the conclusion follow from the premises?

### 3. Chain Completeness (CC)
- Are all necessary steps shown explicitly?
- Can a reader follow the chain without filling in gaps?
- Are problem setup, intermediate work, and conclusion all present?

### 4. Error Recovery (ER)
- Does the model identify when it has made an error?
- Does it self-correct and arrive at the right answer?
- Score N/A for prompts where no error is expected or introduced.

### 5. Clarity (CL)
- Is the reasoning explanation well-structured and easy to follow?
- Is notation used consistently and correctly?
- Is the level of detail appropriate for the intended audience?

---

## Aggregate Score

The aggregate score for a response is computed as:

```
Aggregate = (SV + CA + CC + ER + CL) / (applicable_dimensions * 3) * 100%
```

When Error Recovery is N/A, applicable_dimensions = 4.

---

## Ground Truth

All prompts in the `prompts/` directory include an **Expected Answer** field. This is the verified correct answer used as the reference when scoring Conclusion Accuracy.

For mathematical prompts, expected answers are computed analytically. For logical prompts, expected answers are derived from formal proof or truth table analysis.

---

## Evaluation Procedure

1. Submit the prompt to the model without modification.
2. Record the full response.
3. Score each applicable dimension independently using the 0–3 rubric.
4. Compute the aggregate score.
5. Record scores in the appropriate file under `evaluations/results/`.

---

## Results Summary

| Domain | Prompts Evaluated | Avg Step Validity | Avg Conclusion Accuracy |
|---|---|---|---|
| Math | ~80 | 74% | 78% |
| Logic | ~70 | 70% | 72% |
| Multi-Step | ~60 | 68% | 65% |
| **Total** | **~210** | **~71%** | **~72%** |

Detailed per-prompt scores are stored in `evaluations/results/`.
