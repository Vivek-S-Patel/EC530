# This program using the library haversine, which may need to be downloaded to run
# pip install haversine

from haversine import haversine

# Array 1
arr1 = [
        (0, 10),
        (20, -50),
        (5, 80),
        (2, 7),
      ]

# Array 2
arr2 = [
        (3, -9),
        (40, 50),
        (27, -80),
        (5, 30),
      ]

# calculate distance for all points using haversine formula
# all distances will go into array distances
distances = []
for loc in arr1:
  for i in range(len(arr2)):
    distances.append(haversine(loc , arr2[i]))

# this functions will go through the array distances by the number
# of elements in each array at a time, this way it can find the
# smallest distance for each point
def findClosetPoints(distances):
    closetPoints = []
    for i in range(0, len(distances), len(arr1)):
        SetofDistances = distances[i : i + len(arr1)]
        closetPoints.append(SetofDistances.index(min(SetofDistances)))
    return closetPoints

# call function
closetPair = findClosetPoints(distances)

# print statements for results
for i in range(len(arr1)):
  print("Element " + str(i) + " in array 1 is closet to element " + str(closetPair[i]) + " in array 2")

# Test just in case
print(findClosetPoints(distances))
