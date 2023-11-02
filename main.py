from datetime import date, datetime, timedelta

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday' ]


def get_birthdays_per_week(users):
    current_date = date.today()
    upcoming_birthdays = {}
    for user in users:
        try:
            celebrate_day = user["birthday"]
            if celebrate_day.month == 1 and current_date.month == 12 and current_date.day > 25:
                celebrate_day = user["birthday"].replace(year=current_date.year+1)
            else:
                celebrate_day = user["birthday"].replace(year=current_date.year)
        except ValueError:
            celebrate_day = user["birthday"].replace(year=current_date.year, month=current_date.month + 1, day=1)
        if(celebrate_day - current_date).days >= 0 and (celebrate_day - current_date).days < 7:
            if celebrate_day.weekday() == 5:
                celebrate_day = celebrate_day + timedelta(days=2)
            if celebrate_day.weekday() == 6:
                celebrate_day = celebrate_day + timedelta(days=1)
            if weekdays[celebrate_day.weekday()] in upcoming_birthdays:
                upcoming_birthdays[weekdays[celebrate_day.weekday()]].append(user["name"])
            else:
                upcoming_birthdays[weekdays[celebrate_day.weekday()]] = [user["name"]]
    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
