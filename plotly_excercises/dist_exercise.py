import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('iris.csv')

hist_data = [df[df['class'] == response]['petal_length'].tolist() for response in df['class'].unique()]

group_labels = df['class'].unique()

print(df.to_string())
figure = ff.create_distplot(hist_data, group_labels,  bin_size=[0.25, 0.25, 0.25])

pyo.plot(figure)
