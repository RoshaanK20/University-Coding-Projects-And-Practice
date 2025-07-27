import turtle

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.beginfill()
    turtle.circle(radius)
    turtle.endfill()

def draw_text(x, y, text):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, align="center", font=("Arial", 12, "normal"))

def main():
    turtle.speed(1)

    # Student marks
    marks = {
        "Math": 80,
        "Urdu": 90,
        "English": 85,
        "Physics": 95,
        "Chemistry": 80
    }

    # Calculating total marks and average
    total_marks = sum(marks.values())
    average = total_marks / len(marks)

    # Determining grades
    grades = {
        "A": (90, 100),
        "B": (80, 89),
        "C": (70, 79),
        "D": (60, 69),
        "F": (0, 59)
    }

    # Drawing marksheet
    x = -200
    y = 200
    for subject, mark in marks.items():
        draw_text(x, y, f"{subject}: {mark}")
        y -= 30

    draw_text(x, y-50, f"Total Marks: {total_marks}")
    draw_text(x, y-80, f"Average Marks: {average}")

    # Determine grade and draw circle if failing
    grade = None
    for g, (lower, upper) in grades.items():
        if lower <= average <= upper:
            grade = g
            break

    if grade == "F":
        draw_circle(0, 0, 50, "red")

    draw_text(0, -20, f"Grade: {grade}")

    turtle.done()

if __name__== "__main__":
    main()