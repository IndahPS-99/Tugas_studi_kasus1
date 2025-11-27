"""
Definisi kelas Student.
Mewarisi dari Person.
"""
from Person import Person
from typing import TYPE_CHECKING, Optional

# Digunakan untuk menghindari masalah circular dependency selama type hinting.
if TYPE_CHECKING:
    from Professor import Professor 

class Student(Person):
    """
    Kelas Student, mewarisi dari Person.
    """
    def __init__(self, name: str, phone_number: str, email_address: str, student_number: int, average_mark: int, address=None):
        """
        Konstruktor untuk kelas Student.

        :param name: Nama lengkap.
        :param phone_number: Nomor telepon.
        :param email_address: Alamat email.
        :param student_number: Nomor identifikasi mahasiswa.
        :param average_mark: Rata-rata nilai (0-100).
        :param address: Objek Address (optional).
        """
        super().__init__(name, phone_number, email_address, address)
        self.studentNumber: int = student_number
        self.averageMark: int = average_mark
        # Relasi 0..* supervises 1..5 akan dikelola di kelas Professor, 
        # namun Student mungkin menyimpan referensi supervisor
        self.supervisor: Optional['Professor'] = None 

    def isEligibleToEnroll(self, program_code: str) -> bool:
        """
        Memeriksa apakah siswa memenuhi syarat untuk mendaftar program studi tertentu.
        Asumsi: Harus memiliki rata-rata nilai di atas 70.

        :param program_code: Kode program studi (string).
        :return: True jika memenuhi syarat, False sebaliknya.
        """
        print(f"Checking eligibility for {self.name} to enroll in {program_code}...")
        return self.averageMark > 70

    def getSeminarsTaken(self) -> int:
        """
        Mengembalikan jumlah seminar yang telah diambil oleh siswa.
        Asumsi implementasi dasar: mengembalikan nilai tetap.

        :return: Jumlah seminar yang telah diambil (integer).
        """
        # Dalam implementasi nyata, ini akan mengambil data dari sistem.
        return 5 
    
    def get_details(self) -> str:
        """
        Mengoverride method get_details untuk menyertakan detail Student.

        :return: String berisi detail lengkap Student.
        """
        basic_details = super().get_details()
        supervisor_name = self.supervisor.name if self.supervisor else "None"
        return (f"--- Student Details ---\n"
                f"{basic_details}\n"
                f"Student Number: {self.studentNumber}\n"
                f"Average Mark: {self.averageMark}\n"
                f"Supervisor: {supervisor_name}")

# Contoh Penggunaan akan ada di main.py