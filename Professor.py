
from Person import Person
from Student import Student # Mengimpor Student untuk relasi "supervises"
from typing import List, Optional

class Professor(Person):
    # Kelas Professor, mewarisi dari Person
    def __init__(self, name: str, phone_number: str, email_address: str, staff_number: int, years_of_service: int, number_of_classes: int, salary: Optional[int] = None, address=None):
        super().__init__(name, phone_number, email_address, address)
        
        # Protected attribute (#staffNumber)
        self._staffNumber: int = staff_number
        
        # Private attribute (-yearsOfService)
        self.__yearsOfService: int = years_of_service 
        
        self.numberOfClasses: int = number_of_classes
        self._supervised_students: List[Student] = [] # Relasi 1..5

    @property
    def salary(self) -> int:
        """
        Atribut derived (/salary). 
        Asumsi: Gaji dihitung berdasarkan tahun pelayanan dan jumlah kelas.
        """
        # Formula gaji sederhana (misal: 50000 + 2000 * tahun layanan + 500 * jumlah kelas)
        return 50000 + (2000 * self.__yearsOfService) + (500 * self.numberOfClasses)

    def add_student(self, student: Student) -> bool:
        """
        Menambahkan Student ke daftar mahasiswa yang disupervisi (relasi 1..5).

        :param student: Objek Student yang akan disupervisi.
        :return: True jika berhasil ditambahkan, False jika sudah mencapai batas (5).
        """
        if len(self._supervised_students) < 5:
            self._supervised_students.append(student)
            student.supervisor = self # Mengatur balik relasi pada objek Student
            print(f"{student.name} sekarang disupervisi oleh {self.name}.")
            return True
        else:
            print(f"FAILED: {self.name} sudah mencapai batas supervisi (5 mahasiswa).")
            return False

    def get_supervised_students(self) -> List[Student]:
        """
        Mengembalikan daftar mahasiswa yang disupervisi.

        :return: List objek Student.
        """
        return self._supervised_students

    def get_details(self) -> str:
        """
        Mengoverride method get_details untuk menyertakan detail Professor.

        :return: String berisi detail lengkap Professor.
        """
        basic_details = super().get_details()
        
        student_names = [s.name for s in self._supervised_students]
        
        return (f"--- Professor Details ---\n"
                f"{basic_details}\n"
                f"Staff Number: {self._staffNumber} (Protected)\n"
                f"Years of Service: {self.__yearsOfService} (Private)\n"
                f"Number of Classes: {self.numberOfClasses}\n"
                f"Salary: ${self.salary:,} (Derived/Read-only)\n"
                f"Supervises ({len(student_names)}): {', '.join(student_names) if student_names else 'None'}")

# Contoh Penggunaan akan ada di main.py