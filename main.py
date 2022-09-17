# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia

print ("\033[33mBienvenido(a) a mi trivia\033[33m")
print ("\n\033[33m¡Pondremos a prueba tus conocimientos sobre historia del Peru!\033[33m")
nom=input("\n\033[33mprimero dinos tu nombre: \033[33m")

print("\n\033[33mmuy bien ",nom,"acontinuacion te presentaremos tres preguntas:\n\033[33m")
print("\033[33mademas te calificaremos mediante puntuaciones con la que sabras tu nivel en historia del peru..\n\033[33m")
puntaje=0
print("\033[33mtu punaje iinicial es: ",puntaje," y si respondes correctamente las preguntas se te iran sumando 10 puntos mas.\n")

# Es importante dar instrucciones sobre cómo jugar:
print (nom," Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
print("¡empecemos!....\n")

# Pregunta 1
print ("\033[35mpregunta 1)\033[35m\n\033[36m¿en que fecha se proclamo la independencia del peru?\n")
print ("a) 2 de julio de 1831")
print ("b) 28 de julio de 1821")
print ("c) 20 de julio de 1821")
print ("d) 14 de febrero de 1854")

# Almacenamos la respuesta del usuario en la variable "r"

r = input("\033[32m\nTu respuesta es : ")
while r not in ( "a" ,"b" , "c" , "d" ) :
  r = input ( "\033[31m\nDebes responder a , b , c o d . Ingresa nuevamente \ntu respuesta : \033[31m")
if r == "a":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: b)\n")
elif r== "d":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: b)\n")
elif r == "c":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: b)\n")
else:
  puntaje+=10
  print("\033[32m\nbien hecho", nom, "! efectivamente el general San Martín proclamó la independencia del Perú un 28 de julio de 1821 en la Plaza Mayor de Lima.")
  print("\n\033[33mtu puntaje acumulado es: ",puntaje,"\n")

# Pregunta 2
print ("\033[35mpregunta 2)\033[35m\n\033[36m¿que virrey promulgo la creacion de la mita de minas?\n")
print ("a) Francisco de Toledo")
print ("b) Blasco Núñez Vela")
print ("c) Conde de Lemos")
print ("d) Antonio de Mendoza")

# Almacenamos la respuesta del usuario en la variable "r2"

r2 = input("\033[32m\nTu respuesta es : ")
while r2 not in ( "a" ,"b" , "c" , "d" ) :
  r2 = input ( "\033[31m\nDebes responder a , b , c o d . Ingresa nuevamente \ntu respuesta : \033[31m")
if r2 == "b":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: a)\n")
elif r2== "d":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: a)\n")
elif r2== "c":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: a)\n")
else:
  puntaje+=10
  print("\033[32m\nexelente", nom, "! , el virrey Toledo promulgo la mita que era una de las instituciones económicas donde permitió garantizar el aporte de trabajo indígena que se volcaba a las obras públicas o diferentes actividades económicas como la minería, agricultura, ganadería,, etc.")
  print("\n\033[33m\ntu puntaje acumulado es: ",puntaje,"\n")

  # Pregunta 3
print ("\033[35mpregunta 3)\033[35m\n\033[36mLos chankas eran una cultura guerrera y ademas fueron enemigos de los incas, ¿donde seria su ubicacion en la actualidad?\n")
print ("a) chachapoyas(Amazonas)")
print ("b) Limatambo(Cusco)")
print ("c) Andahuaylas(Apurimac)")
print ("d) Azangaro(Puno)")

# Almacenamos la respuesta del usuario en la variable "r3"

r3 = input("\033[32m\nTu respuesta es : ")
while r3 not in ( "a" ,"b" , "c" , "d") :
  r3 = input ( "\033[31m\nDebes responder a , b , c o d . Ingresa nuevamente \ntu respuesta : \033[31m")
if r3 == "a":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: c)\n")
elif r3== "d":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: c)\n")
elif r3 == "b":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: c)\n")
else:
  puntaje+=10
  print("\033[32m\nmuy bien hecho ", nom, "! Los chankas se situaron por zonas Apurimeñas y principalmente por la provincia de Andahuaylas.")
  print("\n\033[33mtu puntaje acumulado es: ",puntaje,"\n")

  # Pregunta 4
print ("\033[35mpregunta 4)\033[35m\n\033[36m¿Cuáles son los elementos del escudo nacional y que significan?\n")
print ("a)\nLa llama(representa la fauna nacional), el arbol de eucalipto(representa la flora nacional) y la corneta(representa la riqueza mineral)\n")
print ("b)\nLa alpaca(representa la fauna nacional), el arbol de la quina(representa la flora nacional) y la coracola(representa la riqueza mineral)\n")
print ("c)\nEl caballo(representa la fauna nacional), el arbol de quinua(representa la flora nacional) y la corneta(representa la riqueza mineral)\n")
print ("d)\nLa vicuña(representa la fauna nacional), el arbol de la quina(representa la flora nacional) y la cornucopia(representa la riqueza mineral)\n")

# Almacenamos la respuesta del usuario en la variable "r4"

r4 = input("\033[32m\nTu respuesta es : ")
while r4 not in ( "a" ,"b" , "c" , "d") :
  r4 = input ( "\033[31m\nDebes responder a , b , c o d . Ingresa nuevamente \ntu respuesta : \033[31m")
if r4 == "a":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: d)\n")
elif r4== "b":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: d)\n")
elif r4 == "c":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: d)\n")
else:
  puntaje+=10
  print("\033[32m\nbien hecho", nom, "! la vicuña, el arbol de la quina y la cornucopia son los tres elementos que representan las riquezas del peru.")
  print("\n\033[33mtu puntaje acumulado es: ",puntaje,"\n")

  # Pregunta 5
print ("\033[35mpregunta 5)\033[35m\n\033[36m¿quien fue apodado como ´caballero de los mares´por su valentia en la guerra del pacifico?\n")
print ("a) Jose Olaya")
print ("b) Francisco Bolognesi")
print ("c) Miguel Grau")
print ("d) Daniel Ugarte")

# Almacenamos la respuesta del usuario en la variable "r5"

r5 = input("\033[32m\nTu respuesta es : ")
while r5 not in ( "a" ,"b" , "c" , "d" ) :
  r5 = input ( "\033[31m\nDebes responder a , b , c o d . Ingresa nuevamente \ntu respuesta : \033[31m")
if r5== "a":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: c)\n")
elif r5== "d":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: c)\n")
elif r5 == "b":
    print("\n\033[31mIncorrecto!", nom,", la respuesta correcta es: c)\n")
else:
  puntaje+=10
  print("\033[32m\nperfecto ", nom, "! en el combate naval de Iquique, Miguel Grau de apodo “Caballero de los Mares” con el monitor Huáscar se enfrentó a la corbeta chilena Esmeralda, que era comandada por el capitán Arturo Prat.\n")
  print("\n\033[33mtu puntaje acumulado es: ",puntaje,"\n")

# culminacion de las preguntas y despedida
print("\033[33mmuy bien",nom,", tu puntaje total es: ",puntaje)  
print("\033[35m\nGracias por participar en esta trivia de preguntas de historia del peru....\n\n¡hasta la proxima!",nom)