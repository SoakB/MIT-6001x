

pussy = "pussy tight pussy clean pussy fresh"
pussy = pussy.split(" ")
print(pussy)
print(type(pussy))


import string

upperList = list(string.ascii_uppercase)
lowerList = list(string.ascii_lowercase)

shift = 3
shifted_dict = {}

# take "letter" in lowerList and upperList (LISTS)
for i in range(len(lowerList)):
    try:
        shifted_dict[lowerList[i]] = lowerList[i + shift]
    except IndexError:
        shifted_dict[lowerList[i]] = lowerList[i + shift - len(lowerList)]

for i in range(len(upperList)):
    try:
        shifted_dict[upperList[i]] = upperList[i + shift]
    except IndexError:
        shifted_dict[upperList[i]] = upperList[i + shift - len(upperList)]

print(shifted_dict)
