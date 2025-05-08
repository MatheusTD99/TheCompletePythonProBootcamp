# Functions with input

#def greet_with_name(name):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")#


# greet_with_name("Jack Bauer")

#def greet_with(name, location):
#    print(f"Ur name is: {name}")
#    print(f"Ur location is: {location}")
#
#greet_with(location="Matheus", name="Brazil")


def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    score = int(f"{true_count}{love_count}")
    print(f"Love Score = {score}")


# Call your function with hard coded values
calculate_love_score("Matheus Tomasi Duarte", "Jordana Petterini Rocha")