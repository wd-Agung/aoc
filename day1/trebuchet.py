from input import puzzle_input

# part 1

result = []

for text in puzzle_input:
    first, last = "", ""
    text = list(text)
    while text:
        head = text.pop(0) if not first else ""
        if head.isdigit():
            first = head
        
        tail = text.pop() if not last and text else ""
        if tail.isdigit():
            last = tail

        if first and last:
            break
        
    first = first if first else last
    last = last if last else first
    result.append(int(first + last))

print("part 1: ", sum(result))

# part 2

result = []

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five" : "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

number_keys = number_map.keys()

def find_all_substrings(text, substring):
    start = 0
    while True:
        start = text.find(substring, start)
        if start == -1: return
        yield start
        start += len(substring)

def find_number_first_and_last(text):
    nums = {}
    for key in number_keys:
        for index in find_all_substrings(text, key):
            nums[index] = number_map[key]

    return nums[min(nums.keys())], nums[max(nums.keys())]

for text in puzzle_input:
    first, last = find_number_first_and_last(text)

    result.append(int(first + last))

print("part 2: ", sum(result))
