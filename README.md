### The 100 Prisoners Riddle

Imagine a riddle involving 100 prisoners, each assigned a unique number. They face a daunting challenge: in a room filled with 100 boxes—each labeled with a number—each box contains a slip of paper bearing a number from 1 to 100, with no duplicates. Crucially, the slip inside each box does not correspond to the box's label.

Each prisoner has the opportunity to open up to 50 boxes in a bid to locate their own slip. If even one prisoner fails to find their slip, the entire group faces execution. Conversely, if they all succeed, they are set free. What strategy should they adopt to maximize their chances?

---

### The Optimal Strategy: The Loop Method

The most effective strategy identified so far is known as the "loop strategy." Here's how it works:

1. Each prisoner starts by opening the box corresponding to their own number.
2. If the slip inside is not their number, they take note of the number on that slip and proceed to open the box labeled with that new number.
3. This process continues, with each prisoner following the chain until they either find their own slip or exhaust their 50 chances.

If the prisoner opens a box and finds their own slip on the first try, they can leave immediately.

---

### The Statistics

Under a purely random guessing strategy, the probability that all prisoners find their slips is astronomically low—comparable to the odds of two people finding the same grain of sand among all the grains on Earth (approximately 0.00000000000000000000000000008%).

In stark contrast, by employing the loop strategy, their success rate rises significantly to about 31%.

---

### Additional Information

To explore the accompanying code for this riddle, ensure you have Visual Studio installed (not to be confused with VS Code). Open the solution file (ending in ".sln") to access the project structure neatly organized in Visual Studio.

**Credit:** This riddle and its intriguing statistics were inspired by the YouTube channel Veritasium. For a deeper dive, check out their video: [Veritasium's Video](https://youtu.be/iSNsgj1OCLA).

---