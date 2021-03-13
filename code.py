Coding:

n=int(input())
arr = list(input().split())
a=input()
arr.append(a)
arr.sort()
for i in range (0, n): 
    print (arr[i], end =" ") 
print(arr[n]) 
