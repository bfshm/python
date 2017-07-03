import re
pt = r"^_?[a-zA-Z]+\d*"
mo = re.match(pt, "aabaaabaaaab")
print(mo.group())