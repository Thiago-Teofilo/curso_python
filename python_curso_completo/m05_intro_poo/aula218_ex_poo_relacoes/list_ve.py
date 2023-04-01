class Vehicle:
    def __init__(self, name):
        self.name = name
        self._manufacturer = None
        self._motor = None

    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, instance):
        self._manufacturer = instance

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, instance):
        self._motor = instance

class Motor:
    def __init__(self, name):
        self.name = name

class Manufacturer:
    def __init__(self, name):
        self.name = name

motor1 = Motor("V8")
motor2 = Motor("V6")
motor3 = Motor("V2")

mf1 = Manufacturer("Fiat")
mf2 = Manufacturer("Chevrolet")

car1 = Vehicle("Uno")
car2 = Vehicle("Cronos")
car3 = Vehicle("Mobi")
car4 = Vehicle("Camaro")

car1.motor = motor1
car2.motor = motor1
car3.motor = motor2
car4.motor = motor3

car1.manufacturer = mf1
car2.manufacturer = mf1
car3.manufacturer = mf1
car4.manufacturer = mf2

for car in [car1, car2, car3, car4]:
    print(f'Carro: {car.name}',
          f'Motor: {car.motor.name}',
          f'Fabricante: {car.manufacturer.name}', 
          sep='\n', end='\n\n')
    