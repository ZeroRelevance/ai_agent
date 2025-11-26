import os
from config import FILE_CHAR_LIMIT

def get_file_content(working_directory, file_path):
    try:
        abs_working_path = os.path.abspath(working_directory)
        abs_path = os.path.abspath(os.path.join(working_directory, file_path))
        if os.path.commonprefix([abs_working_path, abs_path]) != abs_working_path:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_path):
            return f'Error: "{file_path}" is not a file'
        with open(abs_path, 'r') as f:
            contents = f.read()
        if len(contents) > FILE_CHAR_LIMIT:
            return contents[:FILE_CHAR_LIMIT] + f'[...File "{file_path}" truncated at {FILE_CHAR_LIMIT} characters]'
        return contents
    except Exception as e:
        return 'Error: ' + str(e)