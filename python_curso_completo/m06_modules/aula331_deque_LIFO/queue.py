from collections import deque
import json

def get_queue() -> deque:
    file_queue: deque[str] = deque()
    try:
        with open('queue.json', 'r') as file:
            file_dict = json.load(file)
            for item in file_dict.values():
                file_queue.append(item)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        True

    return file_queue

def save_queue(queue) -> None:
    with open('queue.json', 'w') as file:
        file_dict: dict = dict()
        for i, item in enumerate(queue):
            file_dict.update({**file_dict, i: item})
        
        json.dump(file_dict, file)
            

if __name__ == '__main__':
    queue: deque[str] = get_queue()

    action: str = input('(a - add, c - call, s - show): ')

    if action == 'a':
        new_item: str = input('Name: ')
        queue.appendleft(new_item)
    
    if action == 'c':
        queue.pop()

    if action == 's':
        [print(f'{i}) - {item}') for i, item in enumerate(queue)]

    save_queue(queue)
