def age_foo(age):
    new_age = age + 15
    return new_age


age = float(input("Enter your age: "))
print(age_foo(age))


if int(age) > 40:
    print("You are young !")
elif int(age) in range(41, 65):
    print("You are middle aged !")
else:
    print("You are old !")
