# IMPORT ALL LIBRARIES AND MODULES
import os
import subprocess
import time
import random
import csv
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    CLEAR_LINE = '\033[K'

# CREATE CLEAR FUNCTION
def clear():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

# BRING CURSOR UP ONE LINE IN TERMINAL
def cursor_up(lines):
    print("\033[A" * lines, end="")

# BRING CURSOR DOWN ONE LINE IN TERMINAL
def cursor_down(lines):
    print("\033[B" * lines, end="")

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
        print(f"{Colors.OKBLUE}------------------------------------------{Colors.CLEAR_LINE}{Colors.ENDC}")
        print(f"{Colors.BOLD}Percentage: {round(((i+1)/count) * 100)}% | Elapsed Time: {round(time.time() - sim_start_time)}s{Colors.CLEAR_LINE}{Colors.ENDC}")
        print(f"{Colors.OKGREEN}Escaped Simulations: {escapes}{Colors.CLEAR_LINE}{Colors.ENDC}")
        print(f"{Colors.FAIL}Executed Simulations: {executions}{Colors.CLEAR_LINE}{Colors.ENDC}")
        print(f"{Colors.CLEAR_LINE}")
        print(f"{Colors.OKCYAN}Escaped Percentage (Opposed to simulations ran): {round(escapes/(i + 1) * 100)}%{Colors.CLEAR_LINE}{Colors.ENDC}")
        print(f"{Colors.OKCYAN}Escaped Percentage (Opposed to total simulations): {round(escapes/count * 100)}%{Colors.CLEAR_LINE}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}------------------------------------------{Colors.CLEAR_LINE}{Colors.ENDC}")

        if i < count - 1:
            cursor_up(8)
            
    return {
        'count': count,
        'escapes': escapes,
        'executions': executions,
        'elapsed': time.time() - sim_start_time,
        'end_time': datetime.now().isoformat()
    }

def save_stats_to_csv(stats):
    end_time_str = stats['end_time']
    file_exists = os.path.isfile("simulation_runs.csv")
    already_saved = False
    
    if file_exists:
        with open("simulation_runs.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[-1] == end_time_str:
                    already_saved = True
                    break
                    
    if already_saved:
        return False, f"{Colors.FAIL}> Error: This simulation run has already been saved to CSV!{Colors.ENDC}"
        
    with open("simulation_runs.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Simulations Ran", "Escapes", "Executions", "Elapsed Time (s)", "End Timestamp"])
        writer.writerow([stats['count'], stats['escapes'], stats['executions'], round(stats['elapsed'], 2), end_time_str])
        
    return True, f"{Colors.OKGREEN}> Successfully exported logs to CSV!{Colors.ENDC}"

# CREATE CLI/UI THING FOR THE PERSON TO DO THINGS...
def main():
    while True:
        clear()

        print(f"{Colors.HEADER}{Colors.BOLD}--- Prisoner Riddle Simulation ---{Colors.ENDC}")
        user_input = input(f"{Colors.WARNING}How many simulations do you want run? (Each with 100 prisoners): {Colors.ENDC}").strip().lower()
        
        is_advanced = False
        repeats = 1
        auto_save = False
        
        if user_input == 'a':
            is_advanced = True
            try:
                simulation_count = int(input(f"{Colors.OKCYAN}How many simulations do you want to run per batch?: {Colors.ENDC}"))
                repeats = int(input(f"{Colors.OKCYAN}How many repeats of the simulation do you want to run?: {Colors.ENDC}"))
            except ValueError:
                print(f"{Colors.FAIL}Values must be numbers, please try again!{Colors.ENDC}")
                time.sleep(1)
                continue
                
            save_choice = input(f"{Colors.OKCYAN}Do you want to automatically save each batch to CSV? (y/n): {Colors.ENDC}").strip().lower()
            if save_choice in ['y', 'yes', 'true']:
                auto_save = True
        else:
            try:
                simulation_count = int(user_input)
            except ValueError:
                print(f"{Colors.FAIL}Value must be a number, please try again!{Colors.ENDC}")
                time.sleep(1)
                continue

        print("")
        
        if is_advanced:
            for r in range(repeats):
                print(f"{Colors.HEADER}{Colors.BOLD}--- Batch {r+1}/{repeats} ---{Colors.ENDC}")
                stats = simulations(simulation_count)
                
                print("") # Space between stats and logs
                
                if auto_save:
                    # Animate slightly so it looks the same as usual
                    print(f"{Colors.WARNING}> Creating/Updating simulation_runs.csv...{Colors.ENDC}")
                    time.sleep(0.5)
                    success, log_msg = save_stats_to_csv(stats)
                    print(log_msg)
                else:
                    print(f"{Colors.WARNING}> Batch {r+1} finished. (Not saved to CSV){Colors.ENDC}")
                    
                print("") # Spacing before next batch
                
            print(f"{Colors.HEADER}{Colors.BOLD}All {repeats} batches completed!{Colors.ENDC}")
            input(f"{Colors.WARNING}Press Enter to return to main menu...{Colors.ENDC}")
            continue
            
        else:
            stats = simulations(simulation_count)
            
            print("\033[s", end="")  # Save cursor position immediately after stats
            logs = []
            
            def draw_menu():
                print("\033[u\033[J", end="")  # Restore cursor and clear below
                print(f"\n{Colors.HEADER}{Colors.BOLD}Simulation Complete! What would you like to do?{Colors.ENDC}")
                print(f"{Colors.OKGREEN}1.) Export to CSV file{Colors.ENDC}")
                print(f"{Colors.OKCYAN}2.) Rerun a simulation{Colors.ENDC}")
                print(f"{Colors.FAIL}3.) Exit{Colors.ENDC}\n")
                
                if logs:
                    for log in logs:
                        print(log)
                
                print("") # space before input
                    
            while True:
                draw_menu()
                
                choice = input(f"{Colors.WARNING}Enter your choice (1/2/3): {Colors.ENDC}")
                
                if choice == '1':
                    logs = [f"{Colors.WARNING}> Creating/Updating simulation_runs.csv...{Colors.ENDC}"]
                    draw_menu()
                    time.sleep(0.5)
                    success, log_msg = save_stats_to_csv(stats)
                    logs.append(log_msg)
                elif choice == '2':
                    break # breaks inner loop, restarts simulation
                elif choice == '3':
                    print(f"\n{Colors.OKBLUE}Exiting...{Colors.ENDC}")
                    return # exits main()
                else:
                    logs = [f"{Colors.FAIL}> Invalid choice, please enter 1, 2, or 3.{Colors.ENDC}"]

if __name__ == "__main__":
    main()