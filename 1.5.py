

def oneAway(str1, str2):
    map1 = {}

    # populating map
    for x in range(len(str2)):
        if str2[x] in map1:
            map1[str2[x]] += 1
        else:
            map1[str2[x]] = 1

    #comparing strings and map
    count = 1
    for x in range(len(str1)):
        char = str1[x] #testing purposes
        if str1[x] in map1:
            map1.pop(str1[x])
            count += 1

    if (len(str1) - count) + len(map1) < 2:
        return True
    else:
        return False


def main():
    print(oneAway('pale', 'ple'))
    print(oneAway('pales', 'pale'))
    print(oneAway('pale', 'bale'))
    print(oneAway('pale', 'bake'))
    print()
    print(oneAway('ple', 'pale'))
    print(oneAway('pale', 'pales'))
    print(oneAway('bale', 'pale'))
    print(oneAway('bake', 'pale'))
    print()
    print(oneAway('', 'abc'))
    print(oneAway('abc', ''))
main()