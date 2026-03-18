def gps_track(array):
    max_time = 0
    max_height = -1
    longest_mountain = []
    
    i = 1
    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        
        if not is_peak:
            i += 1
            continue

        if array[i] > max_height:
            max_height = array[i]
            
        left = i - 1
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1
            
        right = i + 1
        while right < len(array) and array[right] < array[right - 1]:
            right += 1
            
        current_time = right - left - 1

        if current_time > max_time:
            max_time = current_time
            longest_mountain = array[left + 1 : right]
            
        i = right - 1
        
    return max_height, max_time, longest_mountain

raw_input = input("Введіть висоти GPS через кому (наприклад: 3, 4, 5, 3, 2, 8, 2, 1, 1, 2, 1): ")

gps_data = [int(rawdata.strip()) for rawdata in raw_input.split(',')]

height, time, mountain = gps_track(gps_data)

print(f"\nНайбільша висота серед гір за день: {height} метрів")
print(f"Найдовший час на одну гору: {time}")
print(f"Запис найдовшої гори: {mountain}")