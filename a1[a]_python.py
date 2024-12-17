def common_cricket_badminton(cricket, badminton):
    both = []
    for student in cricket:
        if student in badminton:
            both.append(student)
    return both


def cricket_football_not_badminton(cricket, football, badminton):
    result = []
    for student in cricket:
        if student in football and student not in badminton:
            result.append(student)
    return result


def main():
    cricket = []
    print("Enter the names of students who play cricket one by one (type 'done' to finish):")
    while True:
        name = input().strip()  # Strip extra spaces from input
        if name == 'done':
            break
        cricket.append(name)

    badminton = []
    print("Enter the names of students who play badminton one by one (type 'done' to finish):")
    while True:
        name = input().strip()  # Strip extra spaces from input
        if name == 'done':
            break
        badminton.append(name)

    football = []
    print("Enter the names of students who play football one by one (type 'done' to finish):")
    while True:
        name = input().strip()  # Strip extra spaces from input
        if name == 'done':
            break
        football.append(name)

    both_cricket_badminton = common_cricket_badminton(cricket, badminton)
    cricket_football_not_badminton_students = cricket_football_not_badminton(cricket, football, badminton)

    print("\nStudents who play both cricket and badminton:", both_cricket_badminton)
    print("Number of students who play cricket and football but not badminton:",
          len(cricket_football_not_badminton_students))


if __name__ == "__main__":
    main()
