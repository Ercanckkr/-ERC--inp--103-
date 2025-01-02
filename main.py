# Kullanıcıdan bir sayı al
sayi = input("Bir sayı girin: ")

# Kullanıcının geçerli bir sayı girdiğinden emin olun
if sayi.isdigit():
    sayi = int(sayi)
    
    # Sayıyı büyükten küçüğe kadar sıralayıp toplama işlemi yap
    toplam = 0
    for i in range(sayi, -1, -1):  # Büyükten küçüğe doğru sıralama
        toplam += i

    # Sonucu ekrana yazdır
    print("{} sayısına kadar büyükten küçüğe sıralanıp toplamları: {}".format(sayi, toplam))
else:
    print("Lütfen geçerli bir tam sayı girin.")
