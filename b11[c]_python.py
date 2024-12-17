# Function for Binary Search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            print(f"Student with roll number {key} attended the training program (Binary Search).")
            return True
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Student with roll number {key} did not attend the training program (Binary Search).")
    return False

# Function for Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"Student with roll number {key} attended the training program (Linear Search).")
            return True
    print(f"Student with roll number {key} did not attend the training program (Linear Search).")
    return False

# Main function
def main():
    arr = []
    n = int(input("Enter the number of students who attended the training program: "))
    print("Enter the roll numbers of the students (in sorted order):")
    for _ in range(n):
        roll_number = int(input())
        arr.append(roll_number)

    key = int(input("Enter the roll number to search: "))

    # Perform binary search
    binary_search(arr, key)

    # Perform linear search
    linear_search(arr, key)

if __name__ == "__main__":
    main()
