floor = 0

with open("input", 'rb') as f:
    content = str(f.read())
    array = list(content)
    array = array[2: -3]
    array = [s.replace(',', '') for s in array]
    for i in range(len(array)):
        if "(" in array[i]:
            floor = floor + 1
        elif ")" in array[i]:
            floor = floor - 1
        if floor == -1:
            print(i+1)
print(floor)
