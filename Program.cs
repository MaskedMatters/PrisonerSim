using PrisonerSim;

// Ask how many simulations to run
Console.Write("Prisonor Simulation Count (How many simulations?): ");

// Making sure the input is valid
if (int.TryParse(Console.ReadLine(), out int simulationsToRun))
{
    if (simulationsToRun == 0)
    {   
        // simToRun can't be 0
        Console.WriteLine("Bad Input");
        return;
    }

    if (simulationsToRun == 1)
    {   
        // Not plural for 1 simulation
        Console.WriteLine("Running {0} Simulation", simulationsToRun);
    } 
    else
    {   
        // Plural for !1 simulation
        Console.WriteLine("Running {0} Simulations", simulationsToRun);
    }

}
else
{   
    // Anything else is a bad input
    Console.WriteLine("Bad Input");
    return;
}

int slipsF = 0; // Slips Found
int slipsNF = 0; // Slips Not Found
int simulationSuccess = 0;


for (int simulations = 0; simulations < simulationsToRun; simulations++)
{
    int tempSlipsF = startSimulation(); // Slips Found Per Run
    int tempSlipsNF = 100 - tempSlipsF; // Slips Not Found Per Run

    if (tempSlipsF == 100)
    {   
        // Everytime everyone finds their slip per simulation, add 1 to simulationSucces
        simulationSuccess++;
    }

    slipsF = slipsF + tempSlipsF; // Total slips found being added
    slipsNF = slipsNF + tempSlipsNF; // Total slips found being added

    ConsoleUtility.WritePercentage((float)simulations / (simulationsToRun / 100)); // Write Percentage
}

// RESET CURSOR ----------------------------------------------------------------------------
Console.CursorVisible = true;

Console.SetCursorPosition(0, 3);
Console.Write("100%");

Console.SetCursorPosition(0, 5);
// RESET CURSOR ----------------------------------------------------------------------------

// All Statistics from Simulation
Console.WriteLine("Slips Found: {0} | Slips Not Found: {1}", slipsF, slipsNF);
Console.WriteLine("Successes: {0} out of {1}", simulationSuccess, simulationsToRun);
Console.WriteLine("Success Rate (Percentage): {0}%", ((1.0 * simulationSuccess) / simulationsToRun * 100));

Console.WriteLine("");

Console.WriteLine("Press any key to exit...");

Console.ReadKey();

public static partial class Program
{
    public static int[] createPopulatedArray()
    {
        int[] popArray = new int[100];

        // Populate Array By Looping
        for(int i = 0; i < popArray.Length; i++)
        {
            popArray[i] = i;
        }

        return popArray; // Return populated array

    }

    public static int[] randomizePopulatedArray()
    {
        Random rand = new Random(); // Random Library

        int[] randArray = createPopulatedArray(); // Get Populated Array

        int temp; // Temporary Storage
        int swapNum; // Swap Number 

        for(int j = 0; j < 500; j++)
        {
            for(int i = 0; i < 100; i++)
            {
                swapNum = rand.Next(100); // Gets random number
                temp = randArray[i]; // Stores value _ of randArray
                randArray[i] = randArray[swapNum]; // Changes _ of randArray to randArray[swapNum]
                randArray[swapNum] = temp; // randArray[swapNum] becomes value _ of randArray
            }
        }

        return randArray; // Return Randomized Populated Array

    }

    public static int startSimulation()
    {
        int[] boxes = randomizePopulatedArray(); // Gets Randomized Populated Array

        int slipsF = 0; // Slips Found Per Simulation (aka tempSlipsF)

        for (int prisoner = 0; prisoner < 100; prisoner++)
        {

            int slip = boxes[prisoner]; // Current Slip = boxes[prisoner]
            int attempts = 1; // Add 1 attempt

            while (attempts <= 50)
            {
                if (slip == prisoner)
                {   
                    // Check if slip = prisoner
                    slipsF++;
                    break;
                }

                // Follow Loop of Slips
                slip = boxes[slip]; 
                attempts++;
            }

        }

        return slipsF; // Return Slips Found Per Simulation (aka tempSlipF)
    }
}