a = int(input("Enter a number: "))


if a < 5:
    print("Your input is less than five!")

elif a == 5:
    print("Your input is equal to five!")

elif a > 5:
    print("Your input is more than five!")


def age_foo(age):
    new_age = age + 50
    return new_age


age = float(input("Enter your age: "))


if age < 150:
    print(age_foo(age))
else:
    print("How is that even possible?")
