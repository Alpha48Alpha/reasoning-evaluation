# Project Lumen Cinema — Native Movie-Creation Engine

**ASCENSION PROTOCOL: PROJECT LUMEN CINEMA**

---

## Overview

Project Lumen Cinema is a modular system for generating cinematic stories, scenes, and structured film content through AI-assisted pipelines. Each engine in the system controls a distinct domain of filmmaking and is designed to evolve independently.

This module extends the reasoning evaluation framework to cover **cinematic reasoning** — the ability of a model to structure narrative, visual, audio, and production decisions with consistency, creativity, and technical precision.

---

## Core Principle

A film generator must control four domains:

| Engine | Domain | Responsibility |
|---|---|---|
| [Narrative Engine](narrative-engine/README.md) | Story & Dialogue | Story structure, character arcs, scene logic, screenplay formatting |
| [Visual Engine](visual-engine/README.md) | Scene & Camera | Scene descriptions, character appearance, shot composition, continuity |
| [Audio Engine](audio-engine/README.md) | Music, Sound & Voice | Soundtrack design, ambient audio, voice direction, sound effects |
| [Render Engine](render-engine/README.md) | Assembly & Output | Frame sequencing, timeline assembly, export specification |

---

## Module Structure

```
lumen-cinema/
  README.md                     # This document — system overview
  narrative-engine/
    README.md                   # Narrative Engine description and design
    prompts.md                  # Story structure and dialogue prompts
  visual-engine/
    README.md                   # Visual Engine description and design
    prompts.md                  # Scene, character, and camera prompts
  audio-engine/
    README.md                   # Audio Engine description and design
    prompts.md                  # Music, sound, and voice prompts
  render-engine/
    README.md                   # Render Engine description and design
    prompts.md                  # Frame assembly and output specification prompts
  evaluation/
    metrics.md                  # Cinema-specific evaluation metrics
    framework.md                # Scoring rubric and evaluation methodology
```

---

## Evaluation Dimensions

Cinema generation introduces domain-specific evaluation dimensions beyond standard reasoning metrics. See [`evaluation/metrics.md`](evaluation/metrics.md) for full definitions.

| Metric | Abbreviation | What it measures |
|---|---|---|
| Narrative Coherence | NC | Logical consistency of story structure and plot |
| Visual Consistency | VC | Continuity of character, setting, and camera direction |
| Audio Alignment | AA | How well audio design supports the narrative and visual tone |
| Production Feasibility | PF | Whether the described output could be assembled into a coherent film |
| Creative Quality | CQ | Originality, thematic depth, and cinematic craft |

---

## Design Philosophy

The four engines are **modular** — each can be prompted, evaluated, and improved independently. However, they must also **compose** into a unified film. Evaluation prompts are structured to test both the individual engine outputs and the integration between engines.

Each engine module contains:
- A **README** describing the engine's role, inputs, and expected outputs
- A **prompts file** with structured evaluation prompts following the same format as the core reasoning prompts
