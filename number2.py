import random

#Determine lenght of the number
first = random.randint(0,9)
second = random.randint(0,99)
third = random.randint(0,999)
fourth = random.randint(0,9999)
fifth = random.randint(0,99999)

len = 6

if first == 0:
    len = 5
elif first == 0 and second == 0:
    len = 4
elif first == 0 and second == 0 and third == 0:
    len = 3
elif first == 0 and second == 0 and third == 0 and fourth == 0:
    len = 2
elif first == 0 and second == 0 and third == 0 and fourth == 0 and fifth == 0:
    len = 1

#Generate a number with the determined length
if len == 6:
    num = random.randint(100000,999999)
elif len == 5:
    num = random.randint(10000,99999)
elif len == 4:
    num = random.randint(1000,9999)
elif len == 3:
    num = random.randint(100,999)
elif len == 2:
    num = random.randint(10,99)
elif len == 1:
    num = random.randint(1,9)

print("Num is: ", num)

total = 0

if num % 2 == 0:
    print("Num is even")
    print("Total +100")
    print()
    total += 100
if num % 2 != 0:
    print("Num is odd")
    print("Total +100")
    print()
    total += 100
if num % 3 == 0:
    print("Num is divisible by 3")
    print("Total +150")
    print()
    total += 150
if num % 5 == 0:
    print("Num is divisible by 5")
    print("Total +150")
    print()
    total += 150
if num % 7 == 0:
    print("Num is divisible by 7")
    print("Total +200")
    print()
    total += 200
if num % 11 == 0:
    print("Num is divisible by 11")
    print("Total +250")
    print()
    total += 250
if num % 13 == 0:
    print("Num is divisible by 13")
    print("Total +300")
    print()
    total += 300
if '1' in str(num):
    print("Num contains 1")
    print("Total +100")
    print()
    total += 100
if '2' in str(num):
    print("Num contains 2")
    print("Total +100")
    print()
    total += 100
if '3' in str(num):
    print("Num contains 3")
    print("Total +100")
    print()
    total += 100
if '4' in str(num):
    print("Num contains 4")
    print("Total +100")
    print()
    total += 100
if '5' in str(num):
    print("Num contains 5")
    print("Total +100")
    print()
    total += 100
if '6' in str(num):
    print("Num contains 6")
    print("Total +100")
    print()
    total += 100
if '7' in str(num):
    print("Num contains 7")
    print("Total +100")
    print()
    total += 100
if '8' in str(num):
    print("Num contains 8")
    print("Total +100")
    print()
    total += 100
if '9' in str(num):
    print("Num contains 9")
    print("Total +100")
    print()
    total += 100
if '0' in str(num):
    print("Num contains 0")
    print("Total +100")
    print()
    total += 100
print("Total score: ", total)