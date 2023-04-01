import json
import os

class People:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

p1 = People(
    name="John", 
    age=2007, 
    email="John@example.com"
    )

DIR_FILE = os.getcwd() + '\\m05_intro_poo\\aula206_classe_json\\classes.json'

def make_dump():
    with open(DIR_FILE, 'w',  encoding='utf8') as file:
        json.dump(p1.__dict__,file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print("Gerando JSON")
    make_dump()