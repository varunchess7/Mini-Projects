import calendar

def show_calendar():
    print("📅 Calendar Viewer")
    year = int(input("Enter year (e.g., 2025): "))

    choice = input("Show (M)onth or (F)ull year calendar? ").lower()

    if choice == 'm':
        month = int(input("Enter month (1–12): "))
        print("\n" + calendar.month(year, month))
    else:
        print("\n" + calendar.calendar(year))

show_calendar()
