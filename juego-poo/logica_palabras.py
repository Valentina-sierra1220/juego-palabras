import random
import time


class JuegoPalabrasDificil:
    def __init__(self):
        self.categorias = {
    "animales": ["hipopotamo", "murcielago", "camaleon", "rinoceronte", "alce", "jaguar"],
    "frutas": ["mandarina", "frambuesa", "cereza", "arándano", "ciruela", "pomelo"],
    "paises": ["azerbaiyan", "mozambique", "singapur", "ucrania", "argentina", "colombia"]
}
        self.vidas = 5
        self.puntos = 0
        self.racha = 0
        self.dificultad = 1
        self.palabras_usadas = set()
        self.logros = set()

    def elegir_palabra(self):
        while True:
            categoria = random.choice(list(self.categorias.keys()))
            palabra = random.choice(self.categorias[categoria])
            if palabra not in self.palabras_usadas:
                self.palabras_usadas.add(palabra)
                return categoria, palabra

    def crear_desafio(self, palabra: any):
        letras = list(palabra)
        if self.dificultad >= 3:
            letras_falsas: any = random.choices("qwxzv", k=2)
            letras += letras_falsas
        random.shuffle(letras)
        return "".join(letras)

    def jugar_ronda(self)-> None:
        categoria, palabra = self.elegir_palabra()
        mezcla = self.crear_desafio(palabra)

        print(f"\n🧩 Letras mezcladas: {mezcla}")
        print(f"📁 Categoría: {categoria.upper()}")
        print("⏳ Tienes 20 segundos para adivinar la palabra...")

        intentos: int = 3
        tiempo_limite: int = 20
        inicio: float = time.time()

        while intentos > 0:
            intento: str = input(f"✏️ Intenta adivinar la palabra (intentos restantes: {intentos}): ").lower()
            tiempo = time.time() - inicio

            if tiempo > tiempo_limite:
                print(f"\n⏱️ ¡Te pasaste del tiempo! ({int(tiempo)} segundos)")
                print("❌ Ronda perdida.")
                self.vidas -= 1
                return

            if intento == palabra:
                print("✅ ¡Correcto!")
                self.puntos += 15 + self.racha * 5
                self.racha += 1
                self.dificultad: int = min(5, self.dificultad + 1)
                self.verificar_logros()
                return
            else:
                print("❌ Incorrecto.")
                intentos -= 1

                print(f"💀 Fallaste. La palabra era: {palabra}")
                self.vidas -= 1
                self.racha: int = 0

    def verificar_logros(self) -> None:
        if self.puntos >= 60:
            self.logros.add("💥 Genio del vocabulario")
        if self.racha >= 4:
            self.logros.add("🔥 Racha épica (4 seguidas)")
        if self.dificultad == 5:
            self.logros.add("👑 Modo maestro activado")

    def mostrar_estado(self) -> None:
        print(f"\n❤ Vidas: {self.vidas} | ⭐ Puntos: {self.puntos} | 🔥 Racha: {self.racha} | 🎯 Dificultad: {self.dificultad}")

    def mostrar_logros(self):
        if self.logros:
            print("\n 🏆 LOGROS DESBLOQUEADOS:")
            for logro in self.logros:
                print("-", logro)

if __name__== "__main__":
    juego = JuegoPalabrasDificil()
    print("🎮 Bienvenido al juego de palabras difíciles")

    while juego.vidas > 0:
        juego.jugar_ronda()
        juego.mostrar_estado()

    juego.mostrar_logros()
    print("\n🏁 ¡Juego terminado!")














