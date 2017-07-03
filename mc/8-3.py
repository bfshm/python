def upper_initial(strsrc):
    strdst = strsrc[:1].upper()
    strdst += strsrc[1:].lower()
    return strdst

print(upper_initial('hello'))
print(upper_initial('sunday'))
print(upper_initial('september'))