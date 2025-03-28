import sys

class CosmoCar:
    directions = {1:"up",2:"right",3:"down",4:"left"}
    def __init__(self,x,y,d):
        self.cords = {"x":x,"y":y}
        self.direction = d
        pass

    def rotate(self,turn):
        if turn == "left":
            if self.direction - 1 < 1:
                self.direction = 4
            else:
                self.direction -= 1
        else:
            if self.direction + 1 > 4:
                self.direction = 1
            else:
                self.direction += 1

    def move(self,f):
        match(self.directions[self.direction]):
            case "up":
                 self.cords['y'] += f
            case "right":
                self.cords['x'] += f
            case "down":
                self.cords['y'] -= f
            case "left":
                self.cords['x'] -= f
        self.checkPosition()

    def checkPosition(self):
        print(self.cords)


def main():
    c = CosmoCar(5,5,3)
    c.move(5)
    c.rotate("right")
    c.move(5)
    return 0

if __name__ == '__main__':
    sys.exit(main())
    pass