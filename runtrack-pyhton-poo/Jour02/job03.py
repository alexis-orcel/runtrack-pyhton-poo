class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.titre = "Dune"
        self.auteur = "Frank Herbert"
        self.nombre_pages = 454
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def rendre(self):
        if not self.disponible:
            self.disponible = True
            return True
        return False

    def get_information(self):
        print(f"Informations :'{self.titre}' de {self.auteur}, "
              f"{self.nombre_pages} pages, {'disponible' if self.disponible else 'indisponible'}")

# Exemple d'utilisation
livre = Livre("1984", "Orson Orwell", 326)
livre.get_information()

if livre.emprunter():
    print("Livre emprunté avec succès")
livre.get_information()

if livre.rendre():
    print("Livre rendu avec succès")
livre.get_information()
