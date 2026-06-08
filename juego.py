import random

def obtener_palabra():
    # Lista de palabras relacionadas con la asignatura
    palabras = ["SOFTWARE", "JIRA", "CONFLUENCE", "GIT", "GITHUB", "AGIL", "SPRINT"]
    return random.choice(palabras).upper()

def jugar():
    palabra_secreta = obtener_palabra()
    letras_adivinadas = []
    intentos_restantes = 6
    
    print("=======================================")
    print(" ¡BIENVENIDO AL JUEGO DEL AHORCADO!    ")
    print(" Metodologías de Desarrollo de Software")
    print("=======================================\n")
    print(f"Pista: La palabra tiene {len(palabra_secreta)} letras.")

    while intentos_restantes > 0:
        # Mostrar el progreso de la palabra
        estado_actual = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                estado_actual += letra + " "
            else:
                estado_actual += "_ "
        
        print("\nPalabra: " + estado_actual.strip())
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras intentadas: {', '.join(letras_adivinadas)}")
        
        # Verificar si ya adivinó toda la palabra
        if "_" not in estado_actual:
            print("\n¡FELICITACIONES! Has ganado el juego. 🎉")
            print("\n HAZ LOGRADO ENCONTRAR LA PALABRA SECRETA: " + palabra_secreta)
            break
            
        # Pedir letra al jugador
        intento = input("Introduce una letra: ").upper()
        
        # Validaciones sencillas
        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, introduce solo una letra válida.")
            continue
            
        if intento in letras_adivinadas:
            print("Ya habías intentado esa letra. Prueba otra.")
            continue
            
        letras_adivinadas.append(intento)
        
        # Verificar si la letra está en la palabra
        if intento in palabra_secreta:
            print(f"¡Bien hecho! La letra '{intento}' sí está.")
        else:
            print(f"Lo siento, la letra '{intento}' no está en la palabra.")
            intentos_restantes -= 1
            
    if intentos_restantes == 0:
        print("\n=======================================")
        print(f"¡OH NO! Te has quedado sin intentos. 💀")
        print(f"La palabra correcta era: {palabra_secreta}")
        print("=======================================")

if __name__ == "__main__":
    jugar()