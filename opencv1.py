import numpy as np
import cv2 as cv
import matplotlib as plt

# im = cv.imread('lena.png')
 
# # Pencereyi yeniden boyutlandırılabilir yapmak için.
# cv.namedWindow('Lena', cv.WINDOW_NORMAL)

# # Görüntü ekranda gösterilsin.
# cv.imshow('Lena',im)

# # 32 bit sistem kullananlar için.
# # k = cv.waitKey(0)
 
# # 64 bit sistem kullananlar için.
# k = cv.waitKey(0) & 0xFF
 
# if k == 27: # Çıkmak için ESC tuşuna basınız.
#     print("çıkış")
#     cv.destroyAllWindows()
# elif k == ord('s'): # Görüntüyü kaydetmek için 's' tuşuna basınız.
#     # görüntüyü kaydet
#     cv.imwrite('kayit.png', im)
#     cv.destroyAllWindows()

#--------------------Set Metodu-------------------------------------------

# cap=cv.VideoCapture(0)
# cap.set(3,1024) #genişlik   
# cap.set(4,512)  #uzunluk
# cap.set(10,100) #parlaklık

# while True:
#     success,img=cap.read()
#     if not success:
#         print("Bağlantı kurulamadı")
#         exit()
#     else:
#         cv.imshow("image",img)
#         if cv.waitKey(1) & 0xFF==ord("q"):
#             break

#-------------------- Color Ayarlama--------------------------------------------

# #img=cv.imread("image.jpg",0)
# img=cv.imread("image.jpg")
# gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# thresh, blackAndWhiteImage = cv.threshold(img, 150, 250, cv.THRESH_BINARY)
# #thresh, blackAndWhiteImage = cv.threshold(img, 150, 250, cv.THRESH_BINARY)
# cv.imshow("image",blackAndWhiteImage)
# #plt.imshow(gray_image)
# #plt.show()  bazi versiyonlarda cv kullanılmıyor o yüzden
# cv.waitKey(0) #cv.waitKey(1)
# #print(gray_img.shape) boyutu renkli olursa x3(RGB)
# print(blackAndWhiteImage)
# print(thresh)
#------------------------Kamera Açma ve Video Oynatma---------------------------------------------

# Dosyadan video okumak için
#cap = cv.VideoCapture('TomandJerry.mp4')

# IP Kamera bağlantısı için
#cap = cv.VideoCapture('http://192.168.1.105:8080/video')

# Kamera bağlantısı için (Cihazınıza bağlı diğer kameralar için 0-1-2-3 deneyebilirsiniz.)
# cap = cv.VideoCapture(0)

# if not cap.isOpened():
#     print("Kamera Bağlantısı Başarısız")
#     exit()

# while True:
#     ret,frame=cap.read()
#     if not ret:
#         print("Bağlantıdan görüntü alınamadı!")
#         break
#     gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     cv.imshow("frame",gray)
#     ##print(bool(cv.waitKey(1)))
#     if cv.waitKey(1) == ord("q"): #cv.waitKey(1) & 0xFF == ord('q')
#         break
# # İşin bittikten sonra her şeyi serbest bırak.
# cap.release()
# cv.destroyAllWindows()

# cap=cv.VideoCapture(*args) VideoCapture sınıfını oluşturur.
# cap.isOpened() VideoCapture sınıfını açmayı dener. Hata olup olmadığını kontrol eder. 1 veya 0 ya da True veya False değeri döndürür.
# cap.release() VideoCapture sınıfını kapatır.

#---------------------------Video Kaydetme----------------------------------

# cap = cv.VideoCapture(0)
# # codec tanımlama ve VideoWriter nesnesi oluşturma bilgi için bkz: https://www.fourcc.org/codecs.php
# fourcc = cv.VideoWriter_fourcc(*'XVID')
 
# # Yukarıdaki işlemi aşağıdaki gibi de yapabiliriz.
# #fourcc = cv.VideoWriter_fourcc('X','V','I','D')

# # Kaydedilecek video dosyasının adı, uzantısı, konumu, saniyedeki çerçeve sayısı ve çözünürlüğü
# out = cv.VideoWriter('output.avi',fourcc, 60.0, (640,480))
 
# # Görüntü alma başarılı olduğu süre boyunca kaydetmeye devam et.
# while(cap.isOpened()):
#     # Videodan görüntü oku ve geri döndür.
#     ret, frame = cap.read()
 
#     # Görüntü okuma başarılı ise
#     if ret==True:
#         # cv.flip(src, flipCode, dst) 2 boyutlu diziyi dikey yatay veya her iki eksen etrafında döndürür.
#         # 0 => dikey döndürme
#         # 1 => yatay döndürme
#         # 2 => hem yatay hem dikey döndürme
#         frame = cv.flip(frame,1,dst=None)
 
#         # Döndürülen görüntüyü video dosyasına yaz.
#         out.write(frame)
 
#         # Görüntüyü ekranda göster.
#         cv.imshow('frame',frame)
 
#         # q tuşuna basıldığında çık.
#         if cv.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
 
# # İşin bittikten sonra her şeyi serbest bırak.
# cap.release()
# out.release()
# cv.destroyAllWindows()