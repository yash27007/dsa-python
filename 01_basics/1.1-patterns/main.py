"""
This file contains the patterns problems solutions
Resource Link : https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/ */

"""

"""
Pattern 1
* * * * * 
* * * * * 
* * * * * 
* * * * *
* * * * *
"""

def pattern1(n:int)->None:
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
        print()

# pattern1(5)

"""
Pattern 2

* 
* * 
* * * 
* * * * 
* * * * * 

"""

def pattern2(n:int)->None:
    for i in range(0,n):
        for j in range(i+1):
            print("*",end=" ")
        print()

# pattern2(5)

"""
Pattern 3
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

def pattern3(n:int)->None:
    for i in range(0,n):
        for j in range(i+1):
            print(j+1,end=" ")
        print()

# pattern3(5)

"""
Pattern 4
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

def pattern4(n:int)->None:
    for i in range(0,n):
        for j in range(i+1):
            print(i+1,end=" ")
        print()

# pattern4(5)

"""
Pattern 5

* * * * * 
* * * *
* * *
* *
*

"""

def pattern5(n:int)->None:
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

# pattern5(5)

"""
Pattern 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1
"""

def pattern6(n:int)->None:
    for i in range(n,0,-1):
        for j in range(i):
            print(j+1,end=" ")
        print()

# pattern6(5)

"""
Pattern 7

     *     
    ***    
   *****   
  *******  
 ********* 

"""
def pattern7(n:int)->None:
    for i in range(0,n):
        for _ in range(n-i-1):
            print(" ",end="")
        for _ in range(2*i+1):
            print("*",end="")
        print()

# pattern7(5)

"""
Pattern 8

*********
 ******* 
  *****
   ***
    *

"""
def pattern8(n:int)->None:
    for i in range(n,0,-1):
        for _ in range(n-i):
            print(" ",end="")
        for _ in range(2*i-1):
            print("*",end="")
        print()
# pattern8(5)

"""
Pattern 9

    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

"""

def pattern9(n:int)->None:
    for i in range(0,n):
        for _ in range(n-i-1):
            print(" ",end="")
        for _ in range(2*i+1):
            print("*",end="")
        print()
    for i in range(n,0,-1):
        for _ in range(n-i):
            print(" ",end="")
        for _ in range(2*i-1):
            print("*",end="")
        print()
    
# pattern9(5)

"""
Pattern 10

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
def pattern10(n:int)->None:
    for i in range(0,n):
        for _ in range(i+1):
            print("*",end=" ")
        print()
    
    for i in range(n-1,0,-1):
        for _ in range(i):
            print("*",end=" ")
        print()
        
# pattern10(5)
