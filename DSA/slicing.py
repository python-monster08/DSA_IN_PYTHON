
# Slicing in String
# name = "Sourabh"
# print(name[0])
# print(name[0:4])
# print(name[0:])
# print(name[:4])
# print(name[-1::-1])


# Slicing in list:
lst = [10,2,20,30,4,50]
print(lst)
print(lst[0:])
print(lst[:3])
print(lst[2:5])
print(lst[-1::-1])
print(lst[::-1]) # Reverse the list
print(lst[::2]) # Print every 2nd element
print(lst[1::2]) # Print every 2nd element starting from index 1


# List functions:
print(lst, id(lst))
lst.append(11)
print(lst, id(lst))

lst.insert(0,12)
print(lst)

lst.pop(1)
print(lst)

lst.remove(2)
print(lst)

# String to list converssion separated by ,
sentance = "I'm,Python,Developer"
l = sentance.split(",")
print(l, type(l))

colors = ["Im", "Django", "Developer"]
res = " ".join(colors)
print(res, type(res))