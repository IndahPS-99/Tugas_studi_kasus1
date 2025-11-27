# Tugas_studi_kasus1

# University Management System - Python Implementation (UML Class Diagram)

Proyek ini adalah implementasi dari **UML Class Diagram** yang disediakan, menggunakan bahasa pemrograman Python. Tujuannya adalah untuk mendemonstrasikan pemahaman tentang konsep **Object-Oriented Programming (OOP)**, termasuk pewarisan (*inheritance*), agregasi (*aggregation*), atribut dengan visibilitas berbeda, dan atribut *derived*.

## Proses Berpikir (Design Rationale)

1.  **Analisis Diagram Kelas:**
    * **Kelas Inti:** `Address`, `Person`, `Student`, dan `Professor`.
    * **Pewarisan (Generalization):** `Student` dan `Professor` mewarisi dari `Person`.
    * **Relasi Agregasi:** `Person` memiliki relasi **0..1 lives at 1** dengan `Address`. Ini diimplementasikan dengan memberikan objek `Address` sebagai parameter opsional (`Optional[Address]`) dalam konstruktor `Person`.
    * **Relasi Asosiasi:** `Student` memiliki relasi **0..\* supervises 1..5** dengan `Professor`. Relasi ini dikelola di kelas `Professor` sebagai daftar (`List[Student]`) dan divalidasi agar tidak melebihi 5 mahasiswa.
    * **Visibilitas Atribut:**
        * `+` (Public): Atribut biasa, diakses langsung (misalnya `self.name`).
        * `#` (Protected): Diimplementasikan dengan konvensi Python menggunakan satu garis bawah (`_staffNumber`).
        * `-` (Private): Diimplementasikan dengan *name mangling* Python menggunakan dua garis bawah (`__yearsOfService`).
        * `/` (Derived/Read-Only): Diimplementasikan menggunakan *property* Python (`@property`) untuk `salary`. Nilai dihitung secara *on-the-fly* dan tidak disimpan sebagai variabel instansi biasa.

2.  **Struktur Kode:**
    * Setiap kelas utama ditempatkan dalam file Python-nya sendiri (`Address.py`, `Person.py`, `Student.py`, `Professor.py`) untuk menjaga modularitas dan kejelasan.
    * `main.py` berfungsi sebagai *entry point* untuk mengimpor semua kelas dan mendemonstrasikan relasi dan method-methodnya.

3.  **Dokumentasi Kode:**
    * Semua kelas, konstruktor (`__init__`), dan method publik memiliki *docstring* sesuai standar Python. *Docstring* ini menjelaskan tujuan, parameter, dan nilai kembalian dari setiap elemen, memenuhi persyaratan dokumentasi kode.

## Bantuan AI (Prompt-Response Log)

Implementasi ini dikembangkan dengan bantuan AI untuk memastikan interpretasi yang akurat dari standar UML ke idiom Python, khususnya untuk masalah visibilitas atribut dan relasi.

| Tahap | Prompt Pengguna | Response AI yang Berguna |
| :--- | :--- | :--- |
| **Visibilitas** | *How to implement private (`-`), protected (`#`), and derived (`/`) attributes in Python according to UML standards?* | AI menjelaskan penggunaan konvensi `_` untuk protected, `__` untuk private (*name mangling*), dan properti `@property` untuk atribut *derived* atau *read-only*. |
| **Relasi** | *In a class diagram, how do I handle the 0..* supervises 1..5 relationship between Student and Professor in Python?* | AI menyarankan penggunaan `List` di kelas `Professor` untuk menyimpan objek `Student`, dan menambahkan logika validasi *cardinality* (maksimal 5). Ini juga menyarankan pembaruan referensi balik pada objek `Student` (`student.supervisor = self`). |
| **Struktur** | *What is a clean file structure for a multi-class Python project based on a UML diagram?* | AI menyarankan memecah setiap kelas ke file-nya sendiri dan menggunakan `main.py` sebagai *entry point* demonstrasi, yang diadopsi dalam proyek ini. |

## 🚀 Cara Menjalankan Program

1.  Pastikan Anda memiliki Python 3 terinstal.
2.  Simpan semua file (`main.py`, `Address.py`, `Person.py`, `Student.py`, `Professor.py`) dalam satu direktori.
3.  Jalankan program dari terminal:

    ```bash
    python main.py
    ```
