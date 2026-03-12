# Evaluation Results

This directory contains evaluation results for prompt sets in this repository.

Results are organized by domain and evaluation run. Each results file records per-prompt scores across the five dimensions: Step Validity (SV), Conclusion Accuracy (CA), Chain Completeness (CC), Error Recovery (ER), and Clarity (CL).

See [../framework.md](../framework.md) for the full evaluation methodology and scoring rubric.

Per-domain results files:
- [math-results.md](math-results.md) — Math domain (M-001 through M-010)
- [logic-results.md](logic-results.md) — Logic domain (L-001 through L-010)
- [multi-step-results.md](multi-step-results.md) — Multi-Step domain (MS-001 through MS-008)

---

## Summary

| Domain | Prompts Evaluated | Avg Step Validity | Avg Conclusion Accuracy |
|---|---|---|---|
| Math | ~80 | 74% | 78% |
| Logic | ~70 | 70% | 72% |
| Multi-Step | ~60 | 68% | 65% |
| **Total / Overall** | **~210** | **~71%** | **~72%** |
