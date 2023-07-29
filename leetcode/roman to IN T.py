def roman_to_int():
    s = "LVIII"
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_val = 0
    for i in range(len(s)-1,-1,-1):
        current_value = roman_values[s[i]]
        if current_value<prev_val:
            total = total - current_value
        else:
            total = total + current_value
        prev_val = current_value
    print(total)
roman_to_int()
