study_sessions = []

def add_session():
    while True:
        subject = input("Enter subject name: ")
        if not subject:
            print("Please enter a subject name.")
            continue
        try:
            minutes = int(input("Enter minutes studied: "))
            if minutes <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    session = {
        "subject": subject,
        "minutes": minutes
    }

    study_sessions.append(session)
    print("Study session added!\n")

def show_statistics():
    if not study_sessions:
        print("No study sessions recorded yet.\n")
        return

    total_minutes = 0
    subject_totals = {}

    for session in study_sessions:
        total_minutes += session["minutes"]
        subject = session["subject"]
        minutes = session["minutes"]

        if subject in subject_totals:
            subject_totals[subject] += minutes
        else:
            subject_totals[subject] = minutes
    most_studied_subject = max(subject_totals,key=subject_totals.get)
    print(f"\nTotal minutes studied:{total_minutes}")
    print("\nMinutes per subject:")
    for subject, minutes in subject_totals.items():
        print(f"{subject}:{minutes} minutes")
        print(f"Most studied subject:{most_studied_subject}\n")
  
def menu():
    while True:
            print("Study Session Tracker")
            print("1.Add  study session")
            print("2.View statistics")
            print("3.Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                add_session()
            elif choice == "2":
                show_statistics()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()