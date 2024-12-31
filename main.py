from pynput import mouse
import tkinter as tk
import threading
from PIL import ImageGrab

mouse_controler = mouse.Controller()

def getColor(position: tuple) -> tuple:
    image = ImageGrab.grab(bbox=(position[0], position[1], position[0] + 1, position[1] + 1))
    color = image.getpixel((0, 0))
    return (color)


def update_ui(color: tuple):
    color_hex = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
    colorView.config(bg=color_hex)
    
    rgbEntry.config(state='normal')
    rgbEntry.delete(0, tk.END)
    rgbEntry.insert(0, f"RGB: {color}")
    rgbEntry.config(state='readonly')
    
    hexEntry.config(state='normal')
    hexEntry.delete(0, tk.END)
    hexEntry.insert(0, f"HEX: {color_hex}")
    hexEntry.config(state='readonly')



def on_click(x, y, button, pressed):
    if (pressed):
        if (button == mouse.Button.left):
            update_ui(getColor((x, y)))
     
    return (False)


def listenClick():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()


def start_listener():
    threading.Thread(target=listenClick, daemon=True).start()


def close_window():
    screen.destroy()
    

def click_header(event):
    global diff_x, diff_y
    
    separate = screen.geometry().split('+')
    actual_position = (int(separate[1]), int(separate[2]))
    del separate
    
    diff_x = (event.x_root - actual_position[0])
    diff_y = (event.y_root - actual_position[1])
    

def drag_window(event):
    new_x_position = event.x_root - (diff_x)
    new_y_position = event.y_root - (diff_y)

    screen.geometry(f"+{new_x_position}+{new_y_position}")



screen = tk.Tk("ColorPicker")   
screen.title("Color Picker")
screen.geometry("200x300+200+200")
screen.resizable(False, False)
screen.configure(bg="#23272e")
screen.overrideredirect(True) # Se oculta la barra del titulo

header = tk.Frame(screen, width=250, height=30, bg="#23272e")
header.pack(side=tk.TOP, fill=tk.X)


button_close = tk.Button(header, text="x", bg="#e06c75", fg="#000000", command=close_window, font=("Arial", 10), borderwidth=1, width=2)
button_close.pack(side=tk.RIGHT)

buttonPicker = tk.Button(screen, text="Pick Color", command=start_listener)
buttonPicker.config(font=("Arial", 12), bg="#7289da", fg="#FFFFFF", borderwidth=1, relief='solid')
buttonPicker.pack(pady=10)

# Cuadrado con el color seleccionado 
colorView = tk.Frame(screen, width=100, height=100, bg="#FFFFFF")
colorView.config(borderwidth=1, relief='solid')
colorView.pack(pady=20)

# Texto donde se muestran los valores del color seleccionado
rgbEntry = tk.Entry(screen, font=("Arial", 10), justify="center", state='normal')
rgbEntry.insert(0, "RGB: (255, 255, 255)")
rgbEntry.pack(pady=10)

hexEntry = tk.Entry(screen, font=("Arial", 10), justify='center', state='normal')
hexEntry.insert(0, "HEX: #FFFFFF")
hexEntry.pack()

# Permitir mover la ventana 
header.bind("<ButtonPress-1>", click_header)
header.bind("<B1-Motion>", drag_window)

screen.attributes("-topmost", True)
screen.mainloop()  