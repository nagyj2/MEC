#!/usr/local/bin/python3
import connection_library

def wait_for_cook_input():
    command_string = raw_input("Input (foodID1, foodID2.... -> )")
    food_arr = [word.strip() for word in command_string.split(',')]
    print(food_arr)


def main():
    print("Running cookside....")
    wait_for_cook_input()


if __name__ == "__main__":
    db = Connection()
    db.opencnx()
        
        
    db.closecnx()
