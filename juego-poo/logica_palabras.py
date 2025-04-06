import random
import time

class JuegoPalabrasDificil:
    def _init_(self):
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

    def crear_desafio(self, palabra):
        letras = list(palabra)
        if self.dificultad >= 3:
            letras_falsas = random.choices("qwxzv", k=2)
            letras += letras_falsas
        random.shuffle(letras)
        return "".join(letras)

    def jugar_ronda(self):
        categoria, palabra = self.elegir_palabra()
        mezcla = self.crear_desafio(palabra)

        print(f"\n🧩 Letras mezcladas: {mezcla}")
        print(f"📁 Categoría: {categoria.upper()}")
        print("⏳ Tienes 20 segundos para adivinar la palabra...")

        intentos = 3
        tiempo_limite = 20
        inicio = time.time()

        while intentos > 0:
            intento = input(f"✏️ Intenta adivinar la palabra (intentos restantes: {intentos}): ").lower()
            tiempo = time.time() - inicio

            if tiempo > tiempo_limite:
                print(f"\n⏱️ ¡Te pasaste del tiempo! ({int(tiempo)} segundos)")
                print("❌ Ronda perdida.")
                self.vidas -= 1
                return


