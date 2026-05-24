def manual_parse_file(filepath):
    words = []
    current_word = ""
    
    try:
        with open(filepath, "r", encoding="utf-8") as f_in:
            while True:
                char = f_in.read(1)
                 

                if not char:
                    if current_word:
                        words.append(current_word)
                    break
                    
                if char == ' ' or char == '\n' or char == '\r' or char == '\t':
                    if current_word:
                        words.append(current_word)
                        current_word = ""
                else:
                    current_word += char
                    
        return words
    except FileNotFoundError:
        return []


def get_unique_words(words):
    unique_list = []
    seen = {}
    
    for word in words:
        if word not in seen:
            unique_list.append(word)
            seen[word] = True
            
    return unique_list


def radix_sort_by_length(words):
    if len(words) <= 1:
        return words

    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)

    buckets = [[] for _ in range(max_length + 1)]

    for word in words:
        buckets[len(word)].append(word)

    sorted_words = []
    for bucket in buckets:
        sorted_words.extend(bucket)
 
    return sorted_words


def remove_character(word, index):
    return word[:index] + word[index + 1:]


def find_longest_chain(words):
    if not words:
        return 0

    unique_words = get_unique_words(words)
    
    sorted_words = radix_sort_by_length(unique_words)
    
    dp_table: dict[str, int] = {}
    max_chain_length = 1

    for word in sorted_words:
        current_longest = 1
        word_length = len(word)
        
        for i in range(word_length):
            prev_word = remove_character(word, i)
            
            if prev_word in dp_table:
                if dp_table[prev_word] + 1 > current_longest:
                    current_longest = dp_table[prev_word] + 1
        
        dp_table[word] = current_longest
        
        if current_longest > max_chain_length:
            max_chain_length = current_longest

    return max_chain_length


def process_files(input_file, output_file):
    parsed_data = manual_parse_file(input_file)
    
    if not parsed_data:
        print(f"Помилка: Файл {input_file} не знайдено або він порожній.")
        return
        
    words = parsed_data[1:]

    result = find_longest_chain(words)

    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.write(str(result) + "\n")


if __name__ == "__main__":
    process_files("wchain.in", "wchain.out")