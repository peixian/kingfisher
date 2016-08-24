from unittest2 import TestCase

from voronoi import Voronoi

import numpy as np

class VoronoiTests(TestCase):
    """Tests the Voronoi generation"""
    def setUp(self):
        self.client = Voronoi(dimensions = (2,2), granularity = 2)

    def test_init(self):
        points = np.random.random((2, 10))
        self.client = Voronoi(points=points)
        self.assertEqual(len(points), len(self.client.points))

        self.client = Voronoi(dimensions=(30, 30), granularity = 20)
        self.assertTrue(len(self.client.points[0]) == 20)
        self.assertTrue(max(self.client.points[0]) <= 30)

    def test_eu_distance(self):
        points = np.array([[0,0],[2,1.5]])
        self.client = Voronoi(points = points)
        self.assertEqual(self.client._eu_distance(points[0], points[1]), 2.5)

    def test_generate_voronoi():
        vor = self.client.generate_voronoi()
        self.assertEqual(len(vor.points), len(self.client.points))

    def test_relax_points():
        pass
