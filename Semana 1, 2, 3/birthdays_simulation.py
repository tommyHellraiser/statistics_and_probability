import random


def generate_birthdays(k):
    birthdays = []

    for _ in range(0, k):
        birthdays.append(random.randint(1, 365))

    return birthdays


def are_there_matches(birthdays):
    birthdays_set = set(birthdays)

    if len(birthdays) != len(birthdays_set):
        return True

    return False


def calculate_probability(k, n):
    matches = 0
    no_matches = 0

    for _ in range(0, n):
        birthday_list = generate_birthdays(k)
        if are_there_matches(birthday_list):
            matches += 1
        else:
            no_matches += 1

    return matches / (matches + no_matches)


if __name__ == '__main__':
    # Cantidad de cumpleaños por muestra
    amount_of_persons = 30
    # Cantidad total de muestras
    sample_size = 10000

    # The P(E) is given by the amount_of_matches / amount_of_not_matches
    prob = calculate_probability(amount_of_persons, sample_size)
    print(f"\nThe probability of having at least one repeated birthday for a group of {amount_of_persons} persons, in a sample of size {sample_size} is: {prob}")
