my_dict = {"apple": 3, "banana": 2, "orange": 5, "grape": 3, "kiwi": 1}

frequency_dict = {}

for key, value in my_dict.items():
    if value in frequency_dict:
        frequency_dict[value].append(key)
    else:
        frequency_dict[value] = [key]

print("Element Frequencies:")
for freq, elements in frequency_dict.items():
    print(f"{freq}: {', '.join(elements)}")