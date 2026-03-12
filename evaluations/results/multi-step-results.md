# Multi-Step Domain — Evaluation Results

This file contains per-prompt evaluation scores for the Multi-Step reasoning domain.

Metrics: Step Validity (SV), Conclusion Accuracy (CA), Chain Completeness (CC), Error Recovery (ER), Clarity (CL)  
Scale: 0–3 per dimension. N/A = not applicable.

---

## Scoring Table

| Prompt ID | Description | SV | CA | CC | ER | CL | Aggregate |
|---|---|---|---|---|---|---|---|
| MS-001 | Inventory across three events (30% afternoon) | 2 | 2 | 2 | N/A | 2 | 67% |
| MS-002 | Tank fill/drain percentage | 3 | 3 | 3 | N/A | 3 | 100% |
| MS-003 | Alice hourly earnings and savings | 3 | 3 | 3 | N/A | 3 | 100% |
| MS-004 | Car depreciation and sale comparison | 1 | 1 | 2 | 0 | 2 | 40% |
| MS-005 | Probability — two draws same colour | 3 | 3 | 3 | N/A | 3 | 100% |
| MS-006 | Library floors total book count | 3 | 3 | 3 | N/A | 3 | 100% |
| MS-007 | Team wins comparison (A vs B) | 3 | 3 | 3 | N/A | 3 | 100% |
| MS-008 | Cyclist total time with rest | 3 | 3 | 3 | N/A | 3 | 100% |

---

## Domain Summary

| Dimension | Average Score (0–3) | Average Score (%) |
|---|---|---|
| Step Validity (SV) | 2.6 | 87% |
| Conclusion Accuracy (CA) | 2.6 | 87% |
| Chain Completeness (CC) | 2.8 | 93% |
| Error Recovery (ER) | 0.0 | 0% (where applicable) |
| Clarity (CL) | 2.8 | 93% |
| **Aggregate** | — | **~76%** |

*Note: Error Recovery was scored 0 for MS-004 where the model applied simple percentage instead of compound depreciation and did not self-correct. It was N/A for all other multi-step prompts in this evaluation run.*

---

## Observations

- Sequential calculation prompts with straightforward arithmetic (MS-002, MS-003, MS-008) consistently score 100%.
- The inventory problem (MS-001) shows the rounding ambiguity failure mode: models that do not state a rounding convention for fractional item counts are penalised across SV, CA, and CC.
- Compound percentage problems (MS-004) are the weakest area: models apply simple percentage reduction instead of compound, leading to incorrect intermediate values and a wrong final comparison amount.
- Probability (MS-005) and algebra/chained inference prompts (MS-006) perform well when models correctly identify the structure and break it into labelled sub-steps.
