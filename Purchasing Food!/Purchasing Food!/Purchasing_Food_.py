
#Author: Joanna Wypadlo
#Title: Purchasing Food



price= format(0.5, '.2f')

print("Yummy Gummies costs £" + str(price) +  " each (ex. VAT).")


yummyGummiesQty = int(input("How many would you like to buy: "))




try:
    yummyGummiesQty = int(input("How many would you like to buy: "))
except TypeError
    print("Program accepts only integer numbers.")





totalNoVat= yummyGummiesQty * price
vat = int(totalNoVat) * 0.20


print("\n\nTotal cost ex. VAT: £ " + str(totalNoVat))
print("VAT: £ " + str(vat))
print("Total cost inc VAT: £ " + str(totalNoVat + vat))

input("\n\n\nPress any button to exit")
