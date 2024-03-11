#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


class Teacher(User):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        random_index = random.randint(0, len(knowledge) -1)

        #return element at random index
        return knowledge[random_index]

my_teacher = Teacher("Yuesuf", "Mweru") 
print(my_teacher.teach() )  