import pandas as pd
import numpy as np

fp = open('siniflar.txt', encoding='utf-8')
classes_names = fp.readlines()
fp.close()
classes_names = [x.strip() for x in classes_names]
print(classes_names)