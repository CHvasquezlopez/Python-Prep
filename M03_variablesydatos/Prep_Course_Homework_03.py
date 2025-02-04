#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
x=256
print(x)
# In[7]:
256



# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))
# In[3]:
<class 'float'>




# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(8.5))
# In[8]:

print(type(x))




# 4) Crear una variable que contenga tu nombre
my_name="Carlos Humberto Vasquez Lopez"
# In[2]:




# 5) Crear una variable que contenga un número complejo
numero_complejo=9 + 3j
# In[3]:





# 6) Mostrar el tipo de dato de la variable crada en el punto 5
type(numero_complejo)
# In[4]:





# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi=3.1416
# In[1]:





# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
var1=True    #Valor booleano
var2='True'  #Cadena de texto con la palabra True
# In[3]:





# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(var1))
print(type(var2))
# In[5]:
<class 'bool'>
<class 'str'>




# 10) Asignar a una variable, la suma de un número entero y otro decimal
X=2548+1256.32
# In[1]:





# 11) Realizar una operación de suma de números complejos
x=9+5j
y=3+2j
z=x+y
print(z)
# In[2]:
(12+7j)




# 12) Realizar una operación de suma de un número real y otro complejo
m=x+3.25
print(m)
# In[4]:
(12.25+5j)




# 13) Realizar una operación de multiplicación
20*12
# In[5]:
240




# 14) Mostrar el resultado de elevar 2 a la octava potencia
2**8
# In[6]:
256



# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
x=27/4
print(x)
# In[8]:
6.75




# 16) De la división anterior solamente mostrar la parte entera
x=27//4
print(x)
# In[9]:
6




# 17) De la división de 27 entre 4 mostrar solamente el resto
x=27%4
print(x)
# In[1]:
3




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
x=4*6+3
print(x)
# In[2]:
27




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
l="Carlos "
m="Humberto "
n="Vásquez"
print(l+m+n)
# In[3]:
Carlos Humberto Vásquez




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
"2"             #Esto es una cadena
2               #Esto es un entero
print(2=="2")   #Esto nos arrojará False
# In[4]:
False




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
a=int("2")
b=2
print(a==b)
# In[11]:
True




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a=float('3,8')  #El error está en que se usó una coma y no el punto.
print(a)
# In[12]:





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.
x=3
x-=1
print(x)
# In[15]:
2




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1<<2) #El resultado es cuatro porque el uno se desplaza 2 lugares a la izquierda de su posición.
            #El sistema de numeracion binario es un sistema que usa solo dos digitos el 1 y el 0 para representar
            #la numeración.

# In[29]:
4




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
a=2
b='2'
#print(a+b)  #No se permite esta operacion porque uno es una cadena y el otro un numero entero
#El resultado si son del mismo tipo varia porque si ambos son  enteros dará como resultado un entero.
#pero si son cadenas dará como resultado una concatenación de cadenas 
a=str(2)
b='2'
print(a+b)
a=2
b=int('2')
print(a+b)
# In[23]:
2 2
4





# 26) Realizar una operación válida entre valores de tipo entero y string
a="¡Estoy "
b="muy "
c="feliz!"
d=3
print(a+(b*d)+c)
# In[30]:
¡Estoy muy muy muy feliz!


