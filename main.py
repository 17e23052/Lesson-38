file = open("numbers.txt","r")
total = 0
for line in file:
  total = total + int(line)
print(f"The total of the numbers is {total}")