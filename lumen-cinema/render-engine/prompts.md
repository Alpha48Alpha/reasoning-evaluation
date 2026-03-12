# Render Engine Prompts

This file contains prompts designed to evaluate a model's ability to assemble cinematic outputs into a coherent, ordered timeline — including shot sequencing, cut specification, audio synchronization, and cross-engine continuity verification.

Each prompt includes:
- **Prompt** — The instruction submitted to the model
- **Domain** — Sub-category within render assembly
- **Difficulty** — Easy / Medium / Hard
- **Expected Output** — Description of the correct or high-quality output
- **Metrics** — Which evaluation dimensions apply (PF, VC, AA, CL)

---

## Timeline Assembly

---

### RE-001

**Prompt:** Assemble the following shots and audio cues into a unified timeline. For each timeline entry, specify: timeline position (in seconds), shot or audio track, and any notes on alignment.

**Shot list:**
- Shot 1: Wide establishing shot of the city at night. Duration: 8 seconds.
- Shot 2: Medium shot of a woman walking through a crowd. Duration: 5 seconds.
- Shot 3: Close-up of her hand gripping her bag strap. Duration: 3 seconds.
- Shot 4: Over-the-shoulder shot — she sees something across the street. Duration: 6 seconds.

**Audio cues:**
- CUE A: Ambient city sound (traffic, crowd murmur). Starts at the beginning of Shot 1. Duration: runs through all four shots.
- CUE B: Music motif — a brief, tense 4-second string figure. Trigger: Shot 3.

**Domain:** Timeline Assembly / Audio-Visual Synchronization  
**Difficulty:** Easy  
**Expected Output:** A timeline table showing each shot's in and out points, plus audio cue in and out points, with both video and audio layers displayed. CUE B must align to Shot 3's start point (13 seconds in).  
**Metrics:** PF, AA, CL

**Reference Solution:**

| Timeline Position | Track | Event | Out Point | Notes |
|---|---|---|---|---|
| 0:00 | Video | Shot 1 — Wide city establishing | 0:08 | — |
| 0:08 | Video | Shot 2 — Medium, woman in crowd | 0:13 | — |
| 0:13 | Video | Shot 3 — Close-up, hand on bag | 0:16 | CUE B triggers here |
| 0:16 | Video | Shot 4 — OTS, she sees something | 0:22 | — |
| 0:00 | Audio | CUE A — Ambient city sound | 0:22 | Continuous under all shots |
| 0:13 | Audio | CUE B — Tense string motif | 0:17 | Triggered by Shot 3; ends during Shot 4 |

---

### RE-002

**Prompt:** The following assembled timeline contains an audio synchronization error. Identify the error and state the corrected timeline entry.

| Timeline Position | Track | Event | Out Point |
|---|---|---|---|
| 0:00 | Video | Shot 1 — Character enters room | 0:06 |
| 0:06 | Video | Shot 2 — She opens the envelope | 0:10 |
| 0:10 | Video | Shot 3 — Close-up of her face reacting | 0:15 |
| 0:15 | Video | Shot 4 — She drops the letter | 0:19 |
| 0:10 | Audio | Music cue: piano motif triggers on "letter drop" | 0:16 |

**Domain:** Timeline Assembly / Synchronization Error Detection  
**Difficulty:** Easy  
**Expected Output:** Identification that the music cue's trigger annotation says "letter drop" but its timeline position is 0:10 (which aligns with Shot 3, not Shot 4 where the letter drop occurs at 0:15). The corrected entry should move the audio cue to 0:15.  
**Metrics:** AA, PF, CL

**Reference Solution:**
- **Error:** The music cue is labeled "triggers on 'letter drop'" but is positioned at 0:10, which is the start of Shot 3 (her face reacting). The letter drop occurs in Shot 4, which begins at 0:15.
- **Corrected entry:**

| Timeline Position | Track | Event | Out Point |
|---|---|---|---|
| 0:15 | Audio | Music cue: piano motif triggers on "letter drop" | 0:21 |

---

## Transition Specification

---

### RE-003

**Prompt:** Specify the transition type between each of the following shots, and justify each choice. Transition types available: hard cut, dissolve, fade to black, wipe, match cut.

**Shot sequence:**
1. Close-up of a candle flame burning.
2. Wide shot of the same room, now empty, with the candle extinguished.
3. INT. SAME ROOM — TEN YEARS LATER. A child is playing in the same space.
4. Close-up of the child picking up an old photograph.
5. The photograph fills the frame — it is a picture of the person from the earlier scenes.

**Domain:** Transition Specification / Cinematic Logic  
**Difficulty:** Medium  
**Expected Output:** A transition specified for each of the four cut points (1→2, 2→3, 3→4, 4→5), with justification for each choice based on the narrative and emotional relationship between shots.  
**Metrics:** PF, CL, CQ

**Reference Solution:**

- **1 → 2 (Candle flame → empty room):** **Dissolve** (~2 seconds). The dissolve signals the passage of time within the same location. A hard cut would be too abrupt for the tonal shift from life to absence; a dissolve lets the flame die gently into the empty room.
- **2 → 3 (Empty room → same room ten years later):** **Fade to black, then fade in** (~1.5 seconds each). The complete fade signals a significant time jump — the gap between the darkness and the new scene is the ten-year interval. A dissolve would not adequately convey the passage of a decade.
- **3 → 4 (Wide room → close-up of child's hand):** **Hard cut.** The wide-to-close transition is best served by a clean cut, which focuses attention sharply on the object of interest. No emotional transition is needed here — the cut itself creates the emphasis.
- **4 → 5 (Child holding photograph → photograph fills frame):** **Match cut.** The object — the photograph — is present in both shots. A match cut uses the visual geometry of the photograph to pull the viewer from the child's perspective directly into the image itself, making the reveal feel earned and immediate.

---

## Export Specification

---

### RE-004

**Prompt:** Write an export specification for a short film intended for the following two delivery platforms: (1) theatrical exhibition in a commercial cinema, and (2) streaming release on a standard video platform. Specify resolution, frame rate, codec, color space, and audio channels for each platform. Explain any differences between the two specifications.

**Domain:** Export Specification / Delivery Formats  
**Difficulty:** Medium  
**Expected Output:** Two complete export specifications, one per platform. Specifications must include resolution, frame rate, codec, color space, and audio channels. Differences must be explained, particularly around resolution, codec, and color space.  
**Metrics:** PF, CL

**Reference Solution:**

**Platform 1 — Theatrical Exhibition (DCP standard):**
- **Resolution:** 2K (2048 × 1080) or 4K (4096 × 2160)
- **Frame rate:** 24 fps
- **Codec:** JPEG2000 (as required by Digital Cinema Package standard)
- **Color space:** XYZ (CIE 1931 XYZ, as required by DCI specification)
- **Audio channels:** 5.1 surround (Left, Right, Center, LFE, Left Surround, Right Surround) or 7.1

**Platform 2 — Streaming Release:**
- **Resolution:** 3840 × 2160 (4K UHD) or 1920 × 1080 (Full HD)
- **Frame rate:** 24 fps (match theatrical) or 23.976 fps for broadcast compatibility
- **Codec:** H.264 or H.265 (HEVC) for efficient compression
- **Color space:** Rec. 709 (standard dynamic range) or Rec. 2020 (for HDR delivery)
- **Audio channels:** Stereo (2.0) baseline; Dolby Atmos or 5.1 for premium delivery

**Key differences:**
- **Codec:** Theatrical DCP requires JPEG2000 (lossless, high-bandwidth); streaming uses H.264/H.265 (lossy, compressed for transmission).
- **Color space:** Theatrical uses XYZ, which is a device-independent color space calibrated to DCI projectors. Streaming uses Rec. 709 or Rec. 2020, calibrated to consumer displays.
- **Resolution:** Theatrical 4K is 4096-wide (DCI 4K), which differs from consumer UHD 4K (3840-wide).

---

## Cross-Engine Continuity Verification

---

### RE-005

**Prompt:** Review the following outputs from three engines and identify any cross-engine conflicts that the Render Engine must resolve before assembly.

**Narrative Engine — Scene Card (Scene 9):**
- Setting: INT. KITCHEN — NIGHT
- Character present: Thomas
- Scene objective: Thomas finds a hidden letter.
- Duration estimate: ~2 minutes

**Visual Engine — Shot List (Scene 9):**
- Shot 1: Wide kitchen, daytime light from window. Thomas enters.
- Shot 2: Close-up of Thomas's hands opening a drawer.
- Shot 3: Thomas holds the letter. Camera pushes in on his expression.

**Audio Engine — Cue Sheet (Scene 9):**
- CUE 1: Ambient kitchen sound — daytime. Birds outside, light traffic.
- CUE 2: Music motif triggers when Thomas opens the drawer.

**Domain:** Cross-Engine Verification / Conflict Detection  
**Difficulty:** Medium  
**Expected Output:** Identification of the conflict — the Narrative Engine specifies NIGHT but the Visual Engine's Shot 1 describes daytime light and the Audio Engine's ambient cue describes daytime sounds. The Render Engine cannot proceed without resolving which is correct. A resolution path must be proposed.  
**Metrics:** VC, AA, PF, CL

**Reference Solution:**
- **Conflict identified:** The Narrative Engine specifies the scene takes place at NIGHT (INT. KITCHEN — NIGHT), but the Visual Engine's Shot 1 describes "daytime light from window," and the Audio Engine's CUE 1 specifies "daytime" ambient sound including birds and light traffic. These are directly contradictory.
- **Impact:** The Render Engine cannot assemble this scene without choosing one version, and an incorrect choice will produce either a visually inconsistent film (nighttime scene with daylight) or a narrative inconsistency (if the night setting is load-bearing for the plot).
- **Resolution path:** Return the conflict to the source engines for clarification. The Narrative Engine's scene card is the authoritative source for time of day. If the scene is confirmed as NIGHT, the Visual Engine must revise Shot 1 to describe interior artificial lighting (e.g., overhead light, no exterior light through the window) and the Audio Engine must revise CUE 1 to nighttime ambience (e.g., silence, distant street sounds, no birds). If the time of day was incorrect in the Narrative Engine, the scene card must be updated before the Visual and Audio outputs are re-evaluated.
