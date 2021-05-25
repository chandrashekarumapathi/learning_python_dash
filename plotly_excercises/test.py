import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('mocksurvey.csv', index_col=0)

data = [go.Bar(x=df.index, y=df[response], name=response) for response in df.columns]

layout = go.Layout(title='Bar Chart Exercise', xaxis=dict(title='Questions'), yaxis=dict(title='Answers'), barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
