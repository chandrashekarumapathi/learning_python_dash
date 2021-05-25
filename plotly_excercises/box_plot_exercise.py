import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('abalone.csv')

y1 = np.random.choice(df['rings'], 30, replace=False)
y2 = np.random.choice(df['rings'], 20, replace=False)

data = [go.Box(y=y1, name='Sample 1'),
        go.Box(y=y2, name='Sample 2')]

layout = go.Layout(title='Box plot exercise')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
print(y1, '\n', y2)
