import datetime

# print(json.dumps(listLiputan))

# def configureMonth(month):
#     print(month)
#     if(month == "Jan" or month == "Feb" or month == "Mar" or month == "Apr" or month == "Mei" or month == "Jun" or month == "Jul"or month == "Agu"or month == "Sep"or month == "Okt"or month == "Nov"or month == "Des") :
#         return month.replace("Jan", "1").replace("Feb", "2").replace("Mar", "3").replace("Apr", "4").replace("Mei","5").replace("Jun", "6").replace("Jul", "7").replace("Agu", "8").replace("Sep", "9").replace("Okt","10").replace("Nov", "11").replace("Des", "12")
#     if(month == "Januari" or month == "Februari" or month == "Maret" or month == "April" or month == "Juni" or month == "Juli"or month == "Agustus"or month == "September"or month == "Oktober"or month == "November"or month == "Desember") :
#         return month.replace("Januari", "1").replace("Februari", "2").replace("Maret", "3").replace("April", "4").replace("Juni", "6").replace("Juli", "7").replace("Agustus", "8").replace("September", "9").replace("Oktober","10").replace("November", "11").replace("Desember", "12")

def configureMonth(month):
    return month.replace("Januari", "01").replace("Februari", "02").replace("Maret", "03").replace("April", "04").replace("Juni", "06").replace("Juli", "07").replace("Agustus", "08").replace("September", "09").replace("Oktober","10").replace("November", "11").replace("Desember", "12").replace("Jan", "01").replace("Feb", "02").replace("Mar", "03").replace("Apr", "04").replace("Mei","05").replace("Jun", "06").replace("Jul", "07").replace("Agu", "08").replace("Sep", "09").replace("Okt","10").replace("Nov", "11").replace("Des", "12")

def configureDate(day,website):
    dateTime = datetime.datetime.now()
    year = dateTime.date().strftime("%Y")
    change_month = configureMonth(day)
    if(website == 'tribun' or website == 'detik') :
        remove_views = change_month.split(', ')[-1]
        get_date = remove_views.rpartition(year)[0]
        if(website == 'tribun') :
            if(int(get_date.split(' ')[0]) < 10) :
                get_date = "0" + get_date
        get_year = remove_views.rpartition(year)[1]
        date = get_date + get_year
    if(website == 'liputan') :
        date = change_month.split(', ')[0]
    return date.replace(" ","-")

currentDateTime = datetime.datetime.now().date().strftime("%d-%m-%Y")
