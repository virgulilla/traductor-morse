import tkinter as tk
from src.entities import Morse

def text_to_morse(origin, destination):
    text = origin.get("1.0", "end-1c")
    morse = Morse()
    result = morse.text_to_morse(text)
    destination.delete("1.0", "end")
    destination.insert("1.0", result)

def morse_to_text(origin, destination):
    text = origin.get("1.0", "end-1c")
    morse = Morse()
    result = morse.morse_to_text(text)
    destination.delete("1.0", "end")
    destination.insert("1.0", result)

def add_to_morse(widget, content):
    widget.insert("end", content)

def filter_morse_input(event, widget):
    allowed_characters = ".- "
    content = widget.get("1.0", "end-1c")
    filtered_content = "".join([char for char in content.upper() if char in allowed_characters])
    widget.delete("1.0", "end") 
    widget.insert("1.0", filtered_content)

def filter_plain_input(event, widget):
    allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    content = widget.get("1.0", "end-1c")
    filtered_content = "".join([char for char in content.upper() if char in allowed_characters])
    widget.delete("1.0", "end") 
    widget.insert("1.0", filtered_content)

def menu():
    root = tk.Tk()
    root.title("Traductor Morse")
    root.geometry("800x600")
    root.configure(bg="lightgray")

    # Frame principal que contiene los textos y las flechas
    main_frame = tk.Frame(root, bg="lightgray")
    main_frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Título principal
    label_title = tk.Label(main_frame, text="TRADUCTOR MORSE", bg="lightgray", font=("Arial", 14))
    label_title.pack(side=tk.TOP, pady=10, anchor="w", padx=10)

    # Contenedor para los tres bloques principales (Morse, Flechas, Plano)
    content_frame = tk.Frame(main_frame, bg="lightgray")
    content_frame.pack(expand=True, fill="both")

    # Configurar un grid para distribuir el espacio horizontalmente
    content_frame.grid_columnconfigure(0, weight=1)  # Frame Morse
    content_frame.grid_columnconfigure(1, weight=0)  # Frame Flechas
    content_frame.grid_columnconfigure(2, weight=1)  # Frame Plano
    content_frame.grid_rowconfigure(0, weight=1)

    # Frame para Morse
    frame_morse = tk.Frame(content_frame, bg="lightgray")
    frame_morse.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Etiqueta "MORSE"
    label_morse = tk.Label(frame_morse, text="MORSE", bg="lightgray", font=("Arial", 14))
    label_morse.pack(side="top", pady=10, anchor="w", padx=5)

    # Área de texto para Morse
    text_morse = tk.Text(frame_morse, wrap="word", font=("Arial", 14), bd=1, relief="solid", height=15)
    text_morse.pack(side="top", expand=True, fill="both", padx=10)
    text_morse.bind("<KeyRelease>",  lambda event: filter_morse_input(event, text_morse))

    # Frame para los botones debajo del área de texto Morse
    frame_buttons = tk.Frame(frame_morse, bg="lightgray")
    frame_buttons.pack(side="top", fill="x", padx=10, pady=(0, 10))

    # Botones para Morse
    button_punto = tk.Button(frame_buttons, text="•", font=("Arial", 14), bd=1, relief="solid", width=5, 
                             height=2, command=lambda: add_to_morse(text_morse, "."))
    button_punto.pack(side="left", expand=True, fill="both")
    button_raya = tk.Button(frame_buttons, text="–", font=("Arial", 14), bd=1, relief="solid", width=5, 
                            height=2, command=lambda: add_to_morse(text_morse, "-"))
    button_raya.pack(side="left", expand=True, fill="both")
    button_pausa = tk.Button(frame_buttons, text="pausa", font=("Arial", 14), bd=1, relief="solid", width=5, 
                             height=2, command=lambda: add_to_morse(text_morse, " "))
    button_pausa.pack(side="left", expand=True, fill="both")

    # Frame para las flechas de conversión
    frame_nav = tk.Frame(content_frame, bg="lightgray")
    frame_nav.grid(row=0, column=1, sticky="ns", padx=10, pady=10)

    # Botones de flechas
    button_left = tk.Button(frame_nav, text="←", font=("Arial", 14), width=5, height=2,
                             command=lambda: text_to_morse(text_plain, text_morse))
    button_left.pack(side="top", pady=(100, 5))
    button_right = tk.Button(frame_nav, text="→", font=("Arial", 14), width=5, height=2,
                             command=lambda: morse_to_text(text_morse, text_plain))
    button_right.pack(side="top", pady=5)

    # Frame para Plano
    frame_plain = tk.Frame(content_frame, bg="lightgray")
    frame_plain.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

    # Etiqueta "PLANO"
    label_plain = tk.Label(frame_plain, text="PLANO", bg="lightgray", font=("Arial", 14))
    label_plain.pack(side="top", pady=10, anchor="w", padx=5)

    # Área de texto para Plano
    text_plain = tk.Text(frame_plain, wrap="word", font=("Arial", 14), bd=1, relief="solid", height=15)
    text_plain.pack(side="top", expand=True, fill="both", padx=10, pady=(0, 10))
    text_plain.bind("<KeyRelease>",  lambda event: filter_plain_input(event, text_plain))


    # Ejecutar la aplicación
    root.mainloop()