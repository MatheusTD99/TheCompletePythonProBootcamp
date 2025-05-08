#programming_dictionary = {
#    "Bug": "An error in a program that prevents the program from running as expected.",
#    "Function": "A piece of code that you can easily call over and over again."
#}
#print(programming_dictionary["Bug"])
#programming_dictionary["Loop"] = "doing something over and over again"
#print(programming_dictionary["Loop"])

# Wipe an existing dictionary

#programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in a dictionary
#programming_dictionary["Bug"] = "Moth"
#print(programming_dictionary)

# Loop through a dictionary
#for key in programming_dictionary:
#    print(key)
#    print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)