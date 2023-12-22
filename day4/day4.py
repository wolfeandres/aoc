def winningPoints(filename):
    with open(filename) as file:
        data = file.read().strip().split("\n")
        sum = 0

        for line in data:
            winning = line.split(":")[1].split("|")[0].strip().split(" ")
            nums = line.split(":")[1].split("|")[1].strip().split(" ")
            winCount = 0
            for num in nums:
                if num == '':
                    continue
                if num in winning:
                    winCount = winCount * 2 if winCount != 0 else 1

            sum += winCount
        return sum

def copyCards(filename):
    with open(filename) as file:
        data = file.read().strip().split("\n")
        sum = 0
        cardCounts = {}
        for line in data:
            game = int(line.split(":")[0][line.index(" ") + 1:].strip())
            winning = line.split(":")[1].split("|")[0].strip().split(" ")
            nums = line.split(":")[1].split("|")[1].strip().split(" ")
            winCount = 0
            for num in nums:
                if num == '':
                    continue
                if num in winning:
                    winCount += 1
        
            if game in cardCounts.keys():
                cardCounts[game] += 1
            else:
                cardCounts[game] = 1
            # print(winCount)
            for i in range(1, winCount + 1, 1):
                if i + game >= len(data):
                    break
                if i + game in cardCounts.keys():
                    cardCounts[game + i] += cardCounts[game]
                else:
                    cardCounts[game + i] = cardCounts[game]

        for item in cardCounts.items():
            print(item)
            sum += item[1]

        return sum

if __name__ == "__main__":
    print(copyCards("day4/cards.txt"))
