import uuid


def generate_random_file() -> str:
    """
    Function for generating a random file

    @return: random file name
    """
    return str(uuid.uuid4())
