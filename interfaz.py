import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
from tratamientos import tratamientos

def crear_interfaz(root, iniciar_consulta):
    label = tk.Label(root, text="Diagnóstico de Hardware", font=("Arial", 18))
    label.pack(pady=10)
    
    iniciar_btn = tk.Button(root, text="Iniciar consulta", command=iniciar_consulta, name="iniciar_btn")
    iniciar_btn.pack(pady=20)

    root.state('zoomed')  # Maximiza la ventana principal

def mostrar_pregunta(app, index):
    if index < len(app.preguntas):
        pregunta, img_path = app.preguntas[index]
        
        app.pregunta_label = tk.Label(app.root, text=pregunta, font=("Arial", 14))
        app.pregunta_label.pack(pady=10)
        
        img = Image.open(f"./imagenes/{img_path}")
        img = img.resize((400, 400), Image.Resampling.LANCZOS)
        app.img = ImageTk.PhotoImage(img)
        
        app.img_label = tk.Label(app.root, image=app.img)
        app.img_label.pack(pady=10)
        
        button_frame = tk.Frame(app.root)
        button_frame.pack(pady=20)
        
        app.si_btn = tk.Button(button_frame, text="Sí", command=lambda: app.responder(index, "si"))
        app.no_btn = tk.Button(button_frame, text="No", command=lambda: app.responder(index, "no"))
        app.si_btn.pack(side=tk.LEFT, padx=10)
        app.no_btn.pack(side=tk.LEFT, padx=10)

        app.root.state('zoomed')  # Maximiza la ventana de preguntas
    else:
        app.mostrar_diagnostico()

def mostrar_diagnostico(app):
    diagnosticos = {categoria: [] for categoria in tratamientos.keys()}
    for i, respuesta in enumerate(app.respuestas):
        if respuesta == "si":
            key = app.preguntas[i][1].replace(".jpg", "")
            for categoria, tratamientos_categoria in tratamientos.items():
                if key in tratamientos_categoria:
                    diagnosticos[categoria].append(tratamientos_categoria[key])
    
    diagnostico_final = ""
    for categoria, lista_diagnosticos in diagnosticos.items():
        if lista_diagnosticos:
            diagnostico_final += "\n".join(lista_diagnosticos) + "\n"
        else:
            diagnostico_final += tratamientos[categoria]["default"] + "\n"
    
    result_window = Toplevel(app.root)
    result_window.title("Diagnóstico Final")
    result_window.state('zoomed')
    
    result_label = tk.Label(result_window, text=f"Diagnóstico:\n{diagnostico_final}", font=("Arial", 12), wraplength=1000, justify="left")
    result_label.pack(pady=20)
    
    cerrar_btn = tk.Button(result_window, text="Cerrar", command=app.root.quit)
    cerrar_btn.pack(pady=20)
