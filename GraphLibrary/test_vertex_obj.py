"""
Date: 10/08/2019
Class: CS5310
Assignment: Graph library
Author(s): Zhongqiu Gao
Test script for VertexObj.
"""

from src.VertexObj import VertexObj

vertex_obj = VertexObj()


def test_instantiate():
    assert isinstance(vertex_obj, VertexObj)
