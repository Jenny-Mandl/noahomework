from twilio.rest import TwilioRestClient
import datetime


day_of_week = datetime.date.today().weekday() #0 is Monday, 6 is Sunday
accountSID = 'AC4cfd696fe7a4d48d87b6ede6e11bb83e'
authToken = '0d70a8e8e087f149a9054d5c54dfbb0d'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+14432017284'
noahCellPhone = '+14436761293'
jennyCellPhone = '+14435404066'

if day_of_week == 6:
	body = 'Bah! Tomorrow: ENME350 Homework due at 8am! ENME350 lab Pre Lab due at 3pm! love, sheepy'
elif day_of_week == 0:
	body = 'Bahh! Today:ENME350 Homework due at 8am! ENME350 lab Pre Lab due at 3pm!\n\n Tomorrow: ENME392 -Statistics- due at 9am! I love stat, bah! ENME232 due at 5pm!'
elif day_of_week == 1:
	body = 'U da best Master Noah, here is whats on tap! \n\nToday:ENME392 -Statistics- due at 9am! Bah! I love stat, bah! ENME232 due at 5pm!\n\nTomorrow: ENME350 homework due at 8am! \n\nxoxo, Sheepy'
elif day_of_week == 2:
	body = 'Hi big master Noah!\n\nToday ENME350 homework due at 8am! \n\nTomorrow: ENME392 homework due at 9am!\n\n xoxo, luv Creatinine'
elif day_of_week == 3:
	body = ' *wiggle wiggle* hi!! its me, Creatinine! *squats* Today: ENME392 homework due at 9am! \n\nTomorrow: ENME232 thermo quiz in class at 9am! BIOE120 HW due at noon!'
else:
	body = ''


if len(body) != 0:
	message = twilioCli.messages.create(body = body ,from_ = myTwilioNumber, to = jennyCellPhone)
