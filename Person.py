
from typing import Optional
from Address import Address # Mengimpor Address untuk relasi "lives at"

# Menerapkan atribut dan method dasar yang dimiliki oleh semua entitas Person.
class Person:
    def __init__(self, name: str, phone_number: str, email_address: str, address: Optional[Address] = None):
        self.name: str = name
        self.phoneNumber: str = phone_number
        self.emailAddress: str = email_address
        self.lives_at: Optional[Address] = address

    def purchaseParkingPass(self) -> bool:
        print(f"Parking pass purchased for {self.name}.")
        return True

    def get_details(self) -> str:
        address_label = self.lives_at.outputAsLabel() if self.lives_at else "No Address Specified"
        return (f"Name: {self.name}\n"
                f"Phone: {self.phoneNumber}\n"
                f"Email: {self.emailAddress}\n"
                f"Address: {address_label}")

# Contoh Penggunaan:
# addr = Address("10 King St", "Bandung", "Jawa Barat", 40001, "Indonesia")
# person = Person("Budi Santoso", "08123456789", "budi.s@example.com", addr)
# print(person.get_details())

# person.purchaseParkingPass()
