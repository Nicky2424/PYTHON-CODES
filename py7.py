def find_occurrences(first_str, second_str):
    indices = []
    start = 0

    while True:
        index = first_str.find(second_str, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1

    return indices if indices else -1

# Example usage
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

result = find_occurrences(first_string, second_string)
print("Indices of occurrences:", result)
