study_sessions = []

def add_session():
    """Captures study data including a focus metric for optimization."""
    while True:
        subject = input("Enter subject name: ").strip()
        if not subject:
            print("Please enter a subject name.")
            continue
        try:
            minutes = int(input("Enter minutes spent studying: "))
            if minutes <= 0:
                print("Error: Please enter a positive number.")
                continue
            # New Optimizer Metric: Focus Level (1-10)
            focus = int(input("Enter focus level ( 1 =Distracted, 10=Peak Flow): "))
             if not("Error: Focus level must be between 1 and 10.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    session = {
        "subject": subject,
        "minutes": minutes,
        "focus": focus
    }

    study_sessions.append(session)
    print("Log updated. Study session added!\n")

def show_statistics():
    """Analyzes recorded data and provides optimization feedback."""
    if not study_sessions:
        print("No study sessions recorded yet.\n")
        return

    total_minutes = 0
    total_weighted_score = 0
    subject_totals = {}

    for session in study_sessions:
        minutes = session["minutes"]
        subject = session["subject"]
        total_raw_minutes += minutes

        # Optimizer Logic: Weighted Score
        # Formula: Duration * (Focus / 10)
        weighted_minutes = minutes * (session["focus"] / 10)
        total_weighted_score += weighted_minutes

        if subject in subject_totals:
            subject_totals[subject] += minutes
        else:
            subject_totals[subject] = minutes
    # Identify most time-intensive subject
    most_studied_subject = max(subject_totals,key=subject_totals.get)

    print("-" * 30)
    print("ANALYTICS SUMMARY")
    print(f"Total Raw Duration:{total_raw_minutes} minutes")
    print(f"Adjusted Efficiency Score: {total_weighted_score:.1f}units")
    print(f"Primary Focus:{most_studied_subject}")

    print("\nBreamdown by Subject:")
    for subject, minutes in subject_totals.items():
    print(f" - {subject}:{minutes} mins")
    print("\nMinutes per subject:")
    for subject, minutes in subject_totals.items():
        print(f"{subject}:{minutes} minutes")
        
    print("-" * 30)
    # Optimization Feedback System
    # Compares actual minutes vs. quality of focus
    efficiency_ratio = total_weighted_score / total_raw_minutes

    if efficiency_ratio < 0.7 :
        print("OPTIMIZER ADVICE: Low focus-to-duration ratio detected.")
        print(" Recommendation: Implement a physical reset or interval-based sessions(Pomodoro).")
        print("Status: Current cognitive load is being managed effectively.")
    print("-" * 30 + "\n")

def menu():
    """Main application interface."""
    while True:
            print("===Study Tracker Optimizer")
            print("1.Log study session")
            print("2.View optimization statistics")
            print("3.Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                add_session()
            elif choice == "2":
                show_statistics()
            elif choice == "3":
                print("Progress saved. Goodbye!")
                break
            else:
                print("invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()