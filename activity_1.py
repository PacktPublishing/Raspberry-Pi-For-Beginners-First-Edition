def concatenate_uppercase_string(str_a, str_b):
    return str_a.upper() + " " + str_b.upper()

print(concatenate_uppercase_string("Hello", concatenate_uppercase_string("Hello", "World")))