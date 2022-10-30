print("Welcome to custom affirmations generator!")
print("-----------------------------------------")
name = input("What is your name? \n")
if name == "Mark" or name == "mark":
  print("Welcome Mark! \nPlease answer the following questions")
  day = input("What's the current day of week?\n")
  if day == "Monday" or day == "monday":
    print("Amazing you are here on first day of the week")
    food = input("What's your favourite thing to eat? \n")
    if food == "Chocolate" or food == "chocolate":
      print("Amazing\nYou are the most chocliest person I have met", name, "\nI hope you have the chocoful day")
    else:
      print(f"Sorry we don't like your taste in {food}")
  else:
    print("Well come back on Monday")
else:
  print(f"I just don't like you {name}, Goodbye!")
print()
next = input("For day9-day14, please tell which day's command you wish to run:")
if next == "day9":
  import day9_100days
else:
  print("Invalid choice")