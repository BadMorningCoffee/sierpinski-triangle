import plotly.express as px
import pandas as pd

#Produces a value that smoothly transitions from p0 to p1 as the interpolation factor t goes from 0 to 1
def lerp(t, p0, p1):
    return ((1-t)*p0 + t*p1)

#Produces a list of all the x or y values from a list of points
def getPointsComponent(listOfPoints, pos):
    return list(map (lambda point: point[pos], listOfPoints))

#Produces a new point that has been lerped bewteen p0 and p1 with factor t
def createNewPoint(p0, p1):
    x = lerp(t, p0[0], p1[0])
    y = lerp(t, p0[1], p1[1])
    return (x, y)

#Produces a list of points created by lerping a point to all controlPoints with factor t
def createNewPoints(point):
    newPoints = []
    for controlPoint in controlPoints:
        newPoints.append(createNewPoint(point, controlPoint))
    return newPoints

#Produces a list of points created by lerping all startingPoints to all controlPoints with factor t
def createNewStartingPoints():
    newPoints = []
    for startingPoint in startingPoints:
        newPoints = newPoints + createNewPoints(startingPoint)
    return newPoints

#Updates startingPoints by calling createNewStartPoints n times
def updateStartingPoints(n):
    global startingPoints
    for i in range(n):
        startingPoints = createNewStartingPoints()

controlPoints = [(-1, 0), (1, 0), (0, 2)]
startingPoints = [(0, 0)]
t = 1/2


"""data = {'x_values': getPointsComponent(controlPoints, 0), #Creates a list of all the X positions of the controlPoints
        'y_values': getPointsComponent(controlPoints, 1), #Creates a list of all the Y positions of the controlPoints
        'category': list(map (lambda a : "Control Point", controlPoints))} #Creates a list containing only "Control Point" for every element in control Points
df = pd.DataFrame(data)

# Create a scatter plot
fig = px.scatter(df, x="x_values", y="y_values", color="category",
                 title="Interactive Scatter Plot with Plotly Express")
fig.show()"""