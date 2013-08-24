import datetime
import requests
import  pywapi
import sys
import time
from BeautifulSoup import BeautifulStoneSoup

alarmTime = sys.argv[1]
alarmTimeHours, alarmTimeMinutes = alarmTime.split(':')

Internet = True
WeatherConnection = True
CNNConnection = True
WestBloomConnection = True
alarmTimeText = ''
alarmWeatherText = ''
alarmDiagText = ''
alarmNewsText = ''
#alarmFile = open('AlarmFile', 'w'

def isTime():
	now = datetime.datetime.now()	
	if (alarmTimeHours == now.strftime('%H') and alarmTimeMinutes == now.strftime('%M')):
		return True
	else:
		return False

def genAlarmTimeText():
	now = datetime.datetime.now()
	if (now.strftime('%d') == '01' or now.strftime('%d') == '21' or now.strftime('%d') == '31'): 
		return now.strftime('Today is %A, %B %dst. The current time is %I %M %P.\n')
	elif (now.strftime('%d') == '02' or now.strftime('%d') == '22'): 
		return now.strftime('Today is %A, %B %dnd. The current time is %I %M %P.\n')
	elif (now.strftime('%d') == '03' or now.strftime('%d') == '23'): 
		return now.strftime('Today is %A, %B %drd. The current time is %I %M %P.\n')
	elif(True):
		return now.strftime('Today is %A, %B %dth. The current time is %I %M %P.\n')

def genAlarmDiagText():
	tempalarmdiagtext = ''
	if (requests.get('http://www.weather.com').status_code != requests.codes.ok):
		tempalarmdiagtext = tempalarmdiagtext + "I cannot connect to weather dot com at this time,\n"
		WeatherConnection = False
	elif(True):
		WeatherConnection = True
	if (requests.get('http://www.CNN.com').status_code != requests.codes.ok):
		tempalarmdiagtext = tempalarmdiagtext + "I cannot connect to cnn dot com at this time,\n"
		CNNConnection = False
        elif(True):
                CNNConnection = True
	if (requests.get('http://www.westbloomfield.k12.mi.us').status_code != requests.codes.ok):
		tempalarmdiagtext = tempalarmdiagtext + "I cannot connect to weather dot com at this time,\n\n"
		WestBloomConnection = False
        elif(True):
                WestBloomConnection = True
	if (not WeatherConnection and not CNNConnection and not WestBloomConnection and requests.get('http://www.google.com').status_code != requests.codes.ok):
		Internet = False
		tempalarmdiagtext = tempalarmdiagtext + "In fact, It appears I have no internet connection.\n\n"
        elif(True):
                Internet = True
	return tempalarmdiagtext


def genAlarmWeatherText():
	tempweatherstr = ''
	if (WeatherConnection and Internet):
		weatherResult = pywapi.get_weather_from_weather_com('48324', 'imperial')
		if (weatherResult['current_conditions']['text'] != "N/A"):
			tempweatherstr = 'It is currently ' + weatherResult['current_conditions']['text']
		if(weatherResult['current_conditions']['temperature'] != 'N/A'):
                			tempweatherstr = tempweatherstr + ' with a temperature of ' + weatherResult['current_conditions']['temperature']
		if(weatherResult['current_conditions']['temperature'] != 'N/A'):
                			tempweatherstr = tempweatherstr + ' degrees fairenheit that feels like ' + weatherResult['current_conditions']['feels_like'] + ' degrees fairenheight\n'
		if (weatherResult['forecasts'][0]['high'] != "N/A"):
			tempweatherstr = tempweatherstr + ' The high for today is ' + weatherResult['forecasts'][0]['high'] + ' degrees fairenheight\n'
		if (weatherResult['forecasts'][0]['low'] != "N/A"):
			tempweatherstr = tempweatherstr + ' while the low is ' + weatherResult['forecasts'][0]['low'] + ' degrees fairenheight\n'
		if (weatherResult['forecasts'][0]['high'] != "N/A"):
			tempweatherstr = tempweatherstr + ' The current wind speed is ' + weatherResult['current_conditions']['wind']['speed'] + ' miles per hour'
		if (weatherResult['forecasts'][0]['day']['wind']['speed'] != "N/A"):
			tempweatherstr = tempweatherstr + ' and it is expected to be ' + weatherResult['forecasts'][0]['day']['wind']['speed'] + ' miles per hour later today\n'
		if (weatherResult['forecasts'][0]['day']['chance_precip'] != "N/A"):
			tempweatherstr = tempweatherstr + ' There is a  ' + weatherResult['forecasts'][0]['day']['chance_precip'] + ' percent chance of precipitation today\n\n'

	return tempweatherstr

def genAlarmNewsText():
	newstemptext = ''
	CNNrssTop = requests.get('http://rss.cnn.com/rss/cnn_topstories.rss')
	CNNrssTop = BeautifulStoneSoup(CNNrssTop.text)
	newstemptext = newstemptext + "Today's top headlines are \n" + str(CNNrssTop.findAll('title')[2]).split('>')[1].split('<')[0] + '\n'
	newstemptext = newstemptext + 'with the description \n' + str(CNNrssTop.findAll('description')[2]).split('>')[1].split('&')[0] + '\n'
        newstemptext = newstemptext + 'and \n' + str(CNNrssTop.findAll('title')[3]).split('>')[1].split('<')[0] + '\n'
	newstemptext = newstemptext + 'with the description \n' + str(CNNrssTop.findAll('description')[3]).split('>')[1].split('&')[0] + '\n'
	newstemptext = newstemptext + '\n'
	return newstemptext


while not isTime():
        time.sleep(20)

alarmTimeText = genAlarmTimeText()
alarmDiagText = genAlarmDiagText()
if (Internet):
        alarmWeatherText = genAlarmWeatherText()
	alarmNewsText = genAlarmNewsText()
print alarmTimeText + alarmDiagText + alarmWeatherText + alarmNewsText + "It's time for you to get up!"

