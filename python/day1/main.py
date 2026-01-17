floor = 0

with open("input", 'rb') as f:
    content = str(f.read())
    array = list(content)  # Converting file content to array or list
    # Removing first two and last three elements from string (bytechar, newline etc...)
    array = array[2: -3]
    array = [s.replace(',', '') for s in array]  # To remove commas from list
    for i in range(len(array)):
        if "(" in array[i]:
            floor = floor + 1
        elif ")" in array[i]:
            floor = floor - 1
        if floor == -1:
            print(i+1)  # Shit, array or list starts from zero, gotta add one
print(floor)
