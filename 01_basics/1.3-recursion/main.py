"""
1. Print a name n times using recursion

"""
def print_n_time(name:str,n:int)->None:
    if n<=0:
        return
    if n==1:
        print(name)
        return
    print(name)
    print_n_time(name,n-1)

"""
2. Print n numbers 
"""

def print_n_numbers(current:int, n:int)->None:
    if current > n:
        return
    print(current)
    print_n_numbers(current+1,n)

# print_n_numbers(1,5)

"""
3. Print the sum of N numbers
"""

def sum_of_n(n:int)->int:
    if n <= 0:
        return 0
    return n + sum_of_n(n-1)

# print(sum_of_n(5))

"""
4. Factorial of a number
"""

def factorial(n:int)->int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# print(factorial(5))

"""
5. Check if a string is palidrome
"""

def check_palindrome(text: str) -> bool:
    return text == text[::-1]

print(check_palindrome("malayalam"))
