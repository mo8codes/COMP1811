from json_functions import read_json
from start_menu import start_menu

def main():
    people = read_json()
    start_menu() # Create the start menu in the console


if __name__ == "__main__":
    main()