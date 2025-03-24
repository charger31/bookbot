def get_num_words(file_contents:str):
    list_of_words = file_contents.split()
    return len(list_of_words)

def get_chars_dict(file_contents:str):
    char_count = {}
    
    for char in file_contents:
        # Convert to lowercase
        lowercase_char = char.lower()
        
        # If we've seen this character before, increment its count
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            char_count[lowercase_char] = 1
            
    return char_count
        

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(char_count):
    list_of_nums = []
    for char in char_count:
        list_of_nums.append({"char": char, "num": char_count[char]})
    list_of_nums.sort(reverse = True, key= sort_on)
    return list_of_nums