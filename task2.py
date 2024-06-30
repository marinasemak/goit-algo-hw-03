import random

# Generates unique set of numbers for the lottery
def get_numbers_ticket(min, max, quantity):

    # Check if input data is corect
    if min >= 1 and max <= 1000:
        num_range = list(range(min, max))

        # Generate list of unique random nambers in set range
        random_list = random.sample(num_range, quantity)
        # Sort list in ascending order
        random_list.sort()
    else: 
        random_list = []
    return random_list


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)


