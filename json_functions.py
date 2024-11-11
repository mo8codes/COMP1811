import json
from classes import Person, Parent, Leaf

#JSON create Person object from file
def create_objects_from_json(objects_db):
    for person in objects_db:
        print(person) #Person is a dictionary for example: {'uid': 1, "type": Leaf, 'name': 'John Doe', 'is_male': True, 'is_alive': True, 'date_of_birth': '15-03-1985', 'date_of_death': None, 'spouse': 2, 'parents': {'father': 3, 'mother': 4}}
        #Create the objects from the JSON
        if person["type"] == "Leaf":
            pass#Leaf()
        if person["type"] == "Parent":
            pass#Parent()
    pass

#JSON read file "people.json"
def read_json():
    with open("people.json", "r") as db:
        objects_db = json.load(db)
    return create_objects_from_json(objects_db)