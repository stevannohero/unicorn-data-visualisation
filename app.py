from flask import Flask,render_template
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import json
from funding_graph import *

app = Flask(__name__)

@app.route("/")
def hello():
	graphJSON = {}
	graphJSON['traveloka'] = get_graph("traveloka.csv",'rgb(93, 164, 214)','rgb(93, 93, 93)',100,3)
	graphJSON['bukalapak'] = get_graph("bukalapak.csv",'rgb(93, 164, 214)','rgb(93, 93, 93)',50,1)
	graphJSON['gojek'] = get_graph("gojek.csv",'rgb(93, 164, 214)','rgb(93, 93, 93)',150,5)
	graphJSON['tokopedia'] = get_graph("tokopedia.csv",'rgb(93, 164, 214)','rgb(93, 93, 93)',150,5)
	return render_template('index.html',graphJSON=graphJSON)
	# return render_template('index.html')