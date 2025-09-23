import plotly.express as px
import pandas as pd

# Sample data
data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [2, 4, 1, 5, 3],
        'category': ['A', 'B', 'A', 'C', 'B']}
df = pd.DataFrame(data)

# Create a scatter plot
fig = px.scatter(df, x="x_values", y="y_values", color="category",
                 title="Interactive Scatter Plot with Plotly Express")
fig.show()