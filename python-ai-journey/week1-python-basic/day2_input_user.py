#mengenal casting
#casting adalah mengubah tipe data ke tipe data lain
#contoh casting

print("====INTEGER====")
data_int = 10
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data:", data_int, "type:", type(data_int))
print("data:", data_float, "type:", type(data_float))
print("data:", data_str, "type:", type(data_str))
print("data:", data_bool, "type:", type(data_bool)) #nilai 0 akan menghasilkan False, sedangkan nilai selain 0 akan menghasilkan True

print("====FLOAT====")
data_float = 10.67
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data:", data_float, "type:", type(data_float))
print("data:", data_int, "type:", type(data_int)) #nilai float akan dibulatkan ke bawah saat di-cast ke int, sehingga 10.67 akan menjadi 10
print("data:", data_str, "type:", type(data_str)) 
print("data:", data_bool, "type:", type(data_bool)) #nilai 0.0 akan menghasilkan False, sedangkan nilai selain 0.0 akan menghasilkan True

print("====STRING====")
data_str = "100"
data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)
print("data:", data_str, "type:", type(data_str))
print("data:", data_int, "type:", type(data_int)) #harus angka
print("data:", data_float, "type:", type(data_float)) #harus angka
print("data:", data_bool, "type:", type(data_bool)) #string kosong akan menghasilkan False, sedangkan string yang berisi akan menghasilkan True


data_bool = True
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data:", data_bool, "type:", type(data_bool))
print("data:", data_int, "type:", type(data_int)) #nilai True akan menghasilkan 1, sedangkan nilai False akan menghasilkan 0
print("data:", data_float, "type:", type(data_float)) #nilai True akan menghasilkan 1.0, sedangkan nilai False akan menghasilkan 0.0
print("data:", data_str, "type:", type(data_str))


print("====INPUT USER====")
#data yang dimasukkan oleh user melalui fungsi input() akan selalu dianggap sebagai string, sehingga kita perlu melakukan casting jika ingin mengubahnya ke tipe data lain.
#contoh input user
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))
tinggi = float(input("Masukkan tinggi Anda dalam meter: "))
print("1 untuk Ya, 0 untuk Tidak")
is_student = bool(int(input("Apakah Anda seorang mahasiswa? (1/0): "))) #input akan dianggap sebagai string, sehingga kita perlu mengubahnya ke int terlebih dahulu sebelum di-cast ke bool. Nilai 0 akan menghasilkan False, sedangkan nilai selain 0 akan menghasilkan True.

print("Nama:", nama)
print("Umur:", umur)
print("Tinggi:", tinggi)
print("Mahasiswa:", is_student)

#operrasi aritmatika
#pertambahan
angka1 = 10
angka2 = 5
hasil = angka1 + angka2
print("Hasil penjumlahan:",angka1,"+",angka2,"=", hasil)
#pengurangan
hasil = angka1 - angka2
print("Hasil pengurangan:",angka1,"-",angka2,"=", hasil)
#perkalian
hasil = angka1 * angka2
print("Hasil perkalian:",angka1,"*",angka2,"=", hasil)
#pembagian
hasil = angka1 / angka2
print("Hasil pembagian:",angka1,"/",angka2,"=", hasil)
#pembagian dengan pembulatan ke bawah / floor division
hasil = angka1 // angka2
print("Hasil pembagian dengan pembulatan ke bawah:",angka1,"//",angka2,"=", hasil)
#modulus / sisa bagi
hasil = angka1 % angka2
print("Hasil modulus / sisa bagi:",angka1,"%",angka2,"=", hasil)
#pangkat
hasil = angka1 ** angka2
print("Hasil pangkat:",angka1,"**",angka2,"=", hasil)

#operasi aritmatika dengan input user
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
hasil = angka1 + angka2
print("Hasil penjumlahan:", angka1, "+", angka2, "=", hasil)