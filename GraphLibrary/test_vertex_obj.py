"""
Date: 10/08/2019
Test script for VertexObj.
"""

from src.VertexObj import VertexObj

vertex_obj = VertexObj()


def test_instantiate():
    assert isinstance(vertex_obj, VertexObj)
