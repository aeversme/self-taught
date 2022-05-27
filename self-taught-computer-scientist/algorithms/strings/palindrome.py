def is_palindrome(string):
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False


print(is_palindrome("racecar"))
print(is_palindrome("Madagascar"))
