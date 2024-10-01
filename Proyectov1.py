import tkinter as tk
from tkinter import messagebox


def calcular_divisores(n):
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    return divisores


def validar_y_calcular():
    try:

        entrada = entry_numero.get()

        if not entrada.isdigit():
            raise ValueError("Valor no valido.")

        numero = int(entrada)


        if numero <= 0:
            raise ValueError("Valor no valido.")

        divisores = calcular_divisores(numero)
        resultado.set(f"Los divisores de {numero} son: {divisores}")

    except ValueError as e:

        messagebox.showerror("Entrada inválida", f"Error: {e}")
        entry_numero.delete(0, tk.END)



ventana = tk.Tk()
ventana.title("Calculadora de Divisores")
ventana.geometry("400x200")


resultado = tk.StringVar()


label_instruccion = tk.Label(ventana, text="Ingrese un número natural:")
label_instruccion.pack(pady=10)

entry_numero = tk.Entry(ventana)
entry_numero.pack(pady=5)


boton_calcular = tk.Button(ventana, text="Calcular Divisores", command=validar_y_calcular)
boton_calcular.pack(pady=10)


label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack(pady=10)

ventana.mainloop()
