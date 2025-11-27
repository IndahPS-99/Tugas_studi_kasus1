
from Person import Person
from typing import TYPE_CHECKING, Optional

# Digunakan untuk menghindari masalah circular dependency selama type hinting.
if TYPE_CHECKING:
    from Professor import Professor 

class Student(Person):
    def __init__(self, name: str, phone_number: str, email_address: str, student_number: int, average_mark: int, address=None):
        super().__init__(name, phone_number, email_address, address)
        self.studentNumber: int = student_number
        self.averageMark: int = average_mark
        self.supervisor: Optional['Professor'] = None 

    def isEligibleToEnroll(self, program_code: str) -> bool:
        print(f"Checking eligibility for {self.name} to enroll in {program_code}...")
        return self.averageMark > 70

    def getSeminarsTaken(self) -> int:
        return 5 
    
    def get_details(self) -> str:
        basic_details = super().get_details()
        supervisor_name = self.supervisor.name if self.supervisor else "None"
        return (f"--- Student Details ---\n"
                f"{basic_details}\n"
                f"Student Number: {self.studentNumber}\n"
                f"Average Mark: {self.averageMark}\n"
                f"Supervisor: {supervisor_name}")


# Contoh Penggunaan akan ada di main.py
