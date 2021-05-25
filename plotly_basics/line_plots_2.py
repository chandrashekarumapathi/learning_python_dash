import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import sqlalchemy

engine = sqlalchemy.create_engine(f'mysql+pymysql://{username}:{password}@localhost')

df = pd.read_sql('SELECT * FROM dev.world_data where date between "2021-05-01" and "2021-05-15" AND country IN ('
                 '"India", "US", "Brazil");', con=engine)


data = [go.Scatter(
    x=df['date'],
    y=df['total_confirmed'],
    mode='lines',
    name='line')
]

pyo.plot(data)
