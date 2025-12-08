# Using a For Loop
def cubes_of_even_numbers_for_loop(input_list):
    cubes = []
    for item in input_list:
        if isinstance(item, int) and item % 2 == 0:
            cubes.append(item ** 3)
    return cubes

# Using a List Comprehension
def cubes_of_even_numbers_list_comprehension(input_list):
    return [item ** 3 for item in input_list if isinstance(item, int) and item % 2 == 0]

# Example usage
input_list = [1, 2, 3, 4, 5, 6, 'a', 8.0, 10]

print("Using For Loop:", cubes_of_even_numbers_for_loop(input_list))
print("Using List Comprehension:", cubes_of_even_numbers_list_comprehension(input_list))
