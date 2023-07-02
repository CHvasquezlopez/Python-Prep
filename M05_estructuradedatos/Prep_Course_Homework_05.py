#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
ciudades=['Londres','Paris','Roma','madrid','Buenos Aires','brasilia']
print(ciudades)
# In[3]:
['Londres', 'Paris', 'Roma', 'madrid', 'Buenos Aires', 'brasilia']



# 2) Imprimir por pantalla el segundo elemento de la lista
print(ciudades[1])
# In[4]:
Paris



# 3) Imprimir por pantalla del segundo al cuarto elemento
print(ciudades[1:4])
# In[8]:
['Paris', 'Roma', 'madrid']




# 4) Visualizar el tipo de dato de la lista
type(ciudades)
# In[12]:
list




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
print(ciudades[2:])
# In[14]:
['Roma', 'madrid', 'Buenos Aires', 'brasilia']




# 6) Visualizar los primeros 4 elementos de la lista
print(ciudades[:4])
# In[15]:
['Londres', 'Paris', 'Roma', 'madrid']


    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
ciudades=['Londres','Paris','Roma','madrid','Buenos Aires','brasilia'] #Al insertar los nuevos elementos 
                                                                    #no arroja ningun error.
ciudades.append('Londres')
ciudades.insert(0,'Bogota')
print(ciudades)
# In[16]:
['Bogota', 'Londres', 'Paris', 'Roma', 'madrid', 'Buenos Aires', 'brasilia', 'Londres']








# 8) Agregar otra ciudad, pero en la cuarta posición
ciudades.insert(4,'Rio de Janeiro')
print(ciudades)
# In[20]:
['Bogota', 'Londres', 'Paris', 'Roma', 'Rio de Janeiro', 'madrid', 'Buenos Aires', 'brasilia', 'Londres']




# In[21]:




# 9) Concatenar otra lista a la ya creada
ciudades.extend(['New York','Ontario','Maracaibo'])
print(ciudades)
# In[22]:
['Londres', 'Paris', 'Roma', 'madrid', 'Buenos Aires', 'brasilia', 'New York', 'Ontario', 'Maracaibo']



# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
ciudades.index('Londres') # Solo muestra el primer indice que encuentra con el nombre del elemento.
# In[23]:
1




# 11) ¿Qué pasa si se busca un elemento que no existe?
ciudades.index(londres) # Muestra error porque el elemento no esta definido.
# In[24]:
NameError                                 Traceback (most recent call last)
Cell In[14], line 1
----> 1 ciudades.index(londres)

NameError: name 'londres' is not defined




# 12) Eliminar un elemento de la lista
ciudades.remove('Londres')
print(ciudades)
# In[25]:
['Bogota', 'Paris', 'Roma', 'Rio de Janeiro', 'madrid', 'Buenos Aires', 'brasilia', 'New York', 'Ontario', 'Maracaibo']





# 13) ¿Qué pasa si el elemento a eliminar no existe?
ciudades.remove('londres') # Nos devuelve error porque el elemnto no está en la lista.
# In[27]:
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[17], line 1
----> 1 ciudades.remove('londres')

ValueError: list.remove(x): x not in list




# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
ciudad=ciudades.pop()
print(ciudad)
# In[28]:
Maracaibo




# 15) Mostrar la lista multiplicada por 4
print(ciudades*4)
# In[29]:
['Bogota', 'Paris', 'Roma', 'Rio de Janeiro', 'madrid', 'Buenos Aires', 'brasilia', 'New York', 'Ontario', 'Bogota', 'Paris', 'Roma', 'Rio de Janeiro', 'madrid', 'Buenos Aires', 'brasilia', 'New York', 'Ontario', 'Bogota', 'Paris', 'Roma', 'Rio de Janeiro', 'madrid', 'Buenos Aires', 'brasilia', 'New York', 'Ontario', 'Bogota', 'Paris', 'Roma', 'Rio de Janeiro', 'madrid', 'Buenos Aires', 'brasilia', 'New York', 'Ontario']



# 16) Crear una tupla que contenga los números enteros del 1 al 20
numeros=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
# In[32]:




# 17) Imprimir desde el índice 10 al 15 de la tupla
print(numeros[10:16])
# In[35]:
(11, 12, 13, 14, 15, 16)



# 18) Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in numeros)
print(30 in numeros)
# In[41]:
True
False




# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
'Paris' in ciudades
# In[48]:
True




# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
print(ciudades.count('Londres'))
print(numeros.count(10))
# In[51]:
1
1



# 21) Convertir la tupla en una lista
lista_numeros=list(numeros)
print(lista_numeros)
type(lista_numeros)
# In[52]:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list




# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
uno,dos,tres,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_=numeros
print(uno)
print(dos)
print(tres)
# In[55]:
1
2
3


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
Ciudades=['Londres','Paris','Roma','Madrid','Buenos Aires','brasilia']
dicc_ciudades={'Ciudad':Ciudades,
                'Pais':['Inglaterra','Francia','Italia','España','Argentina','Brasil'],
                'Continente':['Europa','Europa','Europa','Europa','Sudamerica','Sudamerica']}
print(dicc_ciudades)
# In[57]:
{'Ciudad': ['Londres', 'Paris', 'Roma', 'Madrid', 'Buenos Aires', 'brasilia'], 'Pais': ['Inglaterra', 'Francia', 'Italia', 'España', 'Argentina', 'Brasil'], 'Continente': ['Europa', 'Europa', 'Europa', 'Europa', 'Sudamerica', 'Sudamerica']}





# 24) Imprimir las claves del diccionario
print(dicc_ciudades.keys())
# In[59]:
dict_keys(['Ciudad', 'Pais', 'Continente'])



# 25) Imprimir las ciudades a través de su clave
print(dicc_ciudades['Ciudad'])
# In[61]:
['Londres', 'Paris', 'Roma', 'Madrid', 'Buenos Aires', 'brasilia']



