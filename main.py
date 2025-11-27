
from Address import Address
from Student import Student
from Professor import Professor

def main():
    print("--- Demonstrasi Implementasi Class Diagram ---")
    print("-" * 40)

    # 1. Membuat Objek Address
    address_prof = Address(
        street="456 Academic Ave", 
        city="Bandung", 
        state="Jawa Barat", 
        postal_code=40132, 
        country="Indonesia"
    )
    print(f"Address: {address_prof.outputAsLabel()}")
    print(f"Address Valid: {address_prof.validate()}")
    print("-" * 40)

    # 2. Membuat Objek Professor
    prof_diana = Professor(
        name="Prof. Diana Wijaya, Ph.D.",
        phone_number="08765432100",
        email_address="diana.w@uni.ac.id",
        staff_number=9001,
        years_of_service=12,
        number_of_classes=3,
        address=address_prof 
    )
    
    # 3. Membuat Objek Student
    student_ali = Student(
        name="Ali Firdaus",
        phone_number="08112233445",
        email_address="ali.f@student.uni.ac.id",
        student_number=2023001,
        average_mark=85,
        address=Address("789 Student Dorm", "Bandung", "Jawa Barat", 40133, "Indonesia")
    )
    
    student_bela = Student(
        name="Bela Citra",
        phone_number="08221144556",
        email_address="bela.c@student.uni.ac.id",
        student_number=2023002,
        average_mark=65,
    )
    
    student_cici = Student(
        name="Cici Dewi",
        phone_number="08998877665",
        email_address="cici.d@student.uni.ac.id",
        student_number=2023003,
        average_mark=92,
    )

    # 4. Demonstrasi Relasi Supervisi (1..5)
    print("--- Demonstrasi Supervisi ---")
    prof_diana.add_student(student_ali)
    prof_diana.add_student(student_bela)
    prof_diana.add_student(student_cici)
    print("-" * 40)
    
    # 5. Demonstrasi Method Professor dan Derived Attribute
    print(prof_diana.get_details())
    prof_diana.purchaseParkingPass()
    print("-" * 40)

    # 6. Demonstrasi Method Student
    print(student_ali.get_details())
    print(f"Ali Eligible to Enroll: {student_ali.isEligibleToEnroll('CS101')}")
    print(f"Ali Seminars Taken: {student_ali.getSeminarsTaken()}")
    print("-" * 40)
    
    print(student_bela.get_details())
    print(f"Bela Eligible to Enroll: {student_bela.isEligibleToEnroll('CS101')}")
    print("-" * 40)

if __name__ == "__main__":
    main()
    