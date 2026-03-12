# Narrative Engine Prompts

This file contains prompts designed to evaluate a model's ability to generate structured cinematic story content — including story outlines, character arcs, scene cards, and dialogue.

Each prompt includes:
- **Prompt** — The instruction submitted to the model
- **Domain** — Sub-category within narrative generation
- **Difficulty** — Easy / Medium / Hard
- **Expected Output** — Description of the correct or high-quality output
- **Metrics** — Which evaluation dimensions apply (NC, CC, CL, CQ)

---

## Story Structure

---

### NE-001

**Prompt:** Write a three-act story outline for a short film. The logline is: *A retired lighthouse keeper discovers that the signal she has been sending for forty years was never a distress call — it was a reply.*

**Domain:** Story Structure / Three-Act Framework  
**Difficulty:** Medium  
**Expected Output:** A structured outline with Act 1 (setup and inciting incident), Act 2 (rising conflict and midpoint reversal), and Act 3 (climax and resolution). The outline must logically account for the twist implied in the logline.  
**Metrics:** NC, CC, CL, CQ

**Reference Solution:**
- **Act 1:** Introduce the keeper, her isolated lighthouse, and the daily ritual of sending the signal. Establish her belief that the signal is a beacon of hope sent out to no one. Inciting incident: she intercepts a fragment of an incoming transmission.
- **Act 2:** She investigates the transmission's origin and discovers it predates her own arrival at the lighthouse. Midpoint: she realizes someone else sent the signal before her, and she has been answering it for forty years without knowing. Conflict escalates as she tries to decode who sent the original.
- **Act 3:** She decodes the original signal and finds it was sent by her mother, who disappeared at sea before her birth. Climax: she sends a final reply. Resolution: she leaves the lighthouse at peace, the signal finally complete.

---

### NE-002

**Prompt:** Given the following characters, identify who is the protagonist, who is the antagonist, and describe each character's arc in one sentence:
- Elena — a forensic accountant who discovers her firm has been laundering money
- Director Holt — the firm's founder, who built the firm on that money
- Marcus — Elena's colleague, who suspects something but has a family to protect

**Domain:** Character Arc / Role Assignment  
**Difficulty:** Easy  
**Expected Output:** Correct identification of protagonist (Elena), antagonist (Director Holt), and supporting character (Marcus), each with a clearly stated arc.  
**Metrics:** NC, CL, CQ

**Reference Solution:**
- **Protagonist:** Elena — arc: Elena transforms from a loyal employee following the rules into a whistleblower who risks her career and safety to expose the fraud.
- **Antagonist:** Director Holt — arc: Holt escalates from mentor to adversary as he works to suppress Elena's investigation to preserve the empire he built on crime.
- **Supporting:** Marcus — arc: Marcus moves from passive bystander to reluctant ally when the personal cost of inaction becomes greater than the personal cost of speaking up.

---

### NE-003

**Prompt:** Write three scene cards for consecutive scenes in a thriller. The story involves a detective who realizes mid-interrogation that the suspect she is questioning knows details only the actual killer would know — but the suspect is a child.

**Domain:** Scene Cards / Sequential Logic  
**Difficulty:** Hard  
**Expected Output:** Three scene cards, each containing: scene number, INT./EXT. and location, time of day, scene objective, conflict, and outcome. The cards must be causally connected and escalate tension.  
**Metrics:** NC, CC, CL, CQ

**Reference Solution:**

**Scene Card 1**
- Scene: 14
- Setting: INT. POLICE INTERROGATION ROOM — DAY
- Objective: Detective Rivera conducts a routine interview with a child witness.
- Conflict: The child answers routine questions without issue, but Rivera notices an unusual level of calm.
- Outcome: Rivera asks one specific question about the crime scene layout — the child answers correctly without prompting.

**Scene Card 2**
- Scene: 15
- Setting: INT. POLICE INTERROGATION ROOM — CONTINUOUS
- Objective: Rivera attempts to confirm whether the detail was leaked or genuine knowledge.
- Conflict: The child's answers become more precise, naming a detail that was never in any report or news coverage.
- Outcome: Rivera signals her partner outside via the mirror window; she keeps her composure but the dynamic of the room has shifted entirely.

**Scene Card 3**
- Scene: 16
- Setting: INT. OBSERVATION ROOM — CONTINUOUS
- Objective: Rivera's partner, Sergeant Tate, attempts to find an innocent explanation for the child's knowledge.
- Conflict: He checks the case file in real time — the detail the child cited was only ever known to the responding officers and the killer.
- Outcome: Tate picks up his radio. Rivera is alone in the room with the child.

---

## Dialogue

---

### NE-004

**Prompt:** Write a short screenplay scene (8–12 lines of dialogue) in which two former friends meet unexpectedly at a funeral. One of them knows a secret that would change everything the other believes about the person they are mourning. Neither of them says what they are really thinking.

**Domain:** Dialogue / Subtext  
**Difficulty:** Hard  
**Expected Output:** A formatted screenplay scene with INT./EXT. header, action lines, and character cues. Dialogue should demonstrate subtext — what is unsaid should be as meaningful as what is said. Characters should not explicitly state their conflict.  
**Metrics:** NC, CL, CQ

**Reference Solution:**

```
INT. CHURCH HALLWAY — DAY

The reception has moved inside. Quiet murmur of voices. CLAIRE, 
40s, stands near a window holding an untouched glass of water.
DANIEL, 40s, enters from the main hall. He stops when he sees her.

DANIEL
I didn't know you'd be here.

CLAIRE
I almost wasn't.

A beat. He crosses to stand near her. They both look out the window.

DANIEL
He talked about you. Near the end.

CLAIRE
(quietly)
I know.

DANIEL
Good things.

She doesn't respond. He turns to look at her profile.

CLAIRE
You stayed close with him.

DANIEL
I tried to.

CLAIRE
That was kind of you.

She finally looks at him. Something passes between them.

CLAIRE (CONT'D)
Were you there? At the end?

DANIEL
(a beat too long)
No.

She nods slowly. Looks back at the window.

CLAIRE
Neither was I.
```

---

### NE-005

**Prompt:** A character named Yusuf delivers a monologue to an empty room. He is speaking to someone who is no longer alive. Write the monologue (100–150 words). The emotional register is grief mixed with unresolved anger. Yusuf should not directly say "I miss you" or "I'm angry."

**Domain:** Dialogue / Monologue / Emotional Subtext  
**Difficulty:** Medium  
**Expected Output:** A monologue of 100–150 words that conveys grief and anger without stating either emotion directly. The subtext must be achievable through word choice, rhythm, and what is withheld.  
**Metrics:** NC, CL, CQ

**Reference Solution:**

```
YUSUF
I keep finding your things. A pen in a drawer I never open.
Your jacket on a hook I told you a hundred times was mine.

(beat)

I threw it out. The jacket. Last Tuesday. Took me six months 
to do it and I did it in about four seconds. Dropped it in 
the bin downstairs and went straight back up and made dinner 
like it was nothing.

(beat)

I should have said more. When I had the chance, I should have 
said more. But you always talked first and I always let you 
because it was easier.

(beat)

It's very quiet now.

I'm not sure what to do with that.
```

---

## Story Continuity

---

### NE-006

**Prompt:** The following two scene summaries are consecutive. Identify any continuity errors in the narrative logic and explain how to correct them.

**Scene 12 Summary:** Maya, carrying only a flashlight, enters the abandoned warehouse through a broken window. She finds a locked metal box on a workbench and pries it open with a crowbar she finds nearby. Inside is a photograph and a set of car keys.

**Scene 13 Summary:** Maya runs to the car park outside and uses the keys to find the matching vehicle. She loads the box into the car and drives away, turning the headlights on because it is daytime and the road is bright.

**Domain:** Narrative Continuity / Error Detection  
**Difficulty:** Easy  
**Expected Output:** Identification of the continuity error (turning on headlights because it is daytime is contradictory — headlights are used in low light, not bright daylight) and a corrected version of the relevant sentence.  
**Metrics:** NC, CL

**Reference Solution:**
- **Error identified:** "turning the headlights on because it is daytime and the road is bright" — this is internally contradictory. Headlights are activated in low-light conditions, not in bright daylight. The causal phrasing ("because it is daytime") inverts the logical trigger.
- **Correction:** Replace with "driving without headlights in the afternoon glare" or, if dramatic tension requires obscured visibility, revise Scene 13 to establish nighttime or overcast conditions that justify the headlights.
