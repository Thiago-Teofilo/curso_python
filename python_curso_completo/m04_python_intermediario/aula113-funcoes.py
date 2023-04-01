def mult(*args):
    result = 1
    for val in args:
        result *= val
    return result

def itsPair(number):
    return number % 2 == 0

numbers = 1,2,3,4,5
result_mult = mult(*numbers)

print(result_mult)
print(itsPair(result_mult))