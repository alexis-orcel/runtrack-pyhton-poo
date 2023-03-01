class Personnage:
    def __init__(self):
        self.x = 14
        self.y = 11

    def gauche(self):
        self.x -= 1
        return self.x

    def droite(self):
        self.x += 1
        return self.x

    def haut(self):
        self.y += 1
        return self.y

    def bas(self):
        self.y -= 1
        return self.y

    def position(self):
        my_tuple = (self.x, self.y)
        return print("La position du personnage est : ", my_tuple)


personnage = Personnage()
personnage.position()
personnage.gauche()
personnage.haut()
personnage.position()