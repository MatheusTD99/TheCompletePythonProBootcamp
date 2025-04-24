print("Welcome to Python Pizza Deliveries!")
bill = 0
S = 15
M = 20
L = 25
size = str(input("What size pizza do you want? S, M or L: "))
if size == "S":
    Small = bill + S
    bill = Small
    print("Small pizzas are $15")
elif size == "M":
    Medium = bill + M
    bill = Medium
    print("Medium pizzas are $20")
elif size == "L":
    Large = bill + L
    bill = Large
    print("Large pizzas are $25")
else:
    print("You have chosen an invalid size.")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
        print("Pepperoni for small pizzas cost plus $2")
    else:
        bill += 3
        print("Pepperoni for Medium and Large pizzas cost plus $3")

else:
    print("Of course")

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill += 3
    print("Extra cheese cost plus $3")
else:
    print("Okay")

print(f"Ur final bill is: {bill}")