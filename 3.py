class Solution:
    #双指针思路，利用set结构来判断是否出现在子串中
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        n = len(s)
        if n<=1:
            return n
        maxLen = 1
        i=0
        j=0
        while (i<n and j<n):
            if s[j] not in charSet:
                charSet.add(s[j])
                j+=1
                maxLen = max(j-i,maxLen)
            else:
                charSet.remove(s[i])
                i+=1
        return maxLen
if __name__ == '__main__':
    ss = Solution()
    result = ss.lengthOfLongestSubstring("hkajshdkjfhkasdf")
    print(result)