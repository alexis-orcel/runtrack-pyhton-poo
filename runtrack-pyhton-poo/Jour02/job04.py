class Student:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.credits = 0
        self.grade = None

    def add_credits(self, credit):
        if credit > 0:
            self.credits += credit
            self.grade = self.get_grade()

    def get_grade(self):
        if self.credits >= 90:
            return "Excellent"
        elif self.credits >= 80:
            return "Très Bien"
        elif self.credits >= 70:
            return "Bien"
        elif self.credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def show_credits(self):
        self.add_credits(40)
        self.add_credits(50)
        print(f"{self.first_name} {self.last_name} a {self.credits} crédits.")

    def show_info(self):
        print(f"Nom : {self.last_name}"
              f"\nPrénom : {self.first_name}"
              f"\nId : {self.id_number}"
              f"\nNiveau : {self.grade}")


student_01 = Student("John", "Doe", 145)
student_01.show_credits()
student_01.show_info()
