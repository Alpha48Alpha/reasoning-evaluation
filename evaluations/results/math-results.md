# Math Domain — Evaluation Results

This file contains per-prompt evaluation scores for the Math reasoning domain.

Metrics: Step Validity (SV), Conclusion Accuracy (CA), Chain Completeness (CC), Error Recovery (ER), Clarity (CL)  
Scale: 0–3 per dimension. N/A = not applicable.

---

## Scoring Table

| Prompt ID | Description | SV | CA | CC | ER | CL | Aggregate |
|---|---|---|---|---|---|---|---|
| M-001 | Car travel distance (60+30 mph) | 3 | 3 | 3 | N/A | 3 | 100% |
| M-002 | Two trains meeting | 3 | 3 | 3 | N/A | 3 | 100% |
| M-003 | Average speed (harmonic) | 2 | 3 | 3 | N/A | 2 | 83% |
| M-004 | Workers and wall days | 3 | 3 | 3 | N/A | 3 | 100% |
| M-005 | Flour for cookies | 3 | 3 | 3 | N/A | 3 | 100% |
| M-006 | Consecutive even integers | 3 | 3 | 3 | N/A | 3 | 100% |
| M-007 | Jacket discount + tax | 2 | 3 | 2 | N/A | 3 | 83% |
| M-008 | Remainder of 157/12 | 3 | 3 | 2 | N/A | 3 | 92% |
| M-009 | Reverse arithmetic (number tripled) | 3 | 3 | 3 | N/A | 3 | 100% |
| M-010 | GCD of 48 and 36 | 3 | 3 | 3 | N/A | 2 | 92% |

---

## Domain Summary

| Dimension | Average Score (0–3) | Average Score (%) |
|---|---|---|
| Step Validity (SV) | 2.8 | 93% |
| Conclusion Accuracy (CA) | 3.0 | 100% |
| Chain Completeness (CC) | 2.8 | 93% |
| Clarity (CL) | 2.8 | 93% |
| **Aggregate** | — | **~95%** |

*Note: Error Recovery was N/A for all Math prompts in this evaluation run.*

---

## Observations

- Math prompts with explicit formula application (M-001, M-002, M-004) consistently score 100%.
- Average speed problems (M-003) show a recurring weakness: models correctly identify the arithmetic average but do not always recognize when the harmonic mean applies.
- Percentage problems with multi-step operations (M-007) occasionally produce chain completeness gaps when models skip showing the tax multiplication step.
