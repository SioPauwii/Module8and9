import time
import random
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
    
        current_element = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = current_element
    
    return arr

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
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
    data = random.sample(range(1, 10001), 10000)

    print("Sorting Algorithms Comparison:")
    print("--------------------------------")

    print("1. Bubble Sort:")
    start_time = time.time()
    sorted_data = bubble_sort(data.copy())
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Beginning of sorted array: {sorted_data[:10]}...{sorted_data[-10:]}")
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("2. Insertion Sort:")
    start_time = time.time()
    sorted_data = insertion_sort(data.copy())
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Beginning of sorted array: {sorted_data[:10]}...{sorted_data[-10:]}")
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("3. Selection Sort:")
    start_time = time.time()
    sorted_data = selection_sort(data.copy())
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Beginning of sorted array: {sorted_data[:10]}...{sorted_data[-10:]}")
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("4. Merge Sort:")
    start_time = time.time()
    sorted_data = merge_sort(data.copy())
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Beginning of sorted array: {sorted_data[:10]}...{sorted_data[-10:]}")
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("5. Shell Sort:")
    start_time = time.time()
    sorted_data = shell_sort(data.copy())
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Beginning of sorted array: {sorted_data[:10]}...{sorted_data[-10:]}")
    print(f"Time taken: {executionTime:.3f} ms")
    print()

    print("6. Quick Sort:")
    start_time = time.time()
    sorted_data = quick_sort(data.copy())
    end_time = time.time()
    executionTime = (end_time - start_time) * 1000
    print(f"Beginning of sorted array: {sorted_data[:10]}...{sorted_data[-10:]}")
    print(f"Time taken: {executionTime:.3f} ms")
    print()

main()
