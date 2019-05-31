price = float(input())
tip = int(input())
tax = int(input())

tip_amount = price * (float(tip / 100))
tax_amount = price * (float(tax / 100))

final = price + tip_amount + tax_amount
print("The total meal cost is " + str(round(final)) + " dollars.")