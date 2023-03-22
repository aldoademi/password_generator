import random
import tkinter as tk

def generate_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "[]{}()*;/,._-"

    all = lower + upper + numbers + symbols
    length = 16
    password = "".join(random.sample(all, length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Crea la finestra principale
root = tk.Tk()
root.title("Generatore di password")
root.geometry("350x150")

# Crea un frame per i controlli
frame = tk.Frame(root)
frame.pack(pady=20)

# Crea un campo di testo per la password
password_entry = tk.Entry(frame, width=30)
password_entry.pack(padx=10, pady=10)

# Crea un bottone per generare la password
generate_button = tk.Button(frame, text="Genera password", command=generate_password)
generate_button.pack(padx=10, pady=10)

# Crea un'etichetta per le istruzioni
instructions_label = tk.Label(root, text="Clicca sul bottone per generare una password sicura!")
instructions_label.pack(pady=10)

# Avvia il loop della finestra
root.mainloop()
