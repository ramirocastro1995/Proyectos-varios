from tkinter import *

root = Tk()
root.title("Calculadora Simple")
root.configure(bg="#9BA1A8")

e = Entry(root, width = 35,borderwidth = 5, bg="#DBE1E8")
#columnspan te da el espacio para las otras 3 cosas
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#color botones
color_botones = "#ABB6C1"
color_botones_numeros= "#DBE1E8"

#e.insert(0, "Pone tu nombre: ")

def boton_click(numero):
    #e.delete(0, END)
    #current mas el numero para que se escriban en orden
    current = e.get()
    #delete para que no se sumen
    e.delete(0, END)
    e.insert(0, str(current) + str(numero))

def boton_borrar():
    e.delete(0, END)

def boton_igual():
    second_number = e.get()
    e.delete(0, END)

    if calculo == "sumar":
        e.insert(0,f_num + int(second_number))

    if calculo == "restar":
        e.insert(0,f_num - int(second_number))

    if calculo == "multiplicar":
        e.insert(0,f_num * int(second_number))

    if calculo == "dividir":
        e.insert(0,f_num / int(second_number))

def boton_suma():
    first_number = e.get()
    #una variable global para usar afuera de la funcion
    global f_num
    global calculo
    calculo = "sumar"
    f_num = int(first_number)
    e.delete(0, END)

def boton_resta():
    first_number = e.get()
    global f_num
    global calculo
    calculo = "restar"
    f_num = int(first_number)
    e.delete(0, END)

def boton_multiplica():
    first_number = e.get()
    global f_num
    global calculo
    calculo = "multiplicar"
    f_num = int(first_number)
    e.delete(0, END)

def boton_divide():
    first_number = e.get()
    global f_num
    global calculo
    calculo = "dividir"
    f_num = int(first_number)
    e.delete(0, END)

#definir botones
#valores originales padx=40 pady=20
boton_1 = Button(root,text="1", padx=20, pady=15, bg=color_botones_numeros , command=lambda: boton_click(1))
boton_2 = Button(root,text="2", padx=20, pady=10, bg=color_botones_numeros, command=lambda: boton_click(2))
boton_3 = Button(root,text="3", padx=20, pady=10, bg=color_botones_numeros, command=lambda: boton_click(3))
boton_4 = Button(root,text="4", padx=20, pady=15, bg=color_botones_numeros, command=lambda: boton_click(4))
boton_5 = Button(root,text="5", padx=20, pady=10, bg=color_botones_numeros, command=lambda: boton_click(5))
boton_6 = Button(root,text="6", padx=20, pady=10, bg=color_botones_numeros, command=lambda: boton_click(6))
boton_7 = Button(root,text="7", padx=20, pady=15, bg=color_botones_numeros, command=lambda: boton_click(7))
boton_8 = Button(root,text="8", padx=20, pady=10, bg=color_botones_numeros, command=lambda: boton_click(8))
boton_9 = Button(root,text="9", padx=20, pady=10, bg=color_botones_numeros, command=lambda: boton_click(9))
boton_0 = Button(root,text="0", padx=20, pady=15, bg=color_botones_numeros, command=lambda: boton_click(0))
boton_suma = Button(root,text="+", padx=29, pady=10, command=boton_suma, bg=color_botones)
boton_igual = Button(root,text="=", padx=63, pady=15, command=boton_igual, bg=color_botones)
boton_borrar = Button(root,text="Limpiar", padx=45, pady=8, command= boton_borrar, bg=color_botones, font =('Helvetica', 10, 'bold', 'underline'))

boton_resta = Button(root,text="-", padx=31, pady=10, command=boton_resta, bg=color_botones)
boton_multiplica = Button(root,text="*", padx=30, pady=8, command=boton_multiplica , bg=color_botones)
boton_divide = Button(root,text="/", padx=31, pady=8, command=boton_divide , bg=color_botones)

#poner botones en la pantalla

boton_1.grid(row=3, column=0)
boton_2.grid(row=3, column=1)
boton_3.grid(row=3, column=2)

boton_4.grid(row=2, column=0)
boton_5.grid(row=2, column=1)
boton_6.grid(row=2, column=2)

boton_7.grid(row=1, column=0)
boton_8.grid(row=1, column=1)
boton_9.grid(row=1, column=2)

boton_0.grid(row=4, column=0)
#columnspan=2 para que no cree mas columnas de lo necesario en este boton
boton_borrar.grid(row= 4, column=1, columnspan=2)
boton_suma.grid(row = 5, column= 0)
boton_igual.grid(row = 5, column = 1, columnspan=2)

boton_resta.grid(row = 6, column=0)
boton_multiplica.grid(row = 6, column=1)
boton_divide.grid(row = 6, column=2)


root.mainloop()