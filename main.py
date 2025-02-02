import tkinter as tk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Clase para gestionar el Margen Variable
class MargenVariable:
    def __init__(self, eg, pse, cv, ev, pv, psr):
        self.eg = eg
        self.pse = pse
        self.cv = cv
        self.ev = ev
        self.pv = pv
        self.psr = psr

    def calcular_margen_variable(self):
        margen_operativo = self.eg * (self.pse - self.cv)
        margen_comercial = self.ev * (self.pv - self.psr)
        return margen_operativo + margen_comercial

# Clase para la interfaz gráfica
class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de Margen Variable")

        # Campos de entrada de datos
        self.label_eg = tk.Label(self.root, text="Energía Generada (MWh):")
        self.label_eg.grid(row=0, column=0)
        self.entry_eg = tk.Entry(self.root)
        self.entry_eg.grid(row=0, column=1)

        self.label_pse = tk.Label(self.root, text="Precio Spot Entrega ($/MWh):")
        self.label_pse.grid(row=1, column=0)
        self.entry_pse = tk.Entry(self.root)
        self.entry_pse.grid(row=1, column=1)

        self.label_cv = tk.Label(self.root, text="Costo Variable ($/MWh):")
        self.label_cv.grid(row=2, column=0)
        self.entry_cv = tk.Entry(self.root)
        self.entry_cv.grid(row=2, column=1)

        self.label_ev = tk.Label(self.root, text="Energía Vendida (MWh):")
        self.label_ev.grid(row=3, column=0)
        self.entry_ev = tk.Entry(self.root)
        self.entry_ev.grid(row=3, column=1)

        self.label_pv = tk.Label(self.root, text="Precio de Venta ($/MWh):")
        self.label_pv.grid(row=4, column=0)
        self.entry_pv = tk.Entry(self.root)
        self.entry_pv.grid(row=4, column=1)

        self.label_psr = tk.Label(self.root, text="Precio Spot Retiro ($/MWh):")
        self.label_psr.grid(row=5, column=0)
        self.entry_psr = tk.Entry(self.root)
        self.entry_psr.grid(row=5, column=1)

        # Botón "Calcular"
        self.button_calcular = tk.Button(self.root, text="Calcular", command=self.calcular_mv)
        self.button_calcular.grid(row=6, column=0, columnspan=2)

        # Botón "Limpiar"
        self.button_limpiar = tk.Button(self.root, text="Limpiar", command=self.limpiar_campos)
        self.button_limpiar.grid(row=7, column=0, columnspan=2)

        # Botón "Guardar Escenario"
        self.button_guardar = tk.Button(self.root, text="Guardar Escenario", command=self.guardar_escenario)
        self.button_guardar.grid(row=8, column=0, columnspan=2)

        # Botón "Cargar Escenario"
        self.button_cargar = tk.Button(self.root, text="Cargar Escenario", command=self.cargar_escenario)
        self.button_cargar.grid(row=9, column=0, columnspan=2)

        # Botón "Analizar Sensibilidad"
        self.button_sensibilidad = tk.Button(self.root, text="Analizar Sensibilidad", command=self.analizar_sensibilidad)
        self.button_sensibilidad.grid(row=10, column=0, columnspan=2)

        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(self.root, text="")
        self.label_resultado.grid(row=11, column=0, columnspan=2)

        # Área para el gráfico
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=12, column=0, columnspan=2)

        self.root.mainloop()

    def calcular_mv(self):
        try:
            eg = float(self.entry_eg.get())
            pse = float(self.entry_pse.get())
            cv = float(self.entry_cv.get())
            ev = float(self.entry_ev.get())
            pv = float(self.entry_pv.get())
            psr = float(self.entry_psr.get())

            # Validaciones adicionales:
            if eg <= 0 or pse <= 0 or cv <= 0 or ev <= 0 or pv <= 0 or psr <= 0:
                messagebox.showerror("Error", "Por favor, ingrese valores numéricos positivos.")
                return

            margen_variable = MargenVariable(eg, pse, cv, ev, pv, psr).calcular_margen_variable()
            self.label_resultado.config(text=f"Margen Variable: {margen_variable:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def limpiar_campos(self):
        self.entry_eg.delete(0, tk.END)
        self.entry_pse.delete(0, tk.END)
        self.entry_cv.delete(0, tk.END)
        self.entry_ev.delete(0, tk.END)
        self.entry_pv.delete(0, tk.END)
        self.entry_psr.delete(0, tk.END)
        self.label_resultado.config(text="")
        self.ax.clear()
        self.canvas.draw()

    def guardar_escenario(self):
        try:
            eg = float(self.entry_eg.get())
            pse = float(self.entry_pse.get())
            cv = float(self.entry_cv.get())
            ev = float(self.entry_ev.get())
            pv = float(self.entry_pv.get())
            psr = float(self.entry_psr.get())

            escenario = {
                "eg": eg,
                "pse": pse,
                "cv": cv,
                "ev": ev,
                "pv": pv,
                "psr": psr
            }

            with open("escenario.json", "w") as archivo:
                json.dump(escenario, archivo)

            messagebox.showinfo("Guardado", "Escenario guardado correctamente.")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def cargar_escenario(self):
        try:
            with open("escenario.json", "r") as archivo:
                escenario = json.load(archivo)

            self.entry_eg.delete(0, tk.END)
            self.entry_eg.insert(0, str(escenario["eg"]))

            self.entry_pse.delete(0, tk.END)
            self.entry_pse.insert(0, str(escenario["pse"]))

            self.entry_cv.delete(0, tk.END)
            self.entry_cv.insert(0, str(escenario["cv"]))

            self.entry_ev.delete(0, tk.END)
            self.entry_ev.insert(0, str(escenario["ev"]))

            self.entry_pv.delete(0, tk.END)
            self.entry_pv.insert(0, str(escenario["pv"]))

            self.entry_psr.delete(0, tk.END)
            self.entry_psr.insert(0, str(escenario["psr"]))

            messagebox.showinfo("Cargado", "Escenario cargado correctamente.")

        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de escenario.")

    def analizar_sensibilidad(self):
        try:
            eg = float(self.entry_eg.get())
            pse = float(self.entry_pse.get())
            cv = float(self.entry_cv.get())
            ev = float(self.entry_ev.get())
            pv = float(self.entry_pv.get())
            psr = float(self.entry_psr.get())

            # Validaciones adicionales:
            if eg <= 0 or pse <= 0 or cv <= 0 or ev <= 0 or pv <= 0 or psr <= 0:
                messagebox.showerror("Error", "Por favor, ingrese valores numéricos positivos.")
                return

            # Rango de valores para el análisis de sensibilidad
            rango_pse = range(40, 61, 5)

            # Calcular el margen variable para cada valor de PSe
            mvs = []
            for pse_valor in rango_pse:
                mv = MargenVariable(eg, pse_valor, cv, ev, pv, psr).calcular_margen_variable()
                mvs.append(mv)

            # Graficar los resultados
            self.ax.clear()
            self.ax.plot(rango_pse, mvs)
            self.ax.set_xlabel("Precio Spot Entrega ($/MWh)")
            self.ax.set_ylabel("Margen Variable")
            self.ax.set_title("Análisis de Sensibilidad")
            self.canvas.draw()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Ejecutar la interfaz gráfica
if __name__ == "__main__":
    Interfaz()
