from unittest2 import TestCase

from voronoi import Voronoi

class VoronoiTests(TestCase):
    """Tests the Voronoi generation"""
    def setUp(self):
        self.client = Voronoi()

