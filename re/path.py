import re
pt = "c:\rapidminer\lib\plugs"
mo = re.match(pt, "c:\rapidminer\lib\plugs")
print(mo.group())