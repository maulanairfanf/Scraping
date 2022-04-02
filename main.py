from sqlalchemy import create_engine
import pandas as pd
from liputan import listLiputan
from tribun import listTribun
from detik import listDetik
from help import currentDateTime
# print(listLiputan)
# print(listTribun)
# print(listDetik)
# listBerita = []
# listBerita.extend(listLiputan)
# listBerita.extend(listDetiik) #buat JSON
# listBerita.extend(listTribun)

arrBerita = [listLiputan,listTribun,listDetik]
listBerita = pd.concat(arrBerita)
listBerita.reset_index(drop=True, inplace=True)
listBerita.to_csv(f"Data/Berita{currentDateTime}.csv",index=False)

engine = create_engine('mysql+pymysql://root@127.0.0.1:3306/webscraping') 

listBerita.to_sql('berita',con=engine,if_exists='append',index=False) 

# with open("Berita.json",'w') as f :
#     f.write(json.dumps(listBerita))