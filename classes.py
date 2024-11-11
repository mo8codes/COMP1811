from datetime import datetime


class Person:
    def __init__(self, uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents):
        self.uid = uid # Integer
        self.type_of = type_of # String parent or Leaf
        self.name = name # String
        self.is_male = is_male # Boolean
        self.is_alive = is_alive # Boolean
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y") # ? String ?
        self.date_of_death = datetime.strptime(date_of_death, "%d-%m-%Y") # ? String ?
        self.spouse = spouse # Object or None (Leaves and Parents can have a spouse)
        self.parents = parents # Dictionary of their UID?


class Parent(Person):
    def __init__(self, uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents, children,
                 grandchildren):
        super().__init__(uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents)
        self.children = children #tuple of UIDs?
        self.grandchildren = grandchildren #tuple of UIDs?


class Leaf(Person):
    def __init__(self, uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents):
        super().__init__(uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents)
        self.children = None
        self.grandchildren = None

