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
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap(1999))