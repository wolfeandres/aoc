def possibleGames(filename):
    with open(filename) as file:
        sum = 0
        for line in file:
            valid = True
            lineArr = line.split(":")
            id = lineArr[0][lineArr[0].index(" ") + 1:]
            showing = lineArr[1].split(";")

            for show in showing:
                set = show.split(",")
                for cubes in set:
                    amount = int(cubes.strip().split(" ")[0])
                    color = cubes.strip().split(" ")[1]
                    
                    if color[0] == "r":
                        if amount > 12:
                            valid = False
                            break
                    elif color[0] == "g":
                        if amount > 13:
                            valid = False
                            break
                    elif color [0] == "b":
                        if amount > 14:
                            valid = False
                            break

                if not valid:
                    break

            if valid:
                sum += int(id)
    return sum

def powerCubes(filename):
    with open(filename) as file:
        sum = 0
        for line in file:
            showing = line.split(":")[1].split(";")

            r = g = b = 1
            for show in showing:
                set = show.split(",")
                for cubes in set:
                    amount = int(cubes.strip().split(" ")[0])
                    color = cubes.strip().split(" ")[1]

                    if color[0] == "r" and amount > r:
                        r = amount
                    elif color[0] == "g" and amount > g:
                        g = amount
                    elif color[0] == "b" and amount > b:
                        b = amount
                
            # print(r * g * b, r, g, b)
            sum += r * g * b

        return sum

if __name__ == '__main__':
    print(powerCubes("day2/games.txt"))