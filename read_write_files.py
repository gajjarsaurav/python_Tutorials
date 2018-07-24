fileWrite = open('sample.txt', 'w')
#    we actually need to create two file objects one for writing file and one for reading it
fileWrite.write("we're gonna write some stuff here\n")
fileWrite.write("hey there everyone\n")
fileWrite.write("saurabh here")
fileWrite.close()

fileRead = open('sample.txt', 'r')
readText = fileRead.read()

print(readText)
