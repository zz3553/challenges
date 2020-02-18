mem = {1: 0, 2: 1, 3: 1}


class Solution():

    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in mem:
            if n-1 not in mem:
                self.tribonacci(n-1)
                self.tribonacci(n)
            else:
                mem[n] = mem[n-3] + mem[n-2] + mem[n-1]
        return sum(mem)

    def sum(mem):
        #temp = mem.copy()
        res = 0
        print(len(mem))
        for x in range(len(mem)):
            # num = mem[temp.pop(x+1)]
            print(mem[x+1])
            res += mem[x + 1]

        return res

if __name__ == '__main__':
    res = Solution()
    #print(sum(mem))
    print(res.tribonacci(4))
    print(res.sum())

    #print(mem[1])
    temp = mem.copy()
    res = 0
    for x in range(len(temp)):
        #num = mem[temp.pop(x+1)]
        res += mem[x+1]

    #print(res)
