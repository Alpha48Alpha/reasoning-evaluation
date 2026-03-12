# Multi-Step Reasoning Prompts

This file contains prompts that require multiple chained reasoning steps to solve. These prompts test a model's ability to maintain state, apply sequential reasoning, and combine multiple concepts.

Each prompt includes:
- **Prompt** — The question submitted to the model
- **Domain** — Sub-category within multi-step reasoning
- **Difficulty** — Easy / Medium / Hard
- **Expected Answer** — Verified correct answer
- **Metrics** — Which evaluation dimensions apply (SV, CA, CC, ER, CL)

---

## Sequential Calculation

---

### MS-001

**Prompt:** A store starts the day with 200 items in stock. In the morning, they sell 45 items and receive a delivery of 80 items. In the afternoon, they sell 30% of the current stock. How many items remain at the end of the day?

**Domain:** Sequential Calculation  
**Difficulty:** Medium  
**Expected Answer:** 165 items (assuming fractional items are rounded down at point of sale)  
**Metrics:** SV, CA, CC, CL

**Solution:**
- After morning sales: 200 - 45 = 155
- After delivery: 155 + 80 = 235
- Afternoon sales: 235 × 0.30 = 70.5 → 70 items sold (rounding down whole items)
- Remaining: 235 - 70 = **165 items**

*Note: If the problem expects exact decimal arithmetic without rounding, the answer is 235 × 0.70 = **164.5 items**. For whole-item inventory, round to **164 or 165** depending on rounding convention. Models should state the rounding assumption.*

---

### MS-002

**Prompt:** A tank is filled to 60% of its 500-liter capacity. Water is drained at 20 liters/minute for 5 minutes, then water is added at 15 liters/minute for 8 minutes. What percentage of the tank's capacity is filled at the end?

**Domain:** Sequential Calculation  
**Difficulty:** Medium  
**Expected Answer:** 64%  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Initial volume: 500 × 0.60 = 300 liters
- After draining (5 min at 20 L/min): 300 - (20 × 5) = 300 - 100 = 200 liters
- After adding (8 min at 15 L/min): 200 + (15 × 8) = 200 + 120 = 320 liters
- Final percentage: 320 / 500 = **64%**

---

### MS-003

**Prompt:** Alice earns $15/hour. She works 8 hours on Monday, 6 hours on Tuesday, and 10 hours on Wednesday. She spends 30% of her total earnings on rent and saves the rest. How much does she save?

**Domain:** Sequential Calculation / Percentage  
**Difficulty:** Easy  
**Expected Answer:** $252  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Total hours: 8 + 6 + 10 = 24 hours
- Total earnings: 24 × $15 = $360
- Rent: $360 × 0.30 = $108
- Savings: $360 - $108 = **$252**

---

## Combined Concepts

---

### MS-004

**Prompt:** A car depreciates in value by 15% per year. It was purchased for $20,000. After 3 years, the owner sells it for $13,000. Did the owner sell it above or below the depreciated value, and by how much?

**Domain:** Compound Percentage / Comparison  
**Difficulty:** Medium  
**Expected Answer:** Above by approximately $717.50  
**Metrics:** SV, CA, CC, CL

**Solution:**
- After year 1: $20,000 × 0.85 = $17,000
- After year 2: $17,000 × 0.85 = $14,450
- After year 3: $14,450 × 0.85 = $12,282.50 (rounded)
- More precisely: $20,000 × (0.85)³ = $20,000 × 0.614125 = **$12,282.50**
- Owner sold for $13,000; depreciated value is $12,282.50
- Sold **above** depreciated value by $13,000 - $12,282.50 = **$717.50**

---

### MS-005

**Prompt:** A bag contains 4 red balls, 3 blue balls, and 2 green balls. You draw one ball without looking, note its color, put it back, and then draw again. What is the probability that both draws are the same color?

**Domain:** Probability / Multi-Step  
**Difficulty:** Medium  
**Expected Answer:** 29/81  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Total balls: 4 + 3 + 2 = 9
- P(both red): (4/9) × (4/9) = 16/81
- P(both blue): (3/9) × (3/9) = 9/81
- P(both green): (2/9) × (2/9) = 4/81
- P(same color): 16/81 + 9/81 + 4/81 = **29/81 ≈ 35.8%**

---

## Chained Inference

---

### MS-006

**Prompt:** A library has three floors. The second floor has twice as many books as the first floor. The third floor has 500 fewer books than the second floor. The total across all floors is 4,500 books. How many books are on each floor?

**Domain:** Algebra / Chained Inference  
**Difficulty:** Medium  
**Expected Answer:** Floor 1: 1,000; Floor 2: 2,000; Floor 3: 1,500  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Let floor 1 = x
- Floor 2 = 2x
- Floor 3 = 2x - 500
- Total: x + 2x + (2x - 500) = 4,500
- 5x - 500 = 4,500
- 5x = 5,000
- x = 1,000
- Floor 1: **1,000**, Floor 2: **2,000**, Floor 3: **1,500**

---

### MS-007

**Prompt:** Team A wins 60% of its games in a season of 40 games. Team B wins 55% of its games in a season of 60 games. Which team won more total games, and by how many?

**Domain:** Percentage / Comparison  
**Difficulty:** Easy  
**Expected Answer:** Team B by 9 games  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Team A wins: 40 × 0.60 = 24 games
- Team B wins: 60 × 0.55 = 33 games
- Team B won more by 33 - 24 = **9 games**

---

### MS-008

**Prompt:** A cyclist travels from Town A to Town B, a distance of 90 km. She rides the first 30 km at 15 km/h, rests for 30 minutes, then rides the remaining 60 km at 20 km/h. What is her total travel time including the rest?

**Domain:** Rate/Distance/Time / Multi-Segment  
**Difficulty:** Medium  
**Expected Answer:** 5.5 hours  
**Metrics:** SV, CA, CC, CL

**Solution:**
- Time for first 30 km: 30 / 15 = 2 hours
- Rest: 0.5 hours
- Time for remaining 60 km: 60 / 20 = 3 hours
- Total: 2 + 0.5 + 3 = **5.5 hours**
