import random

import time

puntaje = 0

iniciar_trivia = True
intentos = 0

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


print (RED+"         Bienvenido a mi trivia sobre sobre la NBA"+RESET)
print (GREEN+"Pondremos a prueba tus conocimientos"+RESET)

print("Tienes", puntaje, "puntos")

nombre = input(BLUE+"Ingresa tu nombre: "+RESET)

time.sleep(1)

print("\n Hola", (CYAN+nombre+RESET), "Bienvenido a la trivia mas divertida, pero primero vayemos con las reglas")

time.sleep(1)

print("\n                       REGLAS")
print("\n- Las 4 primeras preguntas te suman 10 puntos escogiendo la correcta")
print("\n- Las 4 primeras preguntas te restan 5 puntos escogiendo la incorrecta")
print("\n- La ultima pregunta es una sorpresa")
print("\n- Al terminar la trivia se te brindara un bonus sorpresa  ")
print("\n- Hay algunas alternativas sorpresas, DESCUBRELAS!")

time.sleep(1)

print("\n                 ¡A DIVERTIRNOS!")

while iniciar_trivia == True: 
  
  intentos += 1
  puntaje = 0

  print(MAGENTA+"\nIntento número:" + RESET, MAGENTA+str(intentos)+RESET  )
  input("Presiona Enter para continuar ")

  for numero_carga in range (3,0,-1):
   print ("Por favor espera " ,CYAN+str(numero_carga), "segundos"+RESET)
   time.sleep(1)


  print (YELLOW+"\n1) ¿Quién tiene mas triples anotados en la NBA?"+RESET)
  print ("a) Lebron James")
  print ("b) Michael Jordan")
  print ("c) Klat Thompson")
  print ("d) Stephen Curry")

  time.sleep(1)
  
  respuesta_1= input("\nTu respuesta: ")
  
  time.sleep(1)
  
  while respuesta_1 not in ("a", "b", "c", "d", "A", "B", "C","D", "x"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  
  if respuesta_1 == "x":
    puntaje = random.randint(20, 50)
    print(MAGENTA+"INCREIBLE!!!!,Esto es un bonus secreto"+RESET)
    
  
  if respuesta_1 == "a":
    puntaje += -5
    print(RED+"INCORRECTO, ANIMOS!", nombre,",", "Lebron James no es el mejor triplista, pero es uno de los mejores jugadores de la historia"+RESET)
  elif respuesta_1 == "b":
    puntaje += -5
    print(RED+"LASTIMA!", nombre,",", "Michael Jordan no es el mejor triplista, pero tiene dos triples campeonatos consecutivos"+RESET)
  elif respuesta_1 == "c":
    puntaje += -5
    print(RED+"CERCA!", nombre,",", "Klay Thompson no es el mejor triplista, pero tiene el record de mas triples en un quarto de juego"+RESET)
  elif respuesta_1 == "d":
    puntaje += 10
    print(GREEN+"MARAVILLOSO", nombre, "!",",", "Stephen Curry es el mejor triplista de la historia, y sigue activo, una cosa de locos"+RESET)

  if respuesta_1 == "A":
    puntaje += -5
    print(RED+"INCORRECTO, ANIMOS!", nombre,",", "Lebron James no es el mejor triplista, pero es uno de los mejores jugadores de la historia"+RESET)
  elif respuesta_1 == "B":
    puntaje += -5
    print(RED+"LASTIMA!", nombre,",", "Michael Jordan no es el mejor triplista, pero tiene dos triples campeonatos consecutivos"+RESET)
  elif respuesta_1 == "C":
    puntaje += -5
    print(RED+"CERCA!", nombre,",", "Klay Thompson no es el mejor triplista, pero tiene el record de mas triples en un quarto de juego"+RESET)
  elif respuesta_1 == "D":
    puntaje += 10
    print(GREEN+"MARAVILLOSO", nombre, "!",",", "Stephen Curry es el mejor triplista de la historia, y sigue activo, una cosa de locos"+RESET)
    
  print (nombre, "tienes", puntaje, "puntos")

  print("Siguiente...")
  time.sleep(1)
  
  print (YELLOW+"\n2) ¿Quién tiene mas puntos anotados en la historia de la NBA?"+RESET)
  print ("a) Michael Jordan")
  print ("b) Kobe Bryan")
  print ("c) Lebron James")
  print ("d) Kareem Abdul-Jabbar")
  
  time.sleep(1)
  
  respuesta_2 = input("\nTu respuesta: ")
  
  while respuesta_2 not in ("a", "b", "c", "d", "A","B","C","D"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  
  
  if respuesta_2 == "a":
    puntaje += -5
    print(RED+"INCORRECTO, ANIMOS!", nombre,",", "Michael Jordan no es el mayor anotador de la historia, pero considerado el mejor jugador de este deporte"+RESET)
  elif respuesta_2 == "b":
    puntaje += -5
    print(RED+"Lastima!", nombre,",", "Kobe Bryan no es el mayor anotador de la historia, pero considerado el mejor anotador de los Angeles Lakers"+RESET)
  elif respuesta_2 == "c":
    puntaje += -5
    print(CYAN+"MUY CERCA!", nombre,",", "Lebron James no es el mayor anotador de la historia, pero se encuentra activo y esta muy cerca"+RESET)
  elif respuesta_2 == "d":
    puntaje += 10
    print(GREEN+"Excelente", nombre, "!",",", "Kareem Abdul-Jabbar es el mayor anotador de la historia y uno de los 10 mejores jugadores de la historia de la NBA"+RESET)

  if respuesta_2 == "A":
    puntaje += -5
    print(RED+"INCORRECTO, ANIMOS!", nombre,",", "Michael Jordan no es el mayor anotador de la historia, pero considerado el mejor jugador de este deporte"+RESET)
  elif respuesta_2 == "B":
    puntaje += -5
    print(RED+"Lastima!", nombre,",", "Kobe Bryan no es el mayor anotador de la historia, pero considerado el mejor anotador de los Angeles Lakers"+RESET)
  elif respuesta_2 == "C":
    puntaje += -5
    print(RED+"MUY CERCA!", nombre,",", "Lebron James no es el mayor anotador de la historia, pero se encuentra activo y esta muy cerca"+RESET)
  elif respuesta_2 == "D":
    puntaje += 10
    print(GREEN+"Excelente", nombre, "!",",", "Kareem Abdul-Jabbar es el mayor anotador de la historia y uno de los 10 mejores jugadores de la historia de la NBA"+RESET)

  print (nombre, "tienes", puntaje, "puntos")
  
  print("Continuamos...")
  time.sleep(1)
  
  print (YELLOW+"\n3) ¿Que jugador tiene mas anillos obtenidos en la historia de la NBA?"+RESET)
  print ("a) Michael Jordan")
  print ("b) Stephen Curry")
  print ("c) Bill Russel")
  print ("d) Larry Bird")
  
  time.sleep(1)
  
  respuesta_3 = input("\nTu respuesta: ")
  
  while respuesta_3 not in ("a", "b", "c", "d", "A", "B", "C", "D"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    puntaje += -5
    print(RED+"Lastima!", nombre,",", "Michael Jordan no tiene el mayor numero de anillos obtenidos, pero se le considera el GOAT del basquet"+RESET)
  elif respuesta_3 == "b":
    puntaje += -5
    print(RED+"INCORRECTO, ANIMOS!", nombre,",", "Stephen Curry no tiene el mayor numero de anillos obtenidos, pero si se le considere el mejor actualmente"+RESET)
  elif respuesta_3 == "d":
    puntaje += -5
    print(RED+"Muy cerca!", nombre,",", "Larry Bird no tiene el mayor numero de anillos obtenidos, pero fue una maquina en su generación"+RESET)
  elif respuesta_3 == "c":
    puntaje += 10
    print(GREEN+"NICE", nombre, "!",",", "Bill Russel tiene el mayor numero de anillos obtenidos y un referente de los Boston Celtics"+RESET)

  if respuesta_3 == "A":
    puntaje += -5
    print(RED+"LASTIMA!", nombre,",", "Michael Jordan no tiene el mayor numero de anillos obtenidos, pero se lo considera el GOAT del basquet"+RESET)
  elif respuesta_3 == "B":
    puntaje += -5
    print(RED+"INCORRECTO, ANIMOS!", nombre,",", "Stephen Curry no tiene el mayor numero de anillos obtenidos, pero si se le considera el mejor actualmente"+RESET)
  elif respuesta_3 == "D":
    puntaje += -5
    print(RED+"Muy cerca!", nombre,",", "Larry Bird no tiene el mayor numero de anillos obtenidos, pero fue una maquina en su generación"+RESET)
  elif respuesta_3 == "C":
    puntaje += 10
    print(GREEN+"NICE", nombre, "!",",", "Bill Russel tiene el mayor numero de anillos obtenidos y un referente en los Boston Celtics"+RESET)
    
  print (nombre, "tienes", puntaje, "puntos")
  
  print("Proseguimos...")
  time.sleep(1)

  print (YELLOW+"\n4) ¿Que equipo fue el ultimo en obtener  el campeonato de la NBA?"+RESET)
  print ("a) Los Golden Warriors")
  print ("b) Los Brooklyn Nets")
  print ("c) Los Boston Celtics")
  print ("d) Los Angeles Lakers")
  
  time.sleep(1)
  
  respuesta_4 = input("\nTu respuesta: ")
  
  while respuesta_4 not in ("a", "b", "c", "d", "A", "B", "C", "D"):
    respuesta_4 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_4 == "b":
    puntaje += -5
    print(RED+"Lastima!", nombre,",", "Los Brooklyn Nets no tienen ningún campeonato de la NBA, pero este año fueron favoritos"+RESET)
  elif respuesta_4 == "c":
    puntaje += -5
    print(RED+"Muy cerca!", nombre,",", "Los Boston Celtics no fueron campeones, pero llegaron a la final"+RESET)
  elif respuesta_4 == "d":
    puntaje += -5
    print(RED+"Un poco lejos!", nombre,",", "Los Angeles Lakers no fueron campeones, pero si del año pasado"+RESET)
  elif respuesta_4 == "a":
    puntaje += 10
    print(GREEN+"Good", nombre, "!",",", "Los Golden Warriors si fueron campeones y ya suman su 4 campeonato"+RESET)

  if respuesta_4 == "B":
    puntaje += -5
    print(RED+"Lastima!", nombre,",", "Los Brooklyn Nets no tienen ningún campeonato de la NBA, pero este año fueron favoritos"+RESET)
  elif respuesta_4 == "C":
    puntaje += -5
    print(RED+"Muy cerca!", nombre,",", "Los Boston Celtics no fueron campeones pero llegaron a la final"+RESET)
  elif respuesta_4 == "D":
    puntaje += -5
    print(RED+"Un poco lejos!", nombre,",", "Los Angeles Lakers no fueron campeones, pero si del año pasado"+RESET)
  elif respuesta_4 == "A":
    puntaje += 10
    print(GREEN+"Good", nombre, "!",",", "Los Golden Warriors si fueron campeones y ya suman su 4 campeonato"+RESET)
    
  print (nombre, "tienes", puntaje, "puntos")
  
  print("Seguimos adelante...")
  time.sleep(2)
  


  print(MAGENTA+"\nLlegamos al final, esta pregunta es super especial, ¡SUERTE!"+RESET)

  time.sleep(3)
    
  print (YELLOW+"\n5) ¿Quién tiene mas puntos anotados en la historia de la NBA?"+RESET)
  print ("a) Stephen Curry")
  print ("b) Kareem Abdul-Jabbar")
  print ("c) Lebron James")
  print ("d) Michael Jordan")
  
  time.sleep(1)
  
  respuesta_5 = input("\nTu respuesta: ")
  
  while respuesta_5 not in ("a", "b", "c", "d", "A","B","C","D"):
    respuesta_5 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  
  
  if respuesta_5 == "a":
    print(RED+"Lastima!", nombre,",", "Stephen Curry es el jugador con mas MVP's, Uhmmmm.. que mala suerte dividimos tu puntaje a la mitad debido a que es el jugadores con menos MVP's entre los 4 "+RESET)
    puntaje = puntaje / 2
  elif respuesta_5 == "d":
    print(CYAN+"Casi!", nombre,",", "Michael Jordan no es el jugador con mas MVP's pero ganaste 5 puntos por que es el segundo jugador con mas MVP's"+RESET)
    puntaje = puntaje + 5
  elif respuesta_5 == "c":
    print(RED+"Un poco lejos!", nombre,",", "Lebron James no es el jugador con mas MVP's"+RESET)
    puntaje = puntaje -5
  elif respuesta_5 == "b":
    print(GREEN+"Grandioso", nombre, "!",",", "Kareem Abdul-Jabbar es el jugador con mas MVP's, multiplicamos tu puntaje debido a que es la pregunta mas dificil de esta trivia"+RESET)
    puntaje = puntaje * 2

  if respuesta_5 == "A":
    print(RED+"Lastima!", nombre,",", "Stephen Curry no es el jugador con mas MVP's, Uhmmmm.. que mala suerte dividimos tu puntaje a la mitad debido a que es el jugadores con menos MVP's entre los 4 "+RESET)
    puntaje = puntaje / 2
  elif respuesta_5 == "D":
    print(RED+"Casi!", nombre,",", "Michael Jordan no es el jugador con mas MVP's pero ganaste 5 puntos por que es el segundo jugador con mas MVP's"+RESET)
    puntaje = puntaje + 5
  elif respuesta_5 == "C":
    print(RED+"Un poco lejos!", nombre,",", "Lebron James no es el jugador con mas MVP's"+RESET)
    puntaje = puntaje -5
  elif respuesta_5 == "B":
    print(GREEN+"Grandioso", nombre, "!",",", "Kareem Abdul-Jabbar es el jugador con mas MVP's, multiplicamos tu puntaje debido a que es la pregunta mas dificil de esta trivia"+RESET)
    puntaje = puntaje * 2


  for numero_carga in range (5,0,-1):
   variable=random.randint(0,20)
  sumar=variable+puntaje
  
  print("Tienes " , puntaje , " puntos ... \nProbemos tu suerte ")
  time.sleep(2)
  
  print("\nTu suerte te da un puntaje de: " ,CYAN+ str(variable) + RESET," puntos")

  time.sleep(2)
  print(MAGENTA+"\nGracias por jugar a esta trivia, espero que te hayas divertido,lograste los " , sumar, "puntos"+RESET)
  


  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  
  if repetir_trivia != "si":  # != significa "distinto"
    print((CYAN+nombre+RESET), " espero que lo hayas pasado bien, hasta pronto!")
    iniciar_trivia = False

