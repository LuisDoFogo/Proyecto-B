#main 

from tkinter import *
from tkinter import messagebox

from mochila import mochila_fraccionaria
from monedas import cambio_monedas


# =========================
# FUNCIÓN MOCHILA
# =========================

def ventana_mochila():
    ventana = Toplevel()
    ventana.title("Mochila Fraccionaria - Greedy")
    ventana.geometry("500x500")

    Label(ventana, text="Pesos (separados por coma)").pack()
    entry_pesos = Entry(ventana, width=50)
    entry_pesos.pack()

    Label(ventana, text="Ganancias (separadas por coma)").pack()
    entry_ganancias = Entry(ventana, width=50)
    entry_ganancias.pack()

    Label(ventana, text="Capacidad máxima").pack()
    entry_capacidad = Entry(ventana, width=20)
    entry_capacidad.pack()

    resultado = Text(ventana, height=12, width=55)
    resultado.pack()

    def calcular():
        try:
            pesos = list(map(float, entry_pesos.get().split(",")))
            ganancias = list(map(float, entry_ganancias.get().split(",")))
            capacidad = float(entry_capacidad.get())

            if len(pesos) != len(ganancias):
                messagebox.showerror("Error", "Pesos y ganancias deben tener misma cantidad")
                return

            objetos = list(zip(pesos, ganancias))

            valor, seleccion = mochila_fraccionaria(objetos, capacidad)

            resultado.delete("1.0", END)
            resultado.insert(END, f"Valor máximo obtenido: {valor}\n\n")
            resultado.insert(END, "Objetos seleccionados:\n")

            for obj in seleccion:
                resultado.insert(
                    END,
                    f"Peso: {obj[0]} | Ganancia: {obj[1]} | Fracción tomada: {obj[2]}\n"
                )

        except:
            messagebox.showerror("Error", "Datos inválidos")

    Button(
        ventana,
        text="Calcular Mochila",
        command=calcular
    ).pack(pady=10)


# =========================
# FUNCIÓN MONEDAS
# =========================

def ventana_monedas():
    ventana = Toplevel()
    ventana.title("Cambio de Monedas - Programación Dinámica")
    ventana.geometry("500x500")

    Label(ventana, text="Denominaciones (separadas por coma)").pack()
    entry_monedas = Entry(ventana, width=50)
    entry_monedas.pack()

    Label(ventana, text="Cantidad objetivo").pack()
    entry_cantidad = Entry(ventana, width=20)
    entry_cantidad.pack()

    resultado = Text(ventana, height=12, width=55)
    resultado.pack()

    def calcular():
        try:
            denominaciones = list(map(int, entry_monedas.get().split(",")))
            cantidad = int(entry_cantidad.get())

            minimo, combinacion = cambio_monedas(denominaciones, cantidad)

            resultado.delete("1.0", END)
            resultado.insert(END, f"Número mínimo de monedas: {minimo}\n\n")
            resultado.insert(END, f"Combinación óptima: {combinacion}")

        except:
            messagebox.showerror("Error", "Datos inválidos")

    Button(
        ventana,
        text="Calcular Cambio",
        command=calcular
    ).pack(pady=10)


# =========================
# MENÚ PRINCIPAL
# =========================

root = Tk()
root.title("Proyecto Final - Análisis de Algoritmos")
root.geometry("500x400")

Label(
    root,
    text="Proyecto Final\nGreedy vs Programación Dinámica",
    font=("Arial", 14)
).pack(pady=30)

Button(
    root,
    text="Mochila Fraccionaria",
    width=25,
    height=2,
    command=ventana_mochila
).pack(pady=15)

Button(
    root,
    text="Cambio de Monedas",
    width=25,
    height=2,
    command=ventana_monedas
).pack(pady=15)

Button(
    root,
    text="Salir",
    width=25,
    height=2,
    command=root.quit
).pack(pady=15)

root.mainloop()