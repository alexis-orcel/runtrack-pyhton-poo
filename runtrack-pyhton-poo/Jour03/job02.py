class CompteBancaire:
    def __init__(self, numero_compte: int, nom: str, prenom: str, solde: float, decouvert_autorise: bool):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert_autorise = decouvert_autorise

    def get_numero_compte(self) -> int:
        return self.__numero_compte

    def get_nom(self) -> str:
        return self.__nom

    def get_prenom(self) -> str:
        return self.__prenom

    def get_solde(self) -> float:
        return self.__solde

    def afficher(self) -> None:
        print(f"Numéro de compte : {self.get_numero_compte()}")
        print(f"Nom : {self.get_nom()}")
        print(f"Prénom : {self.get_prenom()}")

    def afficher_solde(self) -> None:
        print(f"Solde actuel : {self.get_solde()}")

    def versement(self, montant: float) -> None:
        self.__solde += montant

    def retrait(self, montant: float) -> None:
        if self.__decouvert_autorise == True:
            self.__solde -= montant
            self.agios(0.01)
        else:
            if (self.__solde - montant) > 0:
                self.__solde -= montant
            else:
                print("Retrait refusé")

    def agios(self, agios: float) -> None:
        if self.__solde < 0:
            self.__solde -= (agios * self.__solde)
            print("Agios prélevé")

    def virement(self, reference: int, compte_destinataire: 'CompteBancaire', montant: float) -> None:
        if self.get_solde() < montant:
            print("Virement impossible, solde inférieur")
        else:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de référence {reference} effectué")


compte1 = CompteBancaire(1, "Dupont", "Jean", 200, True)
compte1.versement(300)
compte1.retrait(100)
compte1.afficher()
compte1.afficher_solde()

compte2 = CompteBancaire(2, "Martin", "Marie", -100, True)
compte2.afficher()
compte2.afficher_solde()
compte1.virement(0, compte2, 100)
compte2.afficher_solde()
