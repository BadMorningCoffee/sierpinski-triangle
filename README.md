# sierpinski-triangle

Based on the Chaos game used to create a sierpinski triangle and related geometries
- Create a center point and n control points
- Every interation create a point between the center point and all control points by linear interpolation with a constant t-vaule
- All new points created are new center points
- repeat

When n=3 the limit as the recurrsive calls approach infinity match the sierpinski triangle