.PHONY: environ compile run clean

# Crear el entorno virtual e instalar dependencias
environ:
	python -m venv venv
	./venv/Scripts/pip.exe install -r requirements.txt

# Compilar
compile:
	./venv/Scripts/python.exe setup.py build

# Ejecutar
run:
	./venv/Scripts/python.exe main.py

# Limpiar archivos generados
clean:
	rm -r venv
	rm -r build