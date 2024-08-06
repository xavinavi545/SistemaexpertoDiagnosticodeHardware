from tkinter import Toplevel
from preguntas import preguntas
from tratamientos import tratamientos
from interfaz import crear_interfaz, mostrar_pregunta, mostrar_diagnostico

class DiagnosticoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto - Diagnóstico de Hardware")
        self.root.geometry("600x800")
        
        self.preguntas = preguntas
        self.respuestas = []
        self.tratamientos = tratamientos
        
        self.setup_ui()
    
    def setup_ui(self):
        crear_interfaz(self.root, self.iniciar_consulta)
        
    def iniciar_consulta(self):
        self.root.children['iniciar_btn'].pack_forget()
        self.mostrar_pregunta(0)
    
    def mostrar_pregunta(self, index):
        mostrar_pregunta(self, index)
    
    def responder(self, index, respuesta):
        self.respuestas.append(respuesta)
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.mostrar_pregunta(index + 1)
    
    def mostrar_diagnostico(self):
        mostrar_diagnostico(self)

