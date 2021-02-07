import logging


from remote_code_execution_engine.submission_helper.code_injectors import python_submission_code_injector

logging.basicConfig(level=logging.DEBUG)


class SubmissionHelper:
    """
    Helper class for submission evaluation
    """

    __supported_langs = set(["python", "cpp"])

    @classmethod
    def compose_submission_code(cls, user_code: str, test_code: str, language: str) -> str:
        """
        Function which injects the user's code into test code

        @param user_code: submitted code
        @param test_code: code which tests the given problem
        @param language: programming language to evalate the code

        @return the final code to be executed for testing the submission
        @raise KeyError: if language is not supported
        """

        try:
            if language not in cls.__supported_langs:
                raise KeyError(language)

            logging.info(f"Start injecting code with, injector for {language}")
            if language == "python":
                return python_submission_code_injector(user_code, test_code)

        except KeyError as err:
            logging.info(f"{language} is not supported: err {err}")
            raise err

    @staticmethod
    def extract_info_from_raw_output_sumbission(raw_output: str, language: str) -> dict:
        pass
