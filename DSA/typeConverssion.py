a = 4.5
print(a, type(a))

res = int(a)
print(res, type(res))

res1 = str(a)
print(res1, type(res1))


lst = [3,4,5,6]
print(lst, type(lst))
res2 = tuple(lst)
print(res2, type(res2))
res3 = set(lst)
print(res3, type(res3))

color = ["orange", "pink", "black"]
qty = [3,4,5]

print(dict(zip(color, qty)))

set1 = list((zip(color, qty)))
print(set1, type(set1))

print (bool([]), bool(()), bool({}), bool(""), bool(0), bool(0.0), bool(set()))
print (bool([1]), bool((1)), bool({"1":"Item1"}), bool("Kamlesh"), bool(1), bool(1.0), bool({1}))

# s = set()
s = {1}
print(s,type(s))
print(len(s))