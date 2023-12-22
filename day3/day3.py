def countPartNumbers(filename):
    with open(filename) as file:
        data = file.read().strip().split("\n")
        sum = 0
        for i, line in enumerate(data):
            touching = False
            num = ''
            for j, char in enumerate(line):
                if not char.isdigit():
                    if touching:
                        print(num)
                        sum += int(num)
                    num = ''
                    touching = False
                    continue

                if not touching and ((j + 1 < len(line) and data[i][j + 1] != "." and not data[i][j + 1].isdigit()) or #right
                    (j - 1 >= 0 and data[i][j - 1] != "." and not data[i][j - 1].isdigit()) or # left
                    (i + 1 < len(data) and data[i + 1][j] != "." and not data[i + 1][j].isdigit()) or # down
                    (i - 1 >= 0 and data[i - 1][j] != "." and not data[i - 1][j].isdigit()) or #up
                    (i + 1 < len(data) and j + 1 < len(line) and data[i + 1][j + 1] != "." and not data[i + 1][j + 1].isdigit()) or # down-right
                    (i + 1 < len(data) and j - 1 >= 0 and data[i + 1][j - 1] != "." and not data[i + 1][j - 1].isdigit()) or # down-left
                    (i - 1 >= 0 and j + 1 < len(line) and data[i - 1][j + 1] != "." and not data[i - 1][j + 1].isdigit()) or # up-right
                    (i - 1 >= 0 and j - 1 >= 0 and data[i - 1][j - 1] != "." and not data[i - 1][j - 1].isdigit())): # up-left
                    print(f'[{i}, {j}]: {char}')
                    touching = True

                num += char

                if j == len(line) - 1 and num != '' and touching:
                    sum += int(num)

        return sum

def gearRatios(filename):
    with open(filename) as file:
        data = file.read().strip().split("\n")
        sum = 0
        gearNums = {}

        for i, line in enumerate(data):
            touching = []
            num = ''
            for j, char in enumerate(line):
                if not char.isdigit():
                    for gear in touching:
                        if gear not in gearNums:
                            gearNums[gear] = [int(num)]
                        else:
                            gearNums[gear] += [int(num)]
                    num = ''
                    touching = []
                    continue
                
                if len(touching) == 0:
                    if j + 1 < len(line) and data[i][j + 1] == "*":
                        touching.append(tuple([i, j + 1]))
                    if j - 1 >= 0 and data[i][j - 1] == "*":
                        touching.append(tuple([i, j - 1]))
                    if i + 1 < len(data) and data[i + 1][j] == "*":
                        touching.append(tuple([i + 1, j]))
                    if i - 1 >= 0 and data[i - 1][j] == "*":
                        touching.append(tuple([i - 1, j]))
                    if i + 1 < len(data) and j + 1 < len(line) and data[i + 1][j + 1] == "*":
                        touching.append(tuple([i + 1, j + 1]))
                    if i + 1 < len(data) and j - 1 >= 0 and data[i + 1][j - 1] == "*":
                        touching.append(tuple([i + 1, j -1]))
                    if i - 1 >= 0 and j + 1 < len(line) and data[i - 1][j + 1] == "*":
                        touching.append(tuple([i - 1, j + 1]))
                    if i - 1 >= 0 and j - 1 >= 0 and data[i - 1][j - 1] == "*":
                        touching.append(tuple([i - 1, j - 1]))
                    
                num += char

                if j == len(line) - 1:
                    for gear in touching:
                        if gear not in gearNums:
                            gearNums[gear] = [int(num)]
                        else:
                            gearNums[gear] += [int(num)]
        
        for nums in gearNums.values():
            if len(nums) == 2:
                # print(nums)
                sum += nums[0] * nums[1]
        print(gearNums)
        return sum

if __name__ == "__main__":
    print(gearRatios("day3/schematic.txt"))