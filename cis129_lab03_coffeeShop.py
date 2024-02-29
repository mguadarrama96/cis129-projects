# Lab 03 of CIS 129. We designed a program for a coffee and muffin shop, to be able to create accurate reciepts no matter / 
# what inputs are used.

# First part of the receipt, including the decorative asteriks. Collecting the values for coffees and muffins.
print('***************************************')

# Changed the name of the shop
print('My Coffee and Bakery Shop')

print('Number of coffees bought?')
coffees = int(input())
print('Number of muffins bought?')
muffins = int(input())

# Added 2 more items on the menu.
print('Number of cookies bough?')
cookies = int(input())
print('Number of cakes bought?')
cakes = int(input())
print('***************************************')

# Creating the space between the 2 receipts, equivalent to 2 lines.
print()
print()

# New variables with set values. The price of the coffee and muffins.
coffee_price = 5
muffin_price = 4 
cookie_price = 2
cake_price = 3

# The variable for the cost of the coffee and muffins, without the tax included.
## Added the new menu items to the subtotal variable.
subtotal = (coffees * coffee_price) + (muffins * muffin_price) + (cookies * cookies_price) + (cakes * cakes_price)

# Creating the variable for the cost of the menu items alone, without tax. Formated for Float with 2 decimal points always showing.
coffee_subtotal = (coffees * coffee_price)
fcoffee_subtotal = f'{coffee_subtotal: .2f}'
muffin_subtotal = (muffins * muffin_price)
fmuffin_subtotal = f'{muffin_subtotal: .2f}'

# Created the new varaibles for the added menu items
cookies_subtotal = (cookies * cookies_price)
fcookies_subtotal = f'{cookies_subtotal: .2f}'
cakes_subtotal = (cakes * cakes_price)
fcakes_subtotal = f'{cakes_subtotal: .2f}'

# Variable for the set tax rate. Line 31 variable to figure out the total tax, dependent on the subtotal.
tax_rate = .06
tax = subtotal * tax_rate

# The variable for the total cost.
total = subtotal + tax

# The second part of the receipt, formatted to match the prompt. Experimented to make sure the math is right, no matter what vaulues you choose for the amount of coffees and muffins.
print('***************************************')
print('My Coffee and Bakery Shop Receipt') 
print(coffees, 'Coffee at $' ,coffee_price, 'each: $' ,fcoffee_subtotal)
print(muffins, 'Muffins at $' ,muffin_price, 'each: $' ,fmuffin_subtotal)

# Added the 2 new menu items
print(cookies, 'Cookies at $' ,cookies_price, 'each: $' ,fcookies_subtotal)
print(cakes, 'Cakes at $' ,cakes_price, 'each: $' ,fcakes_subtotal)

print('6% tax: $' ,tax)
print('----------')
print('total: $' ,total)

# Added a thankful message at the end of the receipt.
print()
print('Thank you for your Business! Have a great day!')

print('***************************************')
