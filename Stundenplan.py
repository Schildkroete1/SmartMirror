from requests import *
from datetime import *
from ics import *
from os import *
import codecs

heute = datetime.now()

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
data = { # bitte ausfuellen
    'j_username': '',
    'j_password': '',
    'school': '',
    'token': ''
    }

text = ""
today = []
times = []

r =  post(API_url, data=data, headers=headers)
cookies = dict(JSESSIONID=r.cookies["JSESSIONID"], schoolname=r.cookies["schoolname"]) ##login to webuntis & getting cookies


def request(inp):
        r = get('https://tritone.webuntis.com/WebUntis/Ical.do?elemType=1&elemId=391&rpt_sd=' + str(inp), cookies=cookies)
        if(r.status_code == 200):
            return r.text
        else:
            print ("Error: " + str(r.status_code))


cal = Calendar(request(str(heute.strftime("%Y-%m-%d"))))
for events in cal.events:
    begin = datetime.strptime(str(events.begin), "%Y-%m-%dT%H:%M:%S+00:00")
    if(begin > heute) and (str(events.name) != "None") and (begin.strftime("%d") == heute.strftime("%d")):
        try:
                index = times.index(events.begin) # check if time was seen before
                today[index] = today[index] + " / " + events.name # if time is seen befor add the subject to this
        except:
                times.append(events.begin) # if time hasn't seen before add the element
                today.append(events.name)



if(len(today) == 0):
 tomorrow = True
 for events in cal.events:
        begin = datetime.strptime(str(events.begin), "%Y-%m-%dT%H:%M:%S+00:00")
        if(begin > heute) and (str(events.name) != "None") and (begin.strftime("%d") == (heute + timedelta(days= 1)).strftime("%d")):
                try:
                        index = times.index(events.begin) # check if time was seen before
                        today[index] = today[index] + " / " + events.name # if time is seen befor add the subject to this
                except:
                        times.append(events.begin) # if time hasn't seen before add the element
                        today.append(events.name)

for elements in today:
        text = text + elements + "\n"

with codecs.open("RAM/Stundenplan.txt", "w", "utf-8") as out:
        out.write(text)
        system("touch RAM/refresh")
        out.close()
