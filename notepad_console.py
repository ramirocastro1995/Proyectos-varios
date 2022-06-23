    
notebook = []

#definimos tomar notas
def tomar_notas():
        nota_1 = input("Ingrese su nota y aprete guardar : ")
        notebook.append(nota_1)
        print (notebook)

#definimos ver notas
def ver_notas():
        print(notebook)

#definimos borrar notas
def borrar_notas():
    borrar_notas =input('Estas seguro de borrar las notas? Ingresa si o no :')
    if borrar_notas == ['si','Si']:
        notebook.clear()
        'Las notas fueron borradas!'
    elif borrar_notas == 'no':
        'Derivado al Menu Principal'

#definimos salir del programa (falta terminar)
def salir():
    print('Adios!')


#Definimos el loop principal
def main_loop():
    print ('Elige : \n 1)Tomar nota \n 2)Ver nota \n 3)Borrar nota \n 4)Salir \n')
    selec_user = int(input())
    if selec_user == 1 :
        tomar_notas()
    elif selec_user == 2:
        ver_notas()
    elif selec_user ==3 :
        borrar_notas()
    elif selec_user ==4 :
        salir()    
    else:
        print ('comando erroneo')


def main():
    print("bienvenido a Pynotepad" )
    while True == True : 
        main_loop()

main()