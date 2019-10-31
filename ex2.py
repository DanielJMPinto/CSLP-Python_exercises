import sys


def main(args):
    filename = "g3.csv"
    students_data = readfile(filename)

    for student in students_data.keys():
        print("Student number", student, ", grade: ", process_student_data(students_data[student]))

    print("Average class grade: ", class_average(students_data))

    generate_new_file(students_data, "sortedfile.csv")


def process_student_data(student_data):
    grades = student_data[-3:]
    final_grade = 0

    for grade in grades:
        final_grade += eval(grade)

    final_grade = final_grade / 3

    return final_grade


def class_average(students_data):
    total_grade = 0
    for student in students_data.keys():
        total_grade += process_student_data(students_data[student])

    total_grade = total_grade / len(students_data.keys())

    return total_grade


def generate_new_file(students_data, filename):
    file = open(filename, "w")
    sorted_students = []

    for student in students_data.keys():
        sorted_students.append((student, students_data[student][0], process_student_data(students_data[student])))

    sorted_students = sorted(sorted_students, key=lambda x: x[2], reverse=True)

    file.write("Numero\tNome\tNota\n")

    for line in sorted_students:
        file.write(str(line[0]) + "\t" + str(line[1]) + "\t" + str(round(line[2], 1)) + "\n")

    file.close()


def readfile(filename):
    file = open(filename, "r")
    students = {}

    for line in file:
        student_data = line.split("\t")
        if student_data[0] == "Numero":
            pass
        else:
            student_data[-1] = student_data[-1].replace('\n', '')
            students[student_data[0]] = student_data[1:]
    file.close()
    return students


if __name__ == '__main__':
    main(sys.argv)