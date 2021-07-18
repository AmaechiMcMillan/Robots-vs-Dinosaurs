from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
    
    def create_fleet(self):
        robot1 = Robot('CyBorg')
        robot2 = Robot('CyFi')
        robot3 = Robot('CyClops')

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
        
