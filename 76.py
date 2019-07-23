# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 说明：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t_Counter = Counter(list(t))
        if not s or len(s)<len(t):return ""
        left=0
        right=0
        cur_cnt=0
        n=len(s)
        minLen=n
        result=""
        cur_Counter=Counter()
        # pointer = [False]*len(t)
        dict_point = dict(Counter(list(t)))
        while right<n:

            while [0]*len(dict_point)!= list(dict_point.values()) and right<n:
                w = s[right]
                if w not in t_Counter:
                    right+=1

                    continue
                cur_Counter[w]+=1
                right += 1
                if t_Counter[w]>0 and dict_point[w]>0:
                    dict_point[w]-=1
            while [0]*len(dict_point)== list(dict_point.values()):
                left_w = s[left]
                if left_w not in t_Counter:
                    left+=1
                    continue
                cur_Counter[left_w]-=1
                left+=1
                if cur_Counter[left_w]==t_Counter[left_w]-1:
                    dict_point[left_w]+=1
            if (right-left+1)<=minLen:
                minLen=right-left+1
                result=s[left-1:right]
        return result

if __name__ == '__main__':
    S="ADOBECODEBANC"
    T = "ABC"
    ss=Solution()
    result = ss.minWindow(S,T)
    print(result)