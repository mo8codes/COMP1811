from datetime import datetime

class Person:
    def __init__(self, uid, name, is_male, is_alive, date_of_birth, date_of_death, mother, father, spouse, previous_spouses):
        self.uid = uid # Integer
        self.name = name # String
        self.is_male = is_male # Boolean
        self.is_alive = is_alive # Boolean
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y") # ? String ?
        self.date_of_death = datetime.strptime(date_of_death, "%d-%m-%Y") if date_of_death else None # ? String ?
        self.mother = mother # UID, or if Root object it should be None
        self.father = father # UID, or if Root object it should be None
        self.spouse = spouse if spouse else None # UID or None
        self.previous_spouses = previous_spouses if previous_spouses else None # UID or None

    def get_spouse(self, people): #Mo
        print(people[self.spouse].name)
        return self.spouse #the uid

    def get_extended_family(self):  # Mo
        # (Feature 1bii)
        pass

    def get_parents(self, people): #Mo
        # (Feature 1ai) - prints the name and returns the UIDs, Polymorphism for the Root class returns none and does nothing
            print("Mother: " + people[self.mother].name) # get the object using the mother's uid as the key in the people dictionary
            print("Father: " + people[self.father].name) # get the object using the father's uid as the key in the people dictionary
            return self.mother,self.father

    def get_siblings(self, people):
        # (Feature 2ai)
        # Note from Mo, please include code to print the name of each sibling.
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
    def __init__(self, uid, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, mother, father, children, grandchildren):
        super().__init__(uid, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, mother, father)
        self.children = children #tuple of UIDs?
        self.grandchildren = grandchildren if grandchildren else None #tuple of UIDs?

    def get_grandchildren(self): #Mo
        # (Feature 1aii)
        """
            Returns the UID's for the grandchildren of the object.
        """
        if self.grandchildren:
            i = 1
            print("Grandchildren:")
            for grandchild in self.grandchildren:
                print(str(i)+".", grandchild.name)
                i += 1
            return self.grandchildren

    def get_immediate_family(self, people):  # Mo
        # (Feature 1bi) - Polymorphism used as Leaf, Parent and, Root should have different (but nearly identical) implementations of this method.
        self.get_parents(people)
        self.get_siblings(people)
        self.get_spouse(people)


    def get_num_of_children(self): # Together
        # (Feature 3bi)
        pass


class Leaf(Person):
    def __init__(self, uid, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, mother, father):
        super().__init__(uid, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, mother, father)
        self.children = None
        self.grandchildren = None


# Person that is not a Leaf but is at the top of the family tree meaning their parents aren't included in the family tree when it is printed.
class Root(Person):
    def __init__(self, uid, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, mother, father, children, grandchildren):
        super().__init__(uid, name, is_male, is_alive, date_of_birth, date_of_death, spouse, previous_spouses, mother, father)
        self.mother = None
        self.father = None
        self.children = children if children else None
        self.grandchildren = grandchildren if grandchildren else None

    def get_parents(self, **kwargs):
        print("This person is a root node, their parents are not included")

class FamilyTree:
    def display_family_tree(self):  # Together
        # (Feature 3ai)
        pass

    def average_age_of_death(self):  # Together
        # (Feature 3aiii)
        pass

    def average_num_of_children(self):  # Together
        # (Feature 3bii)
        pass


