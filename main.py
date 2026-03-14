import tracker

def menu():

    running = True

    while running:

        print("\n==== Welcome To The Study Tracker ====")
        print("1: Add study session")
        print("2: View summary")
        print("3: View all sessions")
        print("4: Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            tracker.add_session()

        elif choice == "2":
            tracker.view_summary()

        elif choice == "3":
            tracker.view_all_sessions()

        elif choice == "4":
            print("Goodbye!")
            running = False

        else:
            print("Invalid choice, try again.\n")

menu()