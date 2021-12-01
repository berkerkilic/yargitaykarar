import pandas as pd
import numpy as np

fp = open('dbpedia_csv/classes.txt')
classes_names = fp.readlines()
fp.close()
classes_names = [x.strip() for x in classes_names]
print(classes_names)

df = pd.read_csv('dbpedia_csv/test.csv', encoding='utf-8', header=None)
df.columns=['label','title','description']
fp = open('dbpedia_csv/dbpedia_csv.test','wt',encoding='utf-8')
for i in range(len(df)):
    label = '__label__'+classes_names[df.label[i]-1]+' '
    text = ', '+df.title[i].lower()+' '+df.description[i].lower()
    line = label+text+'\n'
    fp.write(line)
    if i%5000==0:
        print(classes_names[int(i/5000)])
fp.close()