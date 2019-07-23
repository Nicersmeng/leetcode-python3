# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         s1_len = len(s1)
#         s2_len = len(s2)
#         s1_list = sorted(list(s1))
#         left =0
#         right = s1_len-1
#         if s1_len>s2_len:
#             return False
#         while left+s1_len<=s2_len:
#             temp_w = s2[left:left+s1_len]
#             temp_list = sorted(list(temp_w))
#             if temp_list==s1_list:
#                 return True
#             left+=1
#         return False
#
#Counter之间可以比较是否相等
#Counter等于0需要pop出去，大于1做加减

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        s1_len = len(s1)
        s2_len = len(s2)
        left =0
        wordCounter = Counter(s1)
        cur_Counter = Counter(s2[0:s1_len])
        if s1_len>s2_len:
            return False
        while left+s1_len<=s2_len:
            if wordCounter!=cur_Counter:
                if cur_Counter[s2[left]] >0:
                    if cur_Counter[s2[left]]==1:
                        cur_Counter.pop(s2[left])
                    else:
                        cur_Counter[s2[left]] -= 1
                left+=1
                if left+s1_len>s2_len:
                    return False
                cur_Counter[s2[left+s1_len-1]]+=1
            else:
                return True

        return False

if __name__ == '__main__':
    s1 = "adc"
    s2 = "dcda"
    ss = Solution()
    result = ss.checkInclusion(s1,s2)
    print(result)