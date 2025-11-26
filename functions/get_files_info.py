import os

def get_files_info(working_directory, directory="."):
    abs_working_path = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, directory))
    if os.path.commonprefix([abs_working_path, abs_path]) != abs_working_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    contents = os.listdir(abs_path)
    stringified_contents = list()
    for item in contents:
        try:
            item_path = os.path.join(abs_path, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
        except Exception as e:
            return str(e)
        stringified_contents.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')
    return '\n'.join(stringified_contents)