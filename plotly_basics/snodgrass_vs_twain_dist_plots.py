import plotly.offline as pyo
import plotly.figure_factory as ff

snodgrass = [.209, .205, .196, .210, .202, .207, .224, .223, .220, .201]
twain = [.225, .262, .217, .240, .230, .229, .235, .217]

hist_data = [snodgrass, twain]
group_labels = ['snodgrass', 'twain']

figure = ff.create_distplot(hist_data, group_labels, bin_size=[0.0005, 0.0005])

pyo.plot(figure)

