# # Q1
# def sum_of_arrays(a):
#     s = 0
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             s = s + a[i][j]
#
#     return s
#
#
# # Q2
# def sum_of_2D_Array(a, b):
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             a[i][j] = a[i][j] + b[i][j]
#             return a[i][j]
#
#
# # Q3
# def sum_of_diagonals(a):
#     s = 0
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             if i == j or i + j == len(a) - 1:
#                 s = s + a[i][j]
#
#     return s
#
#
# # Q4
# def transpose(a):
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             return a[j][i]
#
#
# # Q5
# def mul(a, b):
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             s = 0
#             for k in range(len(b[i])):
#                 s += a[i][k] * b[k][j]
#             print(s, end=" ")
#     print()
#

# *********************************************************************************************************

# a = ['orange', 'apple']

# a.append("guava")
# print(a)

# a.clear()
# print(a)

# x = a.copy()
# print(x)

# m = a.count("apple")
# print(m)

# b = "guava"
# a = a.extend(b)
# print(a)


# print(a.index("apple"))

# print(a.insert(0, 'guava'))

# a.pop(0)
# print(a)

# a.remove("apple")
# print(a)

# a.reverse()
# print(a)

# a.sort()
# print(a)


# *********************************************************************************************************


# Q - Show the no:of occurrences of a specific element

# ls = [1, 2, 3, 3, 4, 4, 4, 6, 8, 9]
# print(ls.count(4))

# Q - Create a new list with all unique items

# ls = [1, 2, 3, 3, 4, 4, 4, 6, 8, 9]
# new_ls = []
# for i in range(len(ls)):
#     if ls[i] not in new_ls:
#         new_ls.append(ls[i])
# print(new_ls)

