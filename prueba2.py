import tkinter
import sys
from tkinter import ttk


def suma():
    label1 = int(entry1.get())
    label2 = int(entry2.get())
    suma = label1 + label2
    return var.set(suma)

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(3, weight=18)
window.config(background="turquoise")
var = tkinter.StringVar()


#------labels------
label_nombre = tkinter.Label(window, text="Presupuesto Mensual")
label_nombre.config(background="turquoise")
label_nombre.grid(column=1, row= 1)


#------entrys-----
label_entry1 = tkinter.Label(window, text="Alquiler")
label_entry1.grid(column=0, row=2)
label_entry1.configure(background="turquoise")
entry1 = tkinter.Entry(window)
entry1.grid(column=1, row=2)
label_entry2 = tkinter.Label(window, text="Caixa")
label_entry2.grid(column=0, row=3)
label_entry2.configure(background="turquoise")
entry2= tkinter.Entry(window)
entry2.grid(column=1, row=3)


#------Extras---------
label_resultado = tkinter.Entry(window, textvariable=var)
label_resultado.grid(column=3, row=4)
boton_suma = ttk.Button(text="sumar", command= suma)
boton_suma.grid(column=1,row=4)



window.mainloop()
