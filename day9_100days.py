print("Generation Identifier")
print("---------------------")
name = input("Please state your name:\n")
print(f"Welcome to Generation Identifier {name}")
year = int(input(f"What year were you born in {name}?: "))
if year >= 1925 and year <= 1946:
  print(f"You are from a Traditionlists generation {name}!")
elif year >= 1947 and year <= 1964:
  print(f"You are from a Baby Boomers generation {name}!")
elif year >= 1965 and year <= 1981:
  print(f"You are from a Generation X {name}!")
elif year >= 1982 and year <= 1995:
  print(f"You are one of the Millenials {name}!")
elif year >= 1996 and year <= 2015:
  print(f"You are a Generation Z child {name}!")
else:
  print("You are a nobody!")


# print("Int exercise\n")
# myScore = int(input("Your score: "))
# if myScore > 100000:
#   print("Winner!")
# else:
#   print("Try again 😭\n")

# print("Float exercise\n")
# myPi = float(input("What is Pi to 3dp? \n"))
# if myPi == 3.142 :
#   print("Exactly!")
# else:
#   print("Try again 😭\n")

# print("Fix his code\n")
# score = int(input("What was your score on the test? \n"))
# if score >= 80:
#   print("Not too shabby")
# elif score > 70:
#   print("Acceptable.")
# else:
#   print("Dude, you need to study more!")