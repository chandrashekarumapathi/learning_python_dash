import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(
    x=random_x,
    y=random_y,
    text='MY FIRST SCATTER',
    mode='markers',
    marker=dict(
        size=10,
        color='rgb(255, 0, 0)',
        symbol='circle-dot',
        line={'width': 1}
    )
)]

pyo.plot(data)