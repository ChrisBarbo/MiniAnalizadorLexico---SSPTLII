
def main():
    while True:
        cadena = input("Ingresa el texto: ")
        identificadores, num_reales = lexer(cadena)
        print("Identificadores: ", identificadores)
        print("Números reales: ", num_reales)


        print("1. Analizar otra cadena")
        print("0. Salir")
        opc = input("¿Desea analizar otra cadena? ")
        if opc != "1":
            break

def lexer(cadena):
    i = 0; #Recorrer cadena ingresada caracter por caracter 

    longitud = len(cadena)      #cuenta caracteres x cadena 
    
    #Definicion de listas
    identificadores = []
    num_reales = []
    

    while i < longitud:
        if cadena[i].isalpha():         #Verifica si el caracter es letra 
            identificador = cadena[i]   #Se guarda en una variable temporal
            i += 1                      #Avanza al siguiente caracter

            while i < longitud and (cadena[i].isalpha() or cadena[i].isdigit()): #El caracter debe ser letra o numero, y el contador debera ser menor a la longitud de la cadena 
                identificador += cadena[i]   #Se guarda en la variable temporal el caracter de cada iteracion 
                i += 1
            identificadores.append(identificador) #Agrega lo guardado en la variable temporal a la lista de identificadores

        elif cadena[i].isdigit():     #Verifica si el caracter es numero
            numero_real = cadena[i]   #Se guarda en una variable temporal
            i += 1                    #Avanza al caracter siguiente

            while i < longitud and cadena[i].isdigit():  #La cadena debe ser numero
                numero_real += cadena[i]                 #Se gaurda en la variable temporal
                i += 1

            if i < longitud and cadena[i] == '.':    #Compara si el caracter evaluado es punto,  Si si, se guarda en la variable temporal 
                numero_real += cadena[i]
                i += 1

                while i < longitud and cadena[i].isdigit(): #verifica que el siguiente sea numero. Luego de evaluar si es punto para continuar 
                    numero_real += cadena[i]              # Se guarda en variable temporal 
                    i += 1
                num_reales.append(numero_real)            #Se toma como un numero real, tomando en cuenta el punto 
            else:
                num_reales.append(numero_real)
        else:
            i += 1

    return identificadores, num_reales                  #Al terminar retorna las listas 


if __name__ == "__main__":
    main()