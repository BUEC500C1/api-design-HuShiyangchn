import requests
import csv
import sys
import tornado.ioloop
import tornado.web
import json

def weather(airport):
    airportname=airport
    #input("Please enter the full name of the airport you are searching for:")
    filename='us-airport-codes.csv'
    urllist=["http://api.openweathermap.org/data/2.5/weather?lat="]
    #colist=[]
    #count=0
    with open(filename) as f:
        reader = csv.reader(f)
        #header_row = next(reader)
        for row in reader:
            #count=count+1
            if airportname==row[2]:
                #coordinates=row[11]
                airinfo = "The %s is a %s, which is belongs to %s." %(row[2],row[1], row[7])
                costr=row[11]
                #count=0       
    #if count==22875:
        #print("No such airport was found, please enter the full name of airport.")
    #elif count<22875:
    costr.lstrip("'")
    costr.rstrip("'")
    coli=costr.split(",")
    lon=coli[1]
    lat=str(int(float(coli[0])))
    lon=str(int(float(lon.lstrip())))
    urllist.append(lat)
    urllist.append('&lon=')
    urllist.append(lon)
    #add your openweather key here 
    urllist.append('&&APPID=0a129340c5fe92e70a136ea7b21382d5')
    url="".join(urllist)
    r = requests.get(url)
    response_dict = r.json()
    #print(response_dict)
    weather_dic=response_dict['weather']
    weather_info=weather_dic[0]
    wind_dic=response_dict['wind']
    main_dic=response_dict['main']
    '''
    sen1 = "The current weather of the airport is {},".format(weather_info['description'])
    sen2 = "and the temperature is {}.".format(main_dic['temp'])
    sen3 = "The pressure is {}".format(main_dic['pressure'])
    sen4 = "meanwhile the humidity is {}.".format(main_dic['humidity'])
    sen5 = "In addition the wind speed is {}".format(wind_dic['speed'])
    sen6 = "with {}".format(wind_dic['deg'])
    sen7 = "degrees"
    '''

    return   airinfo + " The current weather of the airport is %s, and the temperature is %s. \
             The pressure is %s meanwhile the humidity is %s. \
             In addition, the wind speed is %s \
             with %s degrees." %(weather_info['description'], main_dic['temp'], main_dic['pressure'], main_dic['humidity'], wind_dic['speed'], wind_dic['deg'])
             

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self): 
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        filename='us-airport-codes.csv'
        #if self.request.arguments.has_key("airportname"):
        greeting = self.get_argument('id', 'Hello')
        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                if greeting==row[2]:
                    self.write(str(weather(greeting)))
                #else:
                    #self.write("none")

settings = dict(cookie_secret="P1/V61oETzdkLmGeJJFuYh7Eo5KXQAGaYgEQnp2XdTo=", debug=True)
application = tornado.web.Application([(r"/", MainHandler), ], **settings)

if __name__ == "__main__":
    application.listen(8888)
    print("The rest service is running please use your browser to get the api response. The address should be your ip address:8888?/id=The airport your are searching for")
    tornado.ioloop.IOLoop.current().start()
