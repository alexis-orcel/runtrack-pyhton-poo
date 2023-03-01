class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return print("Les valeurs de x et y sont : ", self.x, "et", self.y)

    def afficherX(self):
        return print("La valeur de x est : ", self.x)

    def afficherY(self):
        return print("La valeur de y est : ", self.y)

    def changerX(self):
        self.x = 10
        return print("La nouvelle valeur de x est : ", self.x)

    def changerY(self):
        self.y = 10
        return print("La nouvelle valeur de y est : ", self.y)


Point(4, 6).afficherLesPoints()
Point(2, 9).afficherX()
Point(1, 7).afficherY()
Point(9, 9).changerX()
Point(8, 2).changerY()