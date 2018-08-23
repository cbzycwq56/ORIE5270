import unittest
# import numpy.testing as npt
from Tree import PrintTree as pt


class TestSum(unittest.TestCase):
    # first case single node
    def testTree1(self):
        a = pt.Node("a", None, None)
        tree = pt.Tree(a)
        tested_list = tree.get_tree()
        correct_list = [["a"]]
        assert tested_list == correct_list

    # second case fill leaves
    def testTree2(self):
        a = pt.Node("a", None, None)
        b = pt.Node("b", None, None)
        c = pt.Node("c", None, None)
        d = pt.Node("d", None, None)
        e = pt.Node("e", None, None)
        f = pt.Node("f", None, None)
        g = pt.Node("g", None, None)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = f
        c.right = g
        tree = pt.Tree(a)
        tested_list = tree.get_tree()
        correct_list = [["|", "|", "|", "a", "|", "|", "|"],
                        ["|", "b", "|", "|", "|", "c", "|"],
                        ["d", "|", "e", "|", "f", "|", "g"]]
        assert tested_list == correct_list

    # third testcase all left node
    def testTree3(self):
        a = pt.Node("a", None, None)
        b = pt.Node("b", None, None)
        c = pt.Node("c", None, None)
        d = pt.Node("d", None, None)
        a.left = b
        b.left = c
        c.left = d
        tree = pt.Tree(a)
        tested_list = tree.get_tree()
        correct_list = [["|", "|", "|", "|", "|", "|", "|", "a", "|", "|", "|", "|", "|", "|", "|"],
                        ["|", "|", "|", "b", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
                        ["|", "c", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
                        ["d", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]]
        assert tested_list == correct_list

    # fourth testcase general tree
    def testTree4(self):
        a = pt.Node("a", None, None)
        b = pt.Node("b", None, None)
        c = pt.Node("c", None, None)
        d = pt.Node("d", None, None)
        e = pt.Node("e", None, None)
        f = pt.Node("f", None, None)
        a.left = b
        a.right = c
        b.right = d
        c.left = e
        e.right = f
        tree = pt.Tree(a)
        tested_list = tree.get_tree()
        correct_list = [["|", "|", "|", "|", "|", "|", "|", "a", "|", "|", "|", "|", "|", "|", "|"],
                        ["|", "|", "|", "b", "|", "|", "|", "|", "|", "|", "|", "c", "|", "|", "|"],
                        ["|", "|", "|", "|", "|", "d", "|", "|", "|", "e", "|", "|", "|", "|", "|"],
                        ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "f", "|", "|", "|", "|"]]
        assert tested_list == correct_list
