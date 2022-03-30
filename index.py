import pandas as pd
import json
from liputan import listLiputan
from detik import listDetik
from tribun import listTribun

listBerita = []
listBerita.extend(listLiputan)
listBerita.extend(listDetik)
listBerita.extend(listTribun)


with open("Berita.json",'w') as f :
    f.write(json.dumps(listBerita))



