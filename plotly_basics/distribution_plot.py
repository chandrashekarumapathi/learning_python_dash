import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200)
x2 = np.random.randn(200)-2
x3 = np.random.randn(200)+4
x4 = np.random.randn(200)+2

hist_data = [x1, x2, x3, x4]
group_labels = ['x1', 'x2', 'x3', 'x4']

figure = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.2, 0.3, 0.4])

pyo.plot(figure)