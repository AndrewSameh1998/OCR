from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Final_Project.py", base=base)]

packages = ["idna","opencv-python","numpy"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "First",
    options = options,
    version = "1.0",
    description = '<any description>',
    executables = executables
)