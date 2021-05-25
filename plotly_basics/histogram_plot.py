import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('mpg.csv')

data = [go.Histogram(x=df['mpg'], xbins=dict(start=0, end=50, size=5))]

layout = go.Layout(title='Histogram')

fig = go.Figure(data=data, layout=layout)

print(df.to_string())

pyo.plot(fig)
