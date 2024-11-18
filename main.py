from json_functions import read_json
from start_menu import start_menu

# Allows creation of people list containing the objects for every single person
def merge_objects(paternal_objects, maternal_objects):
    people = []
    for person in paternal_objects:
        people.append(person)
    for person in maternal_objects:
        people.append(person)
    return people

def main():
    paternal_objects = read_json("paternal.json")
    maternal_objects = read_json("maternal.json")
    people = merge_objects(paternal_objects, maternal_objects) # Contains all people
    print(people) # Temporary for testing line
    start_menu() # Create the start menu in the console


if __name__ == "__main__":
    main()