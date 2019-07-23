
class Solution:

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
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res


if __name__ == '__main__':
    s="wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]
    ss = Solution()
    result = ss.findSubstring(s,words)
    print(result)