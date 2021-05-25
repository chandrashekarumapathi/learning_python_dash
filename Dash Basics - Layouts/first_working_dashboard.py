import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

x = np.random.randint(1, 101, 100)
y = np.random.randint(1, 101, 100)

app.layout = html.Div(children=[
    html.H1('Dashboard', style={'textAlign': 'center', 'color': 'cyan'}),
    dcc.Graph(id='my_dash',
              figure={
                  'data': [
                      go.Scatter(
                          x=x,
                          y=y,
                          mode='markers',
                          marker=dict(size=10,
                                      symbol='star',
                                      color='red'))],
                  'layout': go.Layout(title='My Title',
                                      xaxis=dict(title='My x axis'),
                                      yaxis=dict(title='My y axis'),
                                      plot_bgcolor='black',
                                      paper_bgcolor='black',
                                      font={'color': 'cyan'})
              })], style={'backgroundColor': 'black'}
)


if __name__ == '__main__':
    app.run_server()