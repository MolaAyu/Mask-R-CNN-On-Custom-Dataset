import math
from IPython.display import Image, display
from shapely.geometry import Polygon, Point, LineString

def create_checker(point, angle, length):
    coordinates = point.coords[0]
    # unpack the first point
    x, y = coordinates
    # find the end point
    endy = y + length * math.cos(math.radians(angle))
    endx = x + length * math.sin(math.radians(angle))
    line = LineString([Point(x,y),Point(endx,endy)])
    return line

def find_building(gdf,checker):
    buildings_geometry = gdf.geometry
    for i in range(len(buildings_geometry)):
        building = buildings_geometry[i]
        if checker.intersects(building):
            building_id = gdf.iloc[i,1]
            return building_id