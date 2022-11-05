#each player's input is hidden
from getpass import getpass as input
print("Rock Paper Scissor Battle")
print("Select your move (R, P or S)")
p1 = input("Player 1 > ").lower()
p2 = input("Player 2 > ").lower()

if p1 == p2:
  print("Tie, please try again")
elif p1 == "r":
  if p2 == "p":
    print("Player 2 winner")
  elif p2 == "s":
    print("Player 1 winner")
  else:
    print("Try again")
elif p1 == "p":
  if p2 == "s":
    print("Player 2 winner")
  elif p2 == "r":
    print("Player 1 winner")
  else:
    print("Try again")
elif p1 == "s":
  if p2 == "r":
    print("Player 2 winner")
  elif p2 == "p":
    print("Player 1 winner")
  else:
    print("Try again")
else:
  print("Try again")