

import tkinter as tk


def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "amigo"
    lbl.config(text=f"Hola {nombre}!")


root = tk.Tk()
root.title("saludador") 
root.geometry("300x200")




#crear etiquetas 
#lbl = tk.Label(root, text="escribe tu nombre y picale al boton.") imprime un texto en la ventana, en este caso "escribe tu nombre y picale al boton."
lbl = tk.Label(root, text="escribe tu nombre y picale al boton.")
lbl.pack(pady=10)
#entrada de texto
entrada = tk.Entry(root)
entrada.pack(pady=1)
#crear boton
btn = tk.Button(root, text="saludar",command = saludar) #cuando se le de click al boton, se ejecutara la funcion saludar
btn.pack(pady=10)




root.mainloop()