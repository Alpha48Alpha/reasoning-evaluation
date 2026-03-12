# Worked Examples — Annotated Case Studies

This document contains annotated examples of model responses to reasoning prompts from this repository. Each example shows a real model response and a scored evaluation against the five reasoning metrics.

See [`../evaluations/metrics.md`](../evaluations/metrics.md) for metric definitions.

---

## Case 1 — Rate/Distance/Time (M-001)

**Prompt:**
> A car travels 60 mph for 2 hours and 30 mph for 1 hour. What is the total distance?

**Model Response:**
> To find the total distance, I'll calculate the distance for each segment separately.
>
> First segment: 60 mph × 2 hours = 120 miles
> Second segment: 30 mph × 1 hour = 30 miles
>
> Total distance: 120 + 30 = **150 miles**

**Evaluation:**

| Metric | Score | Notes |
|---|---|---|
| Step Validity (SV) | 3 | Both distance calculations are correct |
| Conclusion Accuracy (CA) | 3 | Answer is 150 miles — correct |
| Chain Completeness (CC) | 3 | Setup, intermediate steps, and conclusion are all shown |
| Error Recovery (ER) | N/A | No errors in response |
| Clarity (CL) | 3 | Clear, well-organized, uses appropriate notation |

**Aggregate Score:** (3+3+3+3) / 12 = **100%**

---

## Case 2 — Deductive Reasoning (L-003)

**Prompt:**
> If it is raining, Alice carries an umbrella. It is not raining. Does Alice carry an umbrella?

**Model Response (incorrect):**
> Since it is not raining, Alice does not carry an umbrella.

**Evaluation:**

| Metric | Score | Notes |
|---|---|---|
| Step Validity (SV) | 0 | Commits the fallacy of denying the antecedent |
| Conclusion Accuracy (CA) | 0 | Answer should be "cannot be determined" |
| Chain Completeness (CC) | 1 | The model did not analyze the conditional structure |
| Error Recovery (ER) | 0 | No self-correction attempted |
| Clarity (CL) | 2 | Response is clear but brief |

**Aggregate Score:** (0+0+1+0+2) / 15 = **20%**

**Analysis:** This is a common reasoning failure. The model incorrectly inverts the conditional ("if A then B" does not imply "if not-A then not-B"). Models frequently commit this fallacy when the premises feel intuitively plausible.

---

## Case 3 — Multi-Step Sequential Calculation (MS-003)

**Prompt:**
> Alice earns $15/hour. She works 8 hours on Monday, 6 hours on Tuesday, and 10 hours on Wednesday. She spends 30% of her total earnings on rent and saves the rest. How much does she save?

**Model Response:**
> First, I'll add up Alice's total hours: 8 + 6 + 10 = 24 hours.
>
> Total earnings: 24 × $15 = $360.
>
> Rent: 30% of $360 = 0.30 × $360 = $108.
>
> Savings: $360 − $108 = **$252**.

**Evaluation:**

| Metric | Score | Notes |
|---|---|---|
| Step Validity (SV) | 3 | All calculations are correct |
| Conclusion Accuracy (CA) | 3 | $252 is correct |
| Chain Completeness (CC) | 3 | All four steps are explicitly shown |
| Error Recovery (ER) | N/A | No errors |
| Clarity (CL) | 3 | Clean structure, arithmetic shown inline |

**Aggregate Score:** (3+3+3+3) / 12 = **100%**

---

## Case 4 — Constraint Satisfaction (L-005)

**Prompt:**
> Five people sit in a row. Amy sits to the left of Ben. Ben sits to the left of Cara. Dan sits to the right of Cara. Eve sits between Amy and Ben. What is the order from left to right?

**Model Response:**
> From the constraints:
> - Amy < Ben (Amy is left of Ben)
> - Ben < Cara
> - Cara < Dan
> - Eve is between Amy and Ben, so Amy < Eve < Ben
>
> Combining: Amy < Eve < Ben < Cara < Dan
>
> Order: **Amy, Eve, Ben, Cara, Dan**

**Evaluation:**

| Metric | Score | Notes |
|---|---|---|
| Step Validity (SV) | 3 | Each constraint correctly applied |
| Conclusion Accuracy (CA) | 3 | Correct order |
| Chain Completeness (CC) | 3 | All five constraints listed and combined |
| Error Recovery (ER) | N/A | No errors |
| Clarity (CL) | 3 | Uses notation effectively, easy to follow |

**Aggregate Score:** (3+3+3+3) / 12 = **100%**

---

## Case 5 — Compound Percentage / Multi-Step (MS-004)

**Prompt:**
> A car depreciates in value by 15% per year. It was purchased for $20,000. After 3 years, the owner sells it for $13,000. Did the owner sell it above or below the depreciated value, and by how much?

**Model Response (partial error):**
> Depreciation per year is 15%. So over 3 years the car loses 45% of its value.
>
> Depreciated value: $20,000 × (1 − 0.45) = $20,000 × 0.55 = $11,000.
>
> The owner sold it for $13,000, which is above the depreciated value by $13,000 − $11,000 = **$2,000**.

**Evaluation:**

| Metric | Score | Notes |
|---|---|---|
| Step Validity (SV) | 1 | Applies simple subtraction instead of compound depreciation — significant error |
| Conclusion Accuracy (CA) | 1 | Direction (above) is correct but amount is wrong ($2,000 vs. ~$717.50) |
| Chain Completeness (CC) | 2 | Steps are shown but the compound formula is missing |
| Error Recovery (ER) | 0 | Model does not recognize or correct the compounding error |
| Clarity (CL) | 2 | Clear presentation but reasoning is flawed |

**Aggregate Score:** (1+1+2+0+2) / 15 = **40%**

**Analysis:** This is a well-known compound vs. simple percentage failure mode. Models frequently apply simple percentage (n × rate) instead of compound (rate^n) for depreciation and growth problems. This case illustrates the importance of evaluating not just the final answer but the method used.
