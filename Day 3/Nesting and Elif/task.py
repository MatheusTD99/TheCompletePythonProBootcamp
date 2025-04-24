#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#
#if height >= 120:
#    print("You can ride the rollercoaster")
#    age = int(input("What is ur age? "))
#    if age <= 12:
#        print("Ur ticket is $5")
#    elif age <= 18:
#        print("Ur ticket is $7")
#    elif age > 70:
#        print("Ur ticket is $99")
#    else:
#        print("Ur ticket is $12")
#else:
#    print("Sorry you have to grow taller before you can ride.")


#weight = 85
#height = 1.85

#bmi = weight / (height ** 2)

weight = int(input("what is ur weight?"))
height = float(input("what is ur height"))

if weight / (height ** 2) <= 18.5:
    print("ur underweight")
elif weight / (height ** 2) >= 25:
    print("ur overweight")
else:
    print("ur in good form")
