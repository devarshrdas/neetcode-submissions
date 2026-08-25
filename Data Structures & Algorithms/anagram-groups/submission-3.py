class Solution:

    def getHash(s):
        hashList = []
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for i in range(26):
            hashList.append(str(freq[i]))
            hashList.append("$")

        return ''.join(hashList)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = {}

        for i in range(len(strs)):
            key = Solution.getHash(strs[i])

            if key not in hashmap:
                hashmap[key] = len(res)
                res.append([])

            res[hashmap[key]].append(strs[i])

        return res