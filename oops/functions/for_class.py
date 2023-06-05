class ForClass:
    def is_prime(self, num):
        flag = 0
        for i in range(1, num + 1):
            if num % i == 0:
                flag += 1

        if flag == 2:
            return f"{num} is prime"
        else:
            return f"{num} is not a prime"

    def factorial(self, num):
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return f"Factorial of {num} is {fact}"

    def size_of_a_num(self, num):
        size = 0
        temp = num
        for i in str(temp):
            size += 1
        return f"The size of the {num} is {size}"

    def factors(self, num):
        ls = []
        for i in range(1, num + 1):
            if num % i == 0:
                ls.append(i)

        return ls

    def prime_factors(self, num):
        ls = []
        for i in range(1, num + 1):
            if num % i == 0 and self.is_prime(i) == f"{i} is prime":
                ls.append(i)

        return ls


obj = ForClass()
print(obj.is_prime(4))
print(obj.factorial(5))
print(obj.size_of_a_num(635))
print(obj.factors(20))
print(obj.prime_factors(20))
