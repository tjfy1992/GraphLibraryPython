"""
Date: 10/08/2019
Test script for Vertex. Only some simple test.
The combined tests for vertices and edges are in test_edge.py
"""

from src.Vertex import Vertex

vertex = Vertex()
vertex2 = Vertex('s')


def test_instantiate():
    assert isinstance(vertex, Vertex)
    assert isinstance(vertex2, Vertex)


def test_label():
    assert vertex.label is None
    assert vertex2.label == 's'
