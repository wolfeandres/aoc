with open('calibration.txt') as file:
    sum = 0
    for line in file:
        c1 = ''
        c2 = ''
        for char in line:
            if char.isdigit():
                c1 = char
                break
        for char in reversed(line):
            if char.isdigit():
                c2 = char
                break
        sum += int(c1 + c2)

    print(sum)