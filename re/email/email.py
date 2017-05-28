import re
pt = "^[\w-]+@[\w-]+(\.[\w-]{2,3})+$"
email = "bEn_-@111.net.com"
mo = re.match(pt, email)
print(mo.group())