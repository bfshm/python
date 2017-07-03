import re
pt = r"\(?\d{3}\)?-?\d{6}"
mo = re.match(pt, "010879556")
print(mo.group())
mo = re.match(pt, "010-879556")
print(mo.group())
mo = re.match(pt, "(010)879556")
print(mo.group())
