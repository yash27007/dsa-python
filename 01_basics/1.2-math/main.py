"""
This file contains solutions to the basic math problems in Striver sheet

"""

import math

"""
1. Count the number of digits in a given number
"""

def count_digits(n:int)->int:
    count = int (math.log10(n)+1)
    return count

"""
2. Reverse a number
"""
def reverse_number(n:int)-> int:
    rev = 0
    while n > 0:
        ld = n%10
        rev = (rev*10) + ld
        n = n//10
    return rev

"""
3. Check if a number is palindrome or not
"""

def check_palindrome(n:int)->bool:
    return n == reverse_number(n)

"""
4. GDC of Two numbers - Euclidean Algorithm
"""

def gcd(a:int, b:int)->int:
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
        
    if a == 0 :
        return b
    return a

"""
5  . Armstrong Number
"""

def armstrong_number(n:int)->bool:
    dup = n
    sum = 0
    dig = count_digits(n)
    while n > 0:
        ld = n % 10
        sum = sum + pow(ld,dig)
        n = n//10
    
    if sum == dup:
        return True
    return False
