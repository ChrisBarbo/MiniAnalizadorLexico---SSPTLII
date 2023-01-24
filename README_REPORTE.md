# MiniAnalizadorLexico---SSPTLII
MiniAnalizador lexico - Garcia Barbosa Christian 216809799

En esta practica se pidio codificar un mini analizador lexico que solo recibiera numeros reales e identificadores. 
Por lo tanto solo trabajariamos con estos tokens, por lo que decidi manejarlos en listas.

![image](https://user-images.githubusercontent.com/104050689/214208713-9c24a932-42db-4cd9-bc99-9f61b10b5d08.png)  Aqui inicialice ambas listas , de numeros reales
                                                                                                                  y de los identificadores
                                                                                                                  
Antes, se creo la funcion llamada lexer que recibira una cadena ingresada por el usuario
con una variable inicializada en i, la cual ira recorriendo la cadena. Ademas de otra variable 
llamada longitud, donde se almacena la longitud de la cadena calculada con "len"

![image](https://user-images.githubusercontent.com/104050689/214209091-dde7e3e9-f772-4d6a-b147-6ada7ec82089.png)

Basicamente, este mini analizador lexico se basa en un while donde la variable debe ser menor que la longitud 
total de la cadena. Para de ahi, utilizar la funcion "isalpha" verificando que el caracter sea letra. Almacenamos en una variable tmporal
y avanza al siguiente caracter.

![image](https://user-images.githubusercontent.com/104050689/214209956-2dfbf0b4-189a-4000-b7be-dbcc320df883.png)

En caso de iniciar con letra, se deduce que en este mini analizador trata de un identificador, por lo que ahora ademas de utilizar la funcion 
"isalpha" tambien hacemos uso de "isdigit" para verificar que sea numero.
Luego de repetir el proceso de guardar en una variable temporal. Agregamos a la lista utilizando 'nombre_lista' + append(variabletemp)

![image](https://user-images.githubusercontent.com/104050689/214210269-181ecd53-e45a-4762-bd89-09423be0db26.png)

Ahora para el caso de un numero real, haremos la misma comparacion con la funcion isdigit, verificamos y guardamos en una variable temporal
ahora llamada "numero_real"

![image](https://user-images.githubusercontent.com/104050689/214210448-87e77652-37f3-422e-ae00-8bf183228839.png)

Ahora, si hay un punto . como caracter lo almacena en  la variable temporal junto al caracter previo para formar asi un numero real y para continuar el siguiente caracter debera ser un numero

![image](https://user-images.githubusercontent.com/104050689/214210646-c56c83fb-7660-4b7e-b235-b86dcb6c7931.png)

Por ultimo agregaremos a la lista como lo hicimos anteriormente, pero esta vez a la lista de numeros reales 

![image](https://user-images.githubusercontent.com/104050689/214210751-1d9193d5-7213-4336-8c5f-00feb49e9465.png)

Para solicitar al usuario un texto a analizar, en el main se solicita y mandamos a llamar a la funcion a las listas para que se impriman 

![image](https://user-images.githubusercontent.com/104050689/214210882-54c185be-3dd0-462c-976d-b5d7070c3309.png)

Resultados: 

![image](https://user-images.githubusercontent.com/104050689/214210979-f4833e19-1d93-4308-a666-207eaea01468.png)

Ingresamos "3.12 id" el identificador es ID mientras que el numero lo muestra tambien en la lista creada




                                                                                                                  


