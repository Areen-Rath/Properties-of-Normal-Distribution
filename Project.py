import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('StudentsPerformance.csv')
scores = df["math score"].tolist()

mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)
std = statistics.stdev(scores)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std}")

std1_start, std1_end = mean - std, mean + std
std2_start, std2_end = mean - std*2, mean + std*2
std3_start, std3_end = mean - std*3, mean + std*3

std1_list = [score for score in scores if score > std1_start and score < std1_end]
std2_list = [score for score in scores if score > std2_start and score < std2_end]
std3_list = [score for score in scores if score > std3_start and score < std3_end]

fig = ff.create_distplot([scores], ["Score"], show_hist = False)
fig.add_trace(go.Scatter(
    x = [mean, mean],
    y = [0, 0.17],
    mode = "lines",
    name = "Mean"
))
fig.add_trace(go.Scatter(
    x = [std1_start, std1_start],
    y = [0, 0.17],
    mode = "lines",
    name = "1st Starting Standard Deviation"
))
fig.add_trace(go.Scatter(
    x = [std1_end, std1_end],
    y = [0, 0.17],
    mode = "lines",
    name = "1st Ending Standard Deviation"
))
fig.add_trace(go.Scatter(
    x = [std2_start, std2_start],
    y = [0, 0.17],
    mode = "lines",
    name = "2nd Starting Standard Deviation"
))
fig.add_trace(go.Scatter(
    x = [std2_end, std2_end],
    y = [0, 0.17],
    mode = "lines",
    name = "2nd Ending Standard Deviation"
))
fig.add_trace(go.Scatter(
    x = [std3_start, std3_start],
    y = [0, 0.17],
    mode = "lines",
    name = "3rd Starting Standard Deviation"
))
fig.add_trace(go.Scatter(
    x = [std3_end, std3_end],
    y = [0, 0.17],
    mode = "lines",
    name = "3rd Ending Standard Deviation"
))
fig.show()