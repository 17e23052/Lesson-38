file1 = open("transcript1.txt","r")
file2 = open("transcript2.txt","r")
for line in file1:
  print(line.strip())
  print(file2.readline().strip())