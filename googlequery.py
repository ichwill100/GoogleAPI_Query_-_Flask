#!/usr/bin/python

from flask import Flask, render_template
import requests
import settings

app = Flask(__name__)

 
@app.route('/')
def main():
	#import pdb ; pdb.set_trace()
	req = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=W128HD&destinations=300+stjohnstreet+London&UK&mode=driving&language=en-US&key={}').format(settings.key)
	
	req_json = req.json()
	print (req_json)

	trip_dist = req_json['rows'][0]['elements'][0]['duration']['text']

	#return ('Your trip duration is: {}').format(trip_duration)
	return render_template('index.html', trip_distance = trip_dist)

if __name__ == "__main__": 
	#main()
	app.run(host='0.0.0.0')


## https://maps.googleapis.com/maps/api/distancematrix/json?origins=W128HD&destinations=300+stjohnstreet+London&UK&mode=driving&language=en-US&key=(key)
