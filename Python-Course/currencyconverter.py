print(1)


def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars


r = input("Enter rate in dollars: ")
e = input("Enter Euros: ")

print(currency_converter(float(r), float(e)))
