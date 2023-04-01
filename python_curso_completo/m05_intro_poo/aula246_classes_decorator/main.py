class Multiplicar:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interna

@Multiplicar(2)
def soma(x, y):
    return x + y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)