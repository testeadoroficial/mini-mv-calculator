import tkinter as tk

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

        # Etiqueta para mostrar el resultado
        self.label_resultado = tk.Label(self.root, text="")
        self.label_resultado.grid(row=7, column=0, columnspan=2)

        self.root.mainloop()

    def calcular_mv(self):
        try:
            eg = float(self.entry_eg.get())
            pse = float(self.entry_pse.get())
            cv = float(self.entry_cv.get())
            ev = float(self.entry_ev.get())
            pv = float(self.entry_pv.get())
            psr = float(self.entry_psr.get())

            margen_variable = MargenVariable(eg, pse, cv, ev, pv, psr).calcular_margen_variable()
            self.label_resultado.config(text=f"Margen Variable: {margen_variable:.2f}")

        except ValueError:
            self.label_resultado.config(text="Por favor, ingrese valores numéricos válidos.")

# Ejecutar la interfaz gráfica
if __name__ == "__main__":
    Interfaz()
