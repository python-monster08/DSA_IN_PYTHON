age = 28
print("my age is %d" %(age))

name = "My name is Kamlesh Lovewanshi"
res = name.split()
print(res,type(res))
rev = res[::-1]
print(" ".join(rev))


name = input()
age = int(input())
intro = f"My name is {name}." \
f" I am {age} years old."
print(intro)
print(f"My name is {name.capitalize()}!")


s = "           Hello World        ".lstrip()
print(s)
s = "           Hello World        ".rstrip()
print(s)

st = "  Solving any problem is an art. ".strip(' ')
print(st)

str1 = "My name is Jaspreet ".rstrip('my ')
print(str1)

spt = "Hello! I am Jaspree".rsplit()
print(spt)


# Can we use the join method to join the integers of the above list without any space between then.
# (a) Yes (b) No 
#  Answer is No because join is the string method.
lst = [1, 2]
result = ''.join(str(num) for num in lst)
print(result)