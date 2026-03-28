#pengenalan dengan python menggunakan print
#print digunakan untuk menampilkan output ke layar
#untuk menampilkan output ke layar, kita bisa menggunakan fungsi print() dengan menuliskan teks yang ingin ditampilkan di dalam tanda kutip.
#contoh penggunaan print
print("Hallo World")

#variabel adalah tempat untuk menyimpan data. Variabel dapat digunakan untuk menyimpan berbagai jenis data, seperti angka, teks, atau nilai boolean.
#assigment variabel
nama = "Affandi Putra Pradana"
umur = 25
print("Nama saya adalah", nama, "dan umur saya adalah", umur, "tahun.")
#multiple assignment
x, y, z = 1, 2, 3
a = b = c = 10
name, age, city = "Alice", 30, "New York"
#mengubah nilai variabel
print("Nilai awal age:", age)
age = 31
print("Nilai baru age:", age)

#tipe data adalah jenis data yang dapat disimpan dalam variabel. Beberapa tipe data yang umum digunakan dalam Python adalah:
#1. String: digunakan untuk menyimpan teks. Contoh: "Hello, World!" atau 'Python is great!'
#2. Integer: digunakan untuk menyimpan bilangan bulat. Contoh: 42 atau -7
#3. Float: digunakan untuk menyimpan bilangan desimal. Contoh: 3.14 atau -0.001
#4. Boolean: digunakan untuk menyimpan nilai benar (True) atau salah (False). Contoh: True atau False

#contoh penggunaan tipe data
#1. String: 
nama = "Affandi Putra Pradana"
#multi-line string
alamat = """Jl. Merdeka No. 123
Kota Jakarta
Indonesia"""

#2. Integer:
umur = 25
saldo = -5000

#3. Float:
tinggi = 1.8
#notasi ilmiah
jarak = 1.5e6  # sama dengan 1.5 x 10^6 atau 1.5 juta
very_small_number = 2.5e-3  # sama dengan 2.5 x 10^-3 atau 0.0025

#4. Boolean:
is_student = True

#menampilkan informasi tentang diri kita menggunakan variabel dan tipe data
print("Nama saya adalah", nama)
print("Umur saya adalah", umur, "tahun.")
print("Tinggi saya adalah", tinggi, "meter.")
print("Apakah saya seorang mahasiswa?", is_student)
print("Tipe data nama:", type(nama))
print("Tipe data umur:", type(umur))
print("Tipe data tinggi:", type(tinggi))
print("Tipe data is_student:", type(is_student))
