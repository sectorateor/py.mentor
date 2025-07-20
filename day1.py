import copy

# 1. Build the nested list
nested = [[1, 2], [3, 4]]
print("nested id =", id(nested))
print("nested[0] id =", id(nested[0]))
print("nested[1] id =", id(nested[1]))

# 2. Shallow copy
shallow = copy.copy(nested)
print("\nshallow id =", id(shallow))          # different from nested
print("shallow[0] id =", id(shallow[0]))      # SAME as nested[0]
print("shallow[1] id =", id(shallow[1]))      # SAME as nested[1]

# 3. Deep copy
deep = copy.deepcopy(nested)
print("\ndeep id =", id(deep))                # different from nested
print("deep[0] id =", id(deep[0]))            # different from nested[0]
print("deep[1] id =", id(deep[1]))            # different from nested[1]

# 4. Mutate via shallow copy
shallow[0].append(99)
print("\nAfter shallow[0].append(99):")
print("nested =", nested)
print("shallow =", shallow)
print("deep =", deep)