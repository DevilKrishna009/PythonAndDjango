# class Armstrong:
#     def size(self, num):
#         s = 0
#         temp = str(num)
#         for i in range(len(temp)):
#             s += 1
#         return s
#
#     def arm(self, num):
#         res = 0
#         t = num
#         for i in range(self.size(num)):
#             res = res + (t % 10) ** self.size(num)
#             t = t // 10
#         if res == num:
#             return f"{num} is an Armstrong number"
#         else:
#             return f"{num} is not an Armstrong number"
#
#
# obj = Armstrong()
# print(obj.size(153))
# print(obj.arm(153))
#

# class Palindrome:
#     def size(self, num):
#         temp = str(num)
#         sz = 0
#         for i in range(len(temp)):
#             sz += 1
#         return sz
#
#     def pal(self, num):
#         s = 0
#         t = num
#         for i in range(self.size(num)):
#             s = s * 10 + (t % 10)
#             t = t // 10
#         if s == num:
#             return f"{num} is a palindrome number"
#         else:
#             return f"{num} is not a palindrome number"
#
#
# obj = Palindrome()
# print(obj.size(121))
# print(obj.pal(121))


# class Fibonacci:
#     def fib(self, num):
#         a = int(input("Enter the first number"))
#         b = int(input("Enter the second number"))
#         c = 0
#         ls = []
#         print("The fibonacci series of the given problem is", end=" ")
#         for i in range(num):
#             c = a + b
#             a = b
#             b = c
#             ls.append(c)
#         return ls
#
#
# obj = Fibonacci()
# print(obj.fib(5))


# import random
#
# d = ['stone', 'paper', 'scissor']
#
#
# def random_play():
#     comp_choice = random.choice(d)
#     return comp_choice
#
# # print(comp_choice)
#
#
# n = int(input("Enter no:of rounds to be played "))
# c_score = 0
# my_score = 0
# for i in range(n):
#     a = input("Enter your choice ")
#     b = random_play()
#     print("Computer_Choice :", b)
#     if a == b:
#         c_score += 0
#         my_score += 0
#     elif a == 'scissor' and b == 'paper':
#         my_score += 1
#         c_score += 0
#     elif a == 'paper' and b == 'stone':
#         my_score += 1
#         c_score += 0
#     elif a == 'stone' and b == 'scissor':
#         my_score += 1
#         c_score += 0
#     elif a == 'paper' and b == 'scissor':
#         my_score += 0
#         c_score += 1
#     elif a == 'stone' and b == 'paper':
#         my_score += 0
#         c_score += 1
#     elif a == 'scissor' and b == 'stone':
#         my_score += 0
#         c_score += 1
#
# if c_score > my_score:
#     print("My Score : ", my_score)
#     print("Computer Score : ", c_score)
#     print("Well Played Computer")
# elif my_score > c_score:
#     print("My Score : ", my_score)
#     print("Computer Score : ", c_score)
#     print("KAL ANA KAL")
# else:
#     print("My Score : ", my_score)
#     print("Computer Score : ", c_score)
#     print("GGS")


board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}


def print_board():
    print(board[1], " |", board[2], "|", board[3])
    print("---+---+---")
    print(board[4], " |", board[5], "|", board[6])
    print("---+---+---")
    print(board[7], " |", board[8], "|", board[9])


print_board()

for i in range(9):
    user_1 = input("User 1, please enter your input: ")
    user_2 = input("User 2, please enter your input: ")
