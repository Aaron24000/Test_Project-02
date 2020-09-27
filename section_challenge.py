print("Please choose option from list below: ")
print("1.\tFirmino")
print("2.\tMane")
print("3.\tSalah")
print("4.\tOrigi")
print("0.\tAll them niggas trash")

while True:
    choice = input()

    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))