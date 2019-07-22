#递归思路，确定第一位对第n-1位进行全排列
def permutations(arr,position,end):
    if position==end:
        print(arr)
    else:
        for index in range(position,end):
            arr[index],arr[position]=arr[position],arr[index]
            permutations(arr, position+1,end)
            arr[index], arr[position] = arr[position], arr[index]

#深度搜索，返回时回溯
visit = [True,True,True]
temp = ["" for x in range(0,3)]
def dfs_permutations(position):
    if position== len(arr):
        print(temp)
        return
    for index in range(0,len(arr)):
        if visit[index] == True:
            temp[position]=arr[index]
            visit[index] = False
            dfs_permutations(position+1)
            visit[index] = True
arr=["a","b","c"]
result = dfs_permutations(0)
print (result)