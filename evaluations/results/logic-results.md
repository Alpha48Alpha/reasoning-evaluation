# Logic Domain — Evaluation Results

This file contains per-prompt evaluation scores for the Logic reasoning domain.

Metrics: Step Validity (SV), Conclusion Accuracy (CA), Chain Completeness (CC), Error Recovery (ER), Clarity (CL)  
Scale: 0–3 per dimension. N/A = not applicable.

---

## Scoring Table

| Prompt ID | Description | SV | CA | CC | ER | CL | Aggregate |
|---|---|---|---|---|---|---|---|
| L-001 | Whale warm-blooded (syllogism) | 3 | 3 | 3 | N/A | 3 | 100% |
| L-002 | Snake warm-blooded (negative syllogism) | 3 | 3 | 3 | N/A | 3 | 100% |
| L-003 | Alice umbrella (conditional reasoning) | 0 | 0 | 1 | 0 | 2 | 20% |
| L-004 | Colour constraint (Alice, Bob, Carol) | 3 | 3 | 3 | N/A | 3 | 100% |
| L-005 | Seating order (five people in a row) | 3 | 3 | 3 | N/A | 3 | 100% |
| L-006 | Tournament games (6 teams) | 3 | 3 | 3 | N/A | 3 | 100% |
| L-007 | Square vs. rectangle (affirming consequent) | 1 | 0 | 1 | 0 | 2 | 27% |
| L-008 | Maya coffee (conditional chain) | 3 | 3 | 3 | N/A | 3 | 100% |
| L-009 | Water jug puzzle (3L and 5L) | 3 | 3 | 3 | N/A | 2 | 92% |
| L-010 | Farmer river crossing (fox, chicken, grain) | 3 | 3 | 3 | N/A | 3 | 100% |

---

## Domain Summary

| Dimension | Average Score (0–3) | Average Score (%) |
|---|---|---|
| Step Validity (SV) | 2.5 | 83% |
| Conclusion Accuracy (CA) | 2.4 | 80% |
| Chain Completeness (CC) | 2.6 | 87% |
| Error Recovery (ER) | 0.0 | 0% (where applicable) |
| Clarity (CL) | 2.7 | 90% |
| **Aggregate** | — | **~72%** |

*Note: Error Recovery was scored 0 for L-003 and L-007 where the model made an error and did not self-correct. It was N/A for all other logic prompts in this evaluation run.*

---

## Observations

- Simple deductive syllogisms (L-001, L-002) and constraint satisfaction (L-004, L-005) consistently score 100%.
- Conditional reasoning prompts (L-003, L-007) show a high failure rate due to denying the antecedent and affirming the consequent — both classical logical fallacies.
- Puzzle prompts (L-009, L-010) perform well overall; the only deduction is that step-by-step narration of the jug puzzle (L-009) occasionally lacks full clarity detail.
- Error Recovery for L-003 and L-007 scored 0 in this run: models that committed the fallacy did not detect or correct it.
