import time

def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def calculate_days_until_birthday(birth_month, birth_day, current_month, current_day):
    if (current_month, current_day) == (birth_month, birth_day):
        return 0
    elif (current_month, current_day) < (birth_month, birth_day):
        return (birth_month - current_month) * 30 + (birth_day - current_day)
    else:
        next_birthday_year = time.localtime().tm_year + 1
        next_birthday = time.struct_time((next_birthday_year, birth_month, birth_day, 0, 0, 0, 0, 0, 0))
        days_until_next_birthday = int((time.mktime(next_birthday) - time.time()) / (24 * 3600))
        return days_until_next_birthday

name = input("What's your name? ")
birthdate = input("Enter your date of birth (YYYY-MM-DD): ")

# Extract year, month, and day from the birthdate
birth_year, birth_month, birth_day = map(int, birthdate.split('-'))

current_time = time.localtime()
current_year = current_time.tm_year
current_month = current_time.tm_mon
current_day = current_time.tm_mday

age_in_years = current_year - birth_year
age_in_months = age_in_years * 12 + current_month - birth_month

print(f"Hello, {name}!")
print(f"Your age is {age_in_years} years, {age_in_months % 12} months, and {current_day - birth_day} days.")

zodiac_sign = get_zodiac_sign(birth_month, birth_day)
print(f"Your zodiac sign is {zodiac_sign}.")

days_until_birthday = calculate_days_until_birthday(birth_month, birth_day, current_month, current_day)
print(f"Your next birthday is in {days_until_birthday} days.")
