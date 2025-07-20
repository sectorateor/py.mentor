nums = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# every non-empty slice (forward and reverse)
slices = [
    (f"{start}:{stop}:{step}", nums[start:stop:step])
    for start in range(10)
    for step in (1, -1)
    for stop in (range(start + 1, 11) if step == 1
                 else range(start - 1, -2, -1))
]

# pretty print
for text, lst in slices:
    print(f"{text} -> {lst}")