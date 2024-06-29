# i = 0
# while i <=15:
#     print(i,"Hello")
#     i = i+1


# for i in range(2,21,2):
#     print(i)


# for i in range(1,11):
#     print(i*2)

lst = [6,7,8,9,40]
for i in range(len(lst)):
    print(i, ":",lst[i])

print("\nReverse")
for i in range(len(lst)-1,-1,-1):
    print(i,lst[i])

lst1 = [10,2,0,3,0,4,5,8]
k = 40
ans = -1
for i in range(len(lst1)):
    if lst1[i] == k:
        ans = i

print(ans)