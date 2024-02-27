print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
coffees = int(input())
print('Number of muffins bought?')
muffins = int(input())
coffee_price = 5
muffin_price = 4 
subtotal = (coffees * coffee_price) + (muffins * muffin_price)
coffee_subtotal = (coffees * coffee_price)
fcoffee_subtotal = f'{coffee_subtotal: .2f}'
muffin_subtotal = (muffins * muffin_price)
fmuffin_subtotal = f'{muffin_subtotal: .2f}'
tax_rate = .06
tax = subtotal * tax_rate
total = subtotal + tax
print('My Coffee and Muffin Shop Receipt') 
print(coffees, 'Coffee at $' ,coffee_price, 'each: $' ,fcoffee_subtotal)
print(muffins, 'Muffins at $' ,muffin_price, 'each: $' ,fmuffin_subtotal)
print('6% tax: $' ,tax)
print('-------------------------')
print('total: $' ,total)
