"""
Definisi kelas Person (abstrak) dan relasi agregasi ke Address.
"""
from typing import Optional
from Address import Address # Mengimpor Address untuk relasi "lives at"

class Person:
    """
    Kelas dasar untuk semua orang dalam sistem (Person).
    Menerapkan atribut dan method dasar yang dimiliki oleh semua entitas Person.
    """
    def __init__(self, name: str, phone_number: str, email_address: str, address: Optional[Address] = None):
        """
        Konstruktor untuk kelas Person.

        :param name: Nama lengkap.
        :param phone_number: Nomor telepon.
        :param email_address: Alamat email.
        :param address: Objek Address yang merepresentasikan alamat tempat tinggal (relasi 0..1 lives at 1).
        """
        self.name: str = name
        self.phoneNumber: str = phone_number
        self.emailAddress: str = email_address
        self.lives_at: Optional[Address] = address

    def purchaseParkingPass(self) -> bool:
        """
        Method untuk memproses pembelian kartu parkir.
        Implementasi dasar hanya mengembalikan True.

        :return: True jika pembelian berhasil.
        """
        print(f"Parking pass purchased for {self.name}.")
        return True

    def get_details(self) -> str:
        """
        Method umum untuk mendapatkan detail Person.

        :return: String berisi detail dasar Person.
        """
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