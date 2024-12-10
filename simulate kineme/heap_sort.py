import time
import threading
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

def bucket_sort(arr):
    min_value = min(arr)
    max_value = max(arr)

    range_value = (max_value - min_value) / len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        j = int((arr[i] - min_value) / range_value)
        if j == len(arr):
            j -= 1
        buckets[j].append(arr[i])

    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

    return arr

def radix_sort(arr):
    max_num = max(arr)
    digits = len(str(abs(max_num)))

    place = 1

    for _ in range(digits):
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // place) % 10
            buckets[digit].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        place *= 10

    return arr

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped == True:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if swapped == False:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1
    return arr

def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 0, -1):
        max_index = arr.index(max(arr[0:curr_size]))
        if max_index != curr_size - 1:
            arr = arr[:max_index+1][::-1] + arr[max_index+1:]
            arr = arr[:curr_size][::-1] + arr[curr_size:]
    return arr

def sleep_sort(arr):
    lock = threading.Lock()

    def sleep_and_print(value):
        time.sleep(value / 10)
        with lock:
            print(value)

    threads = []
    for value in arr:
        thread = threading.Thread(target=sleep_and_print, args=(value,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return arr

def main():
    arr = [23, 10, 5, 1, 18, 31, 16]
    print("Heap Sort:")
    start_time = time.time()
    sorted_arr = heap_sort(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Sorted array:", sorted_arr)
    print(f"Time taken: {execution_time:.3f} ms")
    print()

    print("Bucket Sort:")
    start_time = time.time()
    sorted_arr = bucket_sort(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Sorted array:", sorted_arr)
    print(f"Time taken: {execution_time:.3f} ms")
    print()


    print("Raidx Sort:")
    start_time = time.time()
    sorted_arr = radix_sort(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Sorted array:", sorted_arr)
    print(f"Time taken: {execution_time:.3f} ms")
    print()


    print("Cocktail Sort:")
    start_time = time.time()
    sorted_arr = cocktail_sort(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Sorted array:", sorted_arr)
    print(f"Time taken: {execution_time:.3f} ms")
    print()


    print("Pancake Sort:")
    start_time = time.time()
    sorted_arr = pancake_sort(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Sorted array:", sorted_arr)
    print(f"Time taken: {execution_time:.3f} ms")
    print()


    print("Sleep Sort:")
    start_time = time.time()
    sorted_arr = sleep_sort(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Sorted array:", sorted_arr)
    print(f"Time taken: {execution_time:.3f} ms")
    print()

main()