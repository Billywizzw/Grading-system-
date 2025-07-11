# grading_system_multiple.py

# This program allows grading of multiple students in a loop.
# It takes input for each student's score and returns their grade until the user decides to stop.

def grade_student(score):
    """
    This function takes a numerical score and returns the corresponding grade.
    """
    if score >= 70 and score <= 100:
        return "A"
    elif score >= 60 and score <= 69:
        return "B"
    elif score >= 50 and score <= 59:
        return "C"
    elif score >= 45 and score <= 49:
        return "D"
    elif score >= 40 and score <= 44:
        return "E"
    elif score >= 0 and score < 40:
        return "F"
    else:
        return "Invalid score. Please enter a value between 0 and 100."

def main():
    """
    Main function to grade multiple students in a loop.
    """
    while True:
        try:
            # Ask for the student's score
            score = int(input("Enter the student's score (0 - 100): "))
            # Get and print the grade
            grade = grade_student(score)
            print(f"The grade is: {grade}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Ask the user if they want to grade another student
        again = input("Do you want to grade another student? (yes/no): ").lower()
        if again != "yes":
            print("Exiting the grading system. Goodbye!")
            break

# Run the main function
if __name__ == "__main__":
    main()
