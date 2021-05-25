import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import subplots
import pandas as pd

df1 = pd.read_csv('SantaBarbaraCA.csv')
df2 = pd.read_csv('SitkaAK.csv')
df3 = pd.read_csv('YumaAZ.csv')

data1 = [go.Heatmap(x=df1['DAY'], y=df1['LST_TIME'], z=df1['T_HR_AVG'].values.tolist(), colorscale='Jet', zmin=5, zmax=40)]

data2 = [go.Heatmap(x=df2['DAY'], y=df2['LST_TIME'], z=df2['T_HR_AVG'].values.tolist(), colorscale='Jet', zmin=5, zmax=40)]

data3 = [go.Heatmap(x=df3['DAY'], y=df3['LST_TIME'], z=df3['T_HR_AVG'].values.tolist(), colorscale='Jet', zmin=5, zmax=40)]

fig = subplots.make_subplots(rows=1, cols=3, subplot_titles=['Santa', 'Alaska', 'Arizona'], shared_yaxes=True)

fig.add_traces(data1, 1, 1)
fig.add_traces(data2, 1, 2)
fig.add_traces(data3, 1, 3)

fig['layout'].update(title='Heatmaps with Subplots')

pyo.plot(fig)
