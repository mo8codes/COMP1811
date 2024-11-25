from datetime import datetime

class Person:
    def __init__(self, uid, name, is_male, is_alive, date_of_birth, date_of_death, mother, father, spouse, previous_spouses):
        self.uid = uid # Integer
        self.name = name # String
        self.is_male = is_male # Boolean
        self.is_alive = is_alive # Boolean
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y")
        self.date_of_death = datetime.strptime(date_of_death, "%d-%m-%Y") if date_of_death else None
        self.mother = mother # UID, or if Root object it should be None
        self.father = father # UID, or if Root object it should be None
        self.spouse = spouse if spouse else None # UID or None
        self.previous_spouses = previous_spouses if previous_spouses else None # UID or None
        self.children = None
        self.grandchildren = None

    def get_spouse(self, people): #Mo
        if self.spouse:
            print("Spouse:",people[self.spouse].name)
            return self.spouse #the uid
        else:
            print("No spouse found")

    def get_children(self, people):
        counter = 0
        if self.children:
            for child in self.children:
                counter += 1
                print(str(counter) + ".", people[child].name)
            return counter
        else:
            print("No children found")

    def get_immediate_family(self, people):  # Mo
        # (Feature 1bi)
        self.get_parents(people)
        #self.get_siblings(people) #TODO uncomment after Ashanti's code is merged
        self.get_spouse(people)
        if isinstance(self, (Parent, Root)):
            self.add_descendants(people)
            print("Children:")
            self.get_children(people)
        else:
            print("No children found.")


    def get_parents(self, people):  # Mo
        # (Feature 1ai) - prints the name and returns the UIDs, Polymorphism for the Root class returns none and does nothing
        if self.mother is None or self.father is None:
            return "Parents are not in the family tree."

        # If both mother and father are not None, print their names and return their UIDs
        print("Mother: " + people[int(self.mother)].name)  # get the object using the mother's uid as the key in the people dictionary
        print("Father: " + people[int(self.father)].name)  # get the object using the father's uid as the key in the people dictionary
        return f"Mother UID: {self.mother} \nFather UID: {self.father}"

    def get_siblings(self, people):
        # (Feature 2ai)
        # Note from Mo, please include code to print the name of each sibling like how I have done get parents and get spouse
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
    def __init__(self, uid, name, is_male, is_alive, date_of_birth, date_of_death, mother, father, spouse, previous_spouses, children, grandchildren):
        super().__init__(uid, name, is_male, is_alive, date_of_birth, date_of_death, mother, father, spouse, previous_spouses)
        self.children = children # A tuple of children UIDs
        self.grandchildren = grandchildren # A tuple of grandchildren UIDs

    def get_grandchildren(self, people):  # Mo
        # (Feature 1aii)
        if self.grandchildren:
            i = 1
            print("Grandchildren:")
            for grandchild in self.grandchildren:
                print(str(i) + ".", people[grandchild].name)
                i += 1
            return self.grandchildren

        else:
            return "None found"

    def add_descendants(self, people):  # Add children and grandchildren to objects
        self.children = []
        self.grandchildren = []
        if isinstance(self, (Root, Parent)):
            for person in people:
                if self.is_male:
                    if people[person].father == self.uid:
                        self.children.append(people[person].uid)  # self.children = [uid_of_child, 2 ,3 etc...]
                elif not self.is_male:
                    if people[person].mother == self.uid:
                        self.children.append(people[person].uid)

            for child in self.children:
                # child is the uid ex: 2 or 3
                for person in people:
                    # person is the uid for each person in the dictionary
                    if people[child].is_male:
                        if people[person].father == child:
                            # add uid of person to grandchildren
                            self.grandchildren.append(person)

        else:
            print("No children found.")


class Leaf(Person):
    def add_descendants(self, _people): # Polymorphism, parent class has a different method of the same name.
        # People is passed but never used as this function is filler so that is why there is an underline
        self.children = None  # No children for a Leaf
        self.grandchildren = None  # No grandchildren for a Leaf
        return None # Leaves have no descendants


# Person that could be a Leaf or a Parent but is at the top of the family tree meaning their parents aren't included
# in the family tree when it is printed.  Inherits from parent due to inheritance of some of parent's functions
class Root(Parent):
    def __init__(self, uid, name, is_male, is_alive, date_of_birth, date_of_death, mother, father, spouse, previous_spouses, children, grandchildren):
        super().__init__(uid, name, is_male, is_alive, date_of_birth, date_of_death, mother, father, spouse, previous_spouses, children, grandchildren)
        self.mother = None  # Root has no mother
        self.father = None  # Root has no father
        self.children = children if children else None  # A list of children for the Root
        self.grandchildren = grandchildren if grandchildren else None  # A list of grandchildren for the Root

class FamilyTree:
    def display_family_tree(self):
        # (Feature 3ai)
        pass




