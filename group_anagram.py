class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

                

            




