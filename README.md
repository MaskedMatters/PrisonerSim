# 🔐 The 100 Prisoners Problem — Python Simulation

<p align="center">
  <img src="https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/status-active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/simulations-dynamic-orange?style=for-the-badge">
</p>

<p align="center">
  A simulation of one of the most fascinating probability puzzles — demonstrating how a clever strategy turns near-certain failure into a surprising ~31% success rate.
</p>

---

## 🧠 Overview

The **100 Prisoners Problem** is a well-known probability puzzle involving strategy, permutations, and surprisingly non-intuitive results.

* 100 prisoners are each assigned a unique number from **0 to 99**
* 100 boxes exist, each labeled **0 to 99**
* Each box contains a slip with a number (randomly shuffled, no duplicates)

### 🎯 Objective

Each prisoner must:

* Open **at most 50 boxes**
* Attempt to find the slip containing their own number
* Work **without communication**

### ⚠️ Outcome

* ✅ **All succeed** → Everyone is freed
* ❌ **One fails** → Everyone is executed

---

## 🔄 Optimal Strategy: Cycle Following

Rather than guessing randomly, prisoners use a deterministic approach:

1. Start with the box labeled with your number
2. Read the number inside
3. Go to the box labeled with that number
4. Repeat until:

   * You find your number
   * Or reach 50 attempts

This follows a **cycle in the permutation**.

---

## 📊 Probability Insight

| Strategy        | Success Rate |
| --------------- | ------------ |
| Random Guessing | ~0%          |
| Cycle Strategy  | ~31%         |

> The group only fails if a permutation contains a cycle longer than 50.

---

## 🐍 Python Simulation

This project simulates the problem to empirically verify the probability.

### ✨ Features

* **Configurable Simulations:** Choose how many simulations to run per instance.
* **Real-time Terminal UI:** Beautiful, color-coded, animated terminal updates.
* **Detailed Tracking:** Live tracking of successful runs, failed runs, and running percentages.
* **Lightweight:** Uses only standard library Python modules (no external dependencies).
* **CSV Exporting:** Save out your simulation results and timestamps directly to a CSV file from the interactive post-simulation menu.
* **Interactive Menu:** Easily rerun a fresh simulation or cleanly exit without navigating terminal history.
* **Advanced Batch Mode:** Secretly type `a` instead of a number at the main prompt to unlock automated batch execution, letting you seamlessly run multiple groups of simulations back-to-back with optional automatic CSV saving.

---

## ▶️ Getting Started

### 📦 Requirements

* Python 3.x

### 🚀 Run the Simulation

```bash
python main.py
```

---

## 🧪 Example Output

```
--- Prisoner Riddle Simulation ---
How many simulations do you want run? (Each with 100 prisoners): 1000

------------------------------------------
Percentage: 100% | Elapsed Time: 2s
Escaped Simulations: 315
Executed Simulations: 685

Escaped Percentage (Opposed to simulations ran): 31%
Escaped Percentage (Opposed to total simulations): 31%
------------------------------------------

Simulation Complete! What would you like to do?
1.) Export to CSV file
2.) Rerun a simulation
3.) Exit

> Creating/Updating simulation_runs.csv...
> Successfully exported logs to CSV!

Enter your choice (1/2/3): 
```

---

## 🧩 Code Structure

| Function         | Description                      |
| ---------------- | -------------------------------- |
| `random_array()` | Generates a shuffled permutation |
| `simulation()`   | Runs a single trial              |
| `simulations(n)` | Runs multiple trials with stats  |
| `main()`         | CLI interface                    |

---

## 📈 Expected Results

As the number of simulations increases, results converge to:

```
~31%
```

This matches the theoretical probability of the cycle-following strategy.

---

## 📊 Visualization (Concept)

A possible extension is visualizing permutation cycles:

```
0 → 42 → 17 → 0   (cycle length = 3)
1 → 88 → 5 → ...  (cycle length = 52 ❌ failure)
```

Any cycle longer than 50 causes failure.

---

## 🚀 Future Improvements

* 📊 Graph success rate over time
* 🌐 Web-based dashboard (real-time visualization)
* ⚡ Parallel simulation engine
* 🔀 Compare with random strategy

---

## 🎥 Inspiration

This problem was popularized by:

**Veritasium**
[https://youtu.be/iSNsgj1OCLA](https://youtu.be/iSNsgj1OCLA)

---

## 📜 License

MIT License

---

## ⭐ Contributing

Contributions, ideas, and optimizations are welcome.
Feel free to fork the project and submit a pull request.
