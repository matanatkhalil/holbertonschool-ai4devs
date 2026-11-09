def calculate_average(scores):
    if not scores:
        return None

    total = 0

    for score in scores:
        total += score

    average = total / len(scores)
    return average


def print_student_report(name, scores):
    average = calculate_average(scores)
    print(f"Student: {name}")
    print(f"Scores: {scores}")

    if average is None:
        print("Average: N/A (no recorded scores)")
    else:
        print(f"Average: {average:.2f}")


students = [
    ("Aylin", [85, 90, 78]),
    ("Murad", [92, 88, 95]),
    ("Leyla", [])
]

for student_name, student_scores in students:
    print_student_report(student_name, student_scores)
