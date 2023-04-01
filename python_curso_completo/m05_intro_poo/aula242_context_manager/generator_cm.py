from contextlib import contextmanager
import os

cwd = os.getcwd()

@contextmanager
def my_open(path, mode):
    try:
        file = open(path, mode)
        yield file
    except Exception as err:
        print(err)
    finally:
        file.close()

file_path = cwd + '/text.txt'
with my_open(file_path, 'w') as file:
    file.write('\nLinha1')
    file.write('\nLinha2')
    file.write('\nLinha3')
