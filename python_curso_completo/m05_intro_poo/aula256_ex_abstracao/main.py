""" Sistema Bancário
Cada cliente tem uma conta bancária sendo ela corrente ou poupanca,
o cliente pode sacar/depositar nessa conta. Contas corrente tem um
limite extra. 

* O cliente herda de pessoa e agrega conta
* O banco terá um método de validação para ver se o cliente e a conta
  existe naquele banco
"""
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo=0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo
    
    @abstractmethod
    def depositar(self, qtd):...

    def sacar(self, qtd):
        try:
            self._saldo 
            if self._saldo < 0:
                raise Exception("Erro ao sacar")
        except Exception as err:
            print(err)
            self._saldo += qtd

    def __repr__(self):
        return f"{__class__.__name__}({self._agencia}, {self._numero}, {self._saldo})"

class ContaCorrente(Conta):
    def __init__(self, *args):
        self._limite = 5000.00
        super().__init__(*args)

    def depositar(self, qtd):
        if self._saldo + qtd < self._limite:
            self._saldo += qtd
        else:
            print("Erro limite maximo")

class ContaPoupanca(Conta):
    def __init__(self, *args):
        super().__init__(*args)

    def depositar(self, qtd):
        self._saldo += qtd

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self, outra_class):
        return f"{__class__.__name__}.{outra_class}({self._nome}, {self._idade}, {self._conta})"

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter
    def idade(self, idade):
        self._idade = idade
      
class Cliente(Pessoa):
    def __init__(self, *args):
        super().__init__(*args)
        self.conta = None

    @property
    def conta(self):
        return self._conta
    
    @conta.setter
    def conta(self, conta):
        self._conta = conta

    def __repr__(self):
        return super().__repr__(__class__.__name__)

conta1 = ContaCorrente(133, 18)
cliente1 = Cliente("Thiago", 20)
cliente1.conta = conta1

conta1.depositar(400)
print(cliente1)