class Ville:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def increase_population(self):
        self.population += 1

    def get_population(self):
        return self.population

    def display_info(self):
        print("Nom de la ville : ", self.name)
        print("Population : ", self.population)


class Personne:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.city.increase_population()

    def display_info(self):
        print("Nom de l'habitant : ", self.name)
        print("Age de l'habitant : ", self.age)


v1 = Ville("Lyon", 230000)
v2 = Ville("Marseille", 827803)

p1 = Personne("Alexis", 33, v1)
p2 = Personne("Benoit", 14, v1)
p3 = Personne("Zoé", 9, v2)

v1.display_info()
v2.display_info()
