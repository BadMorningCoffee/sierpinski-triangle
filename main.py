import plotly.express as px
import pandas as pd
import math

#Produces a list of all the x or y values from a list of points
def getPointsComponent(listOfPoints, pos):
    return list(map (lambda point: point[pos], listOfPoints))

#Produces a list of str repeated for every element in the specific list
def createCategoryList(listOfPoints, str):
    return list(map (lambda a : str, listOfPoints))

#Produces a value that smoothly transitions from p0 to p1 as the interpolation factor t goes from 0 to 1
def lerp(t, p0, p1):
    return ((1-t)*p0 + t*p1)

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


controlPoints = [(-2, 0), (2, 0), (0, 4 * math.sin(math.pi/3))] #Set of points that all startingPoints will be pulled towards
startingPoints = [(0, (4 / math.sqrt(3)) * math.sin(math.pi/6))] #Set of points that will be pulled towards the control points
t = 1/2 #Sets the t value for the lerping between the controlPoints and startingPoints
updateStartingPoints(8) #Sets the number of iterations where startPoints are pulled towards controlPoints


data = {'x_values': getPointsComponent(controlPoints, 0) + getPointsComponent(startingPoints, 0), #Creates a list of all the X positions of the points to be plotted
        'y_values': getPointsComponent(controlPoints, 1) + getPointsComponent(startingPoints, 1), #Creates a list of all the Y positions of tthe points to be plotted
        'category': createCategoryList(controlPoints, "Control Point") + createCategoryList(startingPoints, "Starting Point")} #Creates a list that mataches each point to a specific category
df = pd.DataFrame(data)

# Create a scatter plot
fig = px.scatter(df, x="x_values", y="y_values", color="category",
                 title="Interactive Scatter Plot with Plotly Express")
fig.show()