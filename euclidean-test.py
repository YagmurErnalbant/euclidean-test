import sys

def euclideanDistance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

points = [[float(input(f"Enter x for point {i+1}: ")), float(input(f"Enter y for point {i+1}: "))] for i in range(5)]

distances = [euclideanDistance(x1, y1, x2, y2)
             for i, (x1, y1) in enumerate(points)
             for j, (x2, y2) in enumerate(points) if i != j]

formatted_distances = [format(dist, ".2f") for dist in distances]

min_distance = min(float(dist) for dist in formatted_distances)

print("Points:", points)
print("Distances:", formatted_distances)
print(f"Minimum distance: {min_distance}")