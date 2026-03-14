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

def view_all():

    if len(data.subjects) == 0:
        print("No study sessions recorded.")
        return

    print("All Study Sessions")

    for i in range(len(data.subjects)):
        print("----------------------")
        print("Session", i + 1)
        print("Subject:", data.subjects[i])
        print("Minutes:", data.minutes[i])
        print("Location:", data.locations[i])
        print("Notes:", data.notes[i])


def view_summary():

    if len(data.minutes) == 0:
        print("No study sessions recorded.")
        return

    total_sessions = len(data.minutes)
    total_minutes = sum(data.minutes)
    average_minutes = total_minutes / total_sessions
    longest_session = max(data.minutes)
    shortest_session = min(data.minutes)

    print("Study Session Summary")
    print("-----------------------------")
    print("Total Sessions:", total_sessions)
    print("Total Minutes Studied:", total_minutes)
    print("Average Minutes per Session:", round(average_minutes, 2))
    print("Longest Study Session:", longest_session)
    print("Shortest Study Session:", shortest_session)
