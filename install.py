import subprocess as sb
import pathlib as pl
from importlib.util import find_spec

# Check if Pyinstaller is installed

print("The installer script does not currently work due to pathlib's incompatibility with PyInstaller. This will be fixed in a future release")
exit()

if find_spec("PyInstaller") == None:
    raise ImportError("PyInstaller is not installed on your system, which is needed to compile this program")

# If PyInstaller is installed, we go on to compile the program
target = f"{pl.Path(__file__).parent}/src/main.py"

sb.run(["pyinstaller", "-n", "QuickPort", target])