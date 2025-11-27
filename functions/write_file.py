import os

def write_file(working_directory, file_path, content):
    abs_working_path = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    if os.path.commonprefix([abs_working_path, abs_path]) != abs_working_path:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    try:
        with open(abs_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'