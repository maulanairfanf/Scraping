import pandas as pd
import json
from liputan import listLiputan
from detik import listDetik
from tribun import listTribun

listBerita = []
listBerita.extend(listLiputan)
listBerita.extend(listDetik)
listBerita.extend(listTribun)

print(json.dumps(listBerita))



