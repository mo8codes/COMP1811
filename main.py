from json_functions import read_json
from start_menu import start_menu

def main():
    paternal_objects = read_json("paternal.json")
    maternal_objects = read_json("maternal.json")
    start_menu() # Create the start menu in the console


if __name__ == "__main__":
    main()