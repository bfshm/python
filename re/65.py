import re
mo = re.match(r"[[0-9]{2,2}]*", "0123456789")
mo.group()
print(mo.group())