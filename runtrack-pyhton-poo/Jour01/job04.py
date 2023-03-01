class Personne:
    def __init__(self, name, firstname):
        self.nom = name
        self.prenom = firstname

    def SePresenter(self):
        return print("Je suis ", self.prenom, self.nom)


Personne("Doe", "John").SePresenter()
Personne("Dupond", "Jean").SePresenter()