import pandas as pd
import plotly.express as px

df = pd.read_csv('2018-09-19-03_57_11_VN100.csv')

fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
fig.show()