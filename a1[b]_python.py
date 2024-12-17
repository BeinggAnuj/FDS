def cricket_or_badminton_not_both(cricket, badminton):
    result = []
    for student in cricket:
        if student not in badminton:
            result.append(student)
    for student in badminton:
        if student not in cricket:
            result.append(student)
    return result


def neither_cricket_nor_badminton(all_students, cricket, badminton):
    result = []
    for student in all_students:
        if student not in cricket and student not in badminton:
            result.append(student)
    return result


def main():
    all_students = []
    print("Enter the names of all students one by one (type 'done' to finish):")
    while True:
        name = input().strip()
        if name == 'done':
            break
        all_students.append(name)

    cricket = []
    print("Enter the names of students who play cricket one by one (type 'done' to finish):")
    while True:
        name = input().strip()
        if name == 'done':
            break
        cricket.append(name)

    badminton = []
    print("Enter the names of students who play badminton one by one (type 'done' to finish):")
    while True:
        name = input().strip()
        if name == 'done':
            break
        badminton.append(name)

    cricket_or_badminton = cricket_or_badminton_not_both(cricket, badminton)
    neither_cricket_nor_badminton_students = neither_cricket_nor_badminton(all_students, cricket, badminton)

    print("\nStudents who play either cricket or badminton but not both:", cricket_or_badminton)
    print("Number of students who play neither cricket nor badminton:", len(neither_cricket_nor_badminton_students))


if __name__ == "__main__":
    main()
