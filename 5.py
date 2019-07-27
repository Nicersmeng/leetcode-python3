#对于字符串str，假设dp[i,j]=1表示str[i...j]是回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        len_s = len(s)
        if len_s==1:return s
        longest = 1
        start = 0
        dp = [[0 for i in range(len_s)] for j in range(len_s)]
        for i in range(len_s):
            dp[i][i]=1
            if i<len_s-1:
                if s[i]==s[i+1]:
                    dp[i][i+1]=1
                    start = i
                    longest = 2
        i=0
        for l in range(3,len_s+1):
            for i in range(0,len_s-l+1):
                j = i+l-1
                if(s[i]==s[j] and dp[i+1][j-1]==1):
                    dp[i][j]=1
                    start = i
                    longest=l

        return s[start:start+longest]
if __name__ == '__main__':
    ss = Solution()
    s = "aaafasdfaasdsa"
    ss.longestPalindrome(s)