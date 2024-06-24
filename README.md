# Sistema Experto - Diagnóstico de Hardware

## Descripción General

Este proyecto implementa un sistema experto para el diagnóstico de problemas de hardware en una computadora. Utiliza una interfaz gráfica de usuario (GUI) construida con Tkinter en Python para interactuar con el usuario y proporcionar diagnósticos basados en respuestas a una serie de preguntas.

## Estructura del Proyecto

El proyecto está organizado en varios archivos para mantener el código limpio y manejable:

- `main.py`: Punto de entrada principal para iniciar la aplicación.
- `diagnostico_app.py`: Contiene la clase `DiagnosticoApp`, que maneja la lógica principal y la interfaz gráfica.
- `preguntas.py`: Contiene la lista de preguntas e imágenes asociadas.
- `tratamientos.py`: Contiene los tratamientos organizados en categorías.
- `interfaz.py`: Contiene las funciones relacionadas con la interfaz gráfica.

## Conocimiento

El conocimiento en este sistema experto se organiza en forma de reglas de diagnóstico y tratamientos para diferentes problemas de hardware. Estas reglas están categorizadas en cinco áreas principales:

1. **Problemas de Display**
2. **Problemas de Capacitores**
3. **Problemas de Disco**
4. **Problemas de Fuente**
5. **Problemas de Motherboard**

### Ejemplo de Tratamientos

```python
tratamientos = {
    "display": {
        "display_negro": "Apaga el monitor y vuelve a encenderlo. Si el problema persiste, puede ser un fallo de la tarjeta gráfica o del monitor.",
        "display_lineas": "Revisa la conexión del cable de video. Si está bien conectado, puede ser necesario actualizar los controladores de la tarjeta gráfica o que la tarjeta esté dañada.",
        "display_no_signal": "Verifica que el monitor esté bien conectado a la computadora. Si el problema persiste, prueba con otro cable o monitor.",
        "display_parpadea": "Ajusta la frecuencia de actualización del monitor en la configuración de pantalla. Si el problema continúa, puede ser necesario reemplazar el monitor.",
        "default": "No hay problemas con el display."
    },
    "capacitores": {
        "capacitores_chasquidos": "Revisa los capacitores de la fuente de alimentación. Si están dañados, reemplázalos.",
        "capacitores_hinchados": "Reemplaza los capacitores hinchados en la placa madre o la fuente de alimentación.",
        "capacitores_olor": "Desconecta la computadora y revisa los capacitores. Si huelen a quemado, reemplázalos inmediatamente.",
        "default": "No hay problemas con los capacitores."
    },
    // Otros tratamientos...
}
```
## Preguntas

Las preguntas están diseñadas para identificar síntomas específicos de problemas de hardware. Cada pregunta está asociada con una imagen que ayuda a ilustrar el problema al usuario.

Ejemplo de Preguntas

```python
preguntas = [
    ("¿El monitor está negro?", "display_negro.jpg"),
    ("¿El monitor tiene líneas?", "display_lineas.jpg"),
    ("¿El monitor no tiene señal?", "display_no_signal.jpg"),
    ("¿El monitor parpadea?", "display_parpadea.jpg"),
    // Otras preguntas...
]
```
## Motor de Inferencia
El motor de inferencia utiliza las respuestas del usuario para determinar los posibles problemas de hardware y proporcionar los tratamientos correspondientes. El proceso es el siguiente:

Mostrar Pregunta: El sistema muestra una pregunta y una imagen asociada.
Recibir Respuesta: El usuario responde "Sí" o "No".
Actualizar Diagnóstico: Basado en las respuestas, el sistema actualiza el diagnóstico.
Mostrar Resultados: Al final de las preguntas, el sistema muestra un diagnóstico final que incluye los tratamientos para los problemas identificados y mensajes por defecto para las categorías sin problemas.

```python
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

```
## Instalación y Ejecución
Es recomendable hacer un entorno virtual para el uso de la dependecia pillow
1. Python 3.11 
2. Tkinter 
3. Pillow (PIL)

## Ejecución del Sistema
Para ejecutar el sistema, simplemente corre el archivo main.py:
