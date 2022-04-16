import random
def adivinar(x):
    numero_random = random.randint(1 ,x)
    adivinar = 0
    while adivinar != numero_random :
        adivinar = int(input (f" Ingresa un numero entre 1 y {x} :"))
        if adivinar < numero_random:  
            print("El numero es muy chico,intenta de nuevo!")
        elif adivinar > numero_random: 
            print("El numero es muy grande,intenta de nuevo!")
    
    print (f"el numero es {numero_random}, adivinaste!")

adivinar(10)

