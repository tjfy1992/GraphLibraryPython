"""
Date: 10/08/2019
Test script for Graph.
"""

from src.Graph import Graph
from src.Vertex import Vertex
from src.DirectedEdge import DirectedEdge
from src.UndirectedEdge import UndirectedEdge

vertex = Vertex()
vertex2 = Vertex()
vertex3 = Vertex('a')
vertex4 = Vertex('b')
vertex5 = Vertex('c')
graph = Graph(True)
graph2 = Graph(False)
graph3 = Graph(True)


def test_instantiate():
    assert isinstance(graph, Graph)
    assert isinstance(graph2, Graph)
    assert isinstance(graph3, Graph)


# test adding some vertices into the graph
def test_add_vertex():
    assert len(graph.vertices) == 0
    graph.insert_vertex(vertex)
    assert len(graph.vertices) == 1
    graph.insert_vertex(vertex2)
    assert len(graph.vertices) == 2
    graph2.insert_vertex(vertex3)
    graph2.insert_vertex(vertex4)
    graph2.insert_vertex(vertex5)
    assert len(graph2.vertices) == 3


# test of adding directed edges into the graph
def test_add_directed_edge():
    d_edge = DirectedEdge(vertex, vertex2)
    assert graph.is_directed_edge(d_edge)
    graph.insert_directed_edge(d_edge.get_from_vertex(), d_edge.get_to_vertex(), d_edge)
    assert len(graph.edges) == 1


# test of removing the above vertex and the edges incident to it
def test_remove_vertex_1():
    graph.remove_vertex(vertex)
    assert len(graph.edges) == 0
    assert len(graph.vertices) == 1
    assert graph.get_vertices() == [vertex2]


# test of adding undirected edges into a graph
def test_add_undirected_edge():
    u_edge = UndirectedEdge(vertex3, vertex4)
    assert not graph.is_directed_edge(u_edge)
    graph2.insert_undirected_edge(u_edge.get_vertex_1(), u_edge.get_vertex_2(), u_edge)
    assert len(graph2.edges) == 1
    u_edge = UndirectedEdge(vertex3, vertex5)
    graph2.insert_undirected_edge(u_edge.get_vertex_1(), u_edge.get_vertex_2(), u_edge)
    assert len(graph2.edges) == 2
    u_edge = UndirectedEdge(vertex4, vertex5)
    graph2.insert_undirected_edge(u_edge.get_vertex_1(), u_edge.get_vertex_2(), u_edge)
    assert len(graph2.edges) == 3


# test of removing some vertices and the edges incident to it in an undirected graph
def test_remove_vertex_2():
    graph2.remove_vertex(vertex3)
    assert len(graph2.edges) == 1
    assert len(graph2.vertices) == 2
    assert graph2.get_vertices() == [vertex4, vertex5]
    graph2.remove_vertex(vertex5)
    assert len(graph2.edges) == 0
    assert len(graph2.vertices) == 1
    assert graph2.get_vertices() == [vertex4]


# test of getting a vertex from the graph by its label
def test_get_some_vertex():
    assert graph2.get_vertex_by_label('b') == vertex4


q = Vertex('q')
w = Vertex('w')
e = Vertex('e')
graph3.insert_vertex(q)
graph3.insert_vertex(w)
graph3.insert_vertex(e)
d_edge1 = DirectedEdge(q, w)
d_edge2 = DirectedEdge(w, e)
d_edge3 = DirectedEdge(q, e)
graph3.insert_directed_edge(d_edge1.get_from_vertex(), d_edge1.get_to_vertex(), d_edge1)
graph3.insert_directed_edge(d_edge2.get_from_vertex(), d_edge2.get_to_vertex(), d_edge2)
graph3.insert_directed_edge(d_edge3.get_from_vertex(), d_edge3.get_to_vertex(), d_edge3)


# test the incoming edges of a vertex in a directed graph
def test_incoming_edges():
    assert graph3.is_directed_graph
    assert graph3.get_incoming_edges(e) == {d_edge2, d_edge3}
    assert graph3.get_incoming_edges(w) == {d_edge1}


# test the outgoing edges of a vertex in a directed graph
def test_outgoing_edges():
    assert graph3.is_directed_graph
    assert graph3.get_outgoing_edges(q) == {d_edge1, d_edge3}
    assert graph3.get_outgoing_edges(w) == {d_edge2}


# test the adjacent vertices of a vertex
def test_adjacent_vertices():
    assert graph3.get_adjacent_vertices(e) == {q, w}
    assert graph3.get_adjacent_vertices(w) == {q, e}
    assert graph3.get_adjacent_vertices(q) == {w, e}
    graph3.remove_directed_edge(d_edge1)
    assert graph3.get_adjacent_vertices(w) == {e}


# test the incident edges of a vertex
def test_incident_edges():
    assert graph3.get_incident_edges(e) == {d_edge2, d_edge3}
    assert graph3.get_incident_edges(w) == {d_edge2}
    assert graph3.get_incident_edges(q) == {d_edge3}


# test a vertex's adjacent vertices along with its incoming edges in a directed graph
def test_adjacent_vertices_and_incoming_edges():
    assert graph3.get_adjacent_vertices_and_incoming_edges(e) == ({q, w}, {d_edge2, d_edge3})
    assert graph3.get_adjacent_vertices_and_incoming_edges(w) == ({e}, set())


# test a vertex's adjacent vertices along with its outgoing edges in a directed graph
def test_adjacent_vertices_and_outgoing_edges():
    assert graph3.get_adjacent_vertices_and_outgoing_edges(w) == ({e}, {d_edge2})
    assert graph3.get_adjacent_vertices_and_outgoing_edges(q) == ({e}, {d_edge3})


# test the in_degree of a directed edge
def test_in_degree():
    assert graph3.get_in_degree(e) == 2


# test the degree of an edge
def test_degree():
    assert graph3.get_degree(e) == 2
    r = Vertex('r')
    graph3.insert_vertex(r)
    d_edge4 = DirectedEdge(e, r)
    graph3.insert_directed_edge(d_edge4.get_from_vertex(), d_edge4.get_to_vertex(), d_edge4)
    assert graph3.get_degree(e) == 3


# test the two end vertices of an edge
def test_get_two_ends_of_edge():
    assert graph3.get_end_vertices(d_edge2) == (w, e)
    assert graph3.get_end_vertices(d_edge3) == (q, e)


# test if two given vertices are adjacent
def test_adjacent():
    assert graph3.are_adjacent(w, e)
    assert not graph3.are_adjacent(w, q)


# test a vertex with undirected self loop.
def test_self_loop():
    graph4 = Graph(False)
    t = Vertex('t')
    graph4.insert_vertex(t)
    ud_edge = UndirectedEdge(t, t)
    graph4.insert_undirected_edge(ud_edge.get_vertex_1(), ud_edge.get_vertex_2(), ud_edge)
    assert graph4.get_degree(t) == 2


# test a vertex with directed self loop.
def test_self_loop2():
    graph5 = Graph(True)
    y = Vertex('y')
    graph5.insert_vertex(y)
    d_edge = DirectedEdge(y, y)
    graph5.insert_directed_edge(d_edge.get_from_vertex(), d_edge.get_to_vertex(), d_edge)
    assert graph5.get_in_degree(y) == 1
    assert graph5.get_out_degree(y) == 1
    assert graph5.get_degree(y) == 2
