import pymongo
import sys
import urllib,json
from urllib.request import urlopen

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client.Zachet
db.drop_collection('theaters')
coll = db.theaters

url = 'http://bus.gov.ru/public/agency/extendedSearchAgencyNew.json?action=&agency=%D1%82%D0%B5%D0%B0%D1%82%D1%80&documentTypes=A&okatoSubElements=false&orderAttributeName=rank&orderDirectionASC=false&page=[NUM]&pageSize=10&ppoSubElements=false&primaryActivitySubElements=false&searchTermCondition=and&secondaryActivitySubElements=false&vguSubElements=true&withBranches=true'
urlB = 'http://bus.gov.ru/public/agency/last-annual-balance-F0503721-info.json?agencyId=[ID]'
page = 1
noagencies = False

while (noagencies != True):
    pageurl = url.replace('[NUM]', str(page))
    try:
        response = urlopen(pageurl)
        data = json.loads(response.read().decode("utf-8"))
    except:
        print("Page: ", page, " not found", sys.exc_info()[0])
        break
    #print(page)
    page += 1
    noagencies = (not data["agencies"]) ##not data["agencies"] = True when mass agencies empty
    for agency in data["agencies"]:
        id = agency["agencyId"]
        name = agency["fullName"]
        balanceurl = urlB.replace('[ID]', str(id))
        try:
            responseB = urlopen(balanceurl)
            dataB = json.loads(responseB.read().decode("utf-8"))
            incomings_total = dataB["annualBalance"]["incomings"][0]
            balance = float(incomings_total["incomeActivityEndYear"].replace(',', ''))
        except:
            balance = 0
        coll.save({'id': id, 'name': name, 'balance': balance})


html = '<!DOCTYPE html>'
html += '<html>'
html += '<head>'
html += '<meta charset="utf-8">'
html += '<title>Рейтинг "богатые театры / бедные театры" </title>'
html += '</head>'

html = "<body>"
html += '<h1>Рейтинг "богатые театры / бедные театры"</h1>'
html += '<table border="1" width="100%">'

count = 1
for agency in coll.find().sort('balance', pymongo.DESCENDING):
    html += "<tr><td>" + str(count) + "</td><td>" + agency['name'] + "</td><td>" + str(agency['balance']) + "</td></tr>"
    count += 1

html += "</table>"
html += "</body>"
html += "</html>"

with open ('Rating.html', 'w+') as file:
    file.write(html)









