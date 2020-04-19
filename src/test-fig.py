import plotly.express as px
import plotly.plotly as py



fig =px.scatter(x=range(10), y=range(10))
fig.write_html("file.html")