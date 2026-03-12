# reasoning-evaluation
### Reasoning Evaluation — Structured prompts and benchmarks designed to measure LLM reasoning quality.

---

## Overview

This repository contains **200+ prompts** across mathematical, logical, and multi-step reasoning domains, evaluated to benchmark and improve **reasoning quality** in large language models.

The work focuses on how well LLMs:

- **Break down problems** — Do they identify sub-problems and structure their approach?
- **Apply correct reasoning steps** — Are intermediate calculations and logic valid?
- **Reach accurate conclusions** — Do they arrive at the correct final answer?
- **Explain their reasoning** — Is the chain of thought clear and communicable?
- **Handle edge cases** — Do they reason correctly when problems involve unusual constraints?

---

## Prompt Categories

| Domain | Description |
|---|---|
| Math | Arithmetic, algebra, word problems, rate/distance/time, proportional reasoning |
| Logic | Deductive reasoning, syllogisms, constraint satisfaction, lateral thinking |
| Multi-Step | Problems requiring multiple chained reasoning steps with intermediate states |
| [Lumen Cinema](lumen-cinema/README.md) | Cinematic reasoning — story generation, visual specification, audio design, and render assembly |

---

## Evaluation Methodology

Each prompt is evaluated against the following dimensions (see [`evaluations/metrics.md`](evaluations/metrics.md) for full definitions):

1. **Step Validity** — Are individual reasoning steps logically and mathematically correct?
2. **Conclusion Accuracy** — Does the final answer match the ground truth?
3. **Chain Completeness** — Does the model show all necessary steps without skipping?
4. **Error Recovery** — When the model makes an intermediate error, does it detect and correct it?
5. **Clarity** — Is the reasoning explanation readable and appropriate for the intended audience?

---

## Results

| Domain | Prompts Evaluated | Avg Step Validity | Avg Conclusion Accuracy |
|---|---|---|---|
| Math | ~80 | 74% | 78% |
| Logic | ~70 | 70% | 72% |
| Multi-Step | ~60 | 68% | 65% |
| **Total** | **~210** | **~71%** | **~72%** |

---

## Repository Structure

```
prompts/
  math/             # Mathematical reasoning prompts (arithmetic, algebra, word problems)
  logic/            # Logical reasoning prompts (deduction, syllogisms, constraints)
  multi-step/       # Multi-step reasoning prompts requiring chained inference
evaluations/
  metrics.md        # Definitions for all reasoning evaluation metrics
  framework.md      # Scoring rubric and evaluation methodology
  results/          # Per-domain evaluation results and analysis
cases/
  worked-examples.md    # Annotated worked examples with model responses and scores
  failure-analysis.md   # Common failure modes and patterns observed across prompts
lumen-cinema/
  README.md             # Project Lumen Cinema — modular movie-creation engine overview
  narrative-engine/     # Story structure, character arcs, scene cards, and dialogue
  visual-engine/        # Scene descriptions, shot lists, and visual continuity
  audio-engine/         # Music cues, sound design, and voice direction
  render-engine/        # Timeline assembly, transition spec, and export parameters
  evaluation/           # Cinema-specific metrics and evaluation framework
```
