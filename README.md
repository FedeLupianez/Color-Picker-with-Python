#   ColorPicker with Python 

##  Descripción 
Creé este proyecto ya que al crear páginas web necesito obtener los valores RGB o HEX de colores en específico, y si bien ya existen varios programas parecidos en internet, mi conexión no es muy buena, por lo cual a veces se traban o no funcionan de manera fluida, cosa que este proyecto soluciona siendo fácil de instalar, fácil y rápido de usar y con una interfaz simple de entender.
Dicha interfaz gráfica cuenta con un botón rojo con una"x" en la esquina superior derecha, el cual sirve para cerrar la ventana. Si mantiene presionado el click izquierdo en la parte de arriba de la ventana podrá moverla libremente. Más abajo encontrará los elementos principales, un botón celeste que dice "Pick Color" el cual va a permitirle seleccionar un color por una sola vez, si quiere seleccionar nuevamente debe presionarlo de nuevo. Por último tenemos un cuadro que muestra el color seleccionado y dos textos los cuales muestran el valor RGB y HEX de este, estos últimos pudiendo sercopiados.


## Requisitos 
- Python 3.11
- Bibliotecas Requeridas (detalladas en "reqirements.txt"):
    - cx_Freeze
    - pynput 
    - Tkinter
    - pillow (PIL)
    - threading

>[!IMPORTANT]
>Asegurarse de que las librerias "tkinter" y "threading" están instaladas por defecto, sino instalarlas en el entorno.


## Instalación 
>[!NOTE]
>Puedes saltar los últimos 3 pasos si es que piensas usar el ejecutable incluido en el repositorio.
1. **Clona este repositorio**
```bash
    git clone https://github.com/FedeLupianez/Color-Picker-with-Python.git
    cd color-picker-with-python
```

2. **Crea el entorno virtual**
>[!NOTE]
>Si tiene instalado Make, puede ejecutar el comando `make environ` y saltar el paso 4.
> Por el contario el siguiente comando :
```bash
python -m venv venv
```

3. **Activa el entorno virtual**
```bash
./venv/scripts/activate
```

4. **Instala las dependencias**
```bash
pip install -r requirements.txt
```


## Uso 
**Si es desde el Código fuente**
>[!NOTE]
>Si tiene Make instalado, puede ejecutar el comando `make run`.
> Por el contario ejecute el siguiente comando, asegurandose de que el entorno esté activado :
```bash
python main.py
```

**Si deseas usar el ejecutable**
>Dirigete a la dirección dentro de la carpeta principal `./build/exe.win-amd64-3.11` y 
>Haz doble click sobre el archivo "ColorPicker.exe"


## Compilación 
>[!IMPORTANT]
>Si no está usando Make, asegurese de que la libreria cx_Freeze esté instalada y que el entorno virutal está activado.

>[!NOTE]
>Si tiene instalado Make, puede usar el comando `make compile` y saltear el paso 1.
1. **Ejecute el siguiente comando en la terminal**
```bash
python setup.py build
```

2. **Ejecute el archivo .exe**
El archivo ejecutable se encontrará en la dirección `./build/exe.win-amd64-3.11`
