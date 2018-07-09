activity = input("What are you doing? ")
print(activity)


# how to use input properties in order to program a  currency converter:
def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars


r = input("Enter rate in dollars: ")
e = input("Enter Euros: ")

print(currency_converter(float(r), float(e)))
