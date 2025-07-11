def get_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    elif 0 <= score < 40:
        return "F"
    else:
        return "Invalid score"

try:
    score_input = int(input("Enter student score (0 - 100): "))
    grade = get_grade(score_input)
    print(f"Grade: {grade}")
except ValueError:
    print("Please enter a valid integer score.")
