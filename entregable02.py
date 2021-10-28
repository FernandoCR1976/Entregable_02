import random

my_list=[]

for i in range (10):
    my_list.append(round(random.uniform(0.00, 8.99),2))

ordenada = my_list.copy() 
ordenada.sort()

print(" ")
print(" ")
print("***********LISTA DE JUGADORES ALEATORIA***********")
print(" ")
print(" ")
print(my_list)
print(" ")
print(" ")
print("***********LISTA DE JUGADORES ORDENADA***********")
print(" ")
print(" ")
print(ordenada)
print(" ")
print(" ")
input("PRESIONE ENTER PARA CONTINUAR")
print(" ")
print(" ")

contador=0
print("***********CLASIFICACIÓN DE JUGADORES ALEATORIA***********")
print(" ")
print(" ")
while contador < len(my_list):

    if (my_list[contador] >= 0.00) and (my_list[contador]) <= 0.99:
        print("El jugador ",my_list[contador]," pertenece a la liga HIERRO \n")
    elif (my_list[contador] >= 1.00) and (my_list[contador]) <= 1.99:
        print("El jugador ",my_list[contador]," pertenece a la liga BRONCE \n")
    elif (my_list[contador] >= 2.00) and (my_list[contador]) <= 2.99:
        print("El jugador ",my_list[contador]," pertenece a la liga PLATA \n")
    elif (my_list[contador] >= 3.00) and (my_list[contador]) <= 3.99:
        print("El jugador ",my_list[contador]," pertenece a la liga ORO \n")
    elif (my_list[contador] >= 4.00) and (my_list[contador]) <= 4.99:
        print("El jugador ",my_list[contador]," pertenece a la liga PLATINO \n")
    elif (my_list[contador] >= 5.00) and (my_list[contador]) <= 5.99:
        print("El jugador ",my_list[contador]," pertenece a la liga DIAMANTE \n")
    elif (my_list[contador] >= 6.00) and (my_list[contador]) <= 6.99:
        print("El jugador ",my_list[contador]," pertenece a la liga MAESTRO \n")
    elif (my_list[contador] >= 7.00) and (my_list[contador]) <= 7.99:
        print("El jugador ",my_list[contador]," pertenece a la liga GRAN MAESTRO \n")
    elif (my_list[contador] >= 8.00) and (my_list[contador]) <= 8.99:
        print("El jugador ",my_list[contador]," pertenece a la liga GRAN MAESTRO \n")

    contador+=1
input("PRESIONE ENTER PARA CONTINUAR")
print(" ")
print(" ")
print("***********CLASIFICACIÓN DE JUGADORES ORDENADA***********")
print(" ")
print(" ")

contador2=0
while contador2 < len(ordenada):

    if (ordenada[contador2] >= 0.00) and (ordenada[contador2]) <= 0.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga HIERRO \n")
    elif (ordenada[contador2] >= 1.00) and (ordenada[contador2]) <= 1.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga BRONCE \n")
    elif (ordenada[contador2] >= 2.00) and (ordenada[contador2]) <= 2.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga PLATA \n")
    elif (ordenada[contador2] >= 3.00) and (ordenada[contador2]) <= 3.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga ORO \n")
    elif (ordenada[contador2] >= 4.00) and (ordenada[contador2]) <= 4.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga PLATINO \n")
    elif (ordenada[contador2] >= 5.00) and (ordenada[contador2]) <= 5.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga DIAMANTE \n")
    elif (ordenada[contador2] >= 6.00) and (ordenada[contador2]) <= 6.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga MAESTRO \n")
    elif (ordenada[contador2] >= 7.00) and (ordenada[contador2]) <= 7.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga GRAN MAESTRO \n")
    elif (ordenada[contador2] >= 8.00) and (ordenada[contador2]) <= 8.99:
        print("El jugador ",ordenada[contador2]," pertenece a la liga GRAN MAESTRO \n")

    contador2+=1