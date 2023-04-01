def decorator(a=None, b=None, c=None):
    def functionFeatures(func):
        print("Parametros do decorador:", a,b,c)
        def intern(*args, **kwargs):
            return func(*args, **kwargs)
        return intern
    return functionFeatures

@decorator(1,2,3)
def sum(a, b):
    return a + b

mult = decorator(a = 5)(lambda x, y: x * y)

print(mult(10,5))
print(sum(1,3))