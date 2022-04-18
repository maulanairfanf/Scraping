from turtle import title
from colorama import Cursor
import psycopg2.extras as extras
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from liputan import listLiputan
# from tribun import listTribun
# from detik import listDetik
from help import currentDateTime

# print(listLiputan)
# print(listTribun)
# print(listDetik)
# listBerita = []
# listBerita.extend(listLiputan)
# listBerita.extend(listDetik) #buat JSON
# listBerita.extend(listTribun)

# arrBerita = [listLiputan, listDetik]
# listLiputan = pd.concat(arrBerita)
listLiputan.reset_index(drop=True, inplace=True)
listLiputan.drop_duplicates(subset=["link"])
# listLiputan.to_csv(f"Data/Berita({currentDateTime}).csv", index=False)

engine = create_engine(
    'postgresql://postgres:TanpaPassword@localhost:5432/webScraping')
# engine = create_engine(
#     "postgresql://vrsvsluhxmvrnh:1be4aa85913309c31a26df4842d9763f7dd4dca289aad373fea555a3542d499f@ec2-34-192-210-139.compute-1.amazonaws.com:5432/deqif9hrnf9p2t")
# conn = psycopg2.connect()
conn = psycopg2.connect(
    database="webScraping", user='postgres', password='TanpaPassword', host='127.0.0.1', port='5432'
)

cursor = conn.cursor()


for index, row in listLiputan.iterrows():
    title = row["title"]
    date = row["date"]
    author = row["author"]
    link = row["link"]
    category = row["category"]
    website = row["website"]
    content = row["content"]
    query = """INSERT into berita(title,date,author,link,category,website,content) VALUES (%s,%s,%s,%s,%s,%s,%s);"""
    column = (title, date, author, link, category, website, content)
    cursor.execute(query, column)
    conn.commit()

# def execute_values(conn, df, table):

#     tuples = [tuple(x) for x in df.to_numpy()]

#     cols = ','.join(list(df.columns))
#     print(cols)
#     # SQL query to execute
#     query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
#     cursor = conn.cursor()
#     try:
#         extras.execute_values(cursor, query, tuples)
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Error: %s" % error)
#         conn.rollback()
#         cursor.close()
#         return 1
#     print("the dataframe is inserted")
#     cursor.close()


# execute_values(conn, listLiputan, 'berita')


# listLiputan.to_sql('berita', con=conn, if_exists='append', index=False)
