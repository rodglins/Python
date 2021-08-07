def switcher(number):

  # dictionary (from Module 3) to store switch cases
  # If not found, then get() the default value
  return {
    '0':"Entered 0",
    '1':"Entered 1",
    '2':"Entered 2",
    '3':"Entered 3",
    '4':"Entered 4",
    '5':"Entered 5",
    '6':"Entered 6",
    '7':"Entered 7",
    '8':"Entered 8",
    '9':"Entered 9",
  }.get(number,"Invalid number!")


# input() reads in an user input from stdin
number = input("Dial a number")
switcher(number)

if (number == "0"):
  print(number)
elif (number == "1") :
  print(number)
elif (number == "2") :
  print(number)
elif (number == "3") :
  print(number)
elif (number == "4") :
  print(number)
elif (number == "5") :
  print(number)
elif (number == "6") :
  print(number)
elif (number == "7") :
  print(number)
elif (number == "8") :
  print(number)
elif (number == "9") :
  print(number)

else :
  print("invalid inputs")