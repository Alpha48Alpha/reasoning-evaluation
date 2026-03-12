# Failure Analysis — Common Reasoning Failure Modes

This document catalogs recurring failure patterns observed across model responses in this repository. Understanding these patterns supports prompt design, targeted evaluation, and model improvement.

---

## Failure Mode 1: Denying the Antecedent

**Description:** The model incorrectly concludes that "if not-A, then not-B" from the premise "if A, then B."

**Frequency:** High — appears in approximately 30% of conditional logic prompts.

**Example:**
- Premise: "If it is raining, Alice carries an umbrella."
- Observation: "It is not raining."
- Incorrect conclusion: "Alice does not carry an umbrella."
- Correct answer: Cannot be determined (Alice may carry an umbrella for other reasons).

**Why it happens:** The surface plausibility of everyday examples makes the conditional feel biconditional. Models associate "umbrella" strongly with "rain" and invert the relationship.

**Mitigation:** Prompts that include explicit non-obvious examples (e.g., carrying an umbrella for sun protection) reduce the frequency of this error.

---

## Failure Mode 2: Simple vs. Compound Percentage

**Description:** The model applies a flat percentage over multiple periods instead of compounding.

**Frequency:** High — appears in approximately 40% of multi-period percentage prompts.

**Example:**
- Problem: A $20,000 car depreciates 15% per year for 3 years.
- Incorrect approach: $20,000 × (1 − 0.15 × 3) = $11,000
- Correct approach: $20,000 × (0.85)³ = $12,282.50

**Why it happens:** The simpler linear calculation is easier to apply. Models often default to it when the prompt does not explicitly state "compound."

**Mitigation:** Prompts that specify "compound annually" or provide a year-by-year scaffolding produce significantly fewer errors.

---

## Failure Mode 3: Averaging Rates Directly

**Description:** The model averages two rates arithmetically when a harmonic mean or weighted average is required.

**Frequency:** Medium — appears in approximately 25% of average rate problems.

**Example:**
- Problem: A runner goes the first half of a race at 6 mph and the second half at 4 mph. What is the average speed?
- Incorrect approach: (6 + 4) / 2 = **5 mph**
- Correct approach: Harmonic mean = 2 / (1/6 + 1/4) = **4.8 mph**

**Why it happens:** Arithmetic averaging is the default operation for "average." Models do not recognize when equal distances (rather than equal times) require harmonic averaging.

**Mitigation:** Prompts that specify "equal distance segments" and ask models to "show your time calculation" significantly improve accuracy.

---

## Failure Mode 4: Skipping Intermediate Steps

**Description:** The model jumps from problem setup to conclusion, omitting intermediate calculations.

**Frequency:** Medium — appears in approximately 20% of multi-step prompts.

**Example:**
- Problem: Inventory calculation across three events (MS-001).
- Incorrect response: States the final count without showing the morning, delivery, or afternoon steps.
- Impact: Chain Completeness (CC) score drops; answer may be wrong due to mental arithmetic errors.

**Why it happens:** Models may optimize for brevity or treat intermediate steps as trivial. This tendency increases with prompt complexity.

**Mitigation:** Adding explicit instructions ("show all steps") or "explain your reasoning" reduces this failure significantly.

---

## Failure Mode 5: Rounding Without Acknowledgment

**Description:** The model rounds an intermediate value without stating the assumption, leading to an answer that differs from the exact expected answer.

**Frequency:** Low — appears in approximately 10% of prompts involving non-integer results.

**Example:**
- Problem: 30% of 235 items sold = 70.5 items.
- Issue: Model reports 70 or 71 without acknowledging that a rounding convention was applied.

**Why it happens:** Models often apply practical rounding (you cannot sell half an item) without making the assumption explicit.

**Mitigation:** Prompts that specify the expected precision level ("assume fractional items are allowed" or "round to the nearest whole number") eliminate ambiguity.

---

## Failure Mode 6: Incorrect Set-Up of Proportional Problems

**Description:** The model correctly identifies that a problem is proportional but sets up the relationship inverted.

**Frequency:** Low — appears in approximately 8% of proportional reasoning prompts.

**Example:**
- Problem: More workers → fewer days.
- Incorrect setup: 10 workers / 5 workers × 8 days = 16 days (multiplied instead of divided).

**Why it happens:** Inverse proportional problems are counterintuitive. Without careful step labeling, models sometimes apply direct proportion.

**Mitigation:** Prompts that ask "is this directly or inversely proportional?" as a first step significantly reduce inversions.

---

## Summary Table

| Failure Mode | Frequency | Primary Metric Impacted | Primary Mitigation |
|---|---|---|---|
| Denying the Antecedent | High (~30%) | SV, CA | Explicit non-obvious counterexamples |
| Simple vs. Compound % | High (~40%) | SV, CA | Specify "compound" or scaffold year-by-year |
| Averaging Rates Directly | Medium (~25%) | SV, CA | Ask for time calculation step |
| Skipping Intermediate Steps | Medium (~20%) | CC | "Show all steps" instruction |
| Rounding Without Acknowledgment | Low (~10%) | CA | Specify precision requirements |
| Inverted Proportional Setup | Low (~8%) | SV | Ask "direct or inverse?" first |
