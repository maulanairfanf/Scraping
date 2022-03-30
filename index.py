import pandas as pd
import json
from liputan import listLiputan
from tribun import listTribun
from detik import listDetik

print(listLiputan)
print(listTribun)
print(listDetik)
# listBerita = []
# listBerita.extend(listLiputan)
# listBerita.extend(listDetiik) #buat JSON
# listBerita.extend(listTribun)

arrBerita = [listLiputan,listTribun,listDetik]
listBerita = pd.concat(arrBerita)
listBerita.reset_index(drop=True, inplace=True)
listBerita.to_csv("listBerita.csv",index=False)

# with open("Berita.json",'w') as f :
#     f.write(json.dumps(listBerita))