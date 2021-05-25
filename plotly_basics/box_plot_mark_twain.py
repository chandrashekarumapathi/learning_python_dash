import plotly.offline as pyo
import plotly.graph_objs as go

snodgrass = [.209, .205, .196, .210, .202, .207, .224, .223, .220, .201]
twain = [.225, .262, .217, .240, .230, .229, .235, .217]

data = [go.Box(y=snodgrass, name='Snodgrass'),
        go.Box(y=twain, name='Mark Twain')]

layout = go.Layout(title='Mark Twain Analysis')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)