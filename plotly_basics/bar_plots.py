import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('WinterOlympics.csv')

print(df)

data = []

data_0 = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold', marker={'color': '#FFD700'})
data_1 = go.Bar(x=df['NOC'], y=df['Silver'], name='Silver', marker={'color': '#B4B4B4'})
data_2 = go.Bar(x=df['NOC'], y=df['Bronze'], name='Bronze', marker={'color': '#6A3805'})

data.extend([data_0, data_1, data_2])

layout = go.Layout(title='My Bar Chart', xaxis=dict(title='Country'), yaxis=dict(title='Total Medals Won'), barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
