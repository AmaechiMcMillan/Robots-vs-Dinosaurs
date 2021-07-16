from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print(f"Welcome to Robots vs. Dinosaurs!")

    def battle(self):
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            dice_roll = random.randint(1, 10)
            of dice_roll % 2 == 0 

    def dino_turn(self):
        pass

    def robo_turn(self):
        self.show_robo_opponent_options()
        robot_choice = int(input("Which robot will attack?"))
        self.show_dino_opponent_options()
        dino_choice = int(input("Which dinosaur will defend?"))
        self.fleet.robots[robot_choice].attack(
            self.herd.dinosaurs[dino_choice])
        if self.herd.dinosaurs[dino_choice].health <= 0:
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_choice])    

    def show_dino_opponent_options(self):
        print("Choose your dinosaur!")
        index = 0
        for dinosaur in  self.herd.dinosaurs:
            print(f"Press {index} ")

    def show_robo_opponent_options(self):