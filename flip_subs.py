# Written by CanzonE

import sys

ENDING_PUNCTUATION_DICT = {"\"": "\"", "'": "'", ",": ",", ".": ".", "?": "?", "!": "!",
                           ":": ":", "`": "`", "-": "-", " ": " ", "(": ")", ")": "(",
                           "<": ">", ">": "<", "[": "]", "]": "["}
BEGINING_PUNCTUATION_DICT = {"\"": "\"", "-": "-", "'": "'", ",": ",", ".": ".", "?": "?",
                             "!": "!", ":": ":", "`": "`", "-": "-", " ": " ", "(": ")", ")": "(",
                             "<": ">", ">": "<", "[": "]", "]": "["}
CHOPPED = ["<i>", "</i>", "<b>", "</b>", "<u>", "</u>"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
NUMBERS_SEPARATOR = ","

def print_part(part):
    for line in part:
        print(line)

def print_parts(parts):
    for part in parts:
        print_part(part)
        print("========")
        
def split_lines(lines):
    last_split_index = 0
    parts = []
    for i in range(len(lines)):
        if lines[i] == "\n":
            parts.append(lines[last_split_index:i + 1])
            last_split_index = i + 1
    
    parts.append(lines[last_split_index:len(lines)])
    return parts
    
def should_skip_number_flipping(line):
    if (line[-1] in ENDING_PUNCTUATION_DICT.keys() or line[-1] in BEGINING_PUNCTUATION_DICT.keys() or line[-1] in NUMBERS) and \
        (line[0] in ENDING_PUNCTUATION_DICT.keys() or line[0] in BEGINING_PUNCTUATION_DICT.keys() or line[0] in NUMBERS):
        return True
    return False
        
def flip_punctuation(line):
    should_skip_numbers = should_skip_number_flipping(line)
    working_line = line
    to_add_end = []
    to_add_begining = []
    numbers_cache = ""
    
    def should_continue_searching_for_numbers_end(working_line):
        return working_line[-1] in NUMBERS or (working_line[-1] == NUMBERS_SEPARATOR and len(working_line) > 1 and working_line[-2] in NUMBERS and len(numbers_cache) > 0)
        
    def should_continue_searching_for_numbers_begining(working_line):
        return working_line[0] in NUMBERS or (working_line[0] == NUMBERS_SEPARATOR and len(working_line) > 1 and working_line[1] in NUMBERS and len(numbers_cache) > 0)
    
    while len(working_line) > 0 and (working_line[-1] in ENDING_PUNCTUATION_DICT.keys() or working_line[-1] in NUMBERS):
        if len(numbers_cache) > 0 and not should_continue_searching_for_numbers_end(working_line):
            if should_skip_numbers:
                break
            to_add_end.append(numbers_cache)
            numbers_cache = ""
            
        if should_continue_searching_for_numbers_end(working_line):
            if should_skip_numbers:
                break
            numbers_cache += working_line[-1]
        else:
            punctuation = working_line[-1]
            to_add_end.append(ENDING_PUNCTUATION_DICT[punctuation])
        working_line = working_line[0:len(working_line)-1]
        
    if len(numbers_cache) > 0:
        to_add_end.append(numbers_cache)
        numbers_cache = ""
        
    while len(working_line) > 0 and (working_line[0] in BEGINING_PUNCTUATION_DICT.keys() or working_line[0] in NUMBERS):
        if len(numbers_cache) > 0 and not should_continue_searching_for_numbers_begining(working_line):
            if should_skip_numbers:
                break
            to_add_begining.append(numbers_cache)
            numbers_cache = ""
            
        if should_continue_searching_for_numbers_begining(working_line):
            if should_skip_numbers:
                break
            numbers_cache += working_line[0]
        else:
            punctuation = working_line[0]
            to_add_begining.append(BEGINING_PUNCTUATION_DICT[punctuation])
        working_line = working_line[1:len(working_line)]
        
    if len(numbers_cache) > 0:
        to_add_begining.append(numbers_cache)
        numbers_cache = ""
        
    to_add_end.reverse()
    for add in to_add_end:
        working_line = add + working_line
    
    to_add_begining.reverse()
    for add in to_add_begining:
        working_line = working_line + add
    return working_line
    
def process_part(part):
    if len(part) < 4:
        for i in range(4 - len(part)):
            part.append("\n")

    for i in range(len(part[2:len(part)])):
        current_line = part[i + 2]
        if current_line == "\n":
            continue

        chopped_start = ""
        chopped_end = ""
        working_line = current_line.strip()
        
        for chopped_part in CHOPPED:
            if working_line.startswith(chopped_part):
                working_line = working_line[len(chopped_part):len(working_line)]
                chopped_start = chopped_part

            if working_line.endswith(chopped_part):
                working_line = working_line[0:-len(chopped_part)]
                chopped_end = chopped_part

        working_line = flip_punctuation(working_line)

        working_line = chopped_start + working_line + chopped_end + "\n"

        part[i+2] = working_line

    return part

def main():
    assert len(sys.argv) == 3
    file_path = sys.argv[1]
    output_path = sys.argv[2]
    
    lines = []
    with open(file_path, 'r', encoding='latin-1') as file:
        lines = file.readlines()
    
    parts = split_lines(lines)
    
    processed_parts = []
    
    for part in parts:
        processed_parts.append(process_part(part))
     
    with open(output_path, 'w', encoding='latin-1') as file:
        for part in processed_parts:
            file.writelines(part)

    return
    
    
if __name__ == "__main__":
    main()
