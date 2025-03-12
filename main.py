import random  # Importing the random module for generating random ship positions
import Check_input  # Importing custom module for user input validation


def display_board(board):
    print("  1 2 3 4 5")  # Column numbers
    for i, row in enumerate(board):
        print(chr(65 + i), " ".join(row))  # Row labels (A-E) and board contents


def reset_game():
    board = [['~' for _ in range(5)] for _ in range(5)]  # Creates a 5x5 grid filled with water (~)

    # Randomly selects a starting position for the 2x2 ship within bounds
    row = random.randint(0, 3)
    col = random.randint(0, 3)

    # Defines the 2x2 ship's coordinates
    solution = [(row, col), (row, col + 1), (row + 1, col), (row + 1, col + 1)]

    return board, solution  # Returns the game board and the ship's coordinates


def get_row():
    row_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}  # Maps letters to indices
    while True:
        row_input = input("Enter row (A-E): ").upper()  # Converts input to uppercase
        if row_input in row_mapping:
            return row_mapping[row_input]  # Returns the corresponding row index
        else:
            print("Invalid row. Please enter a letter between A and E.")  # Error message for invalid input


def fire_shot(grid, solution, row, col):
    if (row, col) in solution:  # Check if the shot is a hit
        grid[row][col] = '*'  # Mark hit position
        solution.remove((row, col))  # Remove hit position from solution
        print("Hit!")
        return True
    else:
        grid[row][col] = 'x'  # Mark miss position
        print("Miss!")
        return False

def main():
    while True:
        board, solution = reset_game()  # Initialize board and ship position
        shots_fired = set()  # Keep track of fired shots to prevent duplicates

        print("\nWelcome to Battleship!")  # Game introduction

        while True:
            display_board(board)  # Show current board state

            # Display menu options
            print("\nMenu:")
            print("1. Fire a shot")
            print("2. Give up")
            print("3. Quit")

            # Get the player's choice using the Check_input module
            choice = Check_input.get_int_range("Choose an option: ", 1, 3)

            if choice == 1:  # Player chooses to fire a shot
                row = get_row()  # Get row input
                col = Check_input.get_int_range("Enter column (1-5): ", 1,
                                                5) - 1  # Get column input (convert to 0-based index)

                if (row, col) in shots_fired:  # Check if the shot has already been fired
                    print("You've already fired at this location. Try again.")
                    continue  # Ask for a new shot

                shots_fired.add((row, col))  # Record the shot
                fire_shot(board, solution, row, col)  # Process the shot

                if not solution:  # Check if all parts of the ship have been hit
                    print("Congratulations! You've sunk the enemy ship!")
                    break  # End the game

            elif choice == 2:  # Player gives up
                print("You gave up! The enemy ship was at:")
                for r, c in solution:
                    board[r][c] = '*'  # Reveal the ship's position
                display_board(board)  # Show the final board
                break  # End the round

            elif choice == 3:  # Player quits the game
                print("Thanks for playing!")
                return  # Exit the game


if __name__ == "__main__":
    main()  # Run the game
