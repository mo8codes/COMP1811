import time
from classes import *
import time

def start_menu(people):
    print("****************************************************************************************************")
    print("||                         Welcome to the Emmershon Family Tree                                   ||")
    print("||________________________________________________________________________________________________||")
    print("|| Select any option below to learn more (type the text before the .):                            ||")
    print("||________________________________________________________________________________________________||")
    print("||  I. Select an individual and return and display their parents (if any)                         ||")
    print("||  +. Display the entire family tree                                                             ||")
    print("||  II. Select an individual and return and display their grandchildren (if any)                  ||")
    print("||  III. Select an individual and display their immediate family                                  ||")
    print("||  IV. Select an individual and display their extended family                                    ||")
    print("||  V. Select an individual and return and display their siblings (if any)                        ||")
    print("||  VI. Select an individual and return and display their cousins (if any)                        ||")
    print("||  VII. Display a list of birthdays of all family members                                        ||")
    print("||  VIII. Create a sorted birthday calendar (merge if multiple on the same date)                  ||")
    print("||  IX. Create an integrated program with both branches                                           ||")
    print("||  X. Test output using people from the partner's branch                                         ||")
    print("||  XI. Find the average age of death of everyone in the combined family tree                     ||")
    print("||  XII. Find the number of children for each individual                                          ||")
    print("||  XIII. Find the average number of children per person                                          ||")
    print("||  XIV. Exit the program                                                                         ||")
    print("****************************************************************************************************")

    user_input = input("Enter your choice: ").strip()

    match user_input:
        case "+":
            print("************************************************************")
            print("Displaying a list of all the people in the family tree....||")
            print("************************************************************")
            list_people(people)
        # case "I":
        #     print("Feature I: Select an individual and return and display their parents (if any).")
        #     list_people(people)
        #     try:
        #         who = input("Select a number from the list to display a person's parents: ")
        #         people[who].get_cousins(people)
        #     except ValueError:
        #         print("Invalid input. Please enter a valid number.")
        #    except KeyError:


        case "II":
            print("Feature II: Select an individual and return and display their grandchildren (if any).")
            list_people(people)
            who = get_who("Which person's grandchildren would you like to know? Pick a number: ")
            if isinstance(people[who], (Parent, Root)):
                if people[who]:
                    people[who].get_grandchildren(people)
            else:
                print("No grandchildren found.")

        case "III":
            print("Feature III: Select an individual and display their immediate family.")
            list_people(people)
            who = get_who("Which person's immediate family would you like to know? Pick a number: ")
            # Add functionality to display the immediate family
            people[who].get_immediate_family(people)

        case "IV":
            print("Feature IV: Select an individual and display their extended family.")
            # Add functionality to display the extended family
            get_extended_family(people)


        case "V":
            print("Feature II: Select an individual to return and display their siblings (if any).")
            list_people(people)
            who = get_who("Which person's siblings would you like to know? Pick a number: ")
            if isinstance(people[who], (Person , Root)):
                if people[who]:
                    people[who].get_siblings(people)
            else:
                print("No siblings found.")

        case "VI":
            print("Feature VI: Select an individual and return and display their cousins (if any).")
            list_people(people)
            who = get_who("Select an individual to display their cousins: (Pick a number:)")

            try:
                people[who].get_cousins( people)
            except KeyError:
                print("This person has no cousins")
            finally:
                time.sleep(2.5)

        case "VII":
            print("Feature VII: Displaying a list of birthdays of all family members.")
            for uid, person in people.items():
                if person.date_of_birth:
                    print(f"{uid}. {person.name} ({person.date_of_birth.strftime('%d-%m-%Y')})")
                else:
                     print(f"{uid}. {person.name} (No birthday information available)")


        # case "VIII":
        #     print("Feature VIII: Create a sorted birthday calendar.")
        #     calendar = print_birthday_calendar(people)
        #     print("Displaying the Family Birthday Calendar:")
        #     for date_of_birth, names, in calendar.items():
        #         dates = datetime.strptime(date,"%m-%d").strftime("%B %d"))
        #         print(f"{dates}: {', '.join(names)}")

        case "IX":
            print("Feature IX: Create an integrated program with both branches.")
            # Add functionality for integration

        case "X":
            print("Feature 3aii: Test output using people from the partner's branch.")
            # Add functionality to test output with partner branch

        case "XI":
            print("Feature XI: Find the average age of death of everyone in the combined family tree.")
            # Add functionality to calculate average age of death

        case "XII":
            print("Feature XII: Find the number of children for each individual.")
            # Add functionality to count children for each individual
            for person in people:
                people[person].add_descendants(people)  # Add the children and grandchildren to the objects
                if people[person].children:
                    print(people[person].name,"has", len(people[person].children), "children.")

        case "XIII":
            print("Feature XIII: Find the average number of children per person.")
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