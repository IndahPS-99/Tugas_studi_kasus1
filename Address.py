"""
Definisi kelas Address.
Merepresentasikan alamat fisik.
"""
import re

class Address:
    """
    Kelas untuk merepresentasikan alamat.
    """
    def __init__(self, street: str, city: str, state: str, postal_code: int, country: str):
        """
        Konstruktor untuk kelas Address.

        :param street: Nama jalan atau detail alamat.
        :param city: Nama kota.
        :param state: Nama provinsi/negara bagian.
        :param postal_code: Kode pos (integer).
        :param country: Nama negara.
        """
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.postalCode: int = postal_code
        self.country: str = country

    def validate(self) -> bool:
        """
        Memvalidasi alamat.
        Untuk tujuan demonstrasi, ini hanya memeriksa apakah semua string non-kosong dan postalCode positif.

        :return: True jika alamat dianggap valid, False sebaliknya.
        """
        if not all([self.street, self.city, self.state, self.country]):
            return False
        if not isinstance(self.postalCode, int) or self.postalCode <= 0:
            return False
        
        # Contoh validasi sederhana pada format kode pos 
        # (misalnya, 5 digit angka, asumsi format US/Indonesia)
        # Jika country adalah "USA", mungkin perlu 5-9 digit.
        # Untuk kasus ini, kita hanya memastikan postalCode adalah integer positif.
        return True

    def outputAsLabel(self) -> str:
        """
        Menghasilkan representasi alamat sebagai label berformat string.

        :return: String yang merepresentasikan alamat lengkap.
        """
        return f"{self.street}, {self.city}, {self.state} {self.postalCode}, {self.country}"

# Contoh Penggunaan:
# address1 = Address("123 Main St", "Jakarta", "DKI Jakarta", 10001, "Indonesia")
# print(address1.outputAsLabel())