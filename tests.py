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
