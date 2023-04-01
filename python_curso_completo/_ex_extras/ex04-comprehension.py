from functools import partial

def itsDivisible(value, divisor):
    if value % divisor == 0:
        return True
    return False

def elevatedTo(value, elevation):
    return value ** elevation

itsPair = partial(itsDivisible, divisor=2)

list_a = [2,3,4,5,6]

list_b = [
    elevatedTo(el,2) 
    if itsPair(el) else elevatedTo(el,3) 
    for el in list_a 
    ]

print(list_b)