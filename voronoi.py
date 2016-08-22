import numpy as np
from networkx import *
class Voronoi(object):
    """
    Implements Fortune's Algorithm (https://en.wikipedia.org/wiki/Fortune%27s_algorithm) in python.
    1. Takes in a 2D numpy array (or generates points with given boundaries)
    2. Creates a tuple of two graphs (with networkx) representing the Delaunay triangulation (https://en.wikipedia.org/wiki/Delaunay_triangulation)
    3. Relaxes the points through Lloyd's Algorithm (https://en.wikipedia.org/wiki/Lloyd%27s_algorithm)
    4. Returns a Voronoi diagram (http://www.voronoi.com/wiki/index.php?title=Main_Page)
    """

    def __init__(self, points = None, dimensions = (None, None), granularity = None):
        """
        Creates the Voronoi object

        :param points: predefined points
        :type points: numpy array of shape (2, w) where w is the number of points [x, y] style, default None
        :param dimensions: dimensions of the points, from [0, w] where w is the highest value, this *cannot* be None if points is None
        :type dimensions: tuple of ints, maximum (x,y) dimensions, default None
        :param granularity: how many points to create, must be given if dimensions are given
        :type granularity: int, default None
        """
        if points == None and dimensions == (None, None):
            print('You can\'t have both points and dimensions be empty, try passing in some points or dimensions and granularity.')
            return
        if dimensions != None and granularity == None:
            print('Granularity can\'t be none if dimensions are passed in, try passing in a granularity.')
            return
        if points:
            self.points = points
        else:
            points = np.random.random((2, granularity))
            for i in range(len(dimensions)):
                points[i] = points[i]*dimensions[i]
            self.points = points

    def _eu_distance(p1, p2):
        """
        Calculates the Euclidian distance between two points

        :param p1: (x,y) position for the first point
        :type p1: tuple (or list) of floats
        :param p2: (x,y) position for the second point
        :type p2: tuple (or list) of floats

        :return: the euclidian distance
        :rtype: float
        """
        pass

    def generate_voronoi():
        """
        Uses Fortune's Algorithm to create a voronoi diagram
        """
        pass

    def relax_points():
        """
        Relaxes the points after an initial Voronoi is created to refine the graph.
        """
        pass




