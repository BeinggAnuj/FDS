def binary_search(arr, key):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            position = mid
            print(f"Student with roll number {key} attended the training program at location {position}")
            return True
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    print(f"Student with roll number {key} did not attend the training program")
    return False


def fibonacci_search(arr, x, n):
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1
    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    offset = -1
    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)
        if arr[i] < x:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > x:
            fibM = fibMMm2
            fibMMm1 -= fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            print(f"Student with roll number {x} attended the training program at location {i}")
            return i

    if fibMMm1 and arr[offset + 1] == x:
        print(f"Student with roll number {x} attended the training program at location {offset + 1}")
        return offset + 1

    print(f"Student with roll number {x} did not attend the training program")
    return -1


def main():
    arr = []
    n = int(input("Enter the number of students who attended the training program: "))
    print("Enter the roll numbers of the students in sorted order:")
    for _ in range(n):
        roll_number = int(input())
        arr.append(roll_number)

    key = int(input("Enter the roll number to search: "))

    # Perform binary search
    binary_search(arr, key)

    # Perform fibonacci search
    fibonacci_search(arr, key, n)


if __name__ == "__main__":
    main()
