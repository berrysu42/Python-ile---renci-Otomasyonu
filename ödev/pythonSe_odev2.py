# https://github.com/ozdemirdemiroz/kodlama.io/blob/main/kodlamaio%20odev%202.py
ogrenci=["Berk Can","Betül Demir","Saliha Türk"]
while True:
    print("Öğrenci Kayıt sistemine giriş:\n Yapmak istediğiniz işlemi seçin\n \t1->Öğrenci Ekleme\n \t2->Öğrenci Silme\n\t3->Çoklu Öğrenci Eklem\n\t4->Öğrencileri Listeme\n\t5->Öğrenci Numarasını Sorgulama\n\t6->Çoklu Öğrenci Silme\n\t7->Hata\n\t8->Çıkış")
    secenek=int(input("Yukarıdaki işlemlerden yapmak istediğiniz işlemin numarasını giriniz ->"))

    def ogrenci_ekleme():
        full_isim=input("Eklenecek Öğrencinin adı soyadı: ->")
        ogrenci.append(full_isim)
            
    def ogrenci_silme():
        full_isim=input("Silinecek Öğrencinin adı soyadı: ->")
        ogrenci.remove(full_isim)

    def ogr_no():
        full_isim=input("Numarası sorgulanacak öğrencinin adı soyadı: ->")
        ogr_no=ogrenci.index(full_isim)+1
        print(" {}'in öğrenci numarası:{}".format(full_isim,ogr_no))

    def ogrenci_listele():
        ogrenci.sort()
        for i in ogrenci:
            print(i)
    

    if secenek==1:
        ogrenci_ekleme()
    elif secenek==2:
        ogrenci_silme()
    elif secenek==3:
        adet=int(input("Kaç adet öğrenci eklemek istiorsunuz? ->"))
        for i in range(adet):
            ogrenci_ekleme()
    elif secenek==4:
        ogrenci_listele()
        print("Listede {} öğrenci mevcut ".format(len(ogrenci)))     
    elif secenek==5:
        ogr_no()
    elif secenek==6:
        adet=int(input("Kaç adet öğrenci silmek istiorsunuz? ->"))
        for i in range(adet):
            ogrenci_silme()
        
    elif secenek==7:
        print("Hatalı bir sayı girdiniz.Tekrar deneyin!")
    else:
        print("Çıkış yapılıyor!")
        break
