# Arbitrary Arguments, *args
def nums_func(*nums): print("The second number is", nums[1])
nums_func(1, 3, 5, 7, 9) # The second number is 3

# Arbitrary Keyword Arguments, **kwargs
def me_func(**name): print(name["first_name"], name["last_name"])
me_func(first_name = "Zeynep", last_name = "Akkaya") # Zeynep Akkaya

# Default Parameter Value
def country_func(country = "Turkey"): print("I am from", country)
country_func("Poland") # I am from Poland
country_func() # I am from Turkey

# LAMBDA
# small anonymous function

x = lambda a, b, c: a + b + c
print(x(5, 10, 15))  # 30

def multiplier(n): return lambda a : a * n

doubler = multiplier(2)
print(doubler(11)) # 22

tripler = multiplier(3)
print(tripler(11)) # 33

# RECURSION

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
tri_recursion(5)
"""
1
3
6
10
15
"""