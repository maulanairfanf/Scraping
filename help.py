import datetime


def configureMonth(month):
    return month.replace("Januari", "01").replace("Februari", "02").replace("Maret", "03").replace("April", "04").replace("Juni", "06").replace("Juli", "07").replace("Agustus", "08").replace("September", "09").replace("Oktober", "10").replace("November", "11").replace("Desember", "12").replace("Jan", "01").replace("Feb", "02").replace("Mar", "03").replace("Apr", "04").replace("Mei", "05").replace("Jun", "06").replace("Jul", "07").replace("Agu", "08").replace("Sep", "09").replace("Okt", "10").replace("Nov", "11").replace("Des", "12")


def configureDate(day, website):
    dateTime = datetime.datetime.now()
    year = dateTime.date().strftime("%Y")
    change_month = configureMonth(day)
    if(website == 'tribun' or website == 'detik'):
        remove_before = change_month.split(', ')[-1]
        date_month = remove_before.rpartition(year)[0]
        get_year = remove_before.rpartition(year)[1]
        if(website == 'tribun'):
            if(int(date_month.split(' ')[0]) < 10):
                date_month = "0" + date_month
            date = date_month + get_year
        if(website == 'detik'):
            get_date = date_month.split(' ')[0]
            get_month = date_month.split(' ')[1]
            date = get_date + " " + get_month + " " + get_year
    if(website == 'liputan'):
        date = change_month.split(', ')[0]
    return date.replace(" ", "-")


currentDateTime = datetime.datetime.now().date().strftime("%d-%m-%Y")
currentDateTimeExecute = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def executeTime(time, row, column, website):
    f = open("data/time/waktu_execute.txt", "a+")
    f.write(
        f"Tanggal : {currentDateTimeExecute} | Waktu Scraping {website} : {time} detik | Banyak row : {row} | Banyak column : {column} \r\n")
    f.close()
