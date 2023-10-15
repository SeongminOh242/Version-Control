from datetime import datetime

def main():
    name = input("Enter your name: ")
    age = int(input("How old are you now? "))
    current_year = int(input("Enter the current year: "))

    birth_year = current_year - age
    birthday = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthday, "%Y-%m-%d")
    today = datetime.now()

    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        next_birthday = datetime(current_year, birthdate.month, birthdate.day)
    else:
        next_birthday = datetime(current_year + 1, birthdate.month, birthdate.day)

    days_until_next_birthday = (next_birthday - today).days
    print(f"Hi {name}! You were born in {birth_year}. Your next birthday is in {days_until_next_birthday} days.")

if __name__ == "__main":
    main()
