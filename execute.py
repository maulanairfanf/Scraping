import pandas as pd
import re

df = pd.read_csv('data/time/26-04-2022.txt',
                 sep="|", names=['tanggal', 'waktu', 'row', 'column'])
data = pd.DataFrame(df, columns=[
    'tanggal', 'waktu', 'row', 'column'])
# print(data)

data_arr = []
arr_tribun = []
arr_liputan = []
arr_detik = []
arr_total = []

for index, row in data.iterrows():
    tanggal = row["tanggal"].replace("Tanggal : ", " ")
    waktu_website = row["waktu"].replace(
        "Waktu Scraping", " ").replace("detik", " ")
    waktu = waktu_website.split(':')[1].strip()
    website = waktu_website.split(':')[0].strip()
    # print(row['row'].split(":")[1])
    if(website == "Liputan6.com"):
        # arr_liputan.append(website)
        arr_liputan.append(float(waktu))
    elif(website == "Tribunnews.com"):
        # arr_tribun.append(website)
        arr_tribun.append(float(waktu))
    elif(website == "Detik.com"):
        # arr_detik.append(website)
        arr_detik.append(float(waktu))
    else:
        # arr_total.append(website)
        arr_total.append(float(waktu))


def hitungWaktu(waktu, website):
    total_waktu = 0
    for i in range(len(waktu)):
        total_waktu = total_waktu + waktu[i]
    rata_rata = total_waktu/len(waktu)
    print("Waktu rata-rata", website, " : ", rata_rata)


hitungWaktu(arr_liputan, 'website Liputan.com')
hitungWaktu(arr_tribun, 'website Tribunnews.com')
hitungWaktu(arr_detik, 'website Detik.com')
hitungWaktu(arr_total, 'ketiga website berita')
