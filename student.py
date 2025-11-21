class Student:
    def __init__(self,etunimi:str, sukunimi:str):
        self.etunimi = etunimi.capitalize()
        self.sukunimi = sukunimi.capitalize()
        self._kurssia = []
    def add_course(self,course_name:str):
        self._kurssia.append(course_name)

    def add_courses(self,course_name:list):
        self._kurssia.extend(course_name)

    def print_courses(self):
        if ( self._kurssia ):
            print(f"Course listing for {self.etunimi} {self.sukunimi}:")
            for course in self._kurssia:
                print(f"- {course}")
        else:
            print(f"No courses for {self.etunimi} {self.sukunimi}")
bob = Student('Bob', 'Edwards')
# bob.add_course('Math')
# bob.add_course('IT')
# bob.add_course('Art')
bob.add_courses(['Math','IT','Art'])
bob.print_courses()