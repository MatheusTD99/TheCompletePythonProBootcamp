def my_function():
    return 3 * 2
print(my_function())

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "u did not provide valid name"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"  # "return" is the end of the def. even when has more code after.

input(format_name(input("What is ur first name?"), input("What is ur last name?")))

def func_1(text):
    return text + text

def func_2(text):
    return text.title()

output = func_2(func_1("cccc"))
print(output)

