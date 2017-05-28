import re
pt = "\r\n\r\n"
st = "111\
222\
\
333"
mo = re.match(pt, st)
print(mo.group())