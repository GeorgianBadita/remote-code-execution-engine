import re
import logging

from typing import List

logging.basicConfig(level=logging.DEBUG)


def python_result_extractor(raw_test_output: str) -> List[bool]:
    """
    Function which extracts the test resutls for an execution

    @param raw_test_output: output provided by the submission

    @return list of bools, where each element on position i means, that the i-th test passed or not
    """

    logging.info("Start extracting result from raw_output")

    try:
        test_results = raw_test_output.strip().split('\n')[0]

        if not re.match("^[\\.F]*$", test_results):
            raise ValueError("Submission result is not properly formatted")

        return [True if test_res == "." else False for test_res in test_results]

    except (ValueError, IndexError) as err:
        logging.error(f"Error while extracting results from following raw output: {raw_test_output}")
        raise ValueError(f"Invalid raw output format for python err: {str(err)}")
