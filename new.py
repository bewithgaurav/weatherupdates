#import requests
import urllib.request, json
from flask import *
from datetime import *
from celery import Celery
from flask_mail import Mail, Message

celery = Celery()
app=Flask(__name__)
#mail=Mail(celery)
app.config['MAIL_SERVER']='smtp.zoho.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourEmail'
app.config['MAIL_PASSWORD'] = 'yourPass'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@celery.task(name='tasks.add')
def hello():
	'''data = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=london&appid=c2622bee9741899b36c11d84c77ede89").read().decode('utf8')
	output = json.loads(data)
	h=str(datetime.now())
	print(output)'''
	#fun()
	with app.app_context():
		data = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=london&appid=c2622bee9741899b36c11d84c77ede89").read().decode('utf8')
		output = json.loads(data)
		a=str(output['name'])
		b=str(round(output['main']['temp']-273.15,2))
		c=str(round(output['main']['temp_max']-273.15,2))
		d=str(round(output['main']['temp_min']-273.15,2))
		h=str(datetime.now())
		deg=u'\N{DEGREE SIGN}'
		msgstring='The Current Temperature of '+ a + ' is : '+b+deg+'C'+'\nMax Temperature : '+c+deg+'C'+'\nMin Temperature : '+d+deg+'C' 
		msg = Message("Temperature Updates", sender = 'gaurav.sharma@shipoya.com', recipients = ['1995rishi@gmail.com'])
		msg.body = msgstring
		mail.send(msg)
   
	
