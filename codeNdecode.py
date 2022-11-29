abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cifrar(texto,clave):
  longitud=len(texto); #Calculamos la longitud del texto para recorrerlo
  for i in range (0,longitud): #Bucle para recorrer el texto
    for pos in range (0,26): #Bucle para recorrer el Abecedario
      if texto[i]==abc[pos]: #comparo las letras una por una
        pos_abc=pos+int(clave) #Me desplazo en el abecedario en función a la clave
        if pos_abc <26:
           print(abc[pos_abc],end="»»")
        if pos_abc >25 : #En el caso de que me pase del abecedario, calculo el modulo
           print(abc[pos_abc%26],end="»»")
    else:
      print(end="» «")
  return
 
#Funcion de descifrar donde necesita dos valores
def descifrar(texto,clave):
  longitud=len(texto)
  for i in range (0,longitud):
    for pos in range (0,26):
      if texto[i]==abc[pos]:
        pos_abc=pos-(int(clave))
        if pos_abc >-1:
           print(abc[pos_abc],end="»»")
        if pos_abc <0 :
           print(abc[pos_abc%26],end="»»")
    else:
      print(end="» «")
  return
print("«La utilidad de este programa consiste en cifrar o descifrar el texto que introduzca mediante el método César.")
texto=input("«Dime el texto: «")
clave=input("«Dime la clave: «")
print("1.-Cifrar\n2.-Descifrar")
opcion=input("Elija una opción: ")
if opcion =="1":
  cifrar(texto,clave) #llamo a la función pasándole el texto y la clave de cifrado
if opcion == "2":
  descifrar(texto,clave) #llamo a la función pasándole el texto y la clave de cifrado