emotions = {'happiness': 3, 'fear': 2, 'anger': 3}
class Person: 

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions
       
    def __str__(self):
        return f'{self.name} is in the state of {self.emotions}.'

    def feeling(self, scale):
        if scale == 1:
            return f"{self.name} is feeling a low amount of {self.emotions}."
        elif scale == 2:
            return f"{self.name} is feeling a medium amount of {self.emotions}."
        elif scale == 3:
            return f"{self.name} is feeling a high amount of {self.emotions}."
    
    
        
john = Person('John', 'happiness')
mike = Person('Mike', 'anger')
romeo = Person('Romeo', 'fear')
print(john.feeling(3))
print(mike.feeling(2))
print(romeo.feeling(1))
print(john)
