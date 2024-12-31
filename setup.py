from cx_Freeze import setup, Executable

executables = [
    Executable(
        'main.py', # Archivo a compilar
        base="Win32GUI", # Oculta la consola al ejecutarlo
        target_name="ColorPicker.exe" # Nombre que va a tener el ejecutable
    )
]


options = {
    "build_exe": {
        "packages": ["tkinter", "pynput", "threading", "PIL"],
    }
}


setup(
    name="ColorPicker",
    version="1.0",
    description="Una interfaz grafica sencilla que permite obtener los valores rgb y hex de cualquier pixel que el usuario desee solo haciendo click",
    options=options,
    executables=executables
)
