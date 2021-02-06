def get_exec_command_python(language_cmd: str, in_file_path: str) -> str:
    """
    Function which provides the execution command for an upcoming python execution

    @param language_cmd: base language command, in this case "python"
    @param in_file_path: file where the input code will exist

    @return the execution command
    """

    return f"{language_cmd} {in_file_path}"


def get_exec_command_cpp(language_cmd: str, compiled_file_path: str, in_file_path: str, submission: bool) -> str:
    """
    Function which provides the execution command for an upcoming c++ execution

    @param language_cmd: base language command, in this case "g++"
    @param compiled_file_path: path to compiled file
    @param in_file_path: file where the input code will exist
    @param submission: flag which indicates if the execution will be a submission or not

    @return the execution command
    """

    if not submission:
        return (f"{language_cmd} -o {compiled_file_path} {in_file_path}"
                f" && ./{'/'.join(compiled_file_path.split('/')[2:])}")
    else:
        # TODO think what this should be
        return ""
