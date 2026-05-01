class Calendar:
    def __init__(self):
        self.events = {}

    def is_leap_year(self, year):
        return year % 4 == 0

    def get_days_in_month(self, month, year):
        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                return 31
            case 4 | 6 | 9 | 11:
                return 30
            case 2:
                return 29 if self.is_leap_year(year) else 28
            case _:
                return -1

    def get_month_name(self, month):
        months = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]
        return months[month - 1] if 1 <= month <= 12 else "Unknown"

    def is_valid_date(self, day, month, year):
        if year < 2026 or year > 2028:
            print("[ERROR] Year must be between 2026 and 2028 only!")
            return False

        if month < 1 or month > 12:
            print("[ERROR] Month must be between 1 and 12 only!")
            return False

        max_days = self.get_days_in_month(month, year)
        if day < 1 or day > max_days:
            print(f"[ERROR] Day must be between 1 and {max_days} for {self.get_month_name(month)} {year}!")
            return False

        return True

    def get_date_key(self):
        while True:
            try:
                print("Enter the date:")
                year = int(input("Year (2026-2028): "))
                month = int(input("Month (1-12): "))
                day = int(input("Day: "))

                if self.is_valid_date(day, month, year):
                    return f"{year:04d}-{month:02d}-{day:02d}"

                print("Please try again.")

            except ValueError:
                print("Please enter valid numbers. Try again.")

    def add_event(self):
        date_key = self.get_date_key()
        event_name = input("Enter event name: ")

        if date_key not in self.events:
            self.events[date_key] = []

        self.events[date_key].append(event_name)

        year = int(date_key[:4])
        month = int(date_key[5:7])
        day = int(date_key[8:10])
        month_name = self.get_month_name(month)

        print(f"[SUCCESS] Event '{event_name}' added on {month_name} {day}, {year}!")

    def view_events_on_date(self):
        date_key = self.get_date_key()

        if date_key in self.events and self.events[date_key]:
            year = int(date_key[:4])
            month = int(date_key[5:7])
            day = int(date_key[8:10])
            month_name = self.get_month_name(month)

            print(f"Events on {month_name} {day}, {year}:")
            for event in self.events[date_key]:
                print(f"- {event}")
        else:
            print("No events found on this date.")

    def view_all_events(self):
        if not self.events:
            print("No events added yet.")
            return

        print("All Events:")
        for date_key in sorted(self.events.keys()):
            year = int(date_key[:4])
            month = int(date_key[5:7])
            day = int(date_key[8:10])
            month_name = self.get_month_name(month)

            print(f"{month_name} {day}, {year}:")
            for event in self.events[date_key]:
                print(f"  - {event}")

    def delete_event(self):
        date_key = self.get_date_key()

        if date_key not in self.events or not self.events[date_key]:
            print("No events found on this date.")
            return

        year = int(date_key[:4])
        month = int(date_key[5:7])
        day = int(date_key[8:10])
        month_name = self.get_month_name(month)

        print(f"Events on {month_name} {day}, {year}:")
        for i, event in enumerate(self.events[date_key], 1):
            print(f"{i}. {event}")

        try:
            choice = int(input("Enter event number to delete (0 to cancel): "))

            if 1 <= choice <= len(self.events[date_key]):
                removed = self.events[date_key].pop(choice - 1)
                print(f"[SUCCESS] Event '{removed}' deleted!")
            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    cal = Calendar()

    while True:
        print("----MAIN MENU----")
        print("1. Add an Event")
        print("2. View Events on a Date")
        print("3. View All Events")
        print("4. Delete an Event")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                cal.add_event()
            elif choice == 2:
                cal.view_events_on_date()
            elif choice == 3:
                cal.view_all_events()
            elif choice == 4:
                cal.delete_event()
            elif choice == 5:
                print("byebye!")
                break
            else:
                print("Invalid choice. Please enter 1-5.")

        except ValueError:
            print("Please enter a number.")