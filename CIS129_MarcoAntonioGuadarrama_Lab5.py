keepGoing = 'y'

while keepGoing == 'y':

  totalBottles = 0
  counter = 1
  todayBottles = 0
  totalPayout = 0

  while counter <= 7:

    todayBottles = int(input(f'Enter number of bottles returned for day #{counter}: '))
    counter = counter + 1
    totalBottles = totalBottles + todayBottles
    totalPayout = totalBottles * .10

  print(f'\nThe total number of bottles collected is {totalBottles}')

  print(f'The total paid out is ${totalPayout:.2f}\n')

  keepGoing = input('Do you want to enter another week\'s worth of data?\n(Enter y or n): ')

  print()
