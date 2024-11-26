from datetime import datetime


class Person:
    def __init__(self, uid, level, name, is_male, date_of_birth, date_of_death, mother, father, partner):
        self.uid = uid # Integer
        self.level = level # Integer
        self.name = name # String
        self.is_male = is_male # Boolean
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y") if isinstance(date_of_birth, str) else date_of_birth # Datetime (String)
        self.date_of_death = datetime.strptime(date_of_death, "%d-%m-%Y") if isinstance(date_of_death, str) else date_of_death # Datetime (String)
        self.mother = mother # String
        self.father = father # String
        self.partner = partner # Object or None

    def get_partner(self): #Mo
        return self.partner

    def get_parents(self): #Mo
        # (Feature 1ai)
        return self.mother,self.father

    def person_search(search_uid):
        results = []
        for uid, person in sorted(people.items()):
            if person.uid == search_uid:
                results.append(person.name)
                return (results)

    def child1_search(search_uid):
        results = []
        for uid, person in sorted(parents.items()):
            if person.child1 == search_uid:
                results.append(person.name)
                return (results)


class FamilyTree(Person):
    def __init__(self, people, parents, grandparents, uid, level, name, is_male, date_of_birth, date_of_death, mother,
                 father, partner):
        super().__init__(uid, level, name, is_male, date_of_birth, date_of_death, mother, father, partner)
        self.mother = None
        self.father = None
        self.uid = uid
        self.people = people
        self.parents = parents
        self.grandparents = grandparents

    def get_siblings(self, people):
        siblings = []

        #Loop through all people
        for uid, person in people.items():
            if person.uid ==self.uid:
                continue

        if((self.mother and person.mother and self.mother == person.mother) or
                (self.father and person.father and self.father == person.father)):
            siblings.append(person)
        return siblings

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
    def __init__(self, uid, level, name, is_male, date_of_birth, date_of_death, partner, mother, father, child1=None, child2=None):
        super().__init__(uid, level, name, is_male, date_of_birth, date_of_death, partner, mother, father)
        self.child1 = child1
        self.child2 = child2

    def populate_children(self, people, parents):
        # Create a temporary dictionary to store children for each parent
        parent_children = {uid: [] for uid in parents.keys()}

        # Scan through all people to find their parents
        for person in people.values():
            # If mother is in parents dict, add this person as their child
            if person.mother in parent_children:
                parent_children[person.mother].append(person)

            # If father is in parents dict, add this person as their child
            if person.father in parent_children:
                parent_children[person.father].append(person)

        # Now assign children to the parent objects
        for parent_uid, children in parent_children.items():
            # Sorting children by date of birth to ensure consistent assignment
            children.sort(key=lambda x: x.date_of_birth)

            # Assign up to two children to the parent
            if len(children) >= 1:
                parents[parent_uid].child1 = children[0].uid
            if len(children) >= 2:
                parents[parent_uid].child2 = children[1].uid

    def get_grandchildren(self): #Mo
        # (Feature 1aii)
        pass

    def get_num_of_children(self): # Together
        # (Feature 3bi)
        pass


class Grandparent(Person):
    def __init__(self, uid, level, name, is_male, date_of_birth, date_of_death, partner, mother, father, grandchild1=None, grandchild2=None, grandchild3=None, grandchild4=None):
        super().__init__(uid, level, name, is_male, date_of_birth, date_of_death, partner, mother, father)
        self.grandchild1 = grandchild1
        self.grandchild2 = grandchild2
        self.grandchild3 = grandchild3
        self.grandchild4 = grandchild4

    def populate_grandchildren(self, people, grandparents):
        grandchildren = []

        # Scan through all people to find all grandchildren
        for uid, person in sorted(people.items()):
            if person.level == 2:
                grandchildren.append(person)

        # Assigning grandchildren to their respective grandparents
        for uid, grandparent in sorted(grandparents.items()):
            # Assign up to four grandchildren to the grandparent
            if len(grandchildren) >= 1:
                grandparents[uid].grandchild1 = grandchildren[0].uid
            if len(grandchildren) >= 2:
                grandparents[uid].grandchild2 = grandchildren[1].uid
            if len(grandchildren) >= 3:
                grandparents[uid].grandchild3 = grandchildren[2].uid
            if len(grandchildren) >= 4:
                grandparents[uid].grandchild4 = grandchildren[3].uid


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



class FamilyCalculations :
    def __init__(self, people, parents, grandparents):
        self.people = people
        self.parents = parents
        self.grandparents = grandparents

    def average_age_of_death(self):  # Together
        # (Feature 3aiii)
        pass

    def average_num_of_children(self):  # Together
        # (Feature 3bii)
        pass
