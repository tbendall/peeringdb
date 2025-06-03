#!/usr/bin/python3



""" website.py: A DevOps project to learn and demonstrate DevOps skills and knowledge """

__author__      = "Tristan Bendall/tristan@bendall.co" 
__version__     = "v0.1"

from flask import Flask, render_template
import os

application = Flask(__name__,template_folder='/home/azureuser/projects/project/devops/templates')

@application.route('/')
def index():

	a = {"d":"d"}

	print(os.getcwd())
	return render_template('template.html',output=a)



