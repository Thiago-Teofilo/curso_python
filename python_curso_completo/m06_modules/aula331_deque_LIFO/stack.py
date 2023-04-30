from collections import deque
import json

def get_stack() -> deque:
    file_stack: deque[str] = deque()
    try:
        with open('stack.json', 'r') as file:
            file_dict = json.load(file)
            for item in file_dict.values():
                file_stack.append(item)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        True

    return file_stack

def save_stack(stack) -> None:
    with open('stack.json', 'w') as file:
        file_dict: dict = dict()
        for i, item in enumerate(stack):
            file_dict.update({**file_dict, i: item})
        
        json.dump(file_dict, file)
            

if __name__ == '__main__':
    stack: deque[str] = get_stack()

    action: str = input('(a - add, c - call, s - show): ')

    if action == 'a':
        new_item: str = input('Name: ')
        stack.append(new_item)
    
    if action == 'c':
        stack.pop()

    if action == 's':
        [print(f'{i}) - {item}') for i, item in enumerate(stack)]

    save_stack(stack)
