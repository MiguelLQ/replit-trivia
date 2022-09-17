# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido(a) a mi trivia")
print ("\n¡Pondremos a prueba tus conocimientos sobre historia del Peru!")
print("\nacontinuacion te presentaremos tres preguntas:")

# Es importante dar instrucciones sobre cómo jugar:
print ("\nResponda las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

# Pregunta 1
print ("1) ¿en que año se proclamo la independencia del peru?\n")
print ("a) 1831")
print ("b) 1821")
print ("c) 1823")
print ("d) 1854")

# Almacenamos la respuesta del usuario en la variable "r"
r = input("\nTu respuesta es : ")
if r=="b":
  print("\n¡bien hecho acertaste!\n")
else:
 print("\ntu respuesta es incorrecta")
 print("la respuesta correcta es: b)") 

# Pregunta 2
print ("\n2) ¿que virrey promulgo la creacion de la mita de minas?\n")
print ("a) Francisco de Toledo")
print ("b) Blasco Núñez Vela")
print ("c) Conde de Lemos")
print ("d) Antonio de Mendoza")

# Almacenamos la respuesta del usuario en la variable "r2"
r2 = input("\nTu respuesta es : ")
if r2=="a":
  print("\n¡bien hecho acertaste, sigue asi!\n")
else:
 print("\ntu respuesta es incorrecta")
 print("la respuesta correcta es: a)") 
# Pregunta 3
print ("\n3) Los chankas eran una cultura guerrera y ademas fueron enemigos de los incas, ¿donde seria su ubicacion en la actualidad?\n")
print ("a) chachapoyas(Amazonas)")
print ("b) Limatambo(Cusco)")
print ("c) Andahuaylas(Apurimac)")
print ("d) Azangaro(Puno)")

# Almacenamos la respuesta del usuario en la variable "r3"
r3 = input("\nTu respuesta es : ")
if r3=="c":
  print("\n¡bien hecho acertaste, felicidades!\n")
else:
 print("\ntu respuesta es incorrecta")
 print("la respuesta correcta es: c)") 

# culminacion de las preguntas y despedida
print("\nGracias por participar....\n\n¡hasta la proxima!")