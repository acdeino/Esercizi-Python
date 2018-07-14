emails = ["me@yahoo.com", "you@gmail.com", "hesheit@yahoo.com", "we@hotmail.com", "they@me.com"]
for email in emails:
    print(email)


print("-------------")

for item in emails:
    if "hotmail" in item:
        print(item)

print("-------------")

for item in emails:
    if "gmail" in item:
        print(item)


print("_____________")

for item in emails:
    if "me.com" in item:
        print(item)

print("-------------")

for item in emails:
    if "yahoo" in item:
        print(item)

print("-------------")
