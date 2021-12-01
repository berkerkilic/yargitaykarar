import pandas as pd
import numpy as np

fp = open('siniflar.txt', encoding='utf-8')
sinifadlari = fp.readlines()
fp.close()
sinifadlari = [x.strip() for x in sinifadlari]
#print(sinifadlari)

df = pd.read_csv('kararlartam.csv', encoding='utf-8', header=None)
df.columns=['sucturu','kararmetni']
fp = open('karartam.csv','wt',encoding='utf-8')
for i in range(len(df)):
    sinif = '__label__'+sinifadlari[df.sucturu[i]-1]+' '
    karar = df.kararmetni[i].lower()
    kayit = sinif+', '+karar+'\n'
    #print(sinif)
    fp.write(kayit)
    if i%25==0:
        print(sinifadlari[int(i/25)])
fp.close()