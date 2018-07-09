def minutes_to_hours(seconds, minutes=70):
    hours = minutes / 60.0 + seconds / 3600
    return hours


print(minutes_to_hours(300, 200))


# oppure si puo' scrivere:

# def minutes_to_hours(seconds, minutes=70):
    # hours = minutes / 60.0 + seconds / 3600
    # print(hours)


# (minutes_to_hours(300, 200))

# for example, numbers2.py's file function can  be rewritten as
def age_foo(age):
    new_age = float(age) + 50
    return new_age


age = input("Enter your age: ")
print(age_foo(age))
