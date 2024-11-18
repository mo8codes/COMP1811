from datetime import datetime


class Person:
    def __init__(self, uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents):
        self.uid = uid # Integer
        self.type_of = type_of # String parent or Leaf
        self.name = name # String
        self.previous_spouses = previous_spouses
        self.is_male = is_male # Boolean
        self.is_alive = is_alive # Boolean
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y") # ? String ?
        self.date_of_death = datetime.strptime(date_of_death, "%d-%m-%Y") # ? String ?
        self.spouse = spouse # Object or None (Leaves and Parents can have a spouse)
        self.parents = parents # Dictionary of their UID?

    def get_siblings
    def get_cousins(self):
    def get_birthday(self):


class Parent(Person):
    def __init__(self, uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents, children,
                 grandchildren, previous_spouses):
        super().__init__(uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents)
        self.previous_spouses = previous_spouses
        self.children = children #tuple of UIDs?
        self.grandchildren = grandchildren #tuple of UIDs?


class Leaf(Person):
    def __init__(self, uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents):
        super().__init__(uid, type_of, name, is_male, is_alive, date_of_birth, date_of_death, spouse, parents)
        self.children = None
        self.grandchildren = None



    class Family(Person):
        def __init__(self):
            self.members = {}  # Dictionary to store members by their UID

        def add_member(self, person):
            #Add a new member to the family.
            if person.uid in self.members:
                raise ValueError(f"Member with UID {person.uid} already exists.")
            self.members[person.uid] = person

        def get_member(self, uid):
            #Retrieve a family member by UID.
            return self.members.get(uid, None)

        def set_spouse(self, uid1, uid2):
            #Set two members as each other's spouse.
            person1 = self.get_member(uid1)
            person2 = self.get_member(uid2)

            if not person1 or not person2:
                raise ValueError("Error! One or two of the IUDs entered does not exist!")

            person1.spouse = person2
            person2.spouse = person1

        def add_parents(self, child_uid, parent_uids):
            #Set parents for a child and add the child to each parent's children list.
            child = self.get_member(child_uid)
            if not child:
                raise ValueError(f"No child with UID {child_uid}.")

            parents = [self.get_member(uid) for uid in parent_uids]
            if any(parent is None for parent in parents):
                raise ValueError("One or more parent UIDs do not exist.")

            child.parents = {parent.uid: parent for parent in parents}

            for parent in parents:
                if isinstance(parent, Parent):
                    if parent.children is None:
                        parent.children = []
                    parent.children.append(child.uid)

        def add_grandchild(self, grandparent_uid, grandchild_uid):
            #A grandparent is added to a grandparent grandchild list
            grandparent = self.get_member(grandparent_uid)
            grandchild = self.get_member(grandchild_uid)

            if not grandparent or not grandchild:
                raise ValueError("The Grandparent or grandchild UID entered does not exist! Please try again.")

            if isinstance(grandparent, Parent):
                if grandparent.grandchildren is None:
                    grandparent.grandchildren = []
                grandparent.grandchildren.append(grandchild.uid)

        def display_family_tree(self):
            #Displays the family tree with relationships.
            for member in self.members.values():
                print(f"Name: {member.name}, UID: {member.uid}")
                if member.spouse:
                    print(f"  Spouse: {member.spouse.name}")
                if member.parents:
                    parent_names = ", ".join(parent.name for parent in member.parents.values())
                    print(f"  Parents: {parent_names}")
                if isinstance(member, Parent):
                    if member.children:
                        children_names = ", ".join(self.get_member(child_uid).name for child_uid in member.children)
                        print(f"  Children: {children_names}")
                    if member.grandchildren:
                        grandchildren_names = ", ".join(self.get_member(gc_uid).name for gc_uid in member.grandchildren)
                        print(f"  Grandchildren: {grandchildren_names}")
                print()


