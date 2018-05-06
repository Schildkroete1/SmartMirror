import requests
from datetime import *
import os

anzahl_wochen = 10 #anzahl der wochen die abgerufen werden
heute = datetime.now()
listeDatum = []
listeFach = []
Arbeiten = []
Arbeiten2 = []
AnfangStunde = ["7:50", "8:35", "9:40", "10:25", "11:30", "12:15", "13:00", "13:45", "14:30", "15:35", "16:20", "17:05", "18:00", "18:45", "19:45", "20:30"]
EndeStunde = ["8:35", "9:20", "10:25", "11:10", "12:15", "13:00", "13:45", "14:30", "15:15", "16:20", "17:05", "17:50", "18:45", "19:30", "20:30", "21:15"]
headers={
    'POST': '/WebUntis/j_spring_security_check HTTP/1.1',
    'Host': 'tritone.webuntis.com',
    'Connection': 'keep-alive',
    'Content-Length': '64',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json',
    'Origin': 'https://tritone.webuntis.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://tritone.webuntis.com/WebUntis/index.do',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7'
}
API_url = 'https://tritone.webuntis.com/WebUntis/j_spring_security_check'
data = { #Bitte ausfuellen:
    'j_username': '',
    'j_password': '',
    'school': '',
    'token': ''
    }
text = ""
date = ""

def KlassenArbeiten():
    heute = datetime.now()
    listeDatum = []
    listeFach = []
    Arbeiten = []
    Arbeiten2 = []

    r =  requests.post(API_url, data=data, headers=headers)
    cookies = dict(JSESSIONID=r.cookies["JSESSIONID"], schoolname=r.cookies["schoolname"])
    def request(inp):
            r = requests.get('https://tritone.webuntis.com/WebUntis/api/public/printpreview/timetable?type=1&id=391&date=' + str(inp) + '&formatId=2', cookies=cookies)
            return r.text


    def Fach(var):
            return var.split("Z_0_0")[1].split(">")[1].split("<")[0]


    def Arbeit(Z1, Z2, Z3, date):
            tag = 1
            text_split = text.split(Z1 + "<br>")
            text_split = text_split[1] #Z1
            text_split = text_split.split(Z2)
            text_split = text_split[1] #Z2
            text_split = text_split.split(Z3)
            text_split = text_split[0]
            anzahl = text_split.count("</table>")
            text_split = text_split.split("</table>")
            date = date  - timedelta(days = 1)
            for i in range(0, anzahl):
                if (len(text_split[i]) > 100):
                    if (text_split[i].count("br") >= 1):
                        date = date  + timedelta(days = 1)
                    if (text_split[i].count("A_0_13") >= 1):
                            listeDatum.append(date.strftime("%d.%m.%y"))
                            listeFach.append(str(Fach(text_split[i])))
                    if (date == datetime.strptime(str(text.split("Montag<br>")[1].split("<")[0]), "%d.%m.%y")):
                            date = date  + timedelta(days = 1)


    for i in range(0, anzahl_wochen):
            now = heute + timedelta(days = i*7)
            text = request(int(now.strftime("%Y%m%d")))#                          diese Woche
            if (len(text) >= 3000):
                    #Dat_Mon = text.split("Montag<br>")[1].split("<")[0].split(".")
                    date = datetime.strptime(str(text.split("Montag<br>")[1].split("<")[0]), "%d.%m.%y")
                    for x in range(0, len(AnfangStunde) - 1):
                            Arbeit(AnfangStunde[x], EndeStunde[x], AnfangStunde[x + 1], date)

    for i in range(0, len(listeFach)):
            Arbeiten.append(listeDatum[i] + ": " + listeFach[i])

    Arbeiten.sort()
    for i in range (0, len(Arbeiten)):
            if (Arbeiten2.count(Arbeiten[i]) < 1):
                    Arbeiten2.append(Arbeiten[i])
    for i in range(0, len(Arbeiten2)):
        text = text + Arbeiten2[i] + "\n"
    return text

KlassenArbeiten()
with open("RAM/Arbeiten.txt", "w") as out:
    try:
        out.write(KlassenArbeiten().split("</html>")[-1])
    except:
        out.write(KlassenArbeiten())
    os.system("touch RAM/refresh")
    out.close()
