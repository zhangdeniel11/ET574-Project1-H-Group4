import tracker

def menu():
    print("==== Welcome To The Study Tracker ====")
    print("1: Add study Session ")
    print("2: View Summary ")
    print("3: View all sessions ")
    print("4: Exit ")

    running = true

    while running:
        menu()
        choice =input("Please choose a option: ")
        if choice == "1":
            tracker.add_session()
         elif choice == "2":
            tracker.view_summary()
        elif choice == "3":
            tracker.view_all_sessions()
        elif choice == "4":
            print("Goodbye!")
            running = false

        else:
            print("Invalid choice try again!\n")