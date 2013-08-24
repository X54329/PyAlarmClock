import datetime
def genAlarmTimeText():
	now = datetime.datetime.now()
	if (now.strftime('%d') == '01' or now.strftime('%d') == '21' or  now.strftime('%d') == '31'): 
		return now.strftime('Today is %A, %B %dst. The current time is %I %M %P.')
	elif (now.strftime('%d') == '02' or now.strftime('%d') == '22'): 
		return now.strftime('Today is %A, %B %dnd. The current time is %I %M %P.')
	elif (now.strftime('%d') == '03' or now.strftime('%d') == '23'): 
		return now.strftime('Today is %A, %B %drd. The current time is %I %M %P.')
	else:
		return now.strftime('Today is %A, %B %dth. The current time is %I %M %P.')

print genAlarmTimeText()
