def manual_len(arr):
    count = 0
    for _ in arr:
        count += 1
    return count

def manual_max(arr):
    if manual_len(arr) == 0:
        return 0
    maximum = arr[0]
    for x in arr:
        if x > maximum:
            maximum = x
    return maximum

def counting_sort(arr):
    n = manual_len(arr)
    if n == 0:
        return []

    max_val = manual_max(arr)

    count_arr = []
    for _ in range(max_val + 1):
        count_arr.append(0)

    for num in arr:
        count_arr[num] += 1

    sorted_arr = []

    for i in range(manual_len(count_arr)):
        count = count_arr[i]
        while count > 0:
            sorted_arr.append(i)
            count -= 1
            
    return sorted_arr

def can_place_cows(stalls, c_cows, min_dist):
    cows_placed = 1
    last_position = stalls[0]
    n = manual_len(stalls)
    
    for i in range(1, n):
        current_position = stalls[i]
        if current_position - last_position >= min_dist:
            cows_placed += 1
            last_position = current_position
            
            if cows_placed == c_cows:
                return True
    return False

def solve_aggressive_cows(n_stalls, c_cows, free_sections):
    stalls = counting_sort(free_sections)

    low = 0
    high = stalls[manual_len(stalls) - 1] - stalls[0]
    result_dist = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid == 0:
            low = 1
            continue

        if can_place_cows(stalls, c_cows, mid):
            result_dist = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result_dist