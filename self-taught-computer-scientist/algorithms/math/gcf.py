# greatest common factor
def greatest_common_factor(num1, num2):
    gcf = None
    if num1 < 0 or num2 < 0:
        raise ValueError("Numbers must be positive")

    if num1 == 0:
        gcf = num2
    if num2 == 0:
        gcf = num1

    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf


print(greatest_common_factor(644, 5612))


# greatest common factor using euclid's algorithm
def euclid_gcf(x, y):
    if y == 0:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x


print(euclid_gcf(644, -5612))
