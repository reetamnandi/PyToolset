from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages': packages,
    },

}

setup(
    name="PyToolset",
    options=options,
    version="0.1.0",
    description='CLI Toolset with good to have tools',
    executables=executables
)
