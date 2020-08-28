"""
Date: 10/08/2019
Class: CS5310
Assignment: Graph library
Author(s): Zhongqiu Gao
Test script for EdgeObj.
"""

from src.EdgeObj import EdgeObj

edge_obj = EdgeObj()


def test_instantiate():
    assert isinstance(edge_obj, EdgeObj)
