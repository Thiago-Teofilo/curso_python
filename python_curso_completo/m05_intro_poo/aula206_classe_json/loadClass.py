import json
import os
from createClass import People, DIR_FILE, make_dump

make_dump()

with open(DIR_FILE, 'r', encoding='utf-8') as file:
    dict_el = json.load(file)

    p1 = People(**dict_el)

print("Nome:",p1.name)
print("Ano de nascimento:",p1.age)
print("Email:",p1.email)
