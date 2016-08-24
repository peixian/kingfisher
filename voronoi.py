import numpy as np
from networkx import *
from scipy.spatial import Voronoi


class Voronoi(object):
    """
    Uses scipy.spatil to construct a Voronoi diagram according to specifications.

    Implements Fortune's Algorithm (https://en.wikipedia.org/wiki/Fortune%27s_algorithm) in python.
    1. Takes in a 2D numpy array (or generates points with given boundaries)
    2. Creates a tuple of two graphs (with networkx) representing the Delaunay triangulation (https://en.wikipedia.org/wiki/Delaunay_triangulation)
    3. Relaxes the points through Lloyd's Algorithm (https://en.wikipedia.org/wiki/Lloyd%27s_algorithm)
    4. Returns a Voronoi diagram (http://www.voronoi.com/wiki/index.php?title=Main_Page)
    """

    def __init__(self, points = np.array([]), dimensions = (None, None), granularity = None):
        """
        Creates the Voronoi object

        :param points: predefined points
        :type points: numpy array of shape (w, 2) where w is the number of points [x, y] style, default None
        :param dimensions: dimensions of the points, from [w, 2] where w is the highest value, this *cannot* be None if points is None
        :type dimensions: tuple of ints, maximum (x,y) dimensions, default None
        :param granularity: how many points to create, must be given if dimensions are given
        :type granularity: int, default None
        """
        if len(points) == 0 and dimensions == (None, None):
            print('You can\'t have both points and dimensions be empty, try passing in some points or dimensions and granularity.')
            return
        if len(points) == 0 and dimensions != None and granularity == None:
            print('Granularity can\'t be none if dimensions are passed in, try passing in a granularity.')
            return
        if len(points) != 0:
            self.points = points
        else:
            points = np.random.random((granularity, 2))
            for i in range(len(dimensions)):
                points[i] = points[i]*dimensions[i]
            self.points = points

    def _eu_distance(self, p1, p2):
        """
        Calculates the Euclidian distance between two points

        :param p1: (x,y) position for the first point
        :type p1: tuple (or list) of floats
        :param p2: (x,y) position for the second point
        :type p2: tuple (or list) of floats

        :return: the euclidian distance
        :rtype: float
        """
        return np.sqrt(np.power(p1[0]-p2[0], 2) + np.power(p1[1]-p2[1], 2))

    def generate_voronoi(self):
        """
        Uses scipy.spatial.Voronoi to generate a Voronoi diagram

        :return: voronoi graph
        :rtype: scipy.spatial.Voronoi object
        """
        return 0

    def relax_points(self):
        """
        Relaxes the points after an initial Voronoi is created to refine the graph.
        """
        pass




