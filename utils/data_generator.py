import random
import string


def generate_random_string(length=10):
    """
    Generates a random string of specified length.
    :param length: Length of the string to generate.
    :return: A random string.
    """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_int(min_value=0, max_value=100):
    """
    Generates a random integer between min_value and max_value.
    :param min_value: Minimum value of the integer.
    :param max_value: Maximum value of the integer.
    :return: A random integer.
    """
    return random.randint(min_value, max_value)


def generate_random_date(start_year=2000, end_year=2020):
    """
    Generates a random date between two years.
    :param start_year: Start year for the date range.
    :param end_year: End year for the date range.
    :return: A string representing a random date.
    """
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Simplification to avoid invalid dates
    return f"{year}-{month:02d}-{day:02d}"


def generate_user_data():
    """
    Generates a dictionary representing a user with random data.
    :return: A dictionary with user data.
    """
    return {
        'username': generate_random_string(8),
        'age': generate_random_int(18, 70),
        'join_date': generate_random_date()
    }


# Example usage:
if __name__ == "__main__":
    user_data = generate_user_data()
    print(user_data)
