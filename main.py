import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    test = randomArray()
    print(len(test) == len(set(test)))
    print(test)

def populateArray():
    # Create a populated array of digits in order
    boxes = []

    for i in range(100):
        boxes.append(i)
    
    return boxes

def randomArray():
    # Create a populated array of random digits
    boxes = populateArray()

    # To randomize the array, we'll be taking two random values from the array, swapping them, and doing this a bunch of times.
    rand_box = 0
    temp = 0

    for i in range(1000):
        for j in range(100):
            rand_box = random.randint(0, 99)
            temp = boxes[j]
            boxes[j] = boxes[rand_box]
            boxes[rand_box] = temp 
    
    return boxes

def simulation():
    boxes = randomArray()

    for prisoner in range(100):
        slip = boxes[prisoner]

        for i in range(50):
            slip = boxes[slip]

            if slip == prisoner:
                break
        
        if slip != prisoner:
            break


if __name__ == "__main__":
    main()