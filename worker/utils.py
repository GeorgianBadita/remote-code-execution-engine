import uuid


def generate_random_file() -> str:
    """
    Function for generating a random file
    """
    return str(uuid.uuid4())
