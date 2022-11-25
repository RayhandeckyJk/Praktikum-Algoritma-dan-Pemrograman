print("--------------------------------------------------")
print("----------------- Seblak bandung -----------------")
print("--------------------------------------------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsibelanja():
   global totalbeli
   global porsi
   global beli
   print("\n------------------ Toping ------------------")
   print("1. original - Rp 10000")
   print("2. bakso - Rp 12000")
   print("3. sosis - Rp 12000")
   print("4. ceker - Rp 15000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalbeli=porsi*10000
       print (porsi," original = Rp", totalbeli)
       beli=("original")
   elif nomor==2:
       totalbeli=porsi*12000
       print (porsi," bakso = Rp", totalbeli)
       beli=("bakso")
   elif nomor==3:
       totalbeli=porsi*12000
       print (porsi, " sosis = Rp", totalbeli)
       beli=("sosis")
   elif nomor==4:
       totalbeli=porsi*23000
       print (porsi, " ceker = Rp", totalbeli)
       beli=("ceker")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()


fungsibelanja()
totalsemua=totalbeli

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n================== STRUK ORDER ====================")
print("\n================== SEBLAK BANDUNG ===================")
print("alamat : Bekasi,Bulak Kapal")
print("no telf : 085812345678")

import datetime
x=datetime.datetime.now()
print(x)

print("=====================================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,beli,"( Rp", totalbeli,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("=====================================================")
print("========== TERIMA KASIH TELAH MEMBELI ===============")
print("=====================================================")