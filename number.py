import random

list = ["","","","","",""]

first  = random.randint(0,9)
print(first)
if first == 0:
    list[0] = ""
else:
    list[0] = str(random.randint(1,9))

print(list)
print(''.join(list))