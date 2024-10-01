import random

def main():
    # Create a list to hold the box contents
    boxes = list(range(100))
    random.shuffle(boxes)  # Shuffle the box contents to randomize

    all_found = True
    slips_found = 0

    for prisoner in range(100):
        slip = prisoner  # Each prisoner starts looking at their own number
        found = False  # Flag to track if the prisoner found their slip

        for _ in range(50):
            if boxes[slip] == prisoner:
                found = True  # Found their own slip
                break  # Stop looking
            slip = boxes[slip]  # Move to the next slip based on the current one

        if not found:
            all_found = False  # If the prisoner did not find their own slip
            break
        
        slips_found += 1  # Count how many prisoners found their slips

    print(f"Slips Found: {slips_found}, Escape: {all_found}")

if __name__ == "__main__":
    main()
