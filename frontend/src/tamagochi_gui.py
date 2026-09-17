# src/tamagochi_gui.py

import tkinter as tk
from tkinter import messagebox

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
        self.update_display()

    def dormir(self):
        self.health += 5
        self.energy = 100
        self.happiness -= 5
        self.points += 3
        self.update_display()

    def jugar(self):
        self.energy -= 10
        self.happiness += 10
        self.points += 2
        self.update_display()

    def bañar(self):
        self.health += 5
        self.happiness -= 5
        self.points += 3
        self.update_display()

    def mostrar_recompensa(self):
        if self.points >= 10:
            messagebox.showinfo("Recompensa", "¡Felicidades! Recompensa: Estrella")
            self.points -= 10
            self.update_display()

    def update_display(self):
        self.health_label.config(text=f"Salud: {self.health}")
        self.energy_label.config(text=f"Energía: {self.energy}")
        self.happiness_label.config(text=f"Felicidad: {self.happiness}")
        self.points_label.config(text=f"Puntos: {self.points}")

class TamagochiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tamagochi Retro")

        self.tamagochi = Tamagochi("Pikachu")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Tamagochi Retro").pack()

        self.health_label = tk.Label(self.root, text="Salud: 100")
        self.health_label.pack()

        self.energy_label = tk.Label(self.root, text="Energía: 100")
        self.energy_label.pack()

        self.happiness_label = tk.Label(self.root, text="Felicidad: 100")
        self.happiness_label.pack()

        self.points_label = tk.Label(self.root, text="Puntos: 0")
        self.points_label.pack()

        tk.Button(self.root, text="Alimentar", command=self.alimentar).pack()
        tk.Button(self.root, text="Dormir", command=self.dormir).pack()
        tk.Button(self.root, text="Jugar", command=self.jugar).pack()
        tk.Button(self.root, text="Bañar", command=self.bañar).pack()

        self.update_button = tk.Button(self.root, text="Revisar y Mejorar", command=self.show_feedback)
        self.update_button.pack()

    def alimentar(self):
        self.tamagochi.alimentar()

    def dormir(self):
        self.tamagochi.dormir()

    def jugar(self):
        self.tamagochi.jugar()

    def bañar(self):
        self.tamagochi.bañar()

    def show_feedback(self):
        feedback = messagebox.askyesno("Recompensa", "¿Deseas recibir una recompensa por tus acciones?")
        if feedback:
            self.tamagochi.mostrar_recompensa()

if __name__ == "__main__":
    root = tk.Tk()
    app = TamagochiApp(root)
    root.mainloop()# src/tamagochi_gui.py

import tkinter as tk
from tkinter import messagebox

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
        self.update_display()

    def dormir(self):
        self.health += 5
        self.energy = 100
        self.happiness -= 5
        self.points += 3
        self.update_display()

    def jugar(self):
        self.energy -= 10
        self.happiness += 10
        self.points += 2
        self.update_display()

    def bañar(self):
        self.health += 5
        self.happiness -= 5
        self.points += 3
        self.update_display()

    def mostrar_recompensa(self):
        if self.points >= 10:
            messagebox.showinfo("Recompensa", "¡Felicidades! Recompensa: Estrella")
            self.points -= 10
            self.update_display()

    def update_display(self):
        self.health_label.config(text=f"Salud: {self.health}")
        self.energy_label.config(text=f"Energía: {self.energy}")
        self.happiness_label.config(text=f"Felicidad: {self.happiness}")
        self.points_label.config(text=f"Puntos: {self.points}")

class TamagochiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tamagochi Retro")

        self.tamagochi = Tamagochi("Pikachu")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Tamagochi Retro").pack()

        self.health_label = tk.Label(self.root, text="Salud: 100")
        self.health_label.pack()

        self.energy_label = tk.Label(self.root, text="Energía: 100")
        self.energy_label.pack()

        self.happiness_label = tk.Label(self.root, text="Felicidad: 100")
        self.happiness_label.pack()

        self.points_label = tk.Label(self.root, text="Puntos: 0")
        self.points_label.pack()

        tk.Button(self.root, text="Alimentar", command=self.alimentar).pack()
        tk.Button(self.root, text="Dormir", command=self.dormir).pack()
        tk.Button(self.root, text="Jugar", command=self.jugar).pack()
        tk.Button(self.root, text="Bañar", command=self.bañar).pack()

        self.update_button = tk.Button(self.root, text="Revisar y Mejorar", command=self.show_feedback)
        self.update_button.pack()

    def alimentar(self):
        self.tamagochi.alimentar()

    def dormir(self):
        self.tamagochi.dormir()

    def jugar(self):
        self.tamagochi.jugar()

    def bañar(self):
        self.tamagochi.bañar()

    def show_feedback(self):
        feedback = messagebox.askyesno("Recompensa", "¿Deseas recibir una recompensa por tus acciones?")
        if feedback:
            self.tamagochi.mostrar_recompensa()

if __name__ == "__main__":
    root = tk.Tk()
    app = TamagochiApp(root)
    root.mainloop()