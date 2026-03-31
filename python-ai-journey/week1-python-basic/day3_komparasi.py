#operasi komparasi
#operasi komparasi digunakan untuk membandingkan dua nilai dan menghasilkan nilai boolean (True atau False).

# >, <, >=, <=, ==, != (literal sama dengan), is (identitas objek), is not (bukan identitas objek)
#is dan is not digunakan untuk membandingkan identitas objek, bukan nilai. Mereka memeriksa apakah dua variabel merujuk ke objek yang sama di memori.

a = 10
b = 5
print("a > b:", a > b) #True
print("a < b:", a < b) #False
print("a >= b:", a >= b) #True
print("a <= b:", a <= b) #False
print("a == b:", a == b) #False
print("a != b:", a != b) #True

print("===Object Identity(is)===")
x = 5
y = 5
print("Nilai X:", x, "id:", hex(id(x)))
print("Nilai Y:", y, "id:", hex(id(y)))
hasil = x is y
print("x is y:", hasil) #True, karena Python mengoptimalkan penyimpanan untuk nilai kecil seperti 5, sehingga x dan y merujuk ke objek yang sama di memori.
d = 76
e = 5
print("Nilai D:", d, "id:", hex(id(d)))
print("Nilai E:", e, "id:", hex(id(e)))
hasil = d is e
print("d is e:", hasil) #False, karena d dan e merujuk ke objek yang berbeda di memori.

print("===Object Identity(is not)===")
x = 5
y = 5
print("Nilai X:", x, "id:", hex(id(x)))
print("Nilai Y:", y, "id:", hex(id(y)))
hasil = x is not y
print("x is not y:", hasil) #False, karena x dan y merujuk
#ke objek yang sama di memori.
d = 76
e = 5
print("Nilai D:", d, "id:", hex(id(d)))
print("Nilai E:", e, "id:", hex(id(e)))
hasil = d is not e
print("d is not e:", hasil) #True, karena d dan e merujuk ke objek yang berbeda di memori.

#logika boolean
#logika boolean digunakan untuk menggabungkan beberapa kondisi komparasi menggunakan operator logika AND, OR, NOT. XOR

print("===Logika Boolean===")
print("===NOT===")
a = True
hasil = not a
print("data a:", a)
print("___________ NOT")
print("hasil:", hasil)
print("===AND===")
a = True
b = True
hasil = a and b
print(a,"AND", b, "=", hasil)
a = True
b = False
hasil = a and b
print(a,"AND", b, "=", hasil)
a = False
b = True
hasil = a and b
print(a,"AND", b, "=", hasil)
a = False
b = False
hasil = a and b
print(a,"AND", b, "=", hasil)
print("===OR===")
a = True
b = True
hasil = a or b
print(a,"OR", b, "=", hasil)
a = True
b = False
hasil = a or b
print(a,"OR", b, "=", hasil)
a = False
b = True
hasil = a or b
print(a,"OR", b, "=", hasil)
a = False
b = False
hasil = a or b
print(a,"OR", b, "=", hasil)
print("===XOR===")
a = True
b = True
hasil = a ^ b
print(a,"XOR", b, "=", hasil)
a = True
b = False
hasil = a ^ b
print(a,"XOR", b, "=", hasil)
a = False
b = True
hasil = a ^ b
print(a,"XOR", b, "=", hasil)
a = False
b = False
hasil = a ^ b
print(a,"XOR", b, "=", hasil)



