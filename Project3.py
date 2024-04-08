def check_equality(param1, param2, param3):
    if param1 == param2 or param1 == param3 or param2 == param3:
        return True
    else:
        return False
# Example usage:
print(check_equality("apple", "banana", "apple"))  # Output: True