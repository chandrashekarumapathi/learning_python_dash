import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r'C:\Users\chand\PycharmProjects\Learning_Dash\data\mpg.csv')

data = [go.Scatter(
    x=df['acceleration'],
    y=df['displacement'],
    mode='markers',
    text=df['name'],
    marker=dict(size=df['weight'] / 300,
                color=df['model_year'],
                showscale=True)
)]

layout = go.Layout(title='Bubble exercise',
                   xaxis=dict(title='Acceleration'),
                   yaxis=dict(title='Weight'),
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)

print(df.to_string())