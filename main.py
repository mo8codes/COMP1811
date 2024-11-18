from json_functions import read_json
from start_menu import start_menu
from object_management import merge_objects


def main():
    paternal_objects = read_json("paternal.json")
    maternal_objects = read_json("maternal.json")
    people = merge_objects(paternal_objects, maternal_objects) # Contains all people
    print(people) # Temporary for testing line
    start_menu() # Create the start menu in the console


if __name__ == "__main__":
    main()