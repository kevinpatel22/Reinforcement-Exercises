class Task: 

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
    
    def __str__(self):
        return f'Task: {self.description}\nDue Date: {self.due_date}'
    
    def __repr__(self):
        return f'Task: {self.description} ---- Due Date: {self.due_date}'
        
buy_groceries = Task('Buy Apple', '2019/11/02')
print(buy_groceries)

class TodoList:

    tasks = []

    def __init__(self, name):
        self.name = name
    
    def add_task(self):
        TodoList.tasks.append(self.name)
        


