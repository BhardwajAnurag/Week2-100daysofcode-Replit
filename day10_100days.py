myBill = float(input("What was the bill?: \n").replace("$",""))
tip = int(input("How much tip you wish to give? 10% 12% 15%\n").replace("%",""))
numberOfPeople = int(input("How many people?: \n"))
myBill = (tip*0.01 + 1) * myBill
answer = round(myBill / numberOfPeople, 2)
print("You all owe", answer, "including tip")

# Solve the following problems with my code
# # Your goal is to print the solution of all 3 calculations to the screen.

# # multiplication
# mul = 3.4 * 6.8
# print(mul)
# # division
# div = 2467 / 4673
# print(div)
# #raise 10 to the power of 2
# raising = 10 ** 2
# print(raising)
# # print the remainder when 343 is divided by 4
# remain = 343 % 100
# print(remain)

# adding = 4 + 3
# print(adding)

# subtraction = 8 - 9
# print(subtraction)

# multiplication = 4 * 32
# print(multiplication)

# division = 50 / 5
# print(division)

# # a number raised to the power of some number
# # in this example we raise 5 to the power of 2
# squared = 5**2
# print(squared)

# # remainder of a division
# modulo = 15 % 4
# print(modulo)

# # whole number division
# divisor = 15 // 2
# print(divisor)