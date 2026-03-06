import data

def add_session():
    subject = input("enter subject/course: ")
    minutes = int(input("Enter amount of minutes studied: "))
    location = input("Enter the location: ")
    notes = input("enter your notes (optional): ")

    data.subjects.append(subject)
    data.minutes.append(minutes)
    data.locations.append(location)
    data.notes.append(notes)

    print("Session added!")