def size(n):
    s = 0
    while n > 0:
        s += 1
        n = n // 10
    return s


# print(size(153))
