import tkinter as tk
import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="Crissp657",
    password="@Golgo1415",
    database="personal"
)

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Empleados")

# Crear etiquetas y campos de entrada para nombre, apellido, fecha de nacimiento y dirección
nombre_label = tk.Label(root, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(root)
nombre_entry.pack()

apellido_label = tk.Label(root, text="Apellido:")
apellido_label.pack()
apellido_entry = tk.Entry(root)
apellido_entry.pack()

fecha_label = tk.Label(root, text="Fecha de Nacimiento (YYYY-MM-DD):")
fecha_label.pack()
fecha_entry = tk.Entry(root)
fecha_entry.pack()

Dirección_label = tk.Label(root, text="Dirección:")
Dirección_label.pack()
Dirección_entry = tk.Entry(root)
Dirección_entry.pack()

# Función para guardar los datos ingresados
def guardar_datos():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    fecha_nacimiento = fecha_entry.get()
    Dirección = Dirección_entry.get()
    
    cursor = conexion.cursor()
    consulta_insercion = "INSERT INTO empleados (nombre, apellido, fecha_nacimiento, Dirección) VALUES (%s, %s, %s, %s)"
    nuevo_empleado = (nombre, apellido, fecha_nacimiento, Dirección)
    cursor.execute(consulta_insercion, nuevo_empleado)
    conexion.commit()  # Confirmar la inserción
    cursor.close()

# Botón para guardar los datos
guardar_button = tk.Button(root, text="Guardar", command=guardar_datos)
guardar_button.pack()

# Ejecutar la ventana
root.mainloop()

# Cerrar la conexión a la base de datos
conexion.close()