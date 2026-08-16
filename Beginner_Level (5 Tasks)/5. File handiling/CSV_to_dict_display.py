import csv

with open("student_marks.csv","r") as file:
    reader=csv.DictReader(file)
    students=[]

    # Create dictionary
    for row in reader:
        student=dict(row)
        marks = []
        for key,value in student.items():
            try:
                marks.append(float(value))
            except ValueError:
                pass

        total_marks = sum(marks)
        average_marks = total_marks / len(marks)

        student["total_marks"] = total_marks
        student["Average"] = average_marks

        students.append(student)
for student in students:
    print(student)
