#!/usr/bin/python3

""" webServe.py: A Python script to provide a web-front end for the main publicPeerings script """

__author__      = "Tristan Bendall/tristan@bendall.co" 
__version__     = "v1.2"

from publicPeerings import *

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

	return render_template('template.html')

@app.route('/publicPeers/')
def publicPeers():

	result = returnPublicPeers(web=True)

	return render_template('results.html',output=result)

@app.route('/execSummary/')
def execSummary():

	result = execSum(web=True)

	return render_template('results.html',output=result)


if __name__ == '__main__':
	
	app.run(debug=True,host='0.0.0.0',port=80)
