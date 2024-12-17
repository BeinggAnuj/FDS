# Function to implement Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to implement Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Function to display top 5 highest scores
def display_top_five(arr):
    print("\nTop five highest scores are:")
    for i in range(min(5, len(arr))):
        print(f"{arr[-(i + 1)]}%")

# Main function
def main():
    arr = []
    n = int(input("Enter the number of students: "))
    print("Enter the percentages of the students:")
    for _ in range(n):
        percentage = float(input())
        arr.append(percentage)

    # Insertion Sort
    print("\n--- Insertion Sort ---")
    insertion_sort(arr)
    print("Sorted percentages in ascending order:")
    print(arr)
    display_top_five(arr)

    # Resetting the array for Shell Sort
    arr = arr.copy()

    # Shell Sort
    print("\n--- Shell Sort ---")
    shell_sort(arr)
    print("Sorted percentages in ascending order:")
    print(arr)
    display_top_five(arr)

if __name__ == "__main__":
    main()
