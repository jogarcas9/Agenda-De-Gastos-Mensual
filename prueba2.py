import tkinter
from tkinter import *
from tkinter import ttk

def suma():
    label1 = int(entry1.get())
    label2 = int(entry2.get())
    label3 = int(entry3.get())
    label4 = int(entry4.get())
    label5 = int(entry5.get())
    label6 = int(entry6.get())
    label7 = int(entry7.get())
    label8 = int(entry8.get())
    label9 = int(entry9.get())
    suma = label1 + label2 + label3 + label4 + label5 + label6 + label7 + label8 + label9
    return var.set(suma)

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(3, weight=18)
window.config(background="grey")
var = tkinter.StringVar()


#------labels------
label_nombre = tkinter.Label(window, text="Presupuesto Mensual")
label_nombre.config(background="turquoise")
label_nombre.grid(column=1, row= 1)


#------entrys-----
label_entry1 = tkinter.Entry(window)
label_entry1.grid(column=0, row=2)
entry1 = tkinter.Entry(window)
entry1.grid(column=1, row=2)

label_entry2 = tkinter.Entry(window)
label_entry2.grid(column=0, row=3)
entry2= tkinter.Entry(window)
entry2.grid(column=1, row=3)


label_entry3 = tkinter.Entry(window)
label_entry3.grid(column=0, row=4)
entry3 = tkinter.Entry(window)
entry3.grid(column=1,row=4)

label_entry4 = tkinter.Entry(window)
label_entry4.grid(column=0, row=5)
entry4 = tkinter.Entry(window)
entry4.grid(column=1,row=5)

label_entry5 = tkinter.Entry(window)
label_entry5.grid(column=0, row=6)
entry5 = tkinter.Entry(window)
entry5.grid(column=1,row=6)

label_entry6 = tkinter.Entry(window)
label_entry6.grid(column=0, row=7)
entry6 = tkinter.Entry(window)
entry6.grid(column=1,row=7)

label_entry7 = tkinter.Entry(window)
label_entry7.grid(column=0, row=8)
entry7 = tkinter.Entry(window)
entry7.grid(column=1,row=8)

label_entry8 = tkinter.Entry(window)
label_entry8.grid(column=0, row=9)
entry8 = tkinter.Entry(window)
entry8.grid(column=1,row=9)

label_entry9 = tkinter.Entry(window)
label_entry9.grid(column=0, row=10)
entry9 = tkinter.Entry(window)
entry9.grid(column=1,row=10)



#------Extras---------
label_resultado = tkinter.Entry(window, textvariable=var)
label_resultado.grid(column=3, row=18)
boton_suma = ttk.Button(text="sumar", command= suma)
boton_suma.grid(column=1,row=18)




window.mainloop()
