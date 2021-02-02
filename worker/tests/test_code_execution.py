import os
import subprocess
import pytest

from utils import generate_random_file
from code_execution.code_execution import CodeExcution


tmp_dir_path = '/worker/tests/tmp'
compiled_dir_path = '/worker/tests/tmp/compiled_files'


def test_WHEN_hello_world_python_THEN_return_correct_outpu(create_hello_world_py: str):
    """
    Function which tests that a simple hello world python program is executed as expected using python
    """

    language = "python"
    in_file_path = f"{tmp_dir_path}/in_files/{generate_random_file()}.{CodeExcution.get_lang_extension(language)}"
    compiled_file_path = f'{compiled_dir_path}/{generate_random_file()}.out'

    command_to_execute_code = CodeExcution.provide_code_execution_command(
        in_file_path, language, compiled_file_path)

    code_output = CodeExcution.execute_code(command_to_execute_code, in_file_path,
                                            compiled_file_path, create_hello_world_py)

    # output is hello world
    assert code_output == "Hello World\n"

    # resource files are deleted
    assert not os.path.isfile(in_file_path)


def test_WHEN_python_program_timesout_THEN_raise(create_infinite_loop_py: str):
    """
    Function which tests that an infinite looping python program is stopped after some time
    """

    language = "python"
    timeout = 0.5

    in_file_path = f"{tmp_dir_path}/in_files/{generate_random_file()}.{CodeExcution.get_lang_extension(language)}"
    compiled_file_path = f'{compiled_dir_path}/{generate_random_file()}.out'

    command_to_execute_code = CodeExcution.provide_code_execution_command(
        in_file_path, language, compiled_file_path)

    with pytest.raises(subprocess.TimeoutExpired):
        CodeExcution.execute_code(command_to_execute_code, in_file_path, compiled_file_path,
                                  create_infinite_loop_py, timeout=timeout)


def test_WHEN_hello_world_cpp_THEN_return_correct_output(create_hello_world_cpp: str, count_files: callable):
    """
    Function which tests that a simple hello world program is executed as expected using cpp
    """

    language = "cpp"
    in_file_path = f"{tmp_dir_path}/in_files/{generate_random_file()}.{CodeExcution.get_lang_extension(language)}"
    compiled_file_path = f'{compiled_dir_path}/{generate_random_file()}.out'

    command_to_execute_code = CodeExcution.provide_code_execution_command(
        in_file_path, language, compiled_file_path)

    code_output = CodeExcution.execute_code(command_to_execute_code, in_file_path,
                                            compiled_file_path, create_hello_world_cpp)

    # output is hello world
    assert code_output == "Hello World"

    # resource files are deleted
    assert not os.path.isfile(in_file_path)
    assert count_files(compiled_dir_path) == 0


def test_WHEN_cpp_program_timesout_THEN_raise(create_infinite_loop_cpp: str):
    """
    Function which tests that an infinite looping c++ program is stopped after some time
    """

    language = "cpp"
    timeout = 0.5

    in_file_path = f"{tmp_dir_path}/in_files/{generate_random_file()}.{CodeExcution.get_lang_extension(language)}"
    compiled_file_path = f'{compiled_dir_path}/{generate_random_file()}.out'

    command_to_execute_code = CodeExcution.provide_code_execution_command(
        in_file_path, language, compiled_file_path)

    with pytest.raises(subprocess.TimeoutExpired):
        CodeExcution.execute_code(command_to_execute_code, in_file_path, compiled_file_path,
                                  create_infinite_loop_cpp, timeout=timeout)


def test_WHEN_invalid_language_command_creation_THEN_raise():
    """
    Function for testing invalid language command creation
    """

    language = "invalid_language"

    with pytest.raises(KeyError):
        f"{tmp_dir_path}/in_files/{generate_random_file()}.{CodeExcution.get_lang_extension(language)}"


def test_WHEN_invalid_language_THEN_raise():
    """
    Function for testing invalid language execution
    """

    language = "cpp"

    in_file_path = f"{tmp_dir_path}/in_files/{generate_random_file()}.{CodeExcution.get_lang_extension(language)}"
    compiled_file_path = f'{compiled_dir_path}/{generate_random_file()}.out'

    with pytest.raises(KeyError):
        CodeExcution.provide_code_execution_command(
            in_file_path, "language", compiled_file_path)


def test_WHEN_invalid_language_syntax_THEN_raise(create_invalid_syntax_code: str):
    """
    Function for testing invalid language execution
    """

    language = "python"
    in_file_path = f"{tmp_dir_path}/in_files/{generate_random_file()}.{CodeExcution.get_lang_extension(language)}"
    compiled_file_path = f'{compiled_dir_path}/{generate_random_file()}.out'

    command_to_execute_code = CodeExcution.provide_code_execution_command(
        in_file_path, language, compiled_file_path)

    with pytest.raises(subprocess.SubprocessError):
        CodeExcution.execute_code(command_to_execute_code, in_file_path,
                                  compiled_file_path, create_invalid_syntax_code)
