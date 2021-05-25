import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background': 'black', 'text': 'cyan'}

app.layout = html.Div(children=[
    html.H1('My Dash App!!!', style={'textAlign': 'center', 'color': colors['text']}),
    html.Div('My first step towards Dashboards', style={'textAlign': 'center', 'color': colors['text']}),
    dcc.Graph(id='my_graph',
              figure={'data': [
                  {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                  {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'NYC'}
              ],
                  'layout':{
                      'plot_bgcolor': colors['background'],
                      'paper_bgcolor': colors['background'],
                      'font': {'color': colors['text']},
                      'title': 'Example plot'
                  }
              })
], style={'backgroundColor': colors['background']}
)


if __name__ == '__main__':
    app.run_server()