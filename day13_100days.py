print("Grade Generator")
exam = input("What was your test?: ")
max_score = int(input("Max score possible?: "))
score = float(input("How much you scored: "))
perc = round(score * 100 / max_score, 2)

if perc >= 90:
  print(f"You got {perc}% which is an A+")
elif perc >= 80 and perc <= 89:
  print(f"You got {perc}% which is an A-.")
elif perc >= 70 and perc <= 79:
  print(f"You got {perc}% which is a B.")
elif perc >= 60 and perc <= 69:
  print(f"You got {perc}% which is a C.")
elif perc >= 50 and perc <= 59:
  print(f"You got {perc}% which is a D.")
elif perc <= 49:
  print(f"You got {perc}% which is a F.")
else: 
  print("Try again!")