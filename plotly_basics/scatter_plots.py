import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = go.Scatter(x=random_x,
                  y=random_y,
                  mode='markers',
                  marker=dict(
                      size=10,
                      color='rgb(255, 0, 0)',
                      symbol='star',
                      line={'width': 1}
                  ))
layout = go.Layout(title='Hello Dash',
                   xaxis=dict(title='My X axis'),
                   yaxis={'title': 'My Y axis'},
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='scatter.html')