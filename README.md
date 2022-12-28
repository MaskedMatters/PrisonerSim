# PrisonerSim

A simulation of a riddle where there are 100 prisoners each with their own number. They each have one turn to go in a room with 100 boxes all labeled with numbers. Inside of each box is a slip with a number 1-100 and no repeats. The slip in the box does not match the number on the box. The prisoner will be able to open 50 boxes and try to find their slip. If one person doesn't find it, they all get executed. If they all find it, they are freed. What is their best strategy?

**SPOILER------------------------------------------------------------------------------**

The best strategy known right now is the loop strategy. Each prisoner would go in and open the box that matches their number and open it. If the slip != their number they will go to the box with the number that matches the slip the prisoner just found. Once the prisoner finds the slip they can leave. If the first box open = their number they found their slip and can leave.

The Statistics:

Doing the guessing strategy the odds that they all find their slip is the same as two people finding the same grain of sand out of every single sand grain on earth. (0.00000000000000000000000000008%)

With the loop strategy they can get their success percentage all the way up to 31%

To look at the code you must have Visual Studio installed (Not to be confused with VS Code!!). Then, you can open up the SOLUTION along with all of the other files. Open the SOLUTION first and it will create the nice layout in Visual Studio (The SOLUTION ends in the file type ".sln").

**Credit to Youtube Channel Veritasium for the idea & statistics!!**
Youtube Video: https://youtu.be/iSNsgj1OCLA
