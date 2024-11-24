def start_menu():
    print( "*****************************************************************************************************")
    print("||                  Welcome to the Emmershon Family Tree                                           || ")
    print("||________________________________________________________________________________________________||")
    print("Select any option (1-12) below to learn more:                                ||" )
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
    # Could we use case statement here or is that slower?
    if user_input == "1":
        print("Displaying the Emmershon Family Tree")
        #maternal_tree = read_json('maternal.json')
        #paternal_tree = read_json('paternal.json')


    elif user_input =="6":
        print("Displaying the siblings of a member")

    else:
        print("Invalid option ")


