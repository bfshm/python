l1 = ['Hello', 'world', 101]
l2 = [x.upper() for x in l1 if isinstance(x, str) == True]
print(l2)