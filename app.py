from tkinter import Tk, Label, Button, messagebox, simpledialog
from PIL import Image, ImageTk

root = Tk()
root.title("Ventana de Inicio")
root.geometry("500x500")

imagen_fondo = Image.open("static/background.png")
imagen_fondo = imagen_fondo.resize((500, 500), Image.LANCZOS)
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

label_fondo = Label(root, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

label_titulo = Label(root, text="Gestor de tareas", font=("Arial", 24), fg="#E6E6FA", bg="#6A5ACD")
label_titulo.pack(fill='x', pady=20)

tareas = []

def agregar_tarea():
    tarea = simpledialog.askstring("Agregar Tarea", "Introduce la tarea:")
    if tarea:
        tareas.append(tarea)
        messagebox.showinfo("Éxito", f"Tarea '{tarea}' añadida.")

def ver_tareas():
    if tareas:
        tareas_lista = "\n".join(tareas)
        messagebox.showinfo("Lista de Tareas", tareas_lista)
    else:
        messagebox.showinfo("Lista de Tareas", "No hay tareas en la lista.")

def eliminar_tarea():
    tarea = simpledialog.askstring("Eliminar Tarea", "Introduce la tarea a eliminar:")
    if tarea in tareas:
        tareas.remove(tarea)
        messagebox.showinfo("Éxito", f"Tarea '{tarea}' eliminada.")
    else:
        messagebox.showerror("Error", f"Tarea '{tarea}' no encontrada.")

def marcar_completada():
    tarea = simpledialog.askstring("Marcar como Completada", "Introduce la tarea a marcar como completada:")
    if tarea in tareas:
        index = tareas.index(tarea)
        tareas[index] = f"{tarea} (completada)"
        messagebox.showinfo("Éxito", f"Tarea '{tarea}' marcada como completada.")
    else:
        messagebox.showerror("Error", f"Tarea '{tarea}' no encontrada.")

def salir():
    root.quit()

btn_agregar = Button(root, text="Agregar Tarea", 
                      width=20, 
                      height=1, 
                      font=("Arial", 12, "bold"), 
                      bg="#4B0082", 
                      fg="white",
                      command=agregar_tarea)
btn_agregar.pack(pady=20)

btn_ver_tareas = Button(root, text="Ver Tareas", 
                      width=20, 
                      height=1, 
                      font=("Arial", 12, "bold"), 
                      bg="#4B0082", 
                      fg="white",
                      command=ver_tareas)
btn_ver_tareas.pack(pady=20)

btn_eliminar = Button(root, text="Eliminar Tarea", 
                      width=20, 
                      height=1, 
                      font=("Arial", 12, "bold"), 
                      bg="#4B0082", 
                      fg="white",
                      command=eliminar_tarea)
btn_eliminar.pack(pady=20)

btn_completar = Button(root, text="Marcar como Completada", 
                      width=20, 
                      height=1, 
                      font=("Arial", 12, "bold"), 
                      bg="#4B0082", 
                      fg="white",
                      command=marcar_completada)
btn_completar.pack(pady=20)

btn_salir = Button(root, text="Salir", 
                      width=20, 
                      height=1, 
                      font=("Arial", 12, "bold"), 
                      bg="#4B0082", 
                      fg="white",
                      command=salir)
btn_salir.pack(pady=20)

root.mainloop()
