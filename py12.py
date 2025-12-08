t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# (a) Print half values line-by-line
mid = len(t1) // 2
print("First Half:", t1[:mid])
print("Second Half:", t1[mid:])

# (b) Tuple of even numbers
even_tuple = tuple(x for x in t1 if x % 2 == 0)
print("Even Numbers Tuple:", even_tuple)

# (c) Concatenate with t2
t2 = (11, 13, 15)
new_tuple = t1 + t2
print("Concatenated Tuple:", new_tuple)

# (d) Maximum & Minimum
print("Max:", max(t1))
print("Min:", min(t1))
