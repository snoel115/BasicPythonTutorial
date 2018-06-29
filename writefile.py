sFileDestination = 'C:/temp/p.txt'
#write something in the file
fob=open(sFileDestination, 'w') #if the file does not exists, it will be created
fob.write("1 - Bonjour comment ca va? \n")
fob.write("2 - Ca va tres bien, merci? \n")
fob.write("3 - et toi comment ca va? \n")
fob.close()


#read the file in chunck
fob=open(sFileDestination, 'r')
print("The first 3 caracters: " + fob.read(3))
print("The next 4 caracters: " + fob.read(4))
print("Read the rest of the file: " + fob.read())  #read the rest of the document
fob.close()

print ("****************** \r\n")

#read the file line by line
fob=open(sFileDestination, 'r')
print("Print the first line in the file")
print(fob.readline())
fob.close()

print ("****************** \r\n")

#read the file in a list
fob=open(sFileDestination, 'r')
print("This is the file content as a list")
print(fob.readlines())
fob.close()

#read the file in a list
fob=open(sFileDestination, 'a+') #a+ is appen and read
fob.write("4 - This is a new line\n")
print(fob.readlines())
fob.close()

#modified a specific line
fob=open(sFileDestination, 'r')
content = fob.readlines()
fob.close()
content[2] = "5 - ********** I love bacon ************* \n"
fob=open(sFileDestination, 'w')
fob.writelines(content)
fob.close()
