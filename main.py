import psycopg2
import pandas as pd
from liputan import listLiputan
from tribun import listTribun
from detik import listDetik
from help import currentDateTime

arrBerita = [listLiputan, listTribun, listDetik]
listBerita = pd.concat(arrBerita)
listBerita.reset_index(drop=True, inplace=True)
listBerita.drop_duplicates(subset=["link"])
listBerita.to_csv(f"Data/Berita({currentDateTime}).csv", index=False)

conn = psycopg2.connect(
    database="d93p694gn91dn4", user='lcwsaujkplbtoa', password='f222a0c158038fbc55d1b815143ab41e42f3ae27f9d8d999ef7c944e4490cda6', host='ec2-34-197-84-74.compute-1.amazonaws.com', port='5432'
)
cursor = conn.cursor()

try:
    cur = conn.cursor()
    for index, row in listBerita.iterrows():
        title = row["title"]
        date = row["date"]
        author = row["author"]
        link = row["link"]
        category = row["category"]
        website = row["website"]
        content = row["content"]
        try:
            query = """INSERT into berita(title,date,author,link,category,website,content) VALUES (%s,%s,%s,%s,%s,%s,%s);"""
            column = (title, date, author, link, category, website, content)
            cursor.execute(query, column)
        except psycopg2.IntegrityError:
            conn.rollback()
        else:
            conn.commit()

        cur.close()
except Exception:
    print("error", Exception[0])
