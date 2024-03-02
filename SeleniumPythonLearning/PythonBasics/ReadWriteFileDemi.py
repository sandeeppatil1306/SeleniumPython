file = open("TestFile.txt")

# print(file.read(5))
# file.readline()#
# print(file.readline())
# print(file.readline())


# Print line by line using readline method

#line = file.readline()

#while line != "":
   # print(line)
   # line = file.readline()

for line in file.readlines():
    print(line)

file.close()
