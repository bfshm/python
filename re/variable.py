import re
pt = r"^_?[a-zA-Z]+\d*"
mo = re.match(pt, "a")
print(mo.group())
mo = re.match(pt, "a1")
print(mo.group())
mo = re.match(pt, "ab1")
print(mo.group())
mo = re.match(pt, "_a")
print(mo.group())
mo = re.match(pt, "_a1")
print(mo.group())
mo = re.match(pt, "_ab1")
print(mo.group())