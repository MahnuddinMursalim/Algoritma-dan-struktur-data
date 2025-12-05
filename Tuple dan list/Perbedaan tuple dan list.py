# Nama : Mahmuddin Mursalim
# Nim : D0425509
# Kelas : B Saistem Informasi

#Perbedaan tuple dan list
# Tuple bersifat tidak dapat diubah (immutable), sedangkan list bersifat dapat diubah (mutable).

# tuple



negara = ("argentina", "portugal", "italia")	#tuple tidak bisa di ubah

print("isi tuple: " ,negara)

print("Elemen ke-1:" ,negara[0])

# negara[1] = "portugal"	# ini akan ERROR karena tuple tidak bisa diubah





# List

pemain = ["messi", "ronaldo", "platini"]	#bisa diubah

print("sebelum diubah: ", pemain)



pemain[1] = "platini"	#mengubah isi

pemain.append("neyamar")	#menambah data



print("setelah diubah: ", pemain)