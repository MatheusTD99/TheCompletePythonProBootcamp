import random
import My_Module

#random_integer = random.randint(1, 10)
#print(random_integer)

#print(My_Module.my_fav_number)

#random_numb_0_to_1 = random.random() * 10
#print(random_numb_0_to_1)

#random_float = random.uniform(1, 10)
#print(random_float)

random_numb_0_to_1 = random.randint(0, 1)
if random_numb_0_to_1 == 0:
    print("head")
else:
    print("tail")