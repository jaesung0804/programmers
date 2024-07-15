def ten2two(n,num):
    row = ''
    for i in range(0,n):
        if num >= (2**(n-i-1)):
            row += '1'
            num -= 2**(n-i-1)
        else: row += '0'
    return row
    
def is_full(str1, str2, n):
    result = ''
    for j in range(n):
        if int(str1[j]) or int(str2[j]):
            result += '#'
        else : result += ' '
    return result
    
def solution(n, arr1, arr2):
    answer = []
    
    map1 = list(map(lambda x:ten2two(n,x), arr1))
    map2 = list(map(lambda x:ten2two(n,x), arr2))
    
    return [is_full(map1[i],map2[i],n) for i in range(n)]