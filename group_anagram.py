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


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        # key of squares: pairs (r/3, c/3)
        # defaultdict(set) creates a dictionary-like object where each key has default value of an empty set.
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # use slicing to find out the length of word
            # 从i到j-1， 不包括j
            # j位置是#
            length = int(s[i:j])
            res.append(s[j+1: j+1 +length])
            i = j + 1 + length
        return res
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # iterate nums, check number -1不在numSet, Set length为0,再记录length最长的长度
        numSet = set(nums)
        longest = 0
        for number in nums:
            if number - 1 not in numSet:
                length = 0
                while number + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

class RandomizedSet:

    def __init__(self):
        self.numMap = {} # used to map each element's index in numList 
        self.numList = [] # store val

    def insert(self, val: int) -> bool:
        res = val not in self.numList
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res
        
    # delete之后，list的最后一个copy到要delete的地方，然后pop list
    def remove(self, val: int) -> bool:
        res = val in self.numList
        if res:
            idx = self.numMap[val]
            lastValue = self.numList[-1]
            self.numList[idx] = self.numList[-1]
            self.numList.pop()
            # remap hashMap to match last element's index of list 
            self.numMap[lastValue] = idx
            del self.numMap[val]
        return res
  
    def getRandom(self) -> int:
        return random.choice(self.numList)
    
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # iterate and add number in nums，找到最小值，然后return负值+1
        total = 0
        minVal = 0
        for number in nums:
            total += number
            print(total)
            minVal = min(minVal, total)
        return (-minVal + 1)


###### Two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
        #use "while" for case： s[left] has 2个连续 Non-AlphNumeric strings but s[right] has 1.
        left, right = 0, len(s)- 1
        while left < right:
            while left< right and not s[left].isalnum():
                left += 1
            while left< right and not s[right].isalnum():
                right -= 1
            print(s[left].lower(),s[right].lower())
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        