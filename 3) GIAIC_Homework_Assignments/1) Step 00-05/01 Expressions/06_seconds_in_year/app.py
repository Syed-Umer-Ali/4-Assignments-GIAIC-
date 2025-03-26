from colorama import Fore, Style

DAYS_IN_YEAR: int = 365
HOURS_IN_DAY: int = 24
MINUTES_IN_HOUR: int = 60
SECONDS_IN_MINUTE: int = 60

# Calculation
def calculate_seconds_in_year(days: int, hours: int, minutes: int, seconds: int) -> int:
    return days * hours * minutes * seconds

seconds_in_year: int = calculate_seconds_in_year(DAYS_IN_YEAR, HOURS_IN_DAY, MINUTES_IN_HOUR, SECONDS_IN_MINUTE)

# result
print(Fore.LIGHTMAGENTA_EX + f"\n\t\t\tThere Are {seconds_in_year} Seconds In A Year!\t\t\t".title() + Style.RESET_ALL)