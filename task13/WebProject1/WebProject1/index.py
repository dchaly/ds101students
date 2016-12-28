from os import environ
from flask import Flask,render_template, request,json
from urllib.request import urlopen
from bs4 import BeautifulSoup
app=Flask(__name__)

@app.route('/')
def index():
    data = {
        "title": 'Home Page'}
    return render_template('site.html',data = data)

@app.route('/widget')
def widget():
    data = {
        "title": 'Widget Page'}
    return render_template('index.html',data = data)

@app.route('/getLinks', methods = ['POST'])
def getLinks():
    links = request.form['links']
    result = getInfo(links)
    keys = getContracts(result)
    return json.dumps({'status':'OK','links':links, 'contr':keys})

def getInfo(urls):
    arr = urls.split(',')
    result = []
    for u in arr:
        chId = u.find('=')
        if chId > 0:
            id = u[chId + 1:len(u)]
            result.append(id)
        else:
            searchStr = "contract/"
            chId = u.find(searchStr)
            if chId > 0:
                id = u[chId + len(searchStr):len(u)-1]
                result.append(id)
    return result;

urlApi = 'http://openapi.clearspending.ru/restapi/v3/contracts/get/?regnum='

def getContracts(ids):
    res = []
    for id in ids:
        adr = urlApi + id
        print (adr)
        page = urlopen(adr)
        soup = BeautifulSoup(page.read(),fromEncoding="unicode")
        data = json.loads(soup.prettify())
        contractData = data['contracts']['data'][0]
        print(contractData.keys())
        contr = contract()
        contr.url = contractData['contractUrl']
        contr.price = contractData['price']
        contr.currency = contractData['currency']['code']
        contr.regNum = contractData['regNum']
        contr.customer = contractData['customer']['fullName']
        contr.execution = contractData['execution']['startDate']
        contr.execution2 = contractData['execution']['endDate']
        contr.suppliers = contractData['suppliers'][0]['organizationName']
        contr.signDate = contractData['signDate']
        
        res.append(contr.format())
    return res    


def printArr(arr):
    for a in arr:
        print (str(a))
        print ("\n")


class contract:
    url = ''
    name = ''
    price = 0
    currency = ''
    regNum = ''
    customer = ''
    execution = ''
    execution2 = ''
    suppliers = ''
    signDate = ''

    def __init__(self):
        return super().__init__()


    def format(self):
        return {'url':self.url, 'name':self.name, 'currency':self.currency, 'price':self.price, 'regNum':self.regNum,
                'customer':self.customer, 'execution':self.execution, 'execution2':self.execution2,
                'suppliers':self.suppliers, 'signDate':self.signDate}


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT,debug=True)




#{
#    "contracts": {
#        "total": 1,
#        "data": [{
#                "contractProcedure": {
#                    "receiptDocuments": {
#                        "attachment": {
#                            "publishedContentId": "40CFA175FDF000E4E053AC11071AF6C1",
#                            "url": "http://zakupki.gov.ru/44fz/filestore/public/1.0/download/rgk2/file.html?uid=40CFA175FDF000E4E053AC11071AF6C1",
#                            "docRegNumber": "17813045441160004760110",
#                            "docDescription": "\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f 5253",
#                            "fileName": "\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f 5253.tif"
#                        }
#                    },
#                    "@schemeVersion": "6.3",
#                    "publishDate": "2016-11-09T13:30:44.738+03:00",
#                    "executions": {
#                        "execution": [{
#                                "docExecution": {
#                                    "code": "00",
#                                    "documentDate": "2016-11-07",
#                                    "name": "\u041f\u043b\u0430\u0442\u0435\u0436\u043d\u044b\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442",
#                                    "documentNum": "649096"
#                                },
#                                "currency": {
#                                    "code": "RUB",
#                                    "name": "\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u0443\u0431\u043b\u044c"
#                                },
#                                "product": "\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f\t4893",
#                                "paid": "46127.00",
#                                "paidRUR": "46127.00"
#                            },
#                            {
#                                "docExecution": {
#                                    "code": "00",
#                                    "documentDate": "2016-11-07",
#                                    "name": "\u041f\u043b\u0430\u0442\u0435\u0436\u043d\u044b\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442",
#                                    "documentNum": "649106"
#                                },
#                                "currency": {
#                                    "code": "RUB",
#                                    "name": "\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u0443\u0431\u043b\u044c"
#                                },
#                                "product": "\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f\t4880",
#                                "paid": "46127.00",
#                                "paidRUR": "46127.00"
#                            },
#                            {
#                                "docExecution": {
#                                    "code": "00",
#                                    "documentDate": "2016-11-07",
#                                    "name": "\u041f\u043b\u0430\u0442\u0435\u0436\u043d\u044b\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442",
#                                    "documentNum": "649131"
#                                },
#                                "currency": {
#                                    "code": "RUB",
#                                    "name": "\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u0443\u0431\u043b\u044c"
#                                },
#                                "product": "\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f\t4851",
#                                "paid": "46127.00",
#                                "paidRUR": "46127.00"
#                            },
#                            {
#                                "docExecution": {
#                                    "code": "00",
#                                    "documentDate": "2016-11-07",
#                                    "name": "\u041f\u043b\u0430\u0442\u0435\u0436\u043d\u044b\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442",
#                                    "documentNum": "649075"
#                                },
#                                "currency": {
#                                    "code": "RUB",
#                                    "name": "\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u0443\u0431\u043b\u044c"
#                                },
#                                "product": "\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f\t4782",
#                                "paid": "45427.00",
#                                "paidRUR": "45427.00"
#                            },
#                            {
#                                "docExecution": {
#                                    "code": "00",
#                                    "documentDate": "2016-11-07",
#                                    "name": "\u041f\u043b\u0430\u0442\u0435\u0436\u043d\u044b\u0439 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442",
#                                    "documentNum": "649118"
#                                },
#                                "currency": {
#                                    "code": "RUB",
#                                    "name": "\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u0443\u0431\u043b\u044c"
#                                },
#                                "product": "\u041d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f\t4773",
#                                "paid": "45427.00",
#                                "paidRUR": "45427.00"
#                            },
#                            {
#                                "product": "\u0413\u043e\u043b\u043e\u0432\u043a\u0430 CoCr (32.50.23.000): 1,00 \u0428\u0422;\u041d\u043e\u0436\u043a\u0430 Polar (Ti/HA) (32.50.23.000): 1,00 \u0428\u0422;",
#                                "paidRUR": "0.00",
#                                "paid": "0.00",
#                                "docExecution": {
#                                    "code": "01",
#                                    "documentDate": "2016-11-03",
#                                    "name": "\u0422\u043e\u0432\u0430\u0440\u043d\u0430\u044f \u043d\u0430\u043a\u043b\u0430\u0434\u043d\u0430\u044f",
#                                    "documentNum": "5253"
#                                },
#                                "currency": {
#                                    "code": "RUB",
#                                    "name": "\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u0443\u0431\u043b\u044c"
#                                },
#                                "quantityContractSubjects": {
#                                    "quantityContractSubject": [{
#                                            "sid": "109005925",
#                                            "quantity": "1.0"
#                                        },
#                                        {
#                                            "sid": "109005929",
#                                            "quantity": "1.0"
#                                        }]
#                                }
#                            }],
#                        "productsCountries": {
#                            "productsCountry": [{
#                                    "OKPD2": {
#                                        "code": "32.50.23.000",
#                                        "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                                    },
#                                    "productName": "\u0413\u043e\u043b\u043e\u0432\u043a\u0430 CoCr",
#                                    "sid": "109005925",
#                                    "country": {
#                                        "countryCode": "840",
#                                        "countryFullName": "\u0421\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u043d\u044b\u0435 \u0428\u0442\u0430\u0442\u044b \u0410\u043c\u0435\u0440\u0438\u043a\u0438"
#                                    }
#                                },
#                                {
#                                    "OKPD2": {
#                                        "code": "32.50.23.000",
#                                        "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                                    },
#                                    "productName": "\u041d\u043e\u0436\u043a\u0430 Polar (Ti/HA)",
#                                    "sid": "109005929",
#                                    "country": {
#                                        "countryCode": "840",
#                                        "countryFullName": "\u0421\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u043d\u044b\u0435 \u0428\u0442\u0430\u0442\u044b \u0410\u043c\u0435\u0440\u0438\u043a\u0438"
#                                    }
#                                }]
#                        },
#                        "ordinalNumber": "34",
#                        "stage": {
#                            "endDate": "2017-01-31T00:00:00"
#                        },
#                        "finalStageExecution": "false"
#                    },
#                    "versionNumber": 1,
#                    "printForm": {
#                        "url": "http://zakupki.gov.ru/epz/contract/printForm/viewXml.html?contractProcedureId=63800619",
#                        "docRegNumber": "17813045441160004760109"
#                    },
#                    "okpd2okved2": "true",
#                    "id": "63800619"
#                },
#                "documentBase": "\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u043f\u043e\u0434\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0438\u0442\u043e\u0433\u043e\u0432 \u2116 2/441 \u043e\u0442 \u00ab23\u00bb \u0441\u0435\u043d\u0442\u044f\u0431\u0440\u044f 2016\u0433 \u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u043f\u043e\u0434\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0438\u0442\u043e\u0433\u043e\u0432 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0433\u043e \u0430\u0443\u043a\u0446\u0438\u043e\u043d\u0430 \u2116 0372100030616000479-3 \u043e\u0442 23.09.2016",
#                "scan": [{
#                        "url": "http://zakupki.gov.ru/44fz/filestore/public/1.0/download/rgk2/file.html?uid=3FBDA3DE599900C8E053AC11071AB8CE",
#                        "docDescription": "(\u042e\u043d\u0438\u0442\u041c\u0435\u0434\u0438\u043a\u0430\u043b) \u041a\u0422 441-\u044d\u0430.2016",
#                        "fileName": "(\u042e\u043d\u0438\u0442\u041c\u0435\u0434\u0438\u043a\u0430\u043b) \u041a\u0422 441-\u044d\u0430.2016.tif"
#                    }],
#                "number": "441-\u044d\u0430/2016",
#                "currentContractStage": "E",
#                "id": "30080750",
#                "fileVersion": "2016110100_018",
#                "placing": "12011",
#                "regionCode": "78",
#                "contractUrl": "http://zakupki.gov.ru/epz/contract/contractCard/common-info.html?reestrNumber=1781304544116000476",
#                "signDate": "2016-10-04T00:00:00",
#                "price": 3273806.0,
#                "placingWayCode": "EAP44",
#                "foundation": {
#                    "fcsOrder": {
#                        "notificationNumber": "0372100030616000479",
#                        "placing": "12011",
#                        "lotNumber": "1"
#                    }
#                },
#                "fz": "44",
#                "protocolDate": "2016-09-23",
#                "publishDate": "2016-10-26T13:46:25.044+03:00",
#                "regNum": "1781304544116000476",
#                "versionNumber": 2,
#                "schemaVersion": "6.3",
#                "execution": {
#                    "startDate": "2016-10-04T00:00:00",
#                    "endDate": "2017-01-31T00:00:00"
#                },
#                "customer": {
#                    "kpp": "780401001",
#                    "regNum": "03721000306",
#                    "fullName": "\u0424\u0415\u0414\u0415\u0420\u0410\u041b\u042c\u041d\u041e\u0415 \u0413\u041e\u0421\u0423\u0414\u0410\u0420\u0421\u0422\u0412\u0415\u041d\u041d\u041e\u0415 \u0411\u042e\u0414\u0416\u0415\u0422\u041d\u041e\u0415 \u0423\u0427\u0420\u0415\u0416\u0414\u0415\u041d\u0418\u0415 \"\u0420\u041e\u0421\u0421\u0418\u0419\u0421\u041a\u0418\u0419 \u041e\u0420\u0414\u0415\u041d\u0410 \u0422\u0420\u0423\u0414\u041e\u0412\u041e\u0413\u041e \u041a\u0420\u0410\u0421\u041d\u041e\u0413\u041e \u0417\u041d\u0410\u041c\u0415\u041d\u0418 \u041d\u0410\u0423\u0427\u041d\u041e-\u0418\u0421\u0421\u041b\u0415\u0414\u041e\u0412\u0410\u0422\u0415\u041b\u042c\u0421\u041a\u0418\u0419 \u0418\u041d\u0421\u0422\u0418\u0422\u0423\u0422 \u0422\u0420\u0410\u0412\u041c\u0410\u0422\u041e\u041b\u041e\u0413\u0418\u0418 \u0418 \u041e\u0420\u0422\u041e\u041f\u0415\u0414\u0418\u0418 \u0418\u041c\u0415\u041d\u0418 \u0420.\u0420. \u0412\u0420\u0415\u0414\u0415\u041d\u0410\" \u041c\u0418\u041d\u0418\u0421\u0422\u0415\u0420\u0421\u0422\u0412\u0410 \u0417\u0414\u0420\u0410\u0412\u041e\u041e\u0425\u0420\u0410\u041d\u0415\u041d\u0418\u042f \u0420\u041e\u0421\u0421\u0418\u0419\u0421\u041a\u041e\u0419 \u0424\u0415\u0414\u0415\u0420\u0410\u0426\u0418\u0418",
#                    "inn": "7813045441",
#                    "postalAddress": "\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0430\u044f \u0424\u0435\u0434\u0435\u0440\u0430\u0446\u0438\u044f, 195427, \u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433, \u0423\u041b \u0410\u041a\u0410\u0414\u0415\u041c\u0418\u041a\u0410 \u0411\u0410\u0419\u041a\u041e\u0412\u0410, 8"
#                },
#                "currency": {
#                    "code": "RUB",
#                    "name": "\u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u0443\u0431\u043b\u044c"
#                },
#                "suppliers": [{
#                        "kpp": "774301001",
#                        "factualAddress": "125212, \u0420\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0430\u044f \u0424\u0435\u0434\u0435\u0440\u0430\u0446\u0438\u044f  (643) , \u0433. \u041c\u043e\u0441\u043a\u0432\u0430 (77), \u0448\u043e\u0441\u0441\u0435 \u0413\u043e\u043b\u043e\u0432\u0438\u043d\u0441\u043a\u043e\u0435, \u0434.8, \u043a\u043e\u0440\u043f\u0443\u0441 2\u0410, \u043e\u0444\u0438\u0441 64",
#                        "organizationName": "\u041e\u0411\u0429\u0415\u0421\u0422\u0412\u041e \u0421 \u041e\u0413\u0420\u0410\u041d\u0418\u0427\u0415\u041d\u041d\u041e\u0419 \u041e\u0422\u0412\u0415\u0422\u0421\u0422\u0412\u0415\u041d\u041d\u041e\u0421\u0422\u042c\u042e \"\u042e\u041d\u0418\u0422\u041c\u0415\u0414\u0418\u041a\u0410\u041b\"",
#                        "legalForm": {
#                            "code": "12300",
#                            "singularName": "\u041e\u0431\u0449\u0435\u0441\u0442\u0432\u043e \u0441 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043d\u043e\u0439 \u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u044c\u044e"
#                        },
#                        "inn": "7715920560",
#                        "participantType": "U",
#                        "contactInfo": {
#                            "middleName": "\u041a",
#                            "lastName": "\u0422\u0443\u0440\u0434\u044b\u0431\u0435\u043a\u043e\u0432",
#                            "firstName": "\u0421"
#                        }
#                    }],
#                "loadId": 226,
#                "finances": {
#                    "extrabudgetFunds": {
#                        "stages": [{
#                                "endDate": "2017-01-31T00:00:00",
#                                "payments": {
#                                    "paymentSum": "3242506.00",
#                                    "paymentYear": "2016",
#                                    "paymentSumRUR": "3242506.00",
#                                    "paymentMonth": "12"
#                                }
#                            },
#                            {
#                                "payments": {
#                                    "paymentSum": "31300.00",
#                                    "paymentYear": "2017",
#                                    "paymentSumRUR": "31300.00",
#                                    "paymentMonth": "1"
#                                }
#                            }]
#                    },
#                    "extrabudget": {
#                        "code": "60",
#                        "name": "\u0421\u0440\u0435\u0434\u0441\u0442\u0432\u0430 \u0431\u044e\u0434\u0436\u0435\u0442\u043d\u044b\u0445 \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0439"
#                    }
#                },
#                "mongo_id": "582130c5878ec343d82043ff",
#                "products": [{
#                        "name": "\u041d\u043e\u0436\u043a\u0430 SL-Plus MIA (Ti-Plasma/HA)",
#                        "OKEI": {
#                            "code": "796",
#                            "name": "\u0428\u0422"
#                        },
#                        "price": 30659.0,
#                        "OKPD2": {
#                            "code": "32.50.23.000",
#                            "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                        },
#                        "sid": "109005923",
#                        "sum": 398567.0,
#                        "quantity": "13.0"
#                    },
#                    {
#                        "name": "\u0427\u0430\u0448\u043a\u0430 R3 MultiHole",
#                        "OKEI": {
#                            "code": "796",
#                            "name": "\u0428\u0422"
#                        },
#                        "price": 19821.0,
#                        "OKPD2": {
#                            "code": "32.50.23.000",
#                            "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                        },
#                        "sid": "109005924",
#                        "sum": 436062.0,
#                        "quantity": "22.0"
#                    },
#                    {
#                        "name": "\u0413\u043e\u043b\u043e\u0432\u043a\u0430 CoCr",
#                        "OKEI": {
#                            "code": "796",
#                            "name": "\u0428\u0422"
#                        },
#                        "price": 8345.0,
#                        "OKPD2": {
#                            "code": "32.50.23.000",
#                            "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                        },
#                        "sid": "109005925",
#                        "sum": 542425.0,
#                        "quantity": "65.0"
#                    },
#                    {
#                        "name": "\u0427\u0430\u0448\u043a\u0430 R3",
#                        "OKEI": {
#                            "code": "796",
#                            "name": "\u0428\u0422"
#                        },
#                        "price": 15000.0,
#                        "OKPD2": {
#                            "code": "32.50.23.000",
#                            "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                        },
#                        "sid": "109005926",
#                        "sum": 420000.0,
#                        "quantity": "28.0"
#                    },
#                    {
#                        "name": "\u0412\u0438\u043d\u0442 \u0441\u043f\u043e\u043d\u0433\u0438\u043e\u0437\u043d\u044b\u0439 \u0443\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u044b\u0439",
#                        "OKEI": {
#                            "code": "796",
#                            "name": "\u0428\u0422"
#                        },
#                        "price": 2066.0,
#                        "OKPD2": {
#                            "code": "32.50.23.000",
#                            "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                        },
#                        "sid": "109005927",
#                        "sum": 45452.0,
#                        "quantity": "22.0"
#                    },
#                    {
#                        "name": "\u041d\u043e\u0436\u043a\u0430 SL-Plus",
#                        "OKEI": {
#                            "code": "796",
#                            "name": "\u0428\u0422"
#                        },
#                        "price": 31300.0,
#                        "OKPD2": {
#                            "code": "32.50.23.000",
#                            "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                        },
#                        "sid": "109005928",
#                        "sum": 438200.0,
#                        "quantity": "14.0"
#                    },
#                    {
#                        "name": "\u041d\u043e\u0436\u043a\u0430 Polar (Ti/HA)",
#                        "OKEI": {
#                            "code": "796",
#                            "name": "\u0428\u0422"
#                        },
#                        "price": 32000.0,
#                        "OKPD2": {
#                            "code": "32.50.23.000",
#                            "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                        },
#                        "sid": "109005929",
#                        "sum": 704000.0,
#                        "quantity": "22.0"
#                    },
#                    {
#                        "name": "\u0412\u043a\u043b\u0430\u0434\u044b\u0448 R3 \u043a\u0440\u043e\u0441\u0441-\u043b\u0438\u043d\u043a \u043f/\u044d",
#                        "OKEI": {
#                            "code": "796",
#                            "name": "\u0428\u0422"
#                        },
#                        "price": 5782.0,
#                        "OKPD2": {
#                            "code": "32.50.23.000",
#                            "name": "\u0427\u0430\u0441\u0442\u0438 \u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438 \u043f\u0440\u043e\u0442\u0435\u0437\u043e\u0432 \u0438 \u043e\u0440\u0442\u043e\u043f\u0435\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043f\u0440\u0438\u0441\u043f\u043e\u0441\u043e\u0431\u043b\u0435\u043d\u0438\u0439"
#                        },
#                        "sid": "109005930",
#                        "sum": 289100.0,
#                        "quantity": "50.0"
#                    }],
#                "printFormUrl": "http://zakupki.gov.ru/epz/contract/printForm/viewXml.html?contractInfoId=30080750"
#            }],
#        "page": 1,
#        "perpage": 1
#    }
#}