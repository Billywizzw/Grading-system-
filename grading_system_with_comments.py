# grading_system.py

# This program receives a student's score as input
# and prints out the corresponding grade based on the specified grading scale.

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
    Main function to drive the grading system.
    It gets user input and displays the grade.
    """
    try:
        # Prompt user for input
        score = int(input("Enter the student's score (0 - 100): "))

        # Get grade using the grade_student function
        grade = grade_student(score)

        # Display the result
        print(f"The grade is: {grade}")
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid number.")

# Execute the program
if __name__ == "__main__":
    main()
