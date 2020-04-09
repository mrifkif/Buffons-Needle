import random
import numpy as nup
import matplotlib.pyplot as pl
from numpy import pi, cos
import pandas as pd


''' 
  Mencari banyaknya jarum/batang korek api yang berpotongan dengan garis (d)
  Mengembalikan nilai banyaknya jarum/batang korek api yang berpotongan 
  dengan garis (d)
  Pada konsep tersebut diimplementasikan dengan
  1. Mencari nilai random 'd' di [0,d]
  2. Mencari nilai random theta di [0,pi/2]
  3. jika benar nilai dari (d * random di [0,1]) kurang dari  (l * cos(theta))
     maka jarum/batang korek api dianggap memotong garis 
'''

def Buffon(l, d, n):
  combo = 0
  for i in range(n):
    teta = pi*random.random()/2
    if (d*random.random() <= l*cos(teta)):
      combo+=1
  return combo 



''' 
  Menghitung estimasi nilai phi dengan
  Phi_Estimasi = (2*N*L) / (D*Q)
  N : banyaknya ukuran sampel
  L : panjang jarum/batang korek api
  D : lebar garis paralel
  Q : banyaknya jarum/batang korek api 
        yang memotong garis paralel
'''
def phi(n):
  l = 3
  d = 5
  Q = Buffon(l,d,n)
  pi_estimation = 2*n*l / (Q*d)
  return round(pi_estimation,3), Q



# Main Program

x = nup.arange(100,10000,10)  # Menginisiasi N sample dari 100 ~ 10000 dengan penambahan nilai 10 per looping
y = nup.zeros(len(x))         # Membuat array yang memiliki panjang yang sama dengan x
q = nup.zeros(len(x))         # Menampung nilai Q
n = len(x)                    # Panjang x merupakan banyaknya percobaan yang dilakukan
for i in range(n):            # Melakukan looping sebanyak N percobaan
  y[i], q[i] = phi(x[i])
pl.plot(x,y,'.')
pl.axhline(y=pi, color='r', linestyle='-')  # Membuat garis lurus di nilai Phi yang sebenarnya
pl.xlabel('N (Ukuran Sampel)')              # x dilabeli dengan Ukuran Sampel
pl.ylabel('$\pi$')                          # y dilabeli nilai Phi
pl.show()                                   # Menampilkan Grafik
print("Nilai Estimasi Phi =",round((sum(y)/n), 3))     # sum(y)/n merupakan rata-rata nilai estimasi phi

# Uncomment jika ingin menyimpan nilai Q dan estimasi Phi
# dq = pd.DataFrame({'Nilai Q': q,
#                    'Estimasi Phi': y})
# dq.to_csv('Q_and_PhiEst.csv')

# Uncomment jika ingin melikat nilai Q dan Estimasi Phi setiap percobaan
# for i in range(n):
#   print("Q:",q[i]," Phi Estimation",y[i])