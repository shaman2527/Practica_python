lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Suma recursiva de una lista
# def sumar(lista):
#     if lista == []:
#         suma = 0
#     else:
#         suma = lista[0] + sumar(lista[1:])
#     return suma



# def sumar2(lista):
#     invertir = lista[:: -1]
#     if invertir == []:
#         return  0
#     else:
#         return invertir[0] + sumar2(invertir[1:])
    
    
        

# print(sumar2(lista2))

#sumar recursivamente una lista sin invertirla
def sumar(lista):
    if not lista:
        print("Lista vacía")
        return 0
    else:
        return lista[0] + sumar(lista[1:])
        
print(sumar(lista))

#Si quieres sumar la lista invertida (de forma eficiente):


def sumaInvertida(lista):
    lista_invertida = lista[::-1]
    print(lista_invertida)
    def suma_recursiva(sub_lista):
        if not sub_lista:
            return 0
        else:
            return sub_lista[0] + suma_recursiva(sub_lista[1:])   
    return suma_recursiva(lista_invertida)

print(sumaInvertida(lista2))






