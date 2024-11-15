import json
from classes import Person, Parent, Leaf

#JSON create Person object from file
def create_objects_from_json(objects_db):
    created_objects = [] #stored objects
    for person in objects_db:
        print(person) #Person is a dictionary for example: {'uid': 1, "type": Leaf, 'name': 'John Doe', 'is_male': True, 'is_alive': True, 'date_of_birth': '15-03-1985', 'date_of_death': None, 'spouse': 2, 'parents': {'father': 3, 'mother': 4}}
        #Create the objects from the JSON
        if person["type"] == "Leaf":
            pass#Leaf()
        if person["type"] == "Parent":
            pass#Parent()
    pass

#JSON read file "people.json and betty family"
def read_json(db, db2):
    with open("people.json", "r") as db, open("betty_family.json", "r") as db2:
        objects_db = json.load(db)
        betty_family = json.load(db2)

    return create_objects_from_json(objects_db & betty_family)
db1 = "people.json"
db2 = "betty_family"

print("Data from:", db2)

#I am trying to merge our json files. I'm not sure if this is the right way