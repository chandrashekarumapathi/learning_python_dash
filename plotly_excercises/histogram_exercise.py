import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r'C:\Users\chand\PycharmProjects\Learning_Dash\data\abalone.csv')

data = [go.Histogram(x=df['length'], xbins=dict(start=0, end=1, size=0.02))]

layout = go.Layout(title='Histogram Exercise')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)