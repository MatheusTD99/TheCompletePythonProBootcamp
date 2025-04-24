#bmi = 84 / 1.65 ** 2

height = 1.65
weight = 84

bmi = weight / (height * height)

print(round(bmi, 3))             #"round" to round up or down - u can "," number to show the num of decimals

score1 = 0

# User scores a point
score1 += 1
print(score1)

# f-strings
print("ur score is: " + str(score1))

print(f"ur score is = {score1}, ur height is {height}. ur weight is {weight}")

print(6 + 4 / 2 - (1 * 2))

a = int("5") / int(2.7)
print(a)