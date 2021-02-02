import logging
import subprocess
import os


logging.basicConfig(level=logging.DEBUG)

supported_langs = {
    "python": {"cmd": "python", "extension": "py"},
    "cpp": {"cmd": "/usr/bin/g++", "extension": "cpp"}
}


class CodeExcution:

    @staticmethod
    def get_lang_extension(language: str) -> str:
        """
        Function which provides the language file extension

        @param language: the language for which we want to find the extension

        @return: language extensions (e.g. for python -> py)
        @throw: KeyError if the language is not yet supported
        """

        try:
            return supported_langs[language]["extension"]
        except KeyError as err:
            logging.debug(f"{language} not found in supported extensions")
            raise err

    @staticmethod
    def provide_code_execution_command(in_file_path: str, language: str, compiled_file_path: str) -> str:
        """
        Function which provides the bash command which needs to be run in order
        to execute the code

        @param in_file_path: path to the file where the command should be run
        @param language: the language in which the file should be compiled/interpreted
        @param compiled_file_path: path where temporary compiled files will be kept

        @return: the command which just needs to be run in order to get the output of the code
        @throw: KeyError if the language is not supported
        """

        try:
            logging.info(f"Started creating code exec command for {language}, and file: {in_file_path}")
            if language == "python":
                return f'{supported_langs[language]["cmd"]} {in_file_path}'
            elif language == "cpp":
                return (f"{supported_langs[language]['cmd']} -o {compiled_file_path} {in_file_path}"
                        f" && ./{'/'.join(compiled_file_path.split('/')[2:])}")
            else:
                raise KeyError("Language key not found")
        except KeyError as err:
            logging.debug(
                f"Language: {language} not found when creating execution command"
            )
            raise err

    @staticmethod
    def execute_code(command: str,
                     in_file_path: str,
                     compiled_file_path: str,
                     code: str,
                     timeout:
                     float = 10) -> None:
        """
        Function which execudes the given command and outputs the result in the given out_file_path

        @param command: command to be executed
        @param in_file_path: path to the in file where the code is stored
        @param compiled_file_path: path to the file where the obj file is generated for compiled languages
        @param timeout: maximum amount of time the process is allowed to run

        @cde: code to be executed

        @return code execution output

        @raise: FileNotFoundError if the command does not exist
        @raise: IOError if the output file cannot be created
        @raise: CalledProcessError if the command fails to be executed
        """

        proc_ref = None

        try:

            with open(in_file_path, "w+") as in_file_desc:
                in_file_desc.write(code)
                in_file_desc.flush()

                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                proc_ref = process

                out, err = process.communicate(timeout=timeout)
                out, err = out.decode('utf-8'), err.decode('utf-8')

                rc = process.wait()

                logging.info(f"Command: {command}")
                logging.info(f"Out: {out}")
                logging.info(f"Err: {err}")
                logging.info(f"RetCode: {rc}")

                if err or rc != 0:
                    raise subprocess.CalledProcessError(rc, command, err)

                return out

        except IOError as ioe:
            logging.error(
                f"Unable to create file at: {in_file_path}"
            )
            raise ioe
        except FileNotFoundError as fnf:
            logging.error(
                f"Command not found: {command}"
            )
            raise fnf
        except subprocess.CalledProcessError as cpe:
            logging.error(
                f"Process exited with error: {cpe.output}"
            )
            raise cpe
        except subprocess.TimeoutExpired as te:
            logging.error(
                f"Process timed out: {te.timeout}"
            )
            if proc_ref:
                proc_ref.kill()
            raise te
        finally:
            CodeExcution.__clear_resources(in_file_path, compiled_file_path)

    @staticmethod
    def __clear_resources(*args) -> None:
        """
        Function for deleting resources after code execution
        """

        logging.info("Start removing execution resources...")
        for arg in args:
            try:
                logging.info(f"Removing: {arg}")
                os.remove(arg)
                logging.info(f"Success removing: {arg}")
            except OSError:
                pass
