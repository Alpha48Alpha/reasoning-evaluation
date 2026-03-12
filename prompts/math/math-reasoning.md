# Math Reasoning Prompts

This file contains prompts designed to evaluate mathematical reasoning across arithmetic, algebra, and word problem domains.

Each prompt includes:
- **Prompt** — The question submitted to the model
- **Domain** — Sub-category within math reasoning
- **Difficulty** — Easy / Medium / Hard
- **Expected Answer** — Verified correct answer
- **Metrics** — Which evaluation dimensions apply (SV, CA, CC, ER, CL)

---

## Rate, Distance, and Time

---

### M-001

**Prompt:** A car travels 60 mph for 2 hours and 30 mph for 1 hour. What is the total distance?

**Domain:** Rate/Distance/Time  
**Difficulty:** Easy  
**Expected Answer:** 150 miles  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Distance at 60 mph: 60 × 2 = 120 miles
- Distance at 30 mph: 30 × 1 = 30 miles
- Total: 120 + 30 = **150 miles**

---

### M-002

**Prompt:** Two trains leave stations 300 miles apart at the same time, traveling toward each other. Train A travels at 80 mph and Train B travels at 70 mph. How long until they meet?

**Domain:** Rate/Distance/Time  
**Difficulty:** Medium  
**Expected Answer:** 2 hours  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Combined speed: 80 + 70 = 150 mph
- Time to meet: 300 ÷ 150 = **2 hours**

---

### M-003

**Prompt:** A runner completes the first half of a race at 6 mph and the second half at 4 mph. What is her average speed for the entire race?

**Domain:** Rate/Distance/Time  
**Difficulty:** Medium  
**Expected Answer:** 4.8 mph  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Let total distance = 2d
- Time for first half: d/6
- Time for second half: d/4
- Total time: d/6 + d/4 = 2d/12 + 3d/12 = 5d/12
- Average speed: 2d ÷ (5d/12) = 2d × 12/5d = **24/5 = 4.8 mph**

---

## Proportional Reasoning

---

### M-004

**Prompt:** If 5 workers can build a wall in 8 days, how many days will it take 10 workers to build the same wall, assuming constant work rate?

**Domain:** Proportional Reasoning  
**Difficulty:** Easy  
**Expected Answer:** 4 days  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Total work = 5 × 8 = 40 worker-days
- With 10 workers: 40 ÷ 10 = **4 days**

---

### M-005

**Prompt:** A recipe requires 3 cups of flour for 24 cookies. How many cups of flour are needed for 60 cookies?

**Domain:** Proportional Reasoning  
**Difficulty:** Easy  
**Expected Answer:** 7.5 cups  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Flour per cookie: 3 ÷ 24 = 0.125 cups
- For 60 cookies: 0.125 × 60 = **7.5 cups**

---

## Algebra

---

### M-006

**Prompt:** The sum of two consecutive even integers is 46. What are the two integers?

**Domain:** Algebra  
**Difficulty:** Easy  
**Expected Answer:** 22 and 24  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Let the integers be n and n+2
- n + (n+2) = 46
- 2n + 2 = 46
- 2n = 44
- n = 22
- Integers: **22 and 24**

---

### M-007

**Prompt:** A store sells a jacket at a 25% discount from the original price of $120. After the discount, an 8% tax is applied. What is the final price?

**Domain:** Algebra / Percentage  
**Difficulty:** Medium  
**Expected Answer:** $97.20  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Discounted price: 120 × (1 - 0.25) = 120 × 0.75 = $90
- After tax: 90 × (1 + 0.08) = 90 × 1.08 = **$97.20**

---

## Arithmetic and Number Sense

---

### M-008

**Prompt:** What is the remainder when 157 is divided by 12?

**Domain:** Arithmetic  
**Difficulty:** Easy  
**Expected Answer:** 1  
**Metrics:** SV, CA, CL

**Solution:**
- 157 ÷ 12 = 13 remainder 1
- 12 × 13 = 156; 157 - 156 = **1**

---

### M-009

**Prompt:** A number is tripled and then 15 is subtracted. The result is 48. What is the original number?

**Domain:** Arithmetic / Algebra  
**Difficulty:** Easy  
**Expected Answer:** 21  
**Metrics:** SV, CA, CC, CL

**Solution:**
- 3x - 15 = 48
- 3x = 63
- x = **21**

---

### M-010

**Prompt:** What is the greatest common divisor (GCD) of 48 and 36?

**Domain:** Number Theory  
**Difficulty:** Easy  
**Expected Answer:** 12  
**Metrics:** SV, CA, CC, CL

**Solution:**
- 48 = 2⁴ × 3
- 36 = 2² × 3²
- GCD = 2² × 3 = **12**
