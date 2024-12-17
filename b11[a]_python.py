def linear_search(roll_numbers, target):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == target:
            return True
    return False

def sentinel_search(roll_numbers, target):
    roll_numbers.append(target)  # Append target as sentinel value
    i = 0
    while roll_numbers[i] != target:
        i += 1
    return i < len(roll_numbers) - 1  # Check if we found the target before the sentinel

def main():
    roll_numbers = []
    n = int(input("Enter the number of students who attended the training program: "))
    print("Enter the roll numbers of the students:")
    for _ in range(n):
        roll_number = int(input())
        roll_numbers.append(roll_number)

    target = int(input("Enter the roll number to search: "))

    if linear_search(roll_numbers, target):
        print(f"Student with roll number {target} attended the training program (Linear Search).")
    else:
        print(f"Student with roll number {target} did not attend the training program (Linear Search).")

    if sentinel_search(roll_numbers, target):
        print(f"Student with roll number {target} attended the training program (Sentinel Search).")
    else:
        print(f"Student with roll number {target} did not attend the training program (Sentinel Search).")

if __name__ == "__main__":
    main()
