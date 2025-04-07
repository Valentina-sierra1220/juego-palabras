from logica_palabras import JuegoPalabrasDificil

def iniciar_juego():
    print("🎮 BIENVENIDO AL DESAFÍO ULTRA: ¡ADIVINA LA PALABRA IMPOSIBLE!")
    print("Adivina la palabra correcta usando letras mezcladas. Tienes 10 segundos y solo 3 intentos por palabra.")
    print("¿Estás listo? 😈\n")

    juego = JuegoPalabrasDificil()

    while juego.vidas > 0:
        juego.mostrar_estado()
        juego.jugar_ronda()

    print("\n💀 JUEGO TERMINADO 💀")
    print(f"🎯 Puntaje final: {juego.puntos}")
    juego.mostrar_logros()

if _name_ == "_main_":
    iniciar_juego()