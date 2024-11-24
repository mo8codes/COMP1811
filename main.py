from json_functions import create_objects_from_json
from start_menu import start_menu

def main():
    people = create_objects_from_json() # Contains all people
    start_menu() # Create the start menu in the console

if __name__ == "__main__":
    main()