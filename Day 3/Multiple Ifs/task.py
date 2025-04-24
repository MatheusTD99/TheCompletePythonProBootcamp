print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is ur age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Teen tickets are $7")
    elif age > 70:
        bill = 99
        print("Old tickets are $99")
    else:
        bill = 12
        print("Adult tickets are $12")

    want_photo = input("Do u want to have a photo of the ride? Type y for Yes and n for No")
    if want_photo == "y":
        bill += 3    # same as: bill = bill + 3
        print(f"Ur final bill is:{bill}")
    else:
            print(f"Ur final bill is:${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")