strings = ["cat", "elephant", "dog", "ant", "hippopotamus"]
longest = strings[0]
shortest = strings[0]
for s in strings:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s
print(longest, len(longest))
print(shortest, len(shortest))
