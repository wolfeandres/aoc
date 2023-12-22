digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def calibrateValues(filename):
    with open(filename) as file:
        sum = 0
        for line in file:
            c1 = ''
            c2 = ''
            s1 = 0
            s2 = 0

            while s2 < len(line):
                if s2 == s1 and line[s2].isdigit():
                    # print(line[s2])
                    c1 = line[s2]
                    break

                ip = False
                for word, digit in digits.items():
                    if line[s1:s2+1] == word:
                        c1 = digit
                        # print(word)
                        s2 = len(line)
                        ip = True
                        break
                    elif s1 != s2 and line[s1:s2+1] in word[:s2 - s1 + 1]:
                        # print("LIP: [", s1, ",", s2, "] ", line[s1:s2+1], word[:s2 - s1 + 1])
                        ip = True
                        break
                    elif s1 == s2 and line[s1] in word: 
                        # print("LIP: [", s1, ",", s2, "] ", line[s1])
                        ip = True
                        break

                if not ip:
                    s1 += 1
                    s2 = s1
                else:
                    s2 += 1

            s2 = len(line) - 2 if line[-1] == '\n' else len(line) - 1
            s1 = s2
            while s1 >= 0:
                if s2 == s1 and line[s2].isdigit():
                    c2 = line[s2]
                    # print(line[s2])
                    break

                ip = False
                for word, digit in digits.items():
                    if line[s1:s2+1] == word:
                        c2 = digit
                        s1 = -1
                        ip = True
                        # print(word, digit)
                        break
                    elif s1 != s2 and line[s1:s2+1] in word[len(word) - (s2 - s1 + 1):]:
                        # print("RIP: [", s1, ",", s2, "]", line[s1:s2+1], word[len(word) - s2 - s1 - 2:], len(word) - (s2 - s1 + 2))
                        ip = True
                        break
                    elif s1 == s2 and line[s1] == word[-1]:
                        # print("RIP: [", s1, ",", s2, "]", line[s1], word[-1])
                        ip = True
                        break
                    # print(len(word), s1, s2, len(word) - (s2 - s1 + 2))
                if not ip:
                    s2 -= 1
                    s1 = s2
                else:
                    s1 -= 1
        
            # print(line[:-1], c1, c2)
            sum += int(c1 + c2)

        # print(sum)
        return sum
    
if __name__ == '__main__':
    print(calibrateValues("calibration.txt"))