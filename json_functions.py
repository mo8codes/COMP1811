import json
from classes import Parent, Leaf, Root

#JSON create Person object from file
def create_objects_from_json(db):
    for person in db:
        #print(person) #Person is a dictionary for example: {'uid': 1, "type": Leaf, 'name': 'John Doe', 'is_male': True, 'is_alive': True, 'date_of_birth': '15-03-1985', 'date_of_death': None, 'spouse': 2, 'parents': {'father': 3, 'mother': 4}}
        #Create the objects from the JSON
        if person["type"] == "Leaf":
            Leaf()
        if person["type"] == "Parent":
            Parent()
        if person["type"] == "Root":
            Root()


#JSON read file paternal.json and maternal.json
def read_json(jsonfile):
    with open(jsonfile, "r") as db:
        paternal_db = json.load(db)
    return create_objects_from_json(paternal_db)