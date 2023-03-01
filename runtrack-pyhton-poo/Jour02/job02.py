class Livre:
    def __init__(self):
        self.titre = "1984"
        self.auteur = "George Orwell"
        self.nombre_pages = 560

    def set_livre(self, titre, auteur, nombre_pages):
        if nombre_pages < 0:
            raise ValueError("nombre_pages doit être positif")
        self.titre = titre
        self.auteur = auteur
        self.nombre_pages = nombre_pages

    def get_livre(self):
        print(f"{self.titre} par {self.auteur}, {self.nombre_pages} pages")

livre = Livre()
livre.get_livre()
livre.set_livre("Dune", "Frank Herbert,", 334)
livre.get_livre()
