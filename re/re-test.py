import re

# match email, contain '@' and '.'
mo = re.match(r"\w*@\w*\.\w*", "1_23@ab_cAB.C")
print(mo.group())
