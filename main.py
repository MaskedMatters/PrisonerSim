# IMPORT ALL LIBRARIES AND MODULES
import os
import time
import math
import random
import datetime as dt

# CREATE CLEAR FUNCTION
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# BRING CURSOR UP ONE LINE IN TERMINAL
def cursor_up(lines):
    print("\033[A" * lines)

# POPULATE A LIST WITH RANDOM, NON-REPEATING, INTEGERS FROM 0-99
def random_array():
    array = list(range(100))
    random.shuffle(array)

    return array

# RUN 1 ITERATION OF A SIMULATION
def simulation():
    boxes = random_array()                                      # POPULATE THE ARRAY OF BOXES
    slips_found = 0                                             # INSTANTIATE THE VARIABLE THAT HOLD HOW MANY SLIPS HAVE BEEN FOUND

    for prisoner in range(100):                                 # ITERATE THROUGH 100 PRISONERS
        slip = prisoner                                         # LET THE FIRST SLIP BE THE PRISONER # (LOOK AT THE BOX WITH PRISONERS #)
        found = False                                           # INSTANTIATE A FOUND FLAG

        for _ in range(50):                                     # GIVE THE PRISONER 50 TRIES TO FIND THEIR SLIP
            if boxes[slip] == prisoner:                         # IF THE PRISONER FOUND THEIR SLIP...
                found = True                                          # CHANGE THE FOUND FLAG TO TRUE
                break                                                 # BREAK OUT OF THE LOOP

            slip = boxes[slip]                                  # ELSE, LOOK AT THE NEXT BOX

        if not found:                                           # IF THE PRISONER NEVER FOUND THEIR SLIP... (found flag default false)
            break                                                     # BREAK OUT OF THE LOOP (next prisoner goes)

        slips_found += 1                                        # ADD TO THE SLIPS FOUND VARIABLE

    return True if slips_found == 100 else False                # IF ALL PRISONERS FIND THEIR SLIP, THEY SUCCEED, RETURN TRUE, ELSE FALSE

# FUNCTION TO ORCHESTRATE THE SIMULATIONS TO RUN (with data)
def simulations(count):
    escapes = 0                                                 # LET AMOUNT OF ESCAPES BE 0
    executions = 0                                              # LET AMOUNT OF EXECUTIONS BE 0

    sim_start_time = time.time()                                # LET START TIME FOR SIMULATION BE NOW

    for i in range(count):                                      # LOOP THROUGH EVERY SIMULATION
        output = simulation()                                   # LET OUTPUT BE TRUE IF THEY SUCCEEDED, ELSE FALSE
        escapes += 1 if output else 0
        executions += 1 if not output else 0

        # CALCULATE PERCENTAGE COMPLETED AND PERCENTAGE SUCCEEDED
        print("------------------------------------------")
        print("Percentage: " + str(round((i/count) * 100)) + "% | Elapsed Time: " + str(round(time.time() - sim_start_time)))
        print("Escaped Simulations: " + str(escapes))
        print("Executed Simulations: " + str(executions))
        print("")
        print("Escaped Percentage (Opposed to simulations ran): " + str(round(escapes/(i + 1) * 100)) + "%")
        print("Escaped Percentage (Opposed to total simulations): " + str(round(escapes/count * 100)) + "%")
        print("------------------------------------------")

        cursor_up(9)

# CREATE CLI/UI THING FOR THE PERSON TO DO THINGS...
def main():
    clear()

    print("--- Prisoner Riddle Simulation ---")
    try:
        simulation_count = int(input("How many simulations do you want run? (Each with 100 prisoners): "))
    except ValueError:
        print("Value must be a number, please try again!")
        time.sleep(1)
        clear()
        main()

    print("")
    simulations(simulation_count)

if __name__ == "__main__":
    main()