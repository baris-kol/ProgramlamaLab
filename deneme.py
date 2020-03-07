import random #random kütüphanesini ekledim.
pcSayi = random.randint(1000,9999) #Random oluşturdum ve bunları birler onlar yüzler ve binler basamağına ayırdım.
print(pcSayi)
pcSayibb = (pcSayi%10) 
pcSayiob = ((pcSayi%100)-pcSayibb)/10
pcSayiyb = ((pcSayi%1000)-(pcSayiob*10)-pcSayibb)/100
pcSayiBinB = (pcSayi-(pcSayiyb*100)-(pcSayiob*10)-pcSayibb)/1000
print("Tahmin Oyununa Hoşgeldiniz!!!")
tahmin = int(input("4 Basamaklı Bir Sayı Giriniz"))
tahminBB = (tahmin%10) 
tahminOB =  ((tahmin%100)-tahminBB)/10
tahminYB = ((tahmin%1000)-(tahminOB*10)-tahminBB)/100
tahminBinB =  (tahmin-(tahminYB*100)-(tahminOB*10)-tahminBB)/1000
puan = 0
if pcSayiBinB == tahminBinB:
    puan = puan + 1
else:
    puan = puan - 1
if pcSayiyb == tahminYB:
    puan = puan + 1
else:
    puan = puan - 1
if pcSayiob == tahminOB:
    puan = puan + 1
else:
    puan = puan - 1
if pcSayibb == tahminBB:
    puan = puan + 1
else:
    puan = puan - 1
    
print("Oyun Sonlandı Puanınız", puan)
