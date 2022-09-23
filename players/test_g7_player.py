"""unittest for g7_player."""
import unittest
import g7_player
from g7_player import Player
from shapely.geometry import Point, Polygon as ShapelyPolygon
from sympy.geometry import Point2D, Polygon
import numpy as np


class TestG7Player(unittest.TestCase):
    """Class for testing g7 code."""
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    '''
    def test_hello_world(self):
        """test_hello_world."""
        my_string = g7_player.hello_world()
        self.assertEqual(my_string, 'hello function')
    '''

    def test_reachable(self) -> None:
        current = Point2D(0, 0, evaluate=False)
        target = Point2D(0, 300, evaluate=False)
        player = Player(skill=50,
                        rng= np.random.Generator,
                        logger=None,
                        golf_map='',
                        start=current,
                        target=target,
                        sand_traps=[],
                        map_path='',
                        precomp_dir='')
        assert not player.reachable(current, target, 0.75)
