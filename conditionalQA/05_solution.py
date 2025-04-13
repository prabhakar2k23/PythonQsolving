#Q.Given a string, find the first non-repeated character.

str1="teeters"
for char in str1:
    if(str1.count(char)==1):
        print(char)
        break