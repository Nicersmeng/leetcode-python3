
# class Solution:

    # def findSubstring(self, s, words):
    #     from collections import Counter
    #     length = len(words[0])
    #     windows = len(s)/length
    #     wordCounter = Counter(words)
    #     maxLen=1
    #     j=0
    #     i=0
    #     result=[]
    #     cur_Counter=Counter()
    #     while i<windows and j<windows:
    #
    #         temp_word = s[j*length:(j+1)*length]
    #         if temp_word not in words:
    #             j+=1
    #             i=j
    #             cur_Counter.clear()
    #             maxLen=1
    #             continue
    #         if cur_Counter[temp_word] < wordCounter[temp_word] and temp_word in words:
    #             cur_Counter[temp_word]+=1
    #             j+=1
    #             maxLen = max(j-i,maxLen)
    #         else:
    #             if i+1<j:
    #                 cur_Counter[s[i * length:(i + 1) * length]]-=1
    #                 i+=1
    #             else:
    #                 i+=1
    #                 j+=1
    #
    #
    #         if maxLen == len(words):
    #             result.append(i*length)
    #             cur_Counter[s[i * length:(i + 1) * length]] -= 1
    #             i+=1
    #             maxLen-=1
    #
    #
    #     return result
class Solution:
    def findSubstring(self, s, words):
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        words_num = len(words)
        n = len(s)
        if n<one_word:return []
        wordCounter = Counter(words)
        result=[]
        for i in range(one_word):
            cur_cnt = 0
            cur_Counter = Counter()
            # 循环one_word次，遍历所有的可能性
            left=i
            right=i
            while right+one_word<=n:
                temp_word = s[right:right+one_word]
                right+=one_word
                if temp_word not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt=0
                else:
                    cur_Counter[temp_word]+=1
                    cur_cnt+=1
                    while cur_Counter[temp_word]>wordCounter[temp_word]:
                        #删掉左边的
                        left_word = s[left:left+one_word]
                        left+=one_word
                        cur_Counter[left_word]-=1
                        cur_cnt-=1
                    if cur_cnt==words_num:
                        result.append(left)
        return result




if __name__ == '__main__':
    # s="wordgoodgoodgoodbestword"
    # words = ["word","good","best","good"]
    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]
    ss = Solution()
    result = ss.findSubstring(s,words)
    print(result)