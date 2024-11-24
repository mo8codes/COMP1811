def start_menu():
    while True:
        print("****************************************************************************************************")
        print("||                  Welcome to the Emmershon Family Tree                                          ||")
        print("||________________________________________________________________________________________________||")
        print("|| Select any option (1-12) below to learn more:                                                  ||")
        print("||________________________________________________________________________________________________||")
        print("|| To display the entire Family Tree: Enter 1                                                     ||")
        print("||                                                                                                ||")
        print("|| To display parents of a particular family member:  Enter 3                                     ||")
        print("||                                                                                                ||")
        print("|| To display the grandchildren of a particular family member: Enter 4                            ||")
        print("||                                                                                                ||")
        print("|| To display Immediate family members: Enter 5                                                   ||")
        print("||                                                                                                ||")
        print("|| To display siblings of a member: Enter 6                                                       ||")
        print("||                                                                                                ||")
        print("|| To display cousins of a member: Enter 7                                                        ||")
        print("||                                                                                                ||")
        print("|| To display birthdays of a member: Enter 8                                                      ||")
        print("||                                                                                                ||")
        print("|| To display birthdays of members of the entire Emmershon family: Enter 9                        ||")
        print("||                                                                                                ||")
        print("|| To exit the program: Enter 10                                                                  ||")
        print("****************************************************************************************************")

        user_input = input("Enter your choice: ").strip()  # Standardized input handling

        match user_input:
            case "1":
                print("Displaying the Emmershon Family Tree")

            case "3":
                print("Displaying the parents of a family member")

            case "4":
                print("Displaying the grandchildren of a family member")

            case "5":
                print("Displaying immediate family members")

            case "6":
                print("Displaying the siblings of a member")

            case "7":
                print("Displaying the cousins of a member")

            case "8":
                print("Displaying birthdays of a family member")

            case "9":
                print("Displaying all birthdays")

            case "10":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")
