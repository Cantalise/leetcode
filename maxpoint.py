# Requirement:
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
 
class Solution:
    # @param points, a list of Points
    # @return an integer
    @staticmethod
    def getSlope(start, end):
        if start.x != end.x:
            slope = 1.0*(start.y-end.y)/(start.x-end.x)
            return slope

    def maxPoints(self, points):
        # create a slope map to store the slope (which is the key) and
        # the number of nodes( which is the value)
        if len(points) <= 2:
            return len(points)
            
        max_count = 0
        point_count = len(points)
        for i in range(0, point_count):
            slope_map = {}
            dup = 1
            start = points[i]
            for j in range(0, point_count):
                end = points[j]
                if start.x == end.x and start.y == end.y and i!=j:
                    dup += 1
                elif i!=j:
                    if start.x == end.x:
                        slope_map['h'] = slope_map.get('h', 0) + 1
                    elif start.y == end.y:
                        slope_map['v'] = slope_map.get('v', 0) + 1
                    else:
                        # regular slope
                        slope = self.getSlope(start, end)
                        slope_map[slope] = slope_map.get(slope, 0) + 1
                        
            if len(slope_map) > 0:
                max_count = max(max_count, max(slope_map.values())+ dup)
            else:
                max_count = max(max_count, dup)
                
        return max_count

