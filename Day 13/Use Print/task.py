#pages = int(input("Number of pages: "))
#word_per_page = int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)
############
#def odd_or_even(number):
#    if number % 2 == 0:
#        return "This is an even number."
#    else:
#        return "This is an odd number."
#print(odd_or_even(10))
#############
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])

fizz_buzz(50)