import pywapi


def genAlarmWeatherText():
	tempweatherstr = ''
	WeatherConnection = True
	Internet = True
	if (WeatherConnection and Internet):
		weatherResult = pywapi.get_weather_from_weather_com('48324', 'imperial')
		tempweatherstr = 'It is currently ' + weatherResult['current_conditions']['text']
		tempweatherstr = tempweatherstr + ' with a temperature of ' + weatherResult['current_conditions']['temperature'] 
		tempweatherstr = tempweatherstr + ' degrees that feels like ' + weatherResult['current_conditions']['feels_like'] + ' degrees'
		tempweatherstr = tempweatherstr + ' The high for today is ' + weatherResult['forecasts'][0]['high']
		tempweatherstr = tempweatherstr + ' while the low is ' + weatherResult['forecasts'][0]['low']
		tempweatherstr = tempweatherstr + ' The current wind speed is ' + weatherResult['current_conditions']['wind']['speed']
		tempweatherstr = tempweatherstr + ' and it is expected to be ' + weatherResult['forecasts'][0]['day']['wind']['speed'] + ' later today'
		tempweatherstr = tempweatherstr + ' There is a  ' + weatherResult['forecasts'][0]['day']['chance_precip'] + ' percent chance of precipitation '
		tempweatherstr = tempweatherstr + ' The high for today is ' + weatherResult['forecasts'][0]['high']
		print tempweatherstr

genAlarmWeatherText()
