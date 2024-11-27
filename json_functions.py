import json
from classes import Person, Parent, Grandparent

#JSON read file maternal.json

def read_json(jsonfile):
    with open(jsonfile, "r") as file:
        data = json.load(file)
        people = create_people(data)
        parents = create_parents(people)
        grandparents = create_grandparents(people)

        parent_instance = next(iter(parents.values()))
        parent_instance.populate_children(people, parents)

        grandparent_instance = next(iter(grandparents.values()))
        grandparent_instance.populate_grandchildren(people, grandparents)

    return people, parents, grandparents

def create_people(data):
    # Creates a dictionary to store all Person objects with their UIDs as keys
    people = {}

    for member in data["members"]:
        person = Person(
            uid=member["uid"],
            level=member["level"],
            name=member["name"],
            is_male=member["is_male"],
            date_of_birth=member["date_of_birth"],
            date_of_death=member["date_of_death"] if member["date_of_death"] else "01-01-2100",
            # Default future date for living people
            mother=member["mother"],
            father=member["father"],
            partner=member["partner"]
        )
        people[member["uid"]] = person

    return people

def create_parents(people):

    parents = {}

    for uid, person in sorted(people.items()):
        if person.level in [0, 1]:

            parent = Parent(
                uid=person.uid,  # Use dot notation here
                level=person.level,  # Use dot notation here
                name=person.name,  # Use dot notation here
                is_male=person.is_male,  # Use dot notation here
                date_of_birth=person.date_of_birth,  # Use dot notation here
                date_of_death=person.date_of_death,  # Use dot notation here
                mother=person.mother,
                father=person.father,
                partner=person.partner,  # Use dot notation here
                child1=None,
                child2=None
            )
            parents[person.uid] = parent

    return parents


def create_grandparents(people):

    grandparents = {}

    for uid, person in sorted(people.items()):
        if person.level in [0]:

            grandparent = Grandparent(
                uid=person.uid,  # Use dot notation here
                level=person.level,  # Use dot notation here
                name=person.name,  # Use dot notation here
                is_male=person.is_male,  # Use dot notation here
                date_of_birth=person.date_of_birth,  # Use dot notation here
                date_of_death=person.date_of_death,  # Use dot notation here
                mother=person.mother,
                father=person.father,
                partner=person.partner,  # Use dot notation here
                grandchild1=None,
                grandchild2=None
            )
            grandparents[person.uid] = grandparent

    return grandparents


