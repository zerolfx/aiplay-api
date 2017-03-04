import re
import subprocess

_katex_error_message = '<span class="katex">ERROR</span>'
_katex_empty_message = '<span class="katex"></span>'


def convert(eqn_string):
    """ Takes equation string, e.g. "E = mc^2", and outputs KaTeX HTML """
    import os
    command = ['node', os.path.join(os.path.dirname(__file__), 'katex.port.js'), eqn_string]
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        process.wait(20)
        if process.returncode != 0:
            raise ReferenceError
        return process.stdout.read().decode()
    except ReferenceError:
        return _katex_error_message
