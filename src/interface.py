import tkinter as tk

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

    # Frame para los botones debajo del área de texto Morse
    frame_buttons = tk.Frame(frame_morse, bg="lightgray")
    frame_buttons.pack(side="top", fill="x", padx=10, pady=(0, 10))

    # Botones para Morse
    button_punto = tk.Button(frame_buttons, text="•", font=("Arial", 14), bd=1, relief="solid", width=5, height=2)
    button_punto.pack(side="left", expand=True, fill="both")
    button_raya = tk.Button(frame_buttons, text="–", font=("Arial", 14), bd=1, relief="solid", width=5, height=2)
    button_raya.pack(side="left", expand=True, fill="both")
    button_pausa = tk.Button(frame_buttons, text="pausa", font=("Arial", 14), bd=1, relief="solid", width=5, height=2)
    button_pausa.pack(side="left", expand=True, fill="both")

    # Frame para las flechas de conversión
    frame_nav = tk.Frame(content_frame, bg="lightgray")
    frame_nav.grid(row=0, column=1, sticky="ns", padx=10, pady=10)

    # Botones de flechas
    button_left = tk.Button(frame_nav, text="←", font=("Arial", 14), width=5, height=2)
    button_left.pack(side="top", pady=(100, 5))
    button_right = tk.Button(frame_nav, text="→", font=("Arial", 14), width=5, height=2)
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


    # Ejecutar la aplicación
    root.mainloop()