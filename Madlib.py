from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('300x300')
root.title('Madlib')
Label(root, text = 'Generador de Madlibs' , font = 'arial 15 bold').pack()
Label(root, text = 'Click en cualquiera :', font ='arial 15 bold').place(x=40,y=80)
#img = ImageTk.PhotoImage(Image.open("1.jpg"))
#panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

def madlib1():

    animales = input('Ingresar un animal:')
    profesion = input('Ingresar una profesion:')
    ropa = input('Ingresar una ropa:')
    cosas = input('Ingresar una cosa:')
    nombre = input('Ingresar un nombre:')
    verbo = input('Ingresar un verbo en pasado:')
    comida = input('Ingresar una comida:')
    print ('Fuimos al zoologico a ver un ' + animales + ' y mi mama que es '
     + profesion + ' nos dijo que llevemos un ' + cosas + ' pero yo no queria porque ' +
     nombre + ' me dijo que era de mala suerte. Luego nos dio hambre y comimos '
     + comida + ' pero al rato me empezo a dar frio porque no lleve ' + ropa + ' asi que ' + verbo)

def madlib2():
    nombre = input('Ingrese un nombre de persona :')
    hotel = input('Ingrese nombre de un hotel :')
    ciudad = input ('Ingresar una ciudad :')
    verbo = input ('Ingresar un verbo en infinitivo : ')




    print ( nombre +' llega al Hotel '+ hotel + ', situado en las montañas de '+ ciudad +', a 25 millas de la ciudad más cercana, para ser ' + verbo +' con el fin de obtener el puesto de vigilante durante los meses de invierno.' 
    'El hotel, construido sobre un antiguo cementerio de los nativos americanos, queda aislado durante el invierno debido a las fuertes nevadas')

Button( root , text = 'El Zoologico de Palermo', font = 'arial 15' , command = madlib1,
bg = 'ghost white').place(x=60 , y =120)
Button(root, text= 'El Resplandor', font ='arial 15', command = madlib2 , bg = 'ghost white').place(x=70, y=180)
#Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()

