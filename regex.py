import re

with open("regex_test.txt") as f:
    data = f.readlines()
    #print(data)

#print(data)

valid_name = re.compile('[A-Z][a-z]+ ?[A-Z]?[a-z]*? [A-Z][a-z]+')

for name in data:
    output = valid_name.findall(name)
    if output == []:
        print("None.")
    else:
        print(output)