class Person:
    def __init__(self, first_name, last_name, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession

    def person_info(self):
        return f"{self.first_name} {self.last_name}, kasbi: {self.profession}"

class Teacher(Person):
    def __init__(self, first_name, last_name, profession, experience, speciality):
        super().__init__(first_name, last_name, profession)
        self.experience = experience
        self.speciality = speciality

    def person_info(self):
        info = super().person_info()
        return f"{info}, {self.speciality} sohasida {self.experience} yil ishlagan"

    def action(self, action_name):
        return f"{self.first_name} {self.last_name} {action_name}"

    def update_experience(self, new_experience):
        self.experience = new_experience

# Test qismi
person = Teacher("Falonchi", "Pistonchiyev", "O'qituvchi", 10, "Matematika")
print(person.person_info())  # O'qituvchi Falonchi Pistonchiyev, Matematika sohasida 10 yil ishlagan
print(person.action("dars beradi"))  # Falonchi Pistonchiyev dars beradi
person.update_experience(12)
print(person.person_info())  # O'qituvchi Falonchi Pistonchiyev, Matematika sohasida 12 yil ishlagan
