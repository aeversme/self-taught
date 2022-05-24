def last_digit(string):
    digit_list = [d for d in string if d.isdigit()]
    if digit_list:
        return digit_list[-1]
    else:
        return "No digits in this string."


bogo = "Buy 2, get 1 free!"
print(last_digit(bogo))
