import os
cwd = os.getcwd()

class MyOpen:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print("Exception")
            print(exc_type)
            print(exc_value)
            print(traceback)


with MyOpen(cwd + '/text.txt', 'w') as file:
    file.write('\nLinha1')
    file.write('\nLinha2', 3)
    file.write('\nLinha3')
