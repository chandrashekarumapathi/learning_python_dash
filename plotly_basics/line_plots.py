import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

graph_0 = go.Scatter(x=x_values,
                     y=y_values+5,
                     mode='markers',
                     name='stars',
                     marker=dict(
                         size=10,
                         color='rgb(255, 0, 0)',
                         symbol='star',
                         line={'width': 1}))

graph_1 = go.Scatter(x=x_values,
                     y=y_values,
                     mode='lines',
                     name='line',
                     marker=dict(color='rgb(255, 0, 0)'))

graph_2 = go.Scatter(x=x_values,
                     y=y_values-5,
                     mode='lines+markers',
                     name='hybrid',
                     marker=dict(
                         size=10,
                         color='rgb(255, 0, 0)',
                         symbol='star',
                         line={'width': 1}))

data = [graph_0, graph_1, graph_2]

layout = go.Layout(title='Hello Dash',
                   xaxis=dict(title='My X axis'),
                   yaxis={'title': 'My Y axis'})

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
