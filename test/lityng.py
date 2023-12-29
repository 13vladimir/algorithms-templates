
n = 3
array1 = [1, 2, 3]
array2 = [4, 5, 6]


result = []
for i in range(n):
    result.append(array1[i])
    result.append(array2[i])
print(*result)






'''
def lityng(array1, array2):
    result = []
    for i in array1:
        result.append(i)
        for j in array2:
            result.append(j)
    return print(result)


lityng(array1, array2)
'''