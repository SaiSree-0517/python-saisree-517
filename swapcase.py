"""
converting the
character from uppercase to
lower case and vice versa

"""
s=input()
nstr=""
for i in range (len(s)):
    if s[i].isupper():
        nstr+=s[i].lower()
    elif s[i].islower():
        nstr+=s[i].upper()
    else:
        nstr+=s[i]
print(nstr)
#output
All Cse A Students Are Very active
aLL cSE a sTUDENTS aRE vERY ACTIVE
