"""
Date: 10/08/2019
Class: CS5310
Assignment: Graph library
Author(s): Zhongqiu Gao
Test script for Edge, with some Vertex test involved.
"""

from src.Edge import Edge
from src.DirectedEdge import DirectedEdge
from src.UndirectedEdge import UndirectedEdge
from src.Vertex import Vertex

v1 = Vertex()
v2 = Vertex()

edge = Edge()
edge2 = DirectedEdge(v1, v2, 'AA 1206')
edge3 = UndirectedEdge(v1, v2, '849 miles')
edge4 = DirectedEdge(v2, v1, 'AA 1205', 849)


def test_instantiate():
    assert isinstance(edge, Edge)
    assert isinstance(edge2, DirectedEdge)
    assert isinstance(edge2, Edge)
    assert isinstance(edge3, UndirectedEdge)
    assert isinstance(edge3, Edge)
    assert isinstance(edge4, Edge)
    assert isinstance(edge4, DirectedEdge)


def test_label():
    assert edge.label is None
    assert edge2.label == 'AA 1206'
    assert edge3.label == '849 miles'
    assert edge4.label == 'AA 1205'
    assert edge4.weight == 849


def test_add_edge():
    v1.add_directed_edge(edge2)
    assert len(v1.directed_edges) == 1
    assert v1.directed_edges == [edge2]
    v2.add_undirected_edge(edge3)
    assert len(v2.undirected_edges) == 1
    assert v2.undirected_edges == [edge3]


def test_remove_edge():
    v1.remove_directed_edge(edge2)
    assert len(v1.directed_edges) == 0
    v2.remove_undirected_edge(edge3)
    assert len(v2.undirected_edges) == 0
