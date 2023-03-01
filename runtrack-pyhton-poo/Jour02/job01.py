class Rectangle:
    def __init__(self):
        self._longueur = 11
        self._largeur = 7

    @property
    def dimensions(self):
        return self._longueur, self._largeur

    @dimensions.setter
    def dimensions(self, new_dimensions):
        self._longueur, self._largeur = new_dimensions

    def resize(self):
        print("Avant appel au mutateur :", self.dimensions)
        self.dimensions = (24, 32)
        print("Après appel au mutateur :", self.dimensions)


rect = Rectangle()
rect.resize()
