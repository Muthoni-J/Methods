str1 = "children playing in the playing ground"
str =len(str1)//2
str2 = str1[:str].lower() + str1[str:].upper()
print(str2)

str1 = "children playing in the playing ground"
str =len(str1)//2
str2 = str1[:str].upper() + str1[str:].lower()
print(str2)  

str = "children playing in the playing ground"
def splitting():
    str = "children playing in the playing ground"
    # get half of the string
    str1 =len(str)//2
    # joining the string
    str2 = str[:str1].lower() + str[str1:].upper()
    return str2
print(splitting())

