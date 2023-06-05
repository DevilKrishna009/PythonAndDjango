# n = int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n = int(input())
# for i in range(n,0,-1):
#     for j in range(1,i):
#         print(" ",end =" ")
#     for k in range(n-i+1):
#         print("*",end = " ")
#     print()


# n = int(input())
# l = n-1
# for i in range(n):
#     for j in range(l):
#         print(end = " ")
#     for k in range(i+1):
#         print("*",end =" ")
#     print()
#     l-=1

# n = int(input())
# for i in range(n):
#     for j in range(n-1):
#         print("",end = " ")
#     for k in range(i+1):
#         print("*  ")
# for i in range(n-1):
#     ...

# n = int(input())
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==j or i+j == n-1 or i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end =" ")
#         else:
#             print(" ",end =" ")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*",end = " ")
#     print()
# for i in range(n+1,0,-1):
#     for j in range(i-1):
#         print("*",end = " ")
#     print()


"""

*
**
***
****

"""

# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end = " ")
#     print()


"""
     *
    * *
   * * *
  * * * *
 * * * * *

"""

# n = int(input())
# for i in range(1,n+1):
#     for j in range(i,n):
#         print(" ",end = " ")
#     for k in range(i):
#         print("*  ",end = " ")
#     print()


"""
*****
****
***
**
*
"""

# n = int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


"""
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""

n = int(input())

for i in range(1, n+1):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i):
        print("*  ", end=" ")
    print()

for i in range(n-1, 0, -1):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i):
        print("*  ", end=" ")
    print()
