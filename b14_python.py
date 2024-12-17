# Function to implement Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Function to implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Function to display top 5 highest scores in reverse order
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

    # Selection Sort
    print("\n--- Selection Sort ---")
    selection_sort(arr)
    print("Sorted percentages in ascending order:")
    print(arr)
    display_top_five(arr)

    # Resetting the array for Bubble Sort
    arr = arr.copy()

    # Bubble Sort
    print("\n--- Bubble Sort ---")
    bubble_sort(arr)
    print("Sorted percentages in ascending order:")
    print(arr)
    display_top_five(arr)

if __name__ == "__main__":
    main()
