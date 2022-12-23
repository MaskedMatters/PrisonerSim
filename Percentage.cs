namespace PrisonerSim
{
    public static class ConsoleUtility
    {
        public static void WritePercentage(float percent)
        {
            int percentInt;

            if (float.IsNaN(percent))
                percentInt = 0;
            else if (float.IsInfinity(percent))
                percentInt = 0;
            else if (percent < 0)
                percentInt = 0;
            else
                percentInt = Convert.ToInt32(percent);

            Console.CursorVisible = false; // Set cursor visibility to false

            Console.SetCursorPosition(0, 3); // Start cursor at start of line

            Console.Write(percentInt + "%"); // Write the percentage
        }
    }
}