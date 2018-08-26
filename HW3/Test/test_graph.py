import unittest
# import numpy.testing as npt
from Graph import HW3 as hw


class TestGraph(unittest.TestCase):

    def testShortPath1(self):
        filename="shortpath1.txt"
        result=hw.find_shortest_path(filename, 1.,3.)
        correct=(7.,[1.,2.,5.,6.,3.])
        assert result == correct
       
    def testNegCicle1(self):
        filename="negcicle1.txt"
        result=hw.find_negative_cicles(filename)
        correct = [[1.,2.,3.,4.,1.],[2.,3.,4.,1.,2.],
                   [3.,4.,1.,2.,3.],[4.,1.,2.,3.,4.]]
        assert result in correct
