import datetime
from requests import get

url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

def kunlik(time = ""):
    """Bu funksiya ma'lum bir kundagi kurslarni qaytaradi"""
    if time == "":
        response = get(url+"all/"+str(datetime.date.today())+"/")
        response = response.json()
        all_valyuta = 'Valyuta kurslari : \n'
        for i in range(3):
            all_valyuta += f"\t1 {response[i]['Ccy']} - {response[i]['Rate']} so'm.\n"
        all_valyuta += f"Sana : {response[0]['Date']}"
        return all_valyuta
    else:
        response = get(url+"all/"+str(time)+"/")
        response = response.json()
        all_valyuta = 'Valyuta kurslari : \n'
        for i in range(3):
            all_valyuta += f"\t1 {response[i]['Ccy']} - {response[i]['Rate']} so'm.\n"
        all_valyuta += f"Sana : {response[0]['Date']}"
        return all_valyuta
def other(v_name: str):
    response = url+v_name+"/"+str(datetime.date.today())+"/"
    response = get(response).json()
    if response != []:
        return f"1 {response[0]['Ccy']} - {response[0]['Rate']} so'm."
    else:
        return f"<{v_name}> bunday nomli valyuta turi topilmadi."

def maxsus(info: str):
    info = list(info.split())
    if info[0].isalpha() or info[0] in ["🇷🇺","💶","$"]:
        if info[0] == "dollor" or info[0] == "dollar" or info[0] == "$":
            valyuta = "USD"
            date = info[1]
        elif info[0] == "rubl" or "🇷🇺" == info[0]:
            valyuta = "RUB"
            date = info[1]
        elif info[0] == "yevro" or "💶" == info[0]:
            valyuta = "EUR"
            date = info[1]
        else:
            valyuta = info[0]
            date = info[1]
    else:
        if info[1] == "dollor" or info[1] == "dollar" or info[1] == "$":
            valyuta = "USD"
            date = info[0]
        elif info[1] == "rubl" or "🇷🇺" == info[1]:
            valyuta = "RUB"
            date = info[0]
        elif info[1] == "yevro" or "💶" == info[1]:
            valyuta = "EUR"
            date = info[0]
        else:
            valyuta = info[1]
            date = info[0]
    response = get(url+str(valyuta)+"/"+str(date)+"/")
    response = response.json()
    s = f"\t1 {response[0]['CcyNm_UZ']} - {response[0]['Rate']} so'm\n Sana : {response[0]['Date']}"
    return s
def convert_v(info: str):
    info = list(info.split())
    if len(info) == 2:
        if info[0].isalpha() or info[0] in ["🇷🇺","💶","$"]:
            if info[0] == "dollor" or info[0] == "dollar" or info[0] == "$":
                valyuta = "USD"
                x = int(info[1])
            elif "🇷🇺" == info[0]:
                valyuta = "RUB"
                x = int(info[1])
            elif "💶" == info[0]:
                valyuta = "EUR"
                x = int(info[1])
            else:
                valyuta = info[0]
                x = int(info[1])
        elif info[1] == "$":
            valyuta = "USD"
            x = int(info[0])
        elif "🇷🇺" == info[1]:
            valyuta = "RUB"
            x = int(info[0])
        elif "💶" == info[1]:
            valyuta = "EUR"
            x = int(info[0])
        else:
            if info[1] == "dollor" or info[1] == "dollar" or info[1] == "$":
                valyuta = "USD"
                x = int(info[0])
            else:
                valyuta = info[1]
                x = int(info[0])
    else:
        if "$" in info[0]:
            valyuta = "USD"
            x = int(info[0].replace("$",""))
        elif "🇷🇺" in info[0]:
            valyuta = "RUB"
            x = int(info[0].replace("🇷🇺", ""))
        elif "💶" in info[0]:
            valyuta = "EUR"
            x = int(info[0].replace("💶", ""))
    response = get(url+str(valyuta)+"/"+str(datetime.date.today())+"/")
    response = response.json()
    c = x * float(response[0]['Rate'])
    return f"{c} so'm.\n Sana {response[0]['Date']}"
def hafta():
    date1 = str(datetime.date.today())
    yil = date1[:4]
    oy = str(date1[5:7])
    kun = str(date1[8:])
    if int(kun) > 7:
        all_valyuta = 'Valyuta kurslari : \n'
        for i in range(7):
            response = get(url + "all/" + str(yil) + "-" + str(oy) + '-' + str(kun) + "/")
            response = response.json()
            all_valyuta += f"\nSana : {yil}.{oy}.{kun}\n\n"
            for i in range(3):
                all_valyuta += f"\t1 {response[i]['Ccy']} - {response[i]['Rate']} so'm.\n"
            kun = int(kun) - 1
        return all_valyuta
    else:
        all_valyuta = 'Valyuta kurslari : \n'
        if int(oy) > 1:
            for i in range(7):
                if int(kun) > 0:
                    response = get(url + "all/" + str(yil) + "-" + str(oy) + '-' + str(kun) + "/")
                    response = response.json()
                    all_valyuta += f"\nSana : {response[0]['Date']}\n\n"
                    for i in range(3):
                        all_valyuta += f"\t1 {response[i]['Ccy']} - {response[i]['Rate']} so'm.\n"
                else:
                    kun = "30"
                    oy = str(int(oy)-1)
                    response = get(url + "all/" + str(yil) + "-" + str(oy) + '-' + str(kun) + "/")
                    response = response.json()
                    all_valyuta += f"\nSana : {response[0]['Date']}"
                    for i in range(3):
                        all_valyuta += f"\t1 {response[i]['Ccy']} - {response[i]['Rate']} so'm.\n"
                kun = int(kun) -1
        else:
            if int(kun) > 0:
                response = get(url + "all/" + str(yil) + "-" + str(oy) + '-' + str(kun) + "/")
                response = response.json()
                all_valyuta += f"\nSana : {response[0]['Date']}\n\n"
                for i in range(3):
                    all_valyuta += f"\t1 {response[i]['Ccy']} - {response[i]['Rate']} so'm.\n"
            else:
                yil = str(int(yil) - 1)
                oy = "12"
                kun = "30"
                oy = str(int(oy) - 1)
                response = get(url + "all/" + str(yil) + "-" + str(oy) + '-' + str(kun) + "/")
                response = response.json()
                all_valyuta += f"\nSana : {response[0]['Date']}\n\n"
                for i in range(3):
                    all_valyuta += f"\t1 {response[i]['Ccy']} - {response[i]['Rate']} so'm.\n"
            kun = int(kun) - 1
        return all_valyuta
# print(convert_v("1 dollor"))