# 🏆 Tournament Result Calculator

This Python script helps calculate and rank team performance in a multi-match tournament (e.g., Free Fire, PUBG) based on **position points**, **kill points**, **Booyah wins (1st place)**, and **tie-breaking rules**.

---

## 📌 Features

- Takes input for tournament details.
- Accepts custom point values for each position.
- Allows setting point value per kill.
- Supports multiple matches.
- Calculates and displays:
  - Total points
  - Kill points
  - Booyah count (1st place finishes)
  - Final ranking with tie-breaking rules.

---

## 🧠 Tie-Breaking Rules

If multiple teams have the same total points, the following tie-breakers are applied **in order**:

1. **Booyah Count**: Team with more 1st place finishes ranks higher.
2. **Kill Points**: Team with more kill points ranks higher.
3. **Last Match Position**: Team with a better position(lower rank) in last match ranks higher.

This ensures fair ranking even when scores are very close.

---

## 🚀 How to Run

Make sure you have Python installed. Then run:

```bash
python main.py
