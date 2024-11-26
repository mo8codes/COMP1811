import classes
import json_functions
from json_functions import read_json
from classes import FamilyCalculations
from classes import FamilyTree

def person_search(search_uid):
    results = []
    for uid, person in sorted(people.items()):
        if person.uid == search_uid:
            results.append(person.name)
            return (results)


def child1_search(search_uid):
    results = []
    for uid, person in sorted(parents.items()):
        if person.child1 == search_uid:
            results.append(person.name)
            return (results)


def exit_message():
    print("Goodbye!")
    exit()


def start_menu():
    while True: #Loops until the user exits the menu
        print( "*****************************************************************************************************")
print("||________________________________________________________________________________________________||")
print("||                              Welcome to the Family Tree Tool                                   || ")
print("||________________________________________________________________________________________________||")
print("|| To display the entire family tree: Enter 1                                                     ||")
print("||                                                                                                ||")
print("|| To display all parents:  Enter 2                                                               ||")
print("||                                                                                                ||")
print("|| To display all grandparents:  Enter 3                                                          ||")
print("||                                                                                                ||")
print("|| To display all children/grandchildren:  Enter 4                                                ||")
print("||                                                                                                ||")
print("|| To display all grandchildren:  Enter 5                                                         ||")
print("||                                                                                                ||")
print("|| To display the generation index of a particular family member:  Enter 6                        ||")
print("||                                                                                                ||")
print("|| To display the date of birth of a particular family member:  Enter 7                           ||")
print("||                                                                                                ||")
print("|| To display the date of death of a particular family member:  Enter 8                           ||")
print("||                                                                                                ||")
print("|| To display the gender of a particular family member:  Enter 9                                  ||")
print("||                                                                                                ||")
print("|| To display the mother of a particular family member:  Enter 10                                 ||")
print("||                                                                                                ||")
print("|| To display the father of a particular family member:  Enter 11                                 ||")
print("||                                                                                                ||")
print("|| To display the partner of a particular family member:  Enter 12                                ||")
print("||                                                                                                ||")
print("|| To display the children of a particular family member:  Enter 13                               ||")
print("||                                                                                                ||")
print("|| To display the grandchildren of a particular family member:  Enter 14                          ||")
print("||                                                                                                ||")
print("|| To display the parents of a particular family member: Enter 15                                 ||")
print("||                                                                                                ||")
print("|| To display the immediate family members: Enter 16                                              ||") #functions here and above should be added by Mo
print("||                                                                                                ||")
print("|| To display the siblings of a member: Enter 17                                                  ||")
print("||                                                                                                ||")
print("|| To display the cousins of a member: Enter 18                                                   ||")
print("||                                                                                                ||")
print("|| To display birthdays of members of the entire family: Enter 19                                 ||")
print("||                                                                                                ||")
print("|| To exit: Enter 20                                                                              ||")
user_input = input("Select any option (1-20) above to learn more: " )
people, parents, grandparents = read_json('maternal.json')

if user_input == "1":
    print("Displaying the entire family tree:")
    for uid, person in sorted(people.items()):
        print(person.name)
    exit_message()

if user_input == "2":
    print("Displaying all parents:")
    for uid, parent in sorted(parents.items()):
        print(parent.name)
    exit_message()

if user_input == "3":
    print("Displaying all grandparents:")
    for uid, grandparent in sorted(grandparents.items()):
        print(grandparent.name)
    exit_message()

if user_input == "4":
    print("Displaying all children/grandchildren:")
    for uid, person in sorted(people.items()):
        if person.level in [1, 2]:
            print(person.name)
    exit_message()

if user_input == "5":
    print("Displaying all grandchildren:")
    for uid, person in sorted(people.items()):
        if person.level == 2:
            print(person.name)
    exit_message()

if user_input == "6":
    searchName = input("Enter Full Name (Capitalised): ")
    for uid, person in sorted(people.items()):
        if person.name == searchName:
            print(f"They are from generation {person.level + 1} of the family.")
    exit_message()

if user_input == "7":
    searchName = input("Enter Full Name (Capitalised): ")
    for uid, person in sorted(people.items()):
        if person.name == searchName:
            print(f"Their date of birth is: {person.date_of_birth}")
    exit_message()


if user_input == "8":
    chosen_uid = input("Enter the name of a person to find their siblings:")
    for uid, person in sorted(people.items()):
        if chosen_uid in people:
            siblings = get_siblings()
            if siblings:
                print(f"Their siblings are: {siblings}")
            for sibling in siblings:
                print(f"-{sibling}")
            else:
                print(f"{[chosen_uid].name} has no siblings listed in the tree.")

    exit_message()

if user_input == "9":
    searchName = input("Enter Full Name: ")
    for uid, person in sorted(people.items()):
        if person.name == searchName:
            if person.is_male == True:
                print(f"They are male.")
            elif person.is_male == False:
                print(f"They are not male.")
    exit_message()

if user_input == "10":
    searchName = input("Enter Full Name (Capitalised): ")
    for uid, person in sorted(people.items()):
        if person.name == searchName:
            results = person_search(person.mother)
            print(f"Their mother is: {results}")
    exit_message()

if user_input == "11":
    searchName = input("Enter Full Name (Capitalised): ")
    for uid, person in sorted(people.items()):
        if person.name == searchName:
            results = person_search(person.father)
            print(f"Their father is: {results}")
    exit_message()

if user_input == "12":
    searchName = input("Enter Full Name (Capitalised): ")
    for uid, person in sorted(people.items()):
        if person.name == searchName:
            results = person_search(person.partner)
            print(f"Their partner is: {results}")
    exit_message()

if user_input == "13":
    searchName = input("Enter Full Name (Capitalised): ")
    for uid, parent in sorted(parents.items()):
        if parent.name == searchName:
            child1_result = child1_search(parent.child1)
            print(f"Their children are: {child1_result} & ")
    exit_message()

elif user_input =="14":
    searchName = input("Enter Full Name (Capitalised): ")
    for uid, grandparent in sorted(grandparents.items()):
        print(f"{grandparent.name} = {grandparent.grandchild1} & {grandparent.grandchild2} & {grandparent.grandchild3} & {grandparent.grandchild4}")
    exit_message()

if user_input == "19":
    print("Displaying all birthdays:")
    for uid, person in sorted(people.items()):
            print(f"{person.date_of_birth}")
    exit_message()

if user_input == "20":
    print("Enter a person to find their cousins:")
    for uid, person in sorted(people.items()):
        print(f"{person.name}")
    exit_message()

elif user_input == "21":
    exit_message()

else:
    print("Invalid Option, Please Restart.")