def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# Input array from the user
arr = input("Enter the array of integers (comma-separated): ")
arr = [int(x) for x in arr.split(',')]

print("Original array:", arr)

# Bubble Sort
bubble_sort(arr)
print("Sorted array using Bubble Sort:", arr)

# Reset the array
arr = input("Enter the array of integers (comma-separated): ")
arr = [int(x) for x in arr.split(',')]

# Selection Sort
selection_sort(arr)
print("Sorted array using Selection Sort:", arr)

# Reset the array
arr = input("Enter the array of integers (comma-separated): ")
arr = [int(x) for x in arr.split(',')]

# Insertion Sort
insertion_sort(arr)
print("Sorted array using Insertion Sort:", arr)


print("""
#### Bubble Sort:

**Time Complexity:**
- Worst-case: O(n^2)
- Average-case: O(n^2)
- Best-case: O(n) (with optimizations)

**Stability:** Stable

**Preferred Scenarios:**
- Mainly for educational purposes and simple sorting tasks.
- Practical use for small datasets or nearly sorted data.

#### Quick Sort:

**Time Complexity:**
- Worst-case: O(n^2) (with poor pivot choice)
- Average-case: O(n log n)
- Best-case: O(n log n)

**Stability:** Not stable

**Preferred Scenarios:**
- Highly efficient and preferred for most scenarios.
- Particularly useful for large datasets and good average-case performance.
- Not suitable when stable sorting is required.

#### Merge Sort:

**Time Complexity:**
- Worst-case: O(n log n)
- Average-case: O(n log n)
- Best-case: O(n log n)

**Stability:** Stable

**Preferred Scenarios:**
- Efficient and stable, making it suitable for various scenarios.
- Preferred when a stable sort or guaranteed worst-case performance is needed.

#### Python's `sorted` Function:

**Time Complexity:** O(n log n)

**Stability:** Stable

**Preferred Scenarios:**
- Built-in and highly optimized, usually the preferred choice in Python.
- Efficient and stable, making it suitable for general-purpose sorting tasks.

""")

