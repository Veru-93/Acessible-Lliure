# Crear el personaje de Tamagochi

class Tamagochi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.health = 100
        self.energy = 100
        self.happiness = 100
        self.points = 0

    def alimentar(self):
        self.health += 10
        self.energy += 5
        self.happiness += 5
        self.points += 5

    def dormir(self):
        self.health += 5
        self.energy = 100
        self.happiness -= 5
        self.points += 3

    def jugar(self):
        self.energy -= 10
        self.happiness += 10
        self.points += 2

    def bañar(self):
        self.health += 5
        self.happiness -= 5
        self.points += 3

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salud: {self.health}")
        print(f"Energía: {self.energy}")
        print(f"Felicidad: {self.happiness}")
        print(f"Puntos: {self.points}")

# Ejemplo de uso
if __name__ == "__main__":
    tamagochi = Tamagochi("Pikachu")
    tamagochi.alimentar()
    tamagochi.dormir()
    tamagochi.jugar()
    tamagochi.bañar()
    tamagochi.mostrar_estado()


class Tamagochi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.health = 100
        self.energy = 100
        self.happiness = 100
        self.points = 0

    def realizar_tarea(self, tarea):
        if tarea == "alimentar":
            self.alimentar()
        elif tarea == "dormir":
            self.dormir()
        elif tarea == "jugar":
            self.jugar()
        elif tarea == "bañar":
            self.bañar()
        else:
            print("Tarea no válida")

    def mostrar_recompensa(self):
        if self.points >= 10:
            print("¡Felicidades! Recompensa: Estrella")
            self.points -= 10

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salud: {self.health}")
        print(f"Energía: {self.energy}")
        print(f"Felicidad: {self.happiness}")
        print(f"Puntos: {self.points}")

# Ejemplo de uso
if __name__ == "__main__":
    tamagochi = Tamagochi("Pikachu")
    tamagochi.realizar_tarea("alimentar")
    tamagochi.realizar_tarea("dormir")
    tamagochi.realizar_tarea("jugar")
    tamagochi.realizar_tarea("bañar")
    tamagochi.mostrar_recompensa()
    tamagochi.mostrar_estado()
    

# Desarrollar las tareas diarias y el sistema de puntos

class Tamagochi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.health = 100
        self.energy = 100
        self.happiness = 100
        self.points = 0

    def realizar_tarea(self, tarea):
        if tarea == "alimentar":
            self.alimentar()
        elif tarea == "dormir":
            self.dormir()
        elif tarea == "jugar":
            self.jugar()
        elif tarea == "bañar":
            self.bañar()
        else:
            print("Tarea no válida")

    def mostrar_recompensa(self):
        if self.points >= 10:
            print("¡Felicidades! Recompensa: Estrella")
            self.points -= 10

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salud: {self.health}")
        print(f"Energía: {self.energy}")
        print(f"Felicidad: {self.happiness}")
        print(f"Puntos: {self.points}")

# Ejemplo de uso
if __name__ == "__main__":
    tamagochi = Tamagochi("Pikachu")
    tamagochi.realizar_tarea("alimentar")
    tamagochi.realizar_tarea("dormir")
    tamagochi.realizar_tarea("jugar")
    tamagochi.realizar_tarea("bañar")
    tamagochi.mostrar_recompensa()
    tamagochi.mostrar_estado()
    

