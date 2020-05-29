def solution(string):
    res = ' ' #final string to return
    result = res.split()
    count = 1
    for x in range(len(string)):
        y = x + 1
        char = string[x]

        while(string[y] == char): #goes through next characters until new char comes up
            count += 1
            y += 1
            x += 1
            if (string[y] != char):
                result.append(char)
                num = str(count)
                result.append(num)
                count = 1
                y = 0
            continue


    return "".join(result)


def main():
    print(solution('aabcccccaaa'))


main()
