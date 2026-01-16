floor = 0

with open("input", 'rb') as f:
    content = str(f.read())
    array = list(content)
    for i in range(len(array)):
        if "(" in array[i]:
            floor = floor + 1
        elif ")" in array[i]:
            floor = floor - 1


print(floor)
