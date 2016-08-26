from unittest2 import TestCase

from atlas import Atlas
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import voronoi_plot_2d

class AtlasTests(TestCase):
    """Tests the Voronoi generation"""
    def setUp(self):
        self.client = Atlas(dimensions = (2,2), granularity = 2)

    def test_init(self):
        points = np.random.random((10, 2))
        self.client = Atlas(points=points)
        self.assertEqual(len(points), len(self.client.points))

        self.client = Atlas(dimensions=(30, 30), granularity = 20)
        self.assertTrue(len(self.client.points) == 20)
        self.assertTrue(max(self.client.points[0]) <= 30)

    def test_eu_distance(self):
        """Tests euclidian distance function"""
        points = np.array([[0,0],[2,1.5]])
        self.client = Atlas(points = points)
        self.assertEqual(self.client._eu_distance(points[0], points[1]), 2.5)

    def test_generate_voronoi(self):
        """Tests for the generation of the voronoi diagram, commment out the plot to see the diagram"""
        self.client = Atlas(dimensions = (300, 300), granularity = 300)
        self.client.generate_voronoi()
        self.assertEqual(len(self.client.vor.points), len(self.client.points))
        #voronoi_plot_2d(self.client.vor)
        #plt.show()

    def test_relax_points(self):
        """Tests the generation of the relaxation points of the Voronoi diagram"""
        pass

    def test_continent_generation(self):
        """Tests generation of land and sea"""
        pass

    def test_terrain_generation(self):
        """Tests the generation of varius biomes"""
        pass
