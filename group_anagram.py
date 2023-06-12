class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TC: O(m * n)
        #countList is list, index: ord(), value: +=1
        #In res dict, key: countList, value: output(list of list of words),
        #defaultdict designed to help you out with missing keys,没有key，也可以append
        # list 不能当key，得换成tuple
        # dict.values() 是个list
        res = collections.defaultdict(list)
        for word in strs:
            countList = [0]* 26
            for c in word:
                countList[ord(c) - ord('a')] +=1
            res[tuple(countList)].append(word)
        return res.values()

                

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make countList, key: number, value: frequency
        # fill the freq[[]], index = count's value(frequency), value = count's key(num)
        countList = dict()
        freqency = [[] for i in range(len(nums) + 1)]
        for number in nums:
            countList[number] = countList.get(number, 0) + 1
        # make freq to be [[], [3], [2], [1], [], [], []]
        for num, freqIndex in countList.items():
            freqency[freqIndex]. append(num)
        print(freqency)

        #loop every element in every freq[0...n] for NOT add empty[] to res 
        res =[]
        for j in range(len(freqency) -1, 0, -1):
            # if freqency[j] = [], 不会进去
            for n in freqency[j]:
                res.append(n)
                if len(res) == k:
                    return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix 前缀，suffix 后缀, nums = [1,2,3,4],Output: [24,12,8,6]
        # 用prefix把res变成[1, 1, 2, 6]， 用suffix 把res再变成 [24, 12, 8, 6]
        res = [1]* len(nums)
        # iterative and use prefix to store the product of first nums[i-1]value 
        # make res[i] = nums[0]*...*nums[i-1]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix* nums[i]
        # after this, the res list would be all the prefix results
        # res[i]: it stores the prefix product for position i
        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            # res[j] = prefix * suffix 
            res[j] = res[j] * suffix
            # calculate next (j-1)'s suffix in advance
            # suffix is [j+1: ...], use suffix * nums[j], then we get [j: ...]
            suffix *= nums[j]
        return res



