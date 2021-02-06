import os
import pytest


@pytest.fixture
def create_hello_world_py() -> str:
    """
    Fixture which returns a simple hello world code in python
    """

    return "print('Hello World')"


@pytest.fixture
def create_infinite_loop_py() -> str:
    """
    Fixture which returns a simple inifnite loop program in python
    """

    return "while True:\n pass"


@pytest.fixture
def create_invalid_syntax_code() -> str:
    """
    Fixture which returns an inalid pytho program
    """

    return "Invalid program"


@pytest.fixture
def create_hello_world_cpp() -> str:
    """
    Fixture which returns a simple cpp hello world code
    """

    return '#include<iostream>\n using namespace std; int main() {cout << "Hello World"; return 0;}'


@pytest.fixture
def create_infinite_loop_cpp() -> str:
    """
    Fixture which returns a simple infnite loop program in cpp
    """
    return '#include<iostream>\n using namespace std; int main() {while(1){} return 0;}'


@pytest.fixture
def count_files() -> callable:
    """
    Fixture which returns a helper function for counting the number of files in a given directory

    @return: func - to be used in tests for counting number of files in a given directory

    """

    def count_files_in_dir(path: str) -> int:
        file_entries = [entry for entry in os.scandir(path) if entry.is_file()]

        return len(file_entries)

    return count_files_in_dir
