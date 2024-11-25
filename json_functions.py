import json
from classes import Parent, Leaf, Root

#JSON create Person object from file
def create_objects_from_json():
    dbs = ("paternal.json", "maternal_mo.json")
    people = {}
    for file in dbs:  # Should only be 2 maternal side and paternal side
        # Open json file
        with open(file, "r") as db:  # Open and read the JSON file
            data = json.load(db)  # Parse JSON data
            for person in data["people"]:  # Iterate through each person in the JSON
                # Create the objects from the JSON
                if person["type"] == "Leaf":
                    obj = Leaf(
                        uid=person["uid"],
                        name=person["name"],
                        is_male=person["is_male"],
                        is_alive=person["is_alive"],
                        date_of_birth=person["date_of_birth"],
                        date_of_death=person["date_of_death"],
                        mother=person["mother"],
                        father=person["father"],
                        spouse=person["spouse"],
                        previous_spouses=person["previous_spouses"]
                        )
                    #print(obj.uid,obj.name,obj.is_male,obj.is_alive,obj.date_of_birth,obj.date_of_death,obj.mother,obj.father,obj.spouse,obj.previous_spouses)

                elif person["type"] == "Parent":
                    obj = Parent(
                        uid=person["uid"],
                        name=person["name"],
                        is_male=person["is_male"],
                        is_alive=person["is_alive"],
                        date_of_birth=person["date_of_birth"],
                        date_of_death=person["date_of_death"],
                        mother=person["mother"],
                        father=person["father"],
                        spouse=person["spouse"],
                        previous_spouses=person["previous_spouses"],
                        children=person.get("children", None),
                        grandchildren=person.get("grandchildren", None)
                    )
                elif person["type"] == "Root":
                    obj = Root(
                        uid=person["uid"],
                        name=person["name"],
                        is_male=person["is_male"],
                        is_alive=person["is_alive"],
                        date_of_birth=person["date_of_birth"],
                        date_of_death=person["date_of_death"],
                        mother=None,
                        father=None,
                        spouse=person["spouse"],
                        previous_spouses=person["previous_spouses"],
                        children=person.get("children", None),
                        grandchildren=person.get("grandchildren", None)
                    )

                # Add the created object to the dictionary
                people[person["uid"]] = obj

    return people  # Dictionary UID:Object
