import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('OldFaithful.csv')

app.layout = html.Div(children=[
    html.H1('Dashboard Exercise', style={'textAlign': 'center', 'color': 'black'}),
    dcc.Graph(id='exercise',
              figure={
                  'data': [
                      go.Scatter(
                          x=df['X'],
                          y=df['Y'],
                          mode='markers',
                          marker=dict(size=10,
                                      symbol='circle',
                                      # color='red'
                                      )
                      )
                  ],
                  'layout': go.Layout(title='Scatter Plot',
                                      xaxis=dict(title='Duration of current eruption in minutes'),
                                      yaxis=dict(title='Time interval until next eruption in minutes'),
                                      # plot_bgcolor='black',
                                      # paper_bgcolor='black',
                                      # font={'color': 'cyan'}
                                      )
              })
] # style={'backgroundColor': 'black'}
)


if __name__ == '__main__':
    app.run_server()
