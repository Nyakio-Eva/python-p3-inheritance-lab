#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name,knowledge=None) -> None:
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge is not None else []
    
    def learn(self,new_knowledge):
        
        self.knowledge.append(new_knowledge)