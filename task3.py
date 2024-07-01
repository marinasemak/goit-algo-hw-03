import re


# Remove excess symbols in phone numbers and normalize format
def normalize_phone(phone_number):
    # remove excess numbers
    removed_symbols = re.sub(r"[^\+\d]", "", phone_number)
    # add '+' sign if missed
    if removed_symbols.startswith("38"):
        removed_symbols = "+" + removed_symbols
    # add international code '+38' if missed
    elif not removed_symbols.startswith("+38"):
        removed_symbols = "+38" + removed_symbols
    return removed_symbols


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
