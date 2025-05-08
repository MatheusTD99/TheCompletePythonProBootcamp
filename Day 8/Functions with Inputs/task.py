#def life_in_weeks(input):
   #     print(f"Greater than Zero {input}")
  #      print(f"Less than Zero {input}")
 #       print(f"Zero {input}")
#
#greet(input())

def life_in_weeks(age):    
    weeks_in_year = 52
    max_age = 90
    weeks_left = (max_age - age) * weeks_in_year
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(56)