from sqlalchemy import create_engine
# import sqlalchemy
import pandas as pd

df = pd.DataFrame(data=[[111,'Thomas','35','United Kingdom'],
		[222,'Ben',"42",'Australia'],
		],
		columns=['id','name','email','password'])



engine = create_engine('mysql+pymysql://root@127.0.0.1:3306/webscraping') 

df.to_sql('users',con=engine,if_exists='append',index=False) 
