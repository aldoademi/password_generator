import secrets
import string
import tkinter as tk

def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(16))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)

# Crea la finestra principale
root = tk.Tk()
root.title("Generatore di password")
root.geometry("350x200")

# Crea un frame per i controlli
frame = tk.Frame(root)
frame.pack(pady=20)

# Crea un campo di testo per la password
password_entry = tk.Entry(frame, width=30)
password_entry.pack(padx=10, pady=10)

# Crea un bottone per generare la password
generate_button = tk.Button(frame, text="Genera password", command=generate_password)
generate_button.pack(padx=10, pady=10)

# Crea un bottone per copiare la password
copy_button = tk.Button(frame, text="Copia password", command=copy_password)
copy_button.pack(padx=10, pady=10)

# Avvia il loop della finestra
root.mainloop()
