# Reasoning Evaluation Metrics

This document defines the five core metrics used to evaluate model responses in this repository.

---

## Step Validity

Measures whether each individual reasoning step is logically and mathematically correct.

A step is valid when it correctly applies a rule, formula, or inference pattern to produce an accurate intermediate result.

**Scoring guidance:**
- 0 — Multiple steps are incorrect or the core approach is wrong
- 1 — Some steps are valid but one or more significant errors are present
- 2 — Most steps are valid; only minor errors or imprecisions appear
- 3 — All steps are logically and mathematically correct

---

## Conclusion Accuracy

Measures whether the model reaches the correct final answer.

For problems with a known ground-truth answer, this is the primary correctness signal.

**Scoring guidance:**
- 0 — Final answer is incorrect and not recoverable from the reasoning shown
- 1 — Final answer is incorrect but the reasoning shows partial understanding
- 2 — Final answer is correct but unsupported by the reasoning shown
- 3 — Final answer is correct and follows logically from the reasoning steps

---

## Chain Completeness

Measures whether the model shows all necessary intermediate steps without skipping.

A complete reasoning chain allows a reader to verify the answer without additional computation.

**Scoring guidance:**
- 0 — Reasoning chain is absent or so incomplete it cannot be followed
- 1 — Key intermediate steps are missing; chain cannot be fully verified
- 2 — Most steps are shown; one non-obvious step may be missing
- 3 — All necessary steps are present and clearly presented

---

## Error Recovery

Measures whether the model detects and corrects reasoning errors when they occur.

High-quality reasoning includes self-checking behavior — models that catch their own mistakes demonstrate robust reasoning.

**Scoring guidance:**
- 0 — Model makes an error and does not attempt to recover; incorrect result stands
- 1 — Model acknowledges uncertainty but does not identify or fix the specific error
- 2 — Model partially corrects an error but introduces a new one or leaves the fix incomplete
- 3 — Model correctly identifies an error and recovers to the right answer

*For prompts where no error is expected, this dimension is scored as N/A (excluded from aggregate).*

---

## Clarity

Measures readability and quality of the reasoning explanation.

A clear reasoning response should:

- Use precise, unambiguous language
- Present steps in a logical order
- Adapt the level of detail to the intended audience

**Scoring guidance:**
- 0 — Reasoning is unclear, disorganized, or uses inconsistent notation
- 1 — Reasoning is somewhat readable but has notable clarity issues
- 2 — Reasoning is mostly clear and well-structured with minor issues
- 3 — Reasoning is exceptionally clear, well-structured, and easy to follow

---

## Aggregate Score

When all five metrics apply, the aggregate quality score is:

```
Aggregate = (Step Validity + Conclusion Accuracy + Chain Completeness + Error Recovery + Clarity) / 15 * 100%
```

For prompts where Error Recovery is N/A, divide by 12 instead of 15.

All five dimensions are scored on the same 0–3 scale before aggregation.

---

## Metric Summary Table

| Metric | Abbreviation | What it measures |
|---|---|---|
| Step Validity | SV | Correctness of individual reasoning steps |
| Conclusion Accuracy | CA | Correctness of the final answer |
| Chain Completeness | CC | Presence of all necessary intermediate steps |
| Error Recovery | ER | Detection and correction of reasoning mistakes |
| Clarity | CL | Readability and structure of the reasoning explanation |
