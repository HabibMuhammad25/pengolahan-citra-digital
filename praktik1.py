import cv2
# membaca citra digital dari komputer
citra = cv2.imread("D:/Belajar All/Tutorial Python/Pengolahan Citra/gas1.jpg")

# menampilkan citra digital yang sudah dibaca
cv2.imshow("chelsea - blue", citra[:,:,0])
cv2.imshow("chelsea - green", citra[:,:,1])
cv2.imshow("chelsea - red", citra[:,:,2])


# menampilkan matriks dari citra
print(citra[:,:,0])
# Biasanya kita awalan RGB akan tetapi python tidak dia terbalik jadi BGR jadi outputnya Biru luan
# Titik 2 pertama itu baris, Titik 2 itu kolom, dan angka 0 itu channel pertama, jika 1 yaitu green

# menunggu sampai user menekan x tombol
cv2.waitKey()