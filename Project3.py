Create a function that accepts 3 parameters and checks for equality between any two of them.
Your function should return True if 2 or more of the parameters are equal,
and false is none of them are equal to any of the others.


def check_equality(param1, param2, param3):
    if param1 == param2 or param1 == param3 or param2 == param3:
        return True
    else:
        return False
# Example usage:
print(check_equality("apple", "banana", "apple"))  # Output: True
