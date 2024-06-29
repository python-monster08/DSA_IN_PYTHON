"""
Problem 1: Print this given below pettern:
    *
   ***
  *****
 *******
*********

"""
n = int(input())

# SOLUTION :-
for  i in range(n):
    # for space
    for j in range(n-i-1):
        print(" ", end="")
    
    # for star
    for k in range(2*i+1):
        print("*", end="")
    print()

print()
"""
Problem 2: Print this given below pettern:
*********
 *******
  *****
   ***
    *

"""
# SOLUTION :-
for i in range(n):
    for j in range(i):
        print(" ", end="")
    
    for k in range(2*n-2*i-1):
        print("*", end="")
    print()

print()
"""
Problem 3: Print this given below pettern:
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
# SOLUTION 1:-

# Upper half of the pattern
for i in range(1, (n*2 // 2) + 2):
    # Printing spaces
    for j in range((n*2 // 2) + 1 - i):
        print(" ", end="")
    
    # Printing asterisks
    for k in range(2 * i - 1):
        print("*", end="")
    
    print()

# Lower half of the pattern
for i in range((n*2 // 2) + 1, 0, -1):
    # Printing spaces
    for j in range((n*2 // 2) + 1 - i):
        print(" ", end="")
    
    # Printing asterisks
    for k in range(2 * i - 1):
        print("*", end="")
    
    print()

print("------------------------")
# SOLUTION 2: 

# Set the size of the pattern
# Set the size of the pattern
n = 5
rows = 2 * n - 1

# Upper half of the pattern
for i in range(1, rows + 1):
    if i <= n:
        # Upper half including the middle line
        spaces = n - i
        stars = 2 * i - 1
    else:
        # Lower half excluding the middle line
        spaces = i - n
        stars = 2 * (rows - i) + 1
    
    # Print spaces
    print(" " * spaces, end="")
    
    # Print stars
    print("*" * stars)
"""
Problem 4: Print this given below pettern:
*
**
***
****
*****
****
***
**
*
"""
# SOLUTION :-
for i in range(2*n-1):
    if i<n:
        for j in range(i+1):
            print("*", end="")
    else:
        for j in range(2*n-1-i):
            print("*", end="")
    print()

print("--------------")
"""
Problem 5: Print this given below pettern:
1
01
101
0101
10101
"""
# SOLUTION:-
for i in range(n):
    for j in range(i+1):
        print((i+j+1)%2, end=" ")
        # if (i+j)%2==0:
        #     print("1", end=" ")
        # else:
        #     print("0", end=" ")
    print()


print("--------------")
"""
Problem 6: Print this given below pettern:
1      1
12    21
123  321
12344321
"""

n = 4

for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    for j in range((n-i-1)*2):
        print(" ", end="")
    for j in range(i+1,0,-1):
        print(j, end="")
    print()