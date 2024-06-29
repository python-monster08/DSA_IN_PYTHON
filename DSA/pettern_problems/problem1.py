n = int(input())
"""
# Problem-1: Ractangle Pettern Print with * (star)
    *****
    *****
    *****
    *****
    *****
"""
print("solution 1:-\n")
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
   
print()


"""
# Problem-2: Trangle Pettern Print with * (star)
    *
    **
    ***
    ****
    *****
"""
print("solution 2:-\n")
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

print()

"""
# Problem-3: Trangle Pettern Print with integer (star)
    1
    12
    123
    1234
    12345
"""
print("solution 3:-\n")
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

print()
"""
# Problem-4: Trangle Pettern Print with same integer in single line (star)
    1
    22
    333
    4444
    55555
"""
print("solution 4:-\n")
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()

print()

"""
Problem-5: Down Trangle Pettern Print with (star)
    *****
    ****
    ***
    **
    *
"""
print("solution 5:-\n")
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

print()

"""
Problem-6: Down Trangle Pettern Print with number
    12345
    1234
    123
    12
    1
"""
print("solution 6:-\n")
for i in range(n):
    for j in range(n-i):
        print(j+1, end="")
    print()

