import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import json

def get_graph(filename,known_color,unknown_color,unknown_fund_size,scaler):
	dataset = pd.read_csv(filename)
	n_funding = len(dataset)
	unknown_code = -1

	funding_amount = dataset['Amount'].fillna(unknown_code).tolist()
	bubble_size = [s/scaler if s!=-1 else s*unknown_fund_size*-1/scaler for s in funding_amount ]
	bubble_color = [known_color if s!=-1 else unknown_color for s in funding_amount ]
	bubble_date = dataset['Date'].tolist()
	funding_round = dataset['Round'].tolist()
	size = dataset['Amount'].tolist()
	bubble_text=[]
	for i in range(len(funding_round)):
		if str(size[i])=='nan':
			bubble_text.append(funding_round[i]+"<br>"+str(bubble_date[i])+"<br><br>Undisclosed")
		else:
			bubble_text.append(funding_round[i]+"<br>"+str(bubble_date[i])+"<br><br>$"+str(size[i])+" M")


	trace0 = go.Scatter(
		text=bubble_text,
		x=bubble_date,
		y=[0]*n_funding,
		hoverinfo= 'text',
		mode='markers',
		marker=dict(
			color=bubble_color,
			size=bubble_size,
		)
	)
	 
	lay = go.Layout(
		xaxis=dict(
			range = [min(bubble_date),max(bubble_date)],
			showgrid=False,
			zeroline=False,
			showline=False

		),
		yaxis=dict(
			ticks='',
			showgrid=False,
			zeroline=False,
			showline=False,
			showticklabels=False
		),
		
	)
	data=[trace0]
	graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON