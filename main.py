import mysql.connector
import pandas as pd
from liputan import listLiputan, elapsed_time_liputan, row_liputan, column_liputan
from tribun import listTribun, elapsed_time_tribun, row_tribun, column_tribun
from detik import listDetik, elapsed_time_detik, row_detik, column_detik
from help import currentDateTime, executeTime


# DATABASE_URL = 'mysql+pymysql://u116665791_maulanairfanf:TanpaPassword79@31.220.110.101:3306/u116665791_WebScraping'

# conn = mysql.connector.connect(
#     database="u116665791_WebScraping", user='u116665791_maulanairfanf', password='TanpaPassword79', host='31.220.110.101', port='3306'
# )
# if conn.is_connected():
#     print("Succes Connected")

#     totalTime = elapsed_time_liputan + elapsed_time_tribun + elapsed_time_detik
#     totalRow = row_liputan + row_tribun + row_detik
#     totaColumn = (column_liputan + column_tribun + column_detik) / 3
#     print('Execution time total :', totalTime, 'seconds')
#     executeTime(totalTime, totalRow, totaColumn,
#                 "Total Waktu Scraping Ketiga Website")

#     arrBerita = [listLiputan, listTribun, listDetik]
#     listBerita = pd.concat(arrBerita)
#     listBerita.reset_index(drop=True, inplace=True)
#     listBerita.drop_duplicates(subset=["link"])
#     # listBerita.to_excel(f"data/berita/Berita({currentDateTime}).xlsx", index=False)

#     cursor = conn.cursor()

#     try:
#         cur = conn.cursor()
#         for index, row in listBerita.iterrows():
#             title = row["title"]
#             date = row["date"]
#             author = row["author"]
#             link = row["link"]
#             category = row["category"]
#             website = row["website"]
#             content = row["content"]
#             try:
#                 query = """INSERT into berita(title,date,author,link,category,website,content) VALUES (%s,%s,%s,%s,%s,%s,%s);"""
#                 column = (title, date, author, link,
#                           category, website, content)
#                 cursor.execute(query, column)
#             except mysql.connector.IntegrityError:
#                 conn.rollback()
#             else:
#                 conn.commit()

#             cur.close()
#     except Exception:
#         print("error", Exception[0])
# else:
#     print("Connection Failed")
