from flask import Flask, redirect, render_template, request, url_for
from bs4 import BeautifulSoup
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class SelectSity(FlaskForm):
    first_sity = SelectField(
			"Select sity: ", choices=[
    	("mos", "Москва"), 
    	("per", "Пермь"),
			("tor", "Торонто"),
			("sev", "Североуральск"),
			("gor", "Горячий ключ"),
			("eka", "Екатеринбург")])
    second_sity = SelectField(
			"Select sity: ", choices=[
    	("mos", "Москва"), 
    	("per", "Пермь"),
			("tor", "Торонто"),
			("sev", "Североуральск"),
			("gor", "Горячий ключ"),
			("eka", "Екатеринбург")])
@app.route("/", methods=['POST', 'GET'])
def index():
	t_eka = BeautifulSoup(requests.get("https://world-weather.ru/pogoda/russia/yekaterinburg/").text, 'html.parser').find("div", id = "weather-now-number").getText()
	t_tor = BeautifulSoup(requests.get("https://world-weather.ru/pogoda/canada/toronto/").text, 'html.parser').find("div", id = "weather-now-number").getText()
	t_sev = BeautifulSoup(requests.get("https://world-weather.ru/pogoda/russia/severouralsk/").text, 'html.parser').find("div", id = "weather-now-number").getText()
	t_gor = BeautifulSoup(requests.get("https://world-weather.ru/pogoda/russia/goryachy_klyuch/").text, 'html.parser').find("div", id = "weather-now-number").getText()
	t_per = BeautifulSoup(requests.get("https://world-weather.ru/pogoda/russia/perm/").text, 'html.parser').find("div", id = "weather-now-number").getText()
	t_mos = BeautifulSoup(requests.get("https://world-weather.ru/pogoda/russia/moscow/").text, 'html.parser').find("div", id = "weather-now-number").getText()
	tt_gor = int(t_gor[1:-1])
	tt_sev = int(t_sev[1:-1])
	tt_mos = int(t_mos[1:-1])
	tt_per = int(t_per[1:-1])
	tt_eka = int(t_eka[1:-1])
	tt_tor = int(t_tor[1:-1])
	temperatures = ["gor", "sev", "per", "tor", "mos", "eka"]
	sityes = ["Североуральске", "Москве", "Екатиренбурге", "Перми", "Торонто", "Горячем Ключе"]
	form = SelectSity()

	if request.method == 'POST':
		for i in range(len(temperatures)):
			for j in range(len(temperatures)):
				if form.first_sity.data == temperatures[i] and form.second_sity.data == temperatures[j]:
					first = locals()['tt_'+temperatures[i]]
					second = locals()['tt_'+temperatures[j]]
					sity1 = form.first_sity.data
					sity2 = form.second_sity.data
					temp = [first, second]
					max1 = max(temp)
					min2 = min(temp)
				if form.first_sity.data=="sev":
					gor = "Североуральске"
				elif form.first_sity.data=="gor":
					gor = "Горячем Ключе"
				elif form.first_sity.data=="eka":
					gor = "Екатeринбурге"
				elif form.first_sity.data=="per":
					gor = "Перми"
				elif form.first_sity.data=="tor":
					gor = "Торонто"
				elif form.first_sity.data=="mos":
					gor = "Москве"
				if form.second_sity.data=="sev":
					gor2 = "Североуральске"
				elif form.second_sity.data=="gor":
					gor2 = "Горячем Ключе"
				elif form.second_sity.data=="eka":
					gor2 = "Екатиренбурге"
				elif form.second_sity.data=="per":
					gor2 = "Перми"
				elif form.second_sity.data=="tor":
					gor2 = "Торонто"
				elif form.second_sity.data=="mos":
					gor2 = "Москве"
				
		return render_template("index.html", temp=temp, max1=max1, min=min2, gor=gor, gor2=gor2,) 
	return render_template("base.html", form=form)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port = 5000)
