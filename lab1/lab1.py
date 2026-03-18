import unittest

def find_longest_peak(array):
    max_peak_length = 0
    i = 1

    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        
        if not is_peak:
            i += 1
            continue
            
        left_side = i - 1
        while left_side >= 0 and array[left_side] < array[left_side + 1]:
            left_side -= 1

        right_side = i + 1
        while right_side < len(array) and array[right_side] < array[right_side - 1]:
            right_side += 1

        current_peak_length = right_side - left_side - 1
        
        if current_peak_length > max_peak_length:
            max_peak_length = current_peak_length
            
        i = right_side - 1
        
    return max_peak_length