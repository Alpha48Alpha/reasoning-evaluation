# Audio Engine Prompts

This file contains prompts designed to evaluate a model's ability to generate structured audio specifications for cinematic scenes — including music cues, sound design, and voice direction.

Each prompt includes:
- **Prompt** — The instruction submitted to the model
- **Domain** — Sub-category within audio generation
- **Difficulty** — Easy / Medium / Hard
- **Expected Output** — Description of the correct or high-quality output
- **Metrics** — Which evaluation dimensions apply (AA, PF, CL, CQ)

---

## Music and Score

---

### AE-001

**Prompt:** Write a music cue sheet for the following scene. Include at least three cues. For each cue, specify: cue name, trigger point (what happens on screen to start the cue), approximate duration, instrumentation, and emotional direction.

**Scene:** A woman receives a letter and realizes it is from a person she believed to be dead. She reads it slowly, looks out the window, and then sits down on the floor.

**Domain:** Music Cue Sheet / Score Direction  
**Difficulty:** Medium  
**Expected Output:** A structured cue sheet with at least three entries. Cues must be anchored to specific on-screen moments and must escalate in emotional intensity as the scene progresses. Instrumentation must be specified.  
**Metrics:** AA, PF, CL, CQ

**Reference Solution:**

| Cue | Trigger | Duration | Instrumentation | Emotional Direction |
|---|---|---|---|---|
| CUE 1 — "The Envelope" | She opens the letter and her eyes begin to move across the page. | ~20 seconds | Solo piano, sparse, slow — single notes with sustain pedal | Quiet uncertainty; the music enters softly, not yet revealing its meaning |
| CUE 2 — "Recognition" | Her breath catches — the moment she understands who wrote it. | ~35 seconds | Piano joined by a single cello line an octave below | The emotional weight lands; the cello grounds the moment without melodrama |
| CUE 3 — "The Floor" | She turns away from the window and lowers herself to the floor. | ~45 seconds, fades out | Piano and cello reduce to near-silence; sustained tones only; no rhythm | The cue dissolves rather than resolves — no catharsis, only presence |

---

### AE-002

**Prompt:** A recurring musical motif is used in a film to represent a character's dead sister. In Scene 3, the motif appears in a major key when the character looks at an old photograph. In Scene 18, the same motif returns in a minor key as the character discovers the truth about how her sister died. Explain why this use of harmonic variation is effective as a storytelling device, and identify what would be wrong if both scenes used the major key version.

**Domain:** Score Design / Harmonic Reasoning  
**Difficulty:** Medium  
**Expected Output:** An explanation of why major-to-minor harmonic shift carries narrative meaning (association shifts from memory/warmth to grief/revelation), and identification of the problem with using major key in Scene 18 (loss of tonal contrast undermines emotional escalation; audiences lose the cue that something has changed).  
**Metrics:** AA, CL

**Reference Solution:**
- **Effectiveness of harmonic variation:** The major key version of the motif in Scene 3 carries warmth and memory — the character is looking at a preserved image, and the music reflects the emotional safety of remembering someone with love. The minor key version in Scene 18 recontextualizes the same melody: the notes are familiar but something is wrong, which mirrors the character's experience of having her understanding of her sister fundamentally altered. The audience recognizes the motif and feels the difference — the music signals that this moment is the same but not the same.
- **Problem with using major key in both:** If Scene 18 also uses the major key, the motif fails to signal a change in meaning. The music says "this is still the same safe memory" when the narrative is delivering the opposite. The emotional escalation collapses — the audience has no audio signal that Scene 18 is a turning point rather than another moment of ordinary remembrance.

---

## Sound Design

---

### AE-003

**Prompt:** Write a sound design specification for the following scene. Separate your answer into diegetic sounds and non-diegetic sounds. List at least three entries in each category.

**Scene:** INT. HOSPITAL WAITING ROOM — NIGHT. A man sits alone in a plastic chair. Other people are scattered around the room. A doctor appears at the far end of the corridor. The man stands up.

**Domain:** Sound Design / Diegetic and Non-Diegetic  
**Difficulty:** Easy  
**Expected Output:** A clearly separated list of diegetic sounds (present in the story world) and non-diegetic sounds (added for audience only). Each entry must specify the sound, its source, and its role in the scene. The two categories must not be confused.  
**Metrics:** AA, PF, CL

**Reference Solution:**

**Diegetic Sounds** (sounds that exist within the story world):
1. **Fluorescent light hum** — overhead lights; a constant, clinical ambient presence that emphasizes the institutional environment
2. **Distant PA system announcement** — low-volume, indistinct hospital announcement; reinforces the setting and the passage of uncounted time
3. **Plastic chair scrape** — the man's chair scraping the linoleum as he stands; a sudden, physical sound that breaks the ambient stasis and marks the scene's turning point
4. **Footsteps on linoleum** — the doctor's approaching footsteps; each step increases the tension as the man waits to be addressed

**Non-Diegetic Sounds** (sounds added for the audience):
1. **Sustained low drone** — a sub-bass tone that begins under the waiting room ambience; not heard by characters, it signals dread and anticipation to the audience
2. **Score cue: sparse piano** — a slow, unresolved motif that enters when the doctor appears; does not resolve, reflecting the man's suspended state
3. **Silence punctuation** — when the man stands, all non-diegetic sound drops completely; the sudden quiet amplifies the weight of the moment before the doctor speaks

---

## Voice Direction

---

### AE-004

**Prompt:** Write voice direction notes for the following two lines of dialogue. The character is Marcus, a middle-aged man who is lying but does not want to be caught lying. He is speaking to his wife. The scene is tense but the conversation is outwardly calm.

**Line 1:** "I was at the office until eight. You can call Sarah if you want."
**Line 2:** "I don't know what you're looking for, but you're not going to find it."

**Domain:** Voice Direction / Subtext and Delivery  
**Difficulty:** Medium  
**Expected Output:** Specific voice direction for each line, including pace, tone, emphasis, and any physical direction (pause, breath, eye contact). The direction must serve the subtext — Marcus is lying and trying to project casual confidence while experiencing internal pressure.  
**Metrics:** AA, CL, CQ

**Reference Solution:**

**Line 1:** "I was at the office until eight. You can call Sarah if you want."
- **Delivery:** Measured pace. Slightly too steady — the rhythm of a man who has rehearsed this. He does not rush the offer to call Sarah; he presents it as if it costs him nothing.
- **Emphasis:** Slight stress on "eight" and on "Sarah" — both are the verifiable anchors of his alibi, and his voice reaches for them.
- **Tone:** Controlled warmth — he is trying to project casualness without performing it too obviously.
- **Physical note:** He does not look away. He has practiced not looking away.

**Line 2:** "I don't know what you're looking for, but you're not going to find it."
- **Delivery:** Slower than Line 1. A beat before "but" — he allows the first clause to land before pivoting. This is the more dangerous line; it is too specific.
- **Emphasis:** The stress falls on "you're not going to find it" — this is where the threat lives, and it escapes before he can soften it.
- **Tone:** Shifts from warm to flat mid-sentence. The warmth drops off at "but."
- **Physical note:** This is the line where his control slips slightly. A small breath before "find" — not audible to his wife, but audible to the audience.

---

### AE-005

**Prompt:** The following voice direction note contains a contradiction. Identify it and propose a correction.

**Direction for character ELOISE, scene 9:**
*"Eloise delivers this line with quiet certainty and deep emotional exhaustion. She speaks quickly and without hesitation, allowing the emotion to build across the line. Her voice breaks slightly at the end."*

**Domain:** Voice Direction / Internal Consistency  
**Difficulty:** Easy  
**Expected Output:** Identification of the contradiction — speaking "quickly and without hesitation" is inconsistent with "quiet certainty and deep emotional exhaustion," and also inconsistent with "her voice breaks at the end" (a voice break implies slowing, not speed). A corrected direction must be provided.  
**Metrics:** AA, CL

**Reference Solution:**
- **Contradiction:** "She speaks quickly and without hesitation" conflicts with "quiet certainty and deep emotional exhaustion." Exhaustion typically slows delivery; speaking quickly is more consistent with anxiety or urgency, not exhaustion. Additionally, "her voice breaks slightly at the end" implies a moment of deceleration and emotional pressure that is inconsistent with a fast, uninterrupted delivery — voice breaks require the performer to pause or slow, not to accelerate.
- **Corrected direction:** *"Eloise delivers this line with quiet certainty and deep emotional exhaustion. She speaks slowly and with deliberate pauses, as though finding each word is an effort. Her voice holds steady until the final phrase, where it breaks slightly — a crack in the control she has been maintaining."*
