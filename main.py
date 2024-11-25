from json_functions import create_objects_from_json
from start_menu import start_menu

def main():
    people = create_objects_from_json() # Contains all people
    start_menu(people) # Create the start menu in the console

def average_age_of_death(self):  # Together
    # (Feature 3aiii)
    pass

def average_num_of_children_per_person(self):  # Together
    # (Feature 3bii)
    pass

if __name__ == "__main__":
    main()