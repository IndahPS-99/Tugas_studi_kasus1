
import re

class Address:
    def __init__(self, street: str, city: str, state: str, postal_code: int, country: str):
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.postalCode: int = postal_code
        self.country: str = country

    def validate(self) -> bool:
        if not all([self.street, self.city, self.state, self.country]):
            return False
        if not isinstance(self.postalCode, int) or self.postalCode <= 0:
            return False
        return True

    def outputAsLabel(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.postalCode}, {self.country}"

# Contoh Penggunaan:
# address1 = Address("123 Main St", "Jakarta", "DKI Jakarta", 10001, "Indonesia")

# print(address1.outputAsLabel())
