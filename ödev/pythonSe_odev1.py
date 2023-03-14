ilerlemeDurumu=0
sayac=int(input("Sayacı giriniz->"))
for i in range(0,sayac):
    ilerlemeDurumu+=1   
    if ilerlemeDurumu==1:
        print("Ders Programı kısmıdır."+" %25 tamamlandı.")
    elif ilerlemeDurumu==2:
        print("Değerlendirme kısmıdır."+" %50 tamamlandı." )
    elif ilerlemeDurumu==3:
        print("Ödev1 kısmıdır."+" %75 tamamlandı." )
    elif ilerlemeDurumu==4:
        print("Ödev2 kısmıdır."+" %100 tamamlandı." )
    else:
         print("Aşama kalmadı.")






import matplotlib.pyplot as plt
import numpy as np

# Veri oluşturma
np.random.seed(1)
data = np.random.normal(0, 1, size=(100,))

# Box plot çizdirme
fig, ax = plt.subplots()
ax.boxplot(data)

plt.show()