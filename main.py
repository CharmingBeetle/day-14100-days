from getpass import getpass as input
print("***THE MOST EPIC \U0001F5FB vs \U0001F4C4 vs \U00002702 BATTLE OF ALL TIME!***")
print("Type R, P or S to make your move!")
print()
# Player 1
p1 = input("Player 1: ")

# Player 2 
p2 = input("Player 2: ")
if p1 == p2:
  print("You both tied!")
elif p1 == "R" or p1 == "r" and p2 == "P" or p2 == "p":
  print("AH! Congrats Player 2! Paper covers rock!")
elif p1 == "P" or p1 == "p" and p2 == "R" or p2 == "r":
  print("AH! Congrats Player 1! Paper covers rock! \U0001F389")
elif p1 == "S" or p1 == "s" and p2 == "R" or p2 == "r":
  print("Congrats Player 2! Rock breaks your scissors! \U0001F389")
elif p1 == "R" or p1 == "r" and p2 == "S" or p2 == "s":
  print("Congrats Player 1! Rock breaks your scissors! \U0001F389")
elif p1 == "P" or p1 == "p" and p2 == "S" or p2 == "s":
  print("Congrats Player 2! Scissors cuts paper! \U0001F389") 
elif p1 == "S" or p1 == "s" and p2 == "P" or p2 == "p":
  print("Congrats Player 1! Scissors cuts paper! \U0001F389") 
else:
  print('Invalid input. Try again!')
