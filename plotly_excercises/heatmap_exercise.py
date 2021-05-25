import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('flights.csv')

data = [go.Heatmap(x=df['year'], y=df['month'], z=df['passengers'].values.tolist(), colorscale='Jet')]

layout = go.Layout(title='Heatmap Exercise')

fig = go.Figure(data, layout)

pyo.plot(fig)
