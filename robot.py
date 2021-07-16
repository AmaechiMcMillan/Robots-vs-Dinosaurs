# Make a class for the following: Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield
# Give the robot a name, health, and a weapon with a name and attack power
# Give the dinosaur a name, health and attack power
# Instantiate three robot and dinosaur objects and assign the appropriate values to the objects
# Store robot objects in a Fleet and dinosaur objects in a herd (fleet and herd must use a List to store the objects)
# Have robot attack dinosaur and vice versa on a battlefield
# Have robot/dinosaur lose attack points (base on attack power) when another robot/dinosaur attacks it

from weapon import Weapon

class Robot:
    def __init__(self, name, health): 
        self.name = name
        self.health = 100
        self.weapon = Weapon('Kino', 25)

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
