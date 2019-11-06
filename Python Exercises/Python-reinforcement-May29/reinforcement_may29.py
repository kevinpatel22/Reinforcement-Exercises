seats = [
  [None, "Pmpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]


def classroom(spot=1):
  for rindx, row in enumerate(seats, spot): 
    for sindx, seat in enumerate(row, spot):
      if seat == None:
        claimspot = input(f"Row {rindx} Seat {sindx} is free. Do you want to sit there? (y/n)\n")
        if claimspot == 'y' or claimspot == 'yes':
          name = input('Enter your name to reserve the spot:')
          del seats[rindx-spot][sindx-spot]
          seats[rindx-spot].insert(sindx-spot, name)
          return
        elif claimspot == 'n' or claimspot == 'no': 
          continue
        else: 
          print("Enter a valid answer!")
 
classroom()
print(seats)