# First part of the receipt, including the decorative asteriks. Collecting the values for coffees and muffins.
print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
coffees = int(input())
print('Number of muffins bought?')
muffins = int(input())
print('***************************************')

# Creating the space between the 2 receipts, equivalent to 2 lines.
print()
print()

# New variables with set values. The price of the coffee and muffins.
coffee_price = 5
muffin_price = 4 

# The variable for the cost of the coffee and muffins, without the tax included.
subtotal = (coffees * coffee_price) + (muffins * muffin_price)

# Creating the variable for the cost of coffee alone, without tax. Line 23 is the variable for the coffee subtotal, formated for Float with 2 decimal points always showing.
coffee_subtotal = (coffees * coffee_price)
fcoffee_subtotal = f'{coffee_subtotal: .2f}'

# Creating the variable for the cost of muffins alone, without tax. Line 27 is the variable for the muffin subtotal, formated for Float with 2 decimal points always showing.
muffin_subtotal = (muffins * muffin_price)
fmuffin_subtotal = f'{muffin_subtotal: .2f}'

# Variable for the set tax rate. Line 31 variable to figure out the total tax, dependent on the subtotal.
tax_rate = .06
tax = subtotal * tax_rate

# The variable for the total cost.
total = subtotal + tax

# The second part of the receipt, formatted to match the prompt. Experimented to make sure the math is right, no matter what vaulues you choose for the amount of coffees and muffins.
print('***************************************')
print('My Coffee and Muffin Shop Receipt') 
print(coffees, 'Coffee at $' ,coffee_price, 'each: $' ,fcoffee_subtotal)
print(muffins, 'Muffins at $' ,muffin_price, 'each: $' ,fmuffin_subtotal)
print('6% tax: $' ,tax)
print('----------')
print('total: $' ,total)
print('***************************************')
