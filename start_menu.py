import time
from classes import *
def start_menu(people):
    print("****************************************************************************************************")
    print("||                  Welcome to the Emmershon Family Tree                                          ||")
    print("||________________________________________________________________________________________________||")
    print("|| Select any option below to learn more (type the text before the .):                            ||")
    print("||________________________________________________________________________________________________||")
    print("||  1ai. Select an individual and return and display their parents (if any)                       ||")
    print("||  1aii. Select an individual and return and display their grandchildren (if any)                ||")
    print("||  1bi. Select an individual and display their immediate family                                  ||")
    print("||  1bii. Select an individual and display their extended family                                  ||")
    print("||  2ai. Select an individual and return and display their siblings (if any)                      ||")
    print("||  2aii. Select an individual and return and display their cousins (if any)                      ||")
    print("||  2bi. Display a list of birthdays of all family members                                        ||")
    print("||  2bii. Create a sorted birthday calendar (merge if multiple on the same date)                  ||")
    print("||  3ai. Create an integrated program with both branches                                          ||")
    print("||  3aii. Test output using people from the partner's branch                                      ||")
    print("||  3aiii. Find the average age of death of everyone in the combined family tree                  ||")
    print("||  3bi. Find the number of children for each individual                                          ||")
    print("||  3bii. Find the average number of children per person                                          ||")
    print("||  exit. Exit the program                                                                        ||")
    print("****************************************************************************************************")

    user_input = input("Enter your choice: ").strip()

    match user_input:
        case "1ai":
            print("Feature 1ai: Select an individual and return and display their parents (if any).")
            list_people(people)
            who = get_who("Which person's parents would you like to know? Pick a number: ")

            try:
                # Ensure the UID exists in the people dictionary
                print(people[who].get_parents(people))
                time.sleep(2.5)
                start_menu(people)

            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except KeyError:
                print("No person found with that ID.")

        case "1aii":
            print("Feature 1aii: Select an individual and return and display their grandchildren (if any).")
            list_people(people)
            who = get_who("Which person's grandchildren would you like to know? Pick a number: ")
            if isinstance(people[who], (Parent, Root)):
                if people[who]:
                    people[who].get_grandchildren(people)
            else:
                print("No grandchildren found.")

        case "1bi":
            print("Feature 1bi: Select an individual and display their immediate family.")
            list_people(people)
            who = get_who("Which person's immediate family would you like to know? Pick a number: ")
            # Add functionality to display the immediate family
            people[who].get_immediate_family(people)

        case "1bii":
            print("Feature 1bii: Select an individual and display their extended family.")
            # Add functionality to display the extended family
            get_extended_family(people)


        case "2ai":
            print("Feature 2ai: Select an individual and return and display their siblings (if any).")
            list_people(people)
            #who = input("Which person's siblings would you like to know? Pick a number: ")
            # Add functionality to display siblings

        case "2aii":
            print("Feature 2aii: Select an individual and return and display their cousins (if any).")
            list_people(people)
            #who = input("Which person's cousins would you like to know? Pick a number: ")
            # Add functionality to display cousins

        case "2bi":
            print("Feature 2bi: Display a list of birthdays of all family members.")
            # Add functionality to display list of birthdays

        case "2bii":
            print("Feature 2bii: Create a sorted birthday calendar.")
            # Add functionality to create and display birthday calendar

        case "3ai":
            print("Feature 3ai: Create an integrated program with both branches.")
            # Add functionality for integration

        case "3aii":
            print("Feature 3aii: Test output using people from the partner's branch.")
            # Add functionality to test output with partner branch

        case "3aiii":
            print("Feature 3aiii: Find the average age of death of everyone in the combined family tree.")
            # Add functionality to calculate average age of death

        case "3bi":
            print("Feature 3bi: Find the number of children for each individual.")
            # Add functionality to count children for each individual
            for person in people:
                people[person].add_descendants(people)  # Add the children and grandchildren to the objects
                if people[person].children:
                    print(people[person].name,"has", len(people[person].children), "children.")

        case "3bii":
            print("Feature 3bii: Find the average number of children per person.")
            # Add functionality to calculate the average number of children per person
            counter = 0
            num_people = 0
            for person in people:
                if isinstance(people[person], (Parent, Root)):  # Else is a leaf therefore no children
                    if people[person].is_male:  # Only count children once, only works if they have a father, since we made the people in the family tree this isn't a problem
                        people[person].add_descendants(people)  # Add the children and grandchildren to the objects
                        num_people += 1
                        counter += int((people[person].get_children(people)))
            # Print results
            print("Average number of children per person with children:", counter / num_people)
            print("Average number of children per person including those without children:", counter / len(people))

        case "exit":
            print("Exiting the program. Goodbye!")

        case _:
            print("Invalid option. Please try again.")

def list_people(people):
    for uid, person in people.items():
        print(f"{uid}. {person.name}")


def get_who(phrase):
    while True:
        try:
            who = int(input(phrase))
            return who
        except ValueError:
            # If not int then try again
            print("Invalid input. Please enter a valid number.")

def get_extended_family(people):  # Mo
    # (Feature 1bii) - Just prints everyone's name who is alive.
    for person in people:
        if people[person].is_alive:
            print(people[person].name)