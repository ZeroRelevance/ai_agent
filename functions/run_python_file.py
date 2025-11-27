import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_path = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    if os.path.commonprefix([abs_working_path, abs_path]) != abs_working_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'
    if file_path[-3:] != '.py':
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(args=["uv", "run", str(abs_path)] + args, timeout=30, capture_output=True, text=True)
        output = str()
        if len(result.stdout) == 0:
            output += 'STDOUT: No output produced.\n'
        else:
            output += 'STDOUT: ' + result.stdout + '\n'
        output += 'STDERR: ' + result.stderr
        if result.returncode != 0:
            output += '\nProcess exited with code ' + str(result.returncode)
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"