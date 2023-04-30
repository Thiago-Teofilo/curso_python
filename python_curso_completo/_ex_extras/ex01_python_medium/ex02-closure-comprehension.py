def elevatedTo(y):
    def intern(x):
        return x ** y
    return intern

elevatedToThree = elevatedTo(3)

a = [2,3,4,5,6]
b = [elevatedToThree(num) for num in a if elevatedToThree(num) % 8 == 0]

print(b)