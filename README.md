#   ColorPicker with Python 

##  Descripción 
Creé este proyecto ya que al crear páginas web necesito obtener los valores RGB o HEX de coloresenespecífico, y si bien ya existen varios programas parecidos en internet, mi conexión no es muy buena,porlo cual a veces se traban o no funcionan de manera fluida, cosa que este proyecto soluciona siendorápidoy ligero de ejecutar.
Ofrece una interfaz gráfica fácil de comprender, en la esquina superior derecha hay un botón rojo con una"x", el cual sirve para cerrar la ventana. Si mantiene presionado el click izquierdo en la parte dearriba de la ventana podrá moverla libremente. Más abajo encontrará los elementos principales, un botónceleste que dice "Pick Color" el cual va a permitirle seleccionar un color por una sola vez, si quiereseleccionar nuevamente debe presionarlo de nuevo. Por último tenemos un cuadro que muestra el colorseleccionado y dos textos los cuales muestran el valor RGB y HEX de este, estos últimos pudiendo sercopiados.


## Requisitos 
- Python 3.11
- Bibliotecas Requeridas (detalladas en "reqirements.txt"):
    - cx_Freeze
    - pynput 
    - Tkinter
    - pillow (PIL)
    - threading

>[!IMPORTANT]
>Asegurarse de que las librerias "tkinter" y "threading" están instaladas por defecto, sino instalarlas en el entorno


## Instalación 
>[!NOTE]
>Puedes saltar el paso 2 si es que piensas usar el ejecutable
    Sigue estos pasos si es que quieres tener el proyecto en tu máquina local : 
1. **Clona este repositorio**
```bash
    git clone https://github.com/FedeLupianez/Color-Picker-with-Python.git
    cd color-picker-with-python
```

2. **Activa el entorno virtual**
```bash
./venv/scripts/activate
```


## Uso 
**Si es desde el Código fuente**
```bash
python main.py
```

**Si deseas usar el ejecutable**
>Dirigete a la dirección dentro de la carpeta principal "./build/exe.win-amd64-3.11" 
>Haz doble click sobre el archivo "ColorPicker.exe"


## Compilación 
>[!IMPORTANT]
>Asegurese de que la libreria cx_Freeze esté insatalada y que el entorno virutal está activado

**Ejecute el siguiente comando en la terminal**
```bash
python setup.py build
```
El archivoejecutable se encontrará en la dirección `./build/exe.win-amd64-3.11`
