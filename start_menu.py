import classes
from json_functions import read_json
from classes import FamilyTree

def start_menu():
    print( "*****************************************************************************************************")
    print("||                  Welcome to the Emmershon Family Tree                                           || ")
    print("||________________________________________________________________________________________________||")

    while True: #Loops until the user exits the menu
       user_input = input("Select any option (1-12) below to learn more:                                ||" )
print("||________________________________________________________________________________________________||")
print("|| To display the entire Family Tree: Enter 1                                                     ||")
print("||                                                                                                ||")
print("|| To display parents of a particular family member:  Enter 3                                     ||")
print("||                                                                                                ||")
print("|| To display the grandchildren of a particular family member: Enter 4                            ||")
print("||                                                                                                ||")
print("|| To display Immediate family members: Enter 5                                                   ||") #functions here and above should be added by Mo
print("||                                                                                                ||")
print("|| To display siblings of a member: Enter 6                                                       ||")
print("||                                                                                                ||")
print("|| To display cousins of a member: Enter 7                                                        ||")
print("||                                                                                                ||")
print("|| To display birthdays of a member: Enter 8                                                      ||")
print("||                                                                                                ||")
print("|| To display birthdays of members of the entire Emmershon family: Enter 9                        ||")
print("||9. Exit                                                                                         ||")
user_input = input("Enter your choice:")

if user_input == 1:
    print("Displaying the Emmershon Family Tree")
    maternal_tree = read_json('maternal.json')
    paternal_tree = read_json('paternal.json')


elif user_input =="6":
    print("Displaying the siblings of a member")
        break
else:
    print("Invalid option ")


