import time
import random
def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Repeat the process until the array is sorted
    for i in range(n):
        # Initialize a flag to check if any swaps were made
        swapped = False
        
        # Iterate over the array from the first element to the (n-i-1)th element
        for j in range(n - i - 1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set the flag to True
                swapped = True
        
        # If no swaps were made in the inner loop, the array is sorted
        if not swapped:
            break
    
    # Return the sorted array
    return arr

def insertion_sort(arr):
    # Iterate over the array from the second element to the end
    for i in range(1, len(arr)):
        # Store the current element to be inserted
        current_element = arr[i]
        # Initialize the index of the previous element
        j = i - 1
        
        # Shift elements to the right until a smaller element is found
        while j >= 0 and arr[j] > current_element:
            # Shift the element to the right
            arr[j + 1] = arr[j]
            # Move to the previous element
            j -= 1
        
        # Insert the current element at the correct position
        arr[j + 1] = current_element
    
    # Return the sorted array
    return arr

def selection_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Repeat the process until the array is sorted
    for i in range(n):
        # Initialize the minimum index to the current index
        min_index = i
        
        # Iterate over the array from the next element to the end
        for j in range(i + 1, n):
            # If the current element is smaller than the minimum element, update the minimum index
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # Return the sorted array
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def shell_sort(arr):
    n = len(arr)
    gap = n // 2 #5

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
    
def main():
    data = random.sample(range(1, 101), 100)

    print("1. Bubble Sort:")
    start_time = time.time()
    print(f"Sorted array: {bubble_sort(data.copy())}")
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("2. Insertion Sort:")
    start_time = time.time()
    print(f"Sorted array: {insertion_sort(data.copy())}")
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("3. Selection Sort:")
    start_time = time.time()
    print(f"Sorted array: {selection_sort(data.copy())}")
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("4. Merge Sort:")
    start_time = time.time()
    print(f"Sorted array: {merge_sort(data.copy())}")
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("5. Shell Sort:")
    start_time = time.time()
    print(f"Sorted array: {shell_sort(data.copy())}")
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("6. Quick Sort:")
    start_time = time.time()
    print(f"Sorted array: {quick_sort(data.copy())}")
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Time taken: {executionTime:.3f} ms")
    print()

main()
