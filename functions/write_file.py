import os
from google.genai import types

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
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Writes input content to a specified file within the working directory. Overwrites any existing content. Creates a new file if input file does not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the selected file.",
            ),
        },
    ),
)