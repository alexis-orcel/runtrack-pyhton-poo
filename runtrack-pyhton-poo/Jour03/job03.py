class Tache:
    def __init__(self, nom, description, statut):
        self.nom = nom
        self.description = description
        self.statut = statut

    def get_nom(self):
        return self.nom

    def get_description(self):
        return self.description

    def get_statut(self):
        return self.statut


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, nom):
        for tache in self.taches:
            if tache.nom == nom:
                self.taches.remove(tache)

    def marquerCommeFinie(self, nom):
        for tache in self.taches:
            if tache.nom == nom and tache.statut == "A faire":
                tache.statut = "Terminé"
                print(f"La tâche \"{nom}\" a été marquée comme terminée.")

    def afficherListe(self):
        print("Liste de tâches : ")
        for tache in self.taches:
            print(f"    - {tache.nom} : {tache.description}, {tache.statut}")

    def filtrerListe(self):
        self.a_faire = []
        self.termine = []
        for tache in self.taches:
            if tache.statut == "A faire":
                self.a_faire.append(tache)
            elif tache.statut == "Terminé":
                self.termine.append(tache)
        self.taches = self.a_faire + self.termine


t1 = Tache("Faire les courses", "Acheter des légumes et des fruits", "A faire")
t2 = Tache("Réviser pour examen", "Relire les cours et faire des exercices", "Terminé")
t3 = Tache("Faire le ménage", "Nettoyer la cuisine et les toilettes", "A faire")

l1 = ListeDeTaches()
l1.ajouterTache(t1)
l1.ajouterTache(t2)
l1.ajouterTache(t3)
l1.afficherListe()

l1.marquerCommeFinie("Faire les courses")
l1.afficherListe()
t1 = Tache("Menage", "Laver sols", "A faire")
t2 = Tache("Jardin", "Planter tomates", "Terminé")
t3 = Tache("Linge", "Laver linge", "A faire")

l1 = ListeDeTaches()
l1.ajouterTache(t1)
l1.ajouterTache(t2)
l1.ajouterTache(t3)

# Filtrer la liste pour n'avoir que les tâches à faire
l1.filtrerListe()
l1.afficherListe()

# Marquer la tâche "Menage" comme terminée
for tache in l1.taches:
    if tache.titre == "Menage":
        l1.marquerCommeFinie(tache)

# Supprimer la tâche "Linge"
l1.supprimerTache("Linge")
l1.afficherListe()
