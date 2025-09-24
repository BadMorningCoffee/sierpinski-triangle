import plotly.express as px
import pandas as pd

def lerp(t, p0, p1):
    return ((1-t)*p0 + t*p1)


controlPoints = [(-1, 0), (1, 0), (0, 2)]
startingPoints = [(0, 0)]
t = 1/2


data = {'x_values': list (map (lambda point: point[0], controlPoints)), #Creates a list of all the X positions of the controlPoints
        'y_values': list (map (lambda point: point[1], controlPoints)), #Creates a list of all the Y positions of the controlPoints
        'category': list(map(lambda a : "Control Point", controlPoints))} #Creates a list containing only "Control Point" for every element in control Points
df = pd.DataFrame(data)

# Create a scatter plot
fig = px.scatter(df, x="x_values", y="y_values", color="category",
                 title="Interactive Scatter Plot with Plotly Express")
fig.show()