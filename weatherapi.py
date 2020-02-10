import requests
import csv

airportname=input("Please enter the full name of the airport you are searching for:")
filename='us-airport-codes.csv'
urllist=["http://api.openweathermap.org/data/2.5/weather?lat="]
colist=[]
count=0
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        count=count+1
        if airportname==row[2]:
            coordinates=row[11]
            print("The {}".format(row[2]),"is a {}".format(row[1]),"which is belongs to {}.".format(row[7]),end=" ")
            costr=row[11]
            count=0       
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
    urllist.append('&APPID=yourownkeyofapi')
    url="".join(urllist)
    r = requests.get(url)
    response_dict = r.json()
    #print(response_dict)
    weather_dic=response_dict['weather']
    weather_info=weather_dic[0]
    wind_dic=response_dict['wind']
    main_dic=response_dict['main']
    print("The current weather of the airport is {},".format(weather_info['description']),end=" ")
    print("and the temperature is {}".format(main_dic['temp']),"The pressure is {}".format(main_dic['pressure']),"meanwhile the humidity is{}".format(main_dic['humidity']),end=" ")
    print("In addition the wind speed is {}".format(wind_dic['speed']),"with {}".format(wind_dic['deg']),"degrees")
