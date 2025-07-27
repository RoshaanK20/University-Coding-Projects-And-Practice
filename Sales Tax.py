# Sales Tax Calculator

# Getting Country Tax
country_tax = float(input("Enter Country Tax Rate (%): "))

# Product price
product_price = float(input("Enter Product Price: "))

# Validating input
if country_tax < 0 or product_price < 0:
    print("Invalid input. Please enter positive values for tax and product price.")
else:
    # Calculating tax value
    tax_value = country_tax / 100

    # Calculating sales tax
    sales_tax = tax_value * product_price

    # Calculating gross price
    gross_price = product_price + sales_tax

    print("\033[4;31;40m\n------------------RESULT-------------------")
    print("Country Tax Rate: {:.2f}%".format(country_tax))
    print("Product Price: ${:,.2f}".format(product_price))
    print("Sales Tax: ${:,.2f}".format(sales_tax))
    print("Gross Price: ${:,.2f}".format(gross_price))
