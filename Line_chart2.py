import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Data/population.csv')


data = [go.Scatter(x=df.columns,
                   y=df.loc[name],
                   mode='lines',
                   name=name) for name in df.index]

pyo.plot(data)

