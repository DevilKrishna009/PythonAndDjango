# a = []
# print(type(a))

# a = [1, 2, 3, 4, 5, 6]
# # print(len(a))
#
# for i in range(len(a)):
#     print(a[i], end=" ")
#
# print(a[::-1])

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s = s + a[i][j]

print(s)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[j][i],end=" ")
    print()

"""
[[1,2,3]
[4,5,6]
[7,8,9]]

"""
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j or i + j == len(a) - 1:
            s = s + a[i][j]

print(s)

"""
 a = [[1,2,3]
[4,5,6]
[7,8,9]]

b = [[1,2,3]
[4,5,6]
[7,8,9]]
"""

s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = a[i][j] + b[i][j]
        print(a[i][j], end=" ")
    print()


