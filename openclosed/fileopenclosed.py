class Holberton:
    def __init__(self, name):
        self.name = name

class Cohort:
    def __init__(self, students):
        self.students = students

    def add_student(self, new_student):
        self.students.append(new_student)
        print(f"Added: {new_student.name}")

# c'est l'etat initial La classe est "Closed"
s1 = Holberton("Alexandre")
s2 = Holberton("Maxwell")
my_cohort = Cohort([s1, s2])

# c'est Extension La classe est "Open"
s3 = Holberton("Lucasssssssss")
my_cohort = Cohort(s3)
