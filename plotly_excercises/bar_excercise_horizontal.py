import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r'C:\Users\chand\PycharmProjects\Learning_Dash\data\mocksurvey.csv', index_col=0)

data = [go.Bar(x=df[response], y=df.index, name=response, orientation='h') for response in df.columns]

layout = go.Layout(title='Bar Chart Exercise', xaxis=dict(title='Questions'), yaxis=dict(title='Answers'), barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)