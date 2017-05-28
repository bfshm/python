import re
pt = "\d{1,2}[\/-]\d{1,2}[\/-]\d{2,4}"
st = "4/8/03"
#st = "10-6-2004"
#st = "01-01-01"
mo = re.match(pt, st)
print(mo.group())