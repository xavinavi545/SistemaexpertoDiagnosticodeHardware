import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk

def crear_interfaz(root, iniciar_consulta):
    label = tk.Label(root, text="Sistema Experto - Plan Alimenticio", font=("Arial", 18))
    label.pack(pady=10)
    
    iniciar_btn = tk.Button(root, text="Iniciar consulta", command=iniciar_consulta, name="iniciar_btn")
    iniciar_btn.pack(pady=20)

    root.state('zoomed')  # Maximiza la ventana principal

def mostrar_pregunta(app, index):
    if index < len(app.preguntas):
        pregunta, img_path = app.preguntas[index]
        
        app.pregunta_label = tk.Label(app.root, text=pregunta, font=("Arial", 14))
        app.pregunta_label.pack(pady=10)
        
        if img_path:
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
    planes_recomendados = []
    
    if "si" in app.respuestas[2]:
        planes_recomendados.append("esteticos")
    if "si" in app.respuestas[3]:
        planes_recomendados.append("salud")
    if "si" in app.respuestas[4]:
        planes_recomendados.append("musculacion")
    if "si" in app.respuestas[8]:
        planes_recomendados.append("fisioculturismo")
    
    peso_actual_respuesta = app.respuestas[0]
    
    if peso_actual_respuesta == "si":
        categoria = "bajo_peso"
    else:
        peso_ideal = app.respuestas[3] == "si"
        if peso_ideal:
            categoria = "peso_normal"
        else:
            categoria = "sobrepeso"
    
    recomendaciones = []
    for plan in planes_recomendados:
        recomendacion = app.planes.get(plan, {}).get(categoria, app.planes[plan]["default"])
        recomendaciones.append(recomendacion)
    
    resultado_final = "\n\n".join(recomendaciones)
    
    result_window = Toplevel(app.root)
    result_window.title("Plan Alimenticio")
    result_window.state('zoomed')
    
    result_label = tk.Label(result_window, text=f"Recomendación:\n{resultado_final}", font=("Arial", 12), wraplength=1000, justify="left")
    result_label.pack(pady=20)
    
    cerrar_btn = tk.Button(result_window, text="Cerrar", command=app.root.quit)
    cerrar_btn.pack(pady=20)
