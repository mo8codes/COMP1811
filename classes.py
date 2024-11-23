from datetime import datetime


class Person:
    def __init__(self, uid, name, is_male, is_alive, date_of_birth, date_of_death, mother, father, spouse, previous_spouses):
        self.uid = uid # Integer
        self.name = name # String
        self.is_male = is_male # Boolean
        self.is_alive = is_alive # Boolean
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y") # ? String ?
        self.date_of_death = datetime.strptime(date_of_death, "%d-%m-%Y") # ? String ?
        self.mother = mother
        self.father = father
        self.spouse = spouse # Object or None (Leaves and Parents can have a spouse)
        self.previous_spouses = previous_spouses

    def get_spouse(self): #Mo
        return self.spouse

    def get_parents(self): #Mo
        # (Feature 1ai)
        return self.mother,self.father

    def get_siblings(self, uid):
        # (Feature 2ai)
        pass

    def get_cousins(self):
        # (Feature 2aii)
        pass

    def get_all_birthdays(self):
        # (Feature 2bi)
        pass

    def print_birthday_calendar(self):
        # (Feature 2bii)
        pass


class Parent(Person):
    def __init__(self, uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, parents, children,
                 grandchildren):
        super().__init__(uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, parents)
        self.children = children #tuple of UIDs?
        self.grandchildren = grandchildren #tuple of UIDs?

    def get_grandchildren(self): #Mo
        # (Feature 1aii)
        pass

    def get_num_of_children(self): # Together
        # (Feature 3bi)
        pass


class Leaf(Person):
    def __init__(self, uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, parents):
        super().__init__(uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, parents)
        self.children = None
        self.grandchildren = None


# Person that is not a Leaf but is at the top of the family tree meaning their parents aren't included in the family tree when it is printed.
class Root(Person):
    pass

class FamilyTree:
    def get_immediate_family(self):  # Mo
        # (Feature 1bi)
        pass

    def get_extended_family(self):  # Mo
        # (Feature 1bii)
        pass

    def display_family_tree(self):  # Together
        # (Feature 3ai)
        pass

    def average_age_of_death(self):  # Together
        # (Feature 3aiii)
        pass

    def average_num_of_children(self):  # Together
        # (Feature 3bii)
        pass


