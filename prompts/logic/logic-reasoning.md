# Logic Reasoning Prompts

This file contains prompts designed to evaluate logical reasoning across deductive, constraint-based, and conditional reasoning domains.

Each prompt includes:
- **Prompt** — The question submitted to the model
- **Domain** — Sub-category within logic reasoning
- **Difficulty** — Easy / Medium / Hard
- **Expected Answer** — Verified correct answer
- **Metrics** — Which evaluation dimensions apply (SV, CA, CC, ER, CL)

---

## Deductive Reasoning

---

### L-001

**Prompt:** All mammals are warm-blooded. All whales are mammals. Is a whale warm-blooded?

**Domain:** Deductive / Syllogism  
**Difficulty:** Easy  
**Expected Answer:** Yes  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Premise 1: All mammals are warm-blooded.
- Premise 2: All whales are mammals.
- Conclusion: All whales are warm-blooded. A specific whale is therefore warm-blooded. **Yes.**

---

### L-002

**Prompt:** No reptiles are warm-blooded. All snakes are reptiles. Can any snake be warm-blooded?

**Domain:** Deductive / Syllogism  
**Difficulty:** Easy  
**Expected Answer:** No  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Premise 1: No reptiles are warm-blooded.
- Premise 2: All snakes are reptiles.
- Conclusion: No snakes are warm-blooded. **No.**

---

### L-003

**Prompt:** If it is raining, Alice carries an umbrella. It is not raining. Does Alice carry an umbrella?

**Domain:** Deductive / Conditional  
**Difficulty:** Medium  
**Expected Answer:** Cannot be determined  
**Metrics:** SV, CA, CC, CL

**Solution:**
- The statement "if raining → umbrella" does not imply "if not raining → no umbrella."
- This is the fallacy of denying the antecedent.
- Alice may carry an umbrella for other reasons.
- **Cannot be determined** from the given premises.

---

## Constraint Satisfaction

---

### L-004

**Prompt:** Alice, Bob, and Carol each choose a different color from red, blue, and green. Alice does not choose red. Bob chooses blue. What color does Alice choose?

**Domain:** Constraint Satisfaction  
**Difficulty:** Easy  
**Expected Answer:** Green  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Bob chooses blue → blue is taken.
- Alice does not choose red → Alice chooses green or blue.
- Blue is taken, so Alice chooses **green**.
- Carol gets red.

---

### L-005

**Prompt:** Five people sit in a row. Amy sits to the left of Ben. Ben sits to the left of Cara. Dan sits to the right of Cara. Eve sits between Amy and Ben. What is the order from left to right?

**Domain:** Constraint Satisfaction / Ordering  
**Difficulty:** Medium  
**Expected Answer:** Amy, Eve, Ben, Cara, Dan  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Amy is left of Ben; Eve is between Amy and Ben → Amy, Eve, Ben
- Ben is left of Cara → Amy, Eve, Ben, Cara
- Dan is right of Cara → Amy, Eve, Ben, Cara, Dan
- Order: **Amy, Eve, Ben, Cara, Dan**

---

### L-006

**Prompt:** In a tournament, each team plays every other team exactly once. There are 6 teams. How many total games are played?

**Domain:** Combinatorics / Logic  
**Difficulty:** Medium  
**Expected Answer:** 15  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Total games = C(6, 2) = 6! / (2! × 4!) = (6 × 5) / 2 = **15**

---

## Conditional and Hypothetical Reasoning

---

### L-007

**Prompt:** If a shape is a square, then it is a rectangle. Shape X is a rectangle. Is Shape X a square?

**Domain:** Conditional Reasoning  
**Difficulty:** Medium  
**Expected Answer:** Cannot be determined  
**Metrics:** SV, CA, CC, CL

**Solution:**
- "Square → rectangle" does not mean "rectangle → square."
- Shape X being a rectangle is consistent with it being a square or not.
- **Cannot be determined** from the premises.

---

### L-008

**Prompt:** All of the following statements are true: (1) If the alarm rings, Maya wakes up. (2) If Maya wakes up, she makes coffee. (3) The alarm rang. Does Maya make coffee?

**Domain:** Conditional Chain  
**Difficulty:** Easy  
**Expected Answer:** Yes  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Alarm rang → Maya wakes up (from 1 and 3)
- Maya wakes up → she makes coffee (from 2)
- Conclusion: **Yes**, Maya makes coffee.

---

## Lateral and Puzzle Reasoning

---

### L-009

**Prompt:** You have a 3-liter jug and a 5-liter jug with no measurement markings. How do you measure exactly 4 liters of water?

**Domain:** Puzzle / Lateral Reasoning  
**Difficulty:** Medium  
**Expected Answer:** Fill 5L, pour into 3L (leaving 2L in 5L); empty 3L; pour 2L into 3L; fill 5L again; pour from 5L into 3L until full (only 1L fits); 5L jug now has exactly 4L.  
**Metrics:** SV, CA, CC, CL

**Solution:**
1. Fill the 5L jug.
2. Pour from 5L into 3L until full → 5L has 2L, 3L has 3L.
3. Empty the 3L jug.
4. Pour the 2L from 5L into 3L → 3L has 2L.
5. Fill the 5L jug again.
6. Pour from 5L into 3L until full → 3L needs 1 more liter → 5L jug now has **4L**.

---

### L-010

**Prompt:** A farmer needs to cross a river with a fox, a chicken, and a bag of grain. His boat holds only himself and one item. If left alone, the fox eats the chicken, and the chicken eats the grain. How does he get everything across safely?

**Domain:** Puzzle / State-Space Reasoning  
**Difficulty:** Hard  
**Expected Answer:** (See solution below)  
**Metrics:** SV, CA, CC, CL

**Solution:**
1. Take the chicken across. Return alone.
2. Take the fox across. Return with the chicken.
3. Take the grain across. Return alone.
4. Take the chicken across.
- At no point are the fox+chicken or chicken+grain left unsupervised on the same side.
