import tkinter as tk
from tkinter import messagebox
import time
import random

# Lista de letras para el juego Scrabble
letras_scrabble = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Lista de niveles y cantidad de letras por nivel
niveles = [
    (1, 6),
    (2, 8),
    (3, 10),
    (4, 10),
    (5, 10),
    (6, 10),
    (7, 10),
    (8, 10),
    (9, 16),
    (10, 16)
]

# Función para actualizar la interfaz gráfica con las letras y el tiempo restante
def actualizar_interfaz():
    nivel_actual, cantidad_letras = niveles[nivel - 1]
    letras = ' '.join(random.choices(letras_scrabble, k=cantidad_letras))
    letras_label.config(text=f"Letras disponibles: {letras}")
    tiempo_label.config(text=f"Tiempo restante: {tiempo_maximo} segundos")
    nivel_label.config(text=f"Nivel: {nivel_actual}")
    ventana.update_idletasks()

# Función para notificar el cambio de nivel
def notificar_cambio_nivel():
    nivel_actual, _ = niveles[nivel - 1]
    messagebox.showinfo("Siguiente Nivel", f"Siguiente nivel: {nivel_actual}")

# Función para notificar al ganador
def notificar_ganador():
    ganador = max(usuarios, key=usuarios.get)
    mensaje = f"¡El ganador es {ganador} con {usuarios[ganador]} puntos!"
    messagebox.showinfo("¡Juego Terminado!", mensaje)
    ventana.quit()

# Función para manejar eventos de comentarios de TikTok
async def on_ttcomment(event):
    comentario = event.comment.lower()
    if tiempo_maximo > 0:
        usuario = event.author
        if usuario not in usuarios:
            usuarios[usuario] = 0
        puntos = calcular_puntos_palabra(comentario)
        usuarios[usuario] += puntos

if __name__ == "__main__":
    tiktok_username = input("TIKTOK username: ")
    on_ttcomment = tiktok_client.on("comment")(on_ttcomment)
    print("Conectado a TikTok")

    nivel = 1
    nivel_label = None
    ventana = tk.Tk()
    ventana.title("Scrabble en TikTok")

    letras_label = tk.Label(ventana, text="", font=("Arial", 16))
    letras_label.pack()

    tiempo_maximo = 30

    tiempo_label = tk.Label(ventana, text="", font=("Arial", 16))
    tiempo_label.pack()

    usuarios = {}

    while nivel <= 10:
        actualizar_interfaz()
        notificar_cambio_nivel()
        nivel += 1
        tiempo_maximo = 30

    notificar_ganador()
    ventana.mainloop()
