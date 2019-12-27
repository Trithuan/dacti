from cx_Freeze import setup, Executable

# setup.py build
setup(
    name = "dacti",
    version = "2",
    description = "dacti",
    executables = [Executable("dactilodance.py")],
)