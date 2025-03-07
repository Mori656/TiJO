class StudentManagement:
    """
    Klasa zarzadzajaca studentami i ich ocenami.
    """
    def __init__(self):
        self._students = []
        self._grades = []

    def add_student(self, id: str, name: str, age: int) -> bool:
        """
        Dodaje nowego studenta do bazy danych.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli dodanie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if(id and name and age):
            self._students.append({"id":id,"name":name,"age":age})
            return True
        return  False

    def update_student(self, id: str, name: str, age: int) -> bool:
        """
        Aktualizuje dane istniejacego studenta na podstawie identyfikatora.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli aktualizacja zakonczyla sie sukcesem.
            False w przeciwnym wypadku.
        """
        if(id and name and age):
            for student in self._students:
                if id in student["id"]:
                    self._students.append({"id":id,"name":name,"age":age})
                    return True
        return  False

    def remove_student(self, id: str) -> bool:
        """
        Usuwa studenta z bazy danych na podstawie jego identyfikatora.

        Args:
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli usuniecie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        for student in self._students:
            if id in student["id"]:
                self._students.remove(student)
                return True
        return  False

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Dodaje ocene z danego przedmiotu dla okreslonego studenta.

        Args:
            student_id: Unikalny identyfikator studenta.
            subject: Nazwa przedmiotu.
            grade: Ocena.

        Returns:
            True, jesli dodanie oceny zakonczylo sie sukcesem (2.0, 3.0, 3.5, 4.0, 4.5, 5.0),
            False w przeciwnym razie.
        """
        if(student_id and subject and grade):
            self._grades.append({"student_id":student_id,"subject":subject,"grade":grade})
            return True
        return  False

    def avg_grades(self, subject: str) -> float:
        """
        Oblicza srednia ocen z danego przedmiotu dla wszystkich studentow.

        Args:
            subject: Nazwa przedmiotu.

        Returns:
            Srednia ocen z przedmiotu jako liczba zmiennoprzecinkowa.
        """
        sum = 0.0
        count = 0
        for grade in self._grades:
            if grade["subject"] == subject:
                sum = sum + grade["grade"]
                count = count + 1
        if count > 0:
            return sum/count
        return None