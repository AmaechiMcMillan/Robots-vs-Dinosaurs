from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_fleet()
    
    def create_fleet(self):
        dinosaur1 = Dinosaur('Chicken')
        dinosaur2 = Dinosaur('Godzilla')
        dinosaur3 = Dinosaur('Tyrant')

        self.dinosaurs.append(dinosaur1)
        self.dinosaurs.append(dinosaur2)
        self.dinosaurs.append(dinosaur3)
