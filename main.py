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
# listBerita.extend(listDetik) #buat JSON
# listBerita.extend(listTribun)

arrBerita = [listLiputan,listTribun,listDetik]
listBerita = pd.concat(arrBerita)
listBerita.reset_index(drop=True, inplace=True)
listBerita.drop_duplicates(subset=["link"])
listBerita.to_csv(f"Data/Berita{currentDateTime}.csv",index=False)

engine = create_engine('postgresql://sgipiulsrqjqyd:c03109765d8a9574c3adc9273c6e07f531997fbfe0722e1c40e93d8184b0b53f@ec2-34-231-63-30.compute-1.amazonaws.com:5432/durspbi4nbo1m') 

listBerita.to_sql('berita',con=engine,if_exists='append',index=False) 

# print(engine.execute("SELECT * FROM berita").fetchnone())

# with open("Berita.json",'w') as f :
#     f.write(json.dumps(listBerita))