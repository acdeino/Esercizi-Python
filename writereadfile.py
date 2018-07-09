file = open("example.txt", 'w')

file.write("Hello!  ")
file.write("I'm not going down to a new line, at least for the moment\n")
file.write("I am writing this file via python.\n")

list1 = ["line1", "line2", "line3"]
for item in list1:
    file.write(item + "\n")

file.close()
