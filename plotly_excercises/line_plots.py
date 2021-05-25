import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Data Extraction
df = pd.read_csv(r'YumaAZ.csv')

# Prepare a list to execute the analysis as per requirement
# days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

# Initialize an empty list to use in future
# data = []
#
# # Loop through to get the results for each day and append the results to the empty list
# for day in days:
#     meta_data = go.Scatter(
#         x=df['LST_TIME'],
#         y=df[df['DAY'] == day]['T_HR_AVG'],
#         mode='lines',
#         name=day
#     )
#     data.append(meta_data)

data = [{
    'x': df['LST_TIME'],
    'y': df[df['DAY'] == day]['T_HR_AVG'],
    'name': day
    } for day in df['DAY'].unique()
]

# Create a layout
layout = go.Layout(title='Line Exercise',
                   xaxis=dict(title='Time'),
                   yaxis={'title': 'Temperature'})

# Combine the results and the layout to form a figure
fig = go.Figure(data=data, layout=layout)

# Plot the figure
pyo.plot(fig)
