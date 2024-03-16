import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de fallos permitidos
max_fails = 5

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)

# Elegir nivel de dificultad
print("Elija que dificultad quiere jugar.")
print("1.Fácil")
print("2.Normal")
print("3.Dificíl")
difficulty = int(input("Ingresa una dificultad(1-3): "))
while difficulty not in [1,2,3]:
 print("Por favor, ingresa un número válido (1, 2 o 3)")
 difficulty = int(input("Ingresa una dificultad(1-3): "))

# Definir las letras que estan por defecto
new_word_displayed = ""
if difficulty == 1:
 vowels= "aeiou"
 for letter in secret_word:
  if letter in vowels:
   new_word_displayed += letter
   if letter not in guessed_letters:
     guessed_letters.append(letter)
  else:
   new_word_displayed += "_"
else:
 if difficulty == 2:
  for letter in secret_word:
   if letter == secret_word[0] or letter == secret_word[-1]:
     new_word_displayed += letter
     if letter not in guessed_letters:
      guessed_letters.append(letter)
   else:
     new_word_displayed += "_" 
if difficulty != 3:
 word_displayed = new_word_displayed

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

# Cantidad de fallos
fails=0
while(fails != max_fails):
 # Pedir al jugador que ingrese una letra
 letter = input("Ingresa una letra: ").lower()

 # Verificar si la letra ya ha sido adivinada
 if letter in guessed_letters:
  print("Ya has intentado con esa letra. Intenta con otra.")
  fails += 1
  continue
 
 # Agregar la letra a la lista de letras adivinadas
 guessed_letters.append(letter)

 # Verificar si la letra está en la palabra secreta
 if letter != "" and letter in secret_word:
  print("¡Bien hecho! La letra está en la palabra.")
 else:
  fails += 1
  print("Lo siento, la letra no está en la palabra.")

 # Mostrar la palabra parcialmente adivinada
 letters = []
 for letter in secret_word:
  if letter in guessed_letters:
   letters.append(letter)
  else:
   letters.append("_")
 word_displayed = "".join(letters)
 print(f"Palabra: {word_displayed}")
 
 # Verificar si se ha adivinado la palabra completa
 if word_displayed == secret_word:
  print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
  break
else:
 print(f"¡Oh no! Has agotado tus {max_fails} fallos.")
 print(f"La palabra secreta era: {secret_word}")