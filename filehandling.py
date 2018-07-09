file = open("lorem.txt", 'r')

content = file.read()
print(type(content))

content = file.seek(0)
print(content)

content = file.readlines()
print(content)

content1 = [i.rstrip("\n") for i in content]
print(content1)

file.close()
