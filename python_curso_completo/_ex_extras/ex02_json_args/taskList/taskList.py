import json

class TaskList:
    def __init__(self, local_json:str) -> None:
        try:
            with open(local_json, 'r') as file:
                json_tasks = json.load(file)
                self.task_list = json_tasks.values()
        except FileNotFoundError:
            self.task_list = []
        
    def __repr__(self) -> str:
        class_name =  type(self)
        repr_str = f'{class_name}()'
        return repr_str
    
    def add(self, tasks:list) -> None:
        self.task_list = [*self.task_list, *tasks]

    def show(self) -> None:
        for i, task in enumerate(self.task_list):
            print(f'{i}) - {task}')

    def remove(self, rm_task: list) -> None:
        new_task_list = self.task_list
        self.task_list = [task for task in new_task_list
                         if task != rm_task]
        

    def save(self, local_json):
        json_tasks = {i:task for i, task in enumerate(self.task_list)}
        with open(local_json, 'w+') as file:
            json.dump(json_tasks, file, ensure_ascii=False, indent=2)
