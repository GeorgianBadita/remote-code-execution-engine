import re
import logging

from typing import List

logging.basicConfig(level=logging.DEBUG)


def python_submission_code_injector(user_code: str, test_code: str) -> str:
    """
    Function which injects the user code into the test_code in python

    @param user_code: user code
    @param test_code: code for testing the problem

    @return the final code to be evaluated
    @raise ValueError if the test_code does not meets the python testing code requirements
    """

    logging.info("Start injecting user code")

    try:

        if not re.search(".*class.*Test.*", test_code):
            raise ValueError("Test code does not contain a class named Test<<ProblemName>>")

        line_split: List[str] = test_code.split('\n')
        last_import_pos: int = 0

        for i in range(len(line_split)):
            if line_split[i].startswith("import"):
                last_import_pos = i

        final_code = '\n'.join(['\n'] + line_split[:last_import_pos + 1] + ['\n#===========USER CODE START===========',
                                                                            user_code,
                                                                            '\n#===========USER CODE END==========='] +
                               line_split[last_import_pos + 1:])
    except (ValueError, IndexError) as e:
        logging.error(f"Error while composing python code when injecting: {user_code}, {test_code}")
        raise ValueError(f"Invalid code format for python testing, err: {str(e)}")

    logging.info(f"Successfully injected code, {user_code}, {test_code}")
    return final_code
