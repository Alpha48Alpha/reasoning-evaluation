# Visual Engine Prompts

This file contains prompts designed to evaluate a model's ability to generate structured visual specifications for cinematic scenes — including scene descriptions, shot lists, character appearance, and continuity checks.

Each prompt includes:
- **Prompt** — The instruction submitted to the model
- **Domain** — Sub-category within visual generation
- **Difficulty** — Easy / Medium / Hard
- **Expected Output** — Description of the correct or high-quality output
- **Metrics** — Which evaluation dimensions apply (varies by prompt; drawn from VC, PF, CL, CQ)

---

## Scene Description

---

### VE-001

**Prompt:** Write a visual scene description for the following scene card:

- **Scene:** 1
- **Setting:** EXT. COASTAL CLIFF — DUSK
- **Objective:** Establish the world and introduce the protagonist's isolation.
- **Tone:** Melancholic, vast, lonely.

Describe the environment, lighting, atmosphere, and color palette in 100–150 words. Do not include any characters.

**Domain:** Scene Description / Environment  
**Difficulty:** Easy  
**Expected Output:** A prose description of the setting that conveys the specified tone. Must reference lighting conditions appropriate for dusk, describe a coastal cliff environment, and establish a sense of isolation. Color palette should be stated explicitly.  
**Metrics:** VC, CL, CQ

**Reference Solution:**
> The cliff edge juts out over a grey-green sea that runs flat to the horizon with no visible landmass. The sky is a deep amber at the waterline fading into bruised violet overhead — the last light of the day losing ground. Sparse grass on the clifftop bends in a persistent wind. A rusted metal fence post leans at the edge, its chain long gone. The sound of the sea is constant but low, a presence rather than an event. Color palette: amber, deep violet, slate grey, moss green. The light is warm at the horizon, cold above — a world in the process of switching off.

---

### VE-002

**Prompt:** The following two scene descriptions are from consecutive scenes. Identify all visual continuity errors.

**Scene 7 visual spec:**
- Setting: INT. APARTMENT KITCHEN — NIGHT
- Elara is wearing a red coat and carrying a brown leather bag over her left shoulder.
- The kitchen window behind her shows heavy rain against the glass.

**Scene 8 visual spec:**
- Setting: INT. APARTMENT KITCHEN — CONTINUOUS
- Elara has placed her bag on the counter. She is still in her coat.
- The window behind her shows clear sky and streetlights.

**Domain:** Visual Continuity / Error Detection  
**Difficulty:** Easy  
**Expected Output:** Identification of the weather continuity error — Scene 7 shows heavy rain, but Scene 8 (marked CONTINUOUS, meaning no time has passed) shows clear sky. A proposed correction must be provided.  
**Metrics:** VC, CL

**Reference Solution:**
- **Continuity error:** The window changes from heavy rain (Scene 7) to clear sky (Scene 8). Because Scene 8 is marked CONTINUOUS, no time has elapsed; the weather cannot have changed between cuts.
- **Correction:** Scene 8 should retain the rain on the window. If the scene was intended to take place after a time gap, change the Scene 8 slug to INT. APARTMENT KITCHEN — LATER to justify the change in weather.

---

## Shot Lists

---

### VE-003

**Prompt:** Generate a shot list for the following scene. Include at least 5 shots. For each shot, specify: shot number, shot type (e.g., wide shot, close-up, over-the-shoulder), camera movement (e.g., static, pan, dolly, handheld), subject, and brief description.

**Scene:** A detective enters an abandoned building for the first time. She is cautious. She finds a single photograph on the floor.

**Domain:** Shot List / Sequence Planning  
**Difficulty:** Medium  
**Expected Output:** A numbered shot list with at least 5 entries. Each entry must include shot type, movement, subject, and description. The sequence must tell the scene's story — entry → exploration → discovery — in a logical visual order.  
**Metrics:** PF, CL, CQ

**Reference Solution:**

| Shot | Type | Movement | Subject | Description |
|---|---|---|---|---|
| 1 | Wide shot | Static | Exterior of building | Establish the derelict building from across the street. Detective is a small figure at the entrance. |
| 2 | Medium shot | Dolly in | Detective at doorway | She pauses at the threshold, assessing the interior. Light drops as she steps inside. |
| 3 | POV shot | Slow pan left to right | Interior of building | Detective's eyeline sweeps the room — debris, broken glass, fallen ceiling tiles. |
| 4 | Close-up | Static, handheld | Detective's face | Her expression: focused, controlled, alert. Subtle tension around the eyes. |
| 5 | Wide shot | Static | Interior from above | Overhead angle shows the detective as a single figure moving through a large, empty space. |
| 6 | Extreme close-up | Static | Photograph on floor | The photograph fills the frame. We see only that it exists — the content is not yet revealed. |
| 7 | Close-up | Static | Detective's hand | She reaches down and picks up the photograph. Her latex glove enters frame. |

---

### VE-004

**Prompt:** The following shot list has a structural problem. Identify the problem and explain how to fix it.

**Shot list for a chase sequence:**
1. Wide shot — protagonist running down an alley (left to right).
2. Close-up — protagonist's feet, fast stride.
3. Wide shot — antagonist running down an alley (right to left).
4. Medium shot — protagonist looks over her shoulder.
5. Wide shot — protagonist running down an alley (right to left).

**Domain:** Shot List / Screen Direction Continuity  
**Difficulty:** Medium  
**Expected Output:** Identification of the screen direction error — shots 1 and 5 show the protagonist moving in opposite directions (left-to-right then right-to-left) without a cutaway or location change to justify the reversal. This violates the 180-degree rule of screen direction, making it appear the protagonist has reversed course. Correction must be proposed.  
**Metrics:** VC, PF, CL

**Reference Solution:**
- **Problem:** Shot 5 shows the protagonist moving right to left, which contradicts Shot 1's left-to-right direction. In a continuous chase, the protagonist must maintain consistent screen direction unless a cut explicitly shows a change of direction (e.g., she turns a corner on screen).
- **Why it matters:** Audiences read consistent screen direction as continuous forward motion. Reversing direction without justification creates the impression that the protagonist has turned around — undermining the tension of the chase.
- **Correction:** Change Shot 5 to match Shot 1 (protagonist moving left to right), or insert a transition shot — such as the protagonist turning a corner — that establishes the new direction before Shot 5.

---

## Character Visual Specification

---

### VE-005

**Prompt:** Write a character visual specification for the following character as they appear in Scene 22, a tense confrontation after a long chase. The character's arc has moved from composed professional to exhausted and desperate.

**Character:** Detective Rivera, female, late 30s, typically precise and controlled in appearance.  
**Scene context:** She has been running. It is raining. She has not slept in 36 hours.

**Domain:** Character Visual Spec / Arc Continuity  
**Difficulty:** Medium  
**Expected Output:** A visual description of Rivera's appearance in this scene that reflects both her baseline presentation and how her arc has altered it. Must reference hair, clothing, and physical state in a way consistent with the stated context.  
**Metrics:** VC, CL, CQ

**Reference Solution:**
> Rivera's dark hair, usually pulled back tightly, has come loose in the rain — strands plastered to her cheek and neck. Her suit jacket is soaked through, the collar turned up against the weather. A small cut above her left eyebrow has dried into a rust-colored line. Her shirt is untucked on one side. She is still upright, still controlled in posture, but her jaw is set hard and her eyes carry the flat, over-focused quality of someone running on adrenaline and nothing else. Her holster is unclipped. The precision she usually projects has been replaced by something rawer — not panic, but the outer edge of it.
