Date: 10/08/2019
Class: CS5310
Assignment: Graph library
Author(s): Zhongqiu Gao

The source code file are in /src and the test scripts are in the root directory.
Vertex.py: The class of vertex. Each vertex has an optional label and a vertex object which is set to None by default. A vertex
also has an array to store directed edges and an array for undirected edges.

VertexObj.py: The class of vertexObj. A vertexObj is an object which can be stored within a vertex. This class can be modified in
the future if the object to be stored has other attributes.

Edge.py: The class of edge. Each edge has an optional label, a float weight, and an edgeObj, which, similar to vertexObj, is set
to None by default. This class is a parent class of DirectedEdge and UndirectedEdge.

EdgeObj.py: The class of edgeObj. It is the object which can be stored within an edge.

DirectedEdge.py: The class of directed edge. It extends class Edge, and in addition to the optional label, the float weight and
the edgeObj, it has a from_vertex and a to_vertex. The from_vertex is the reference to the edge's origin vertex, and the to_vertex
is a reference to the edge's destination vertex.

UndirectedEdge.py: The class of undirected edge. It also extend class Edge, and it has two more attributes: vertex1 and vertex2,
which are the references to the two end point vertices of the edge.

Graph.py: The class of graph. It implements all of the functions listed in the assignment requirements. The constructor of this
class has one argument, which represents whether this graph is directed. In a directed graph, no undirected edges can be added into
it, and vice versa for undirected graph and directed edges. The assertion in the corresponding functions will not pass if this
situation happens.

test_vertex.py: The test script for class vertex. It contains basic tests of vertex.

test_edge.py: The test script for class edge. It contains test functions on edge itself and combined tests on vertices and edges.
For example, it tests the function of generating an edge between two vertices; and tests the function of adding an edge into a
vertex's edge array. The test also includes removing an edge from the vertex's edge array.

test_edge_obj.py: A test script for edgeObj.

test_vertex_obj.py: A test script for vertexObj.

test_graph.py: It tests every function listed in the assignment requirement. There is a comment line on the top of each test
function showing which function of the graph it is testing.

GraphScript.py: This is a script which builds a directed graph and an undirected graph, and shows how the graph works. There are
a lot of code blocks in the file, and on the top of each of them, there is a comment line demonstrating the method's functionality.
This file is the demonstration of the graph library code: some of the functions are tested in the undirected graph and other functions
are tested in the directed graph. The whole file includes all the functions in the graph class.

The above programs are written within PyCharm for Windows, with Python's version 3.7.4 x64, and pytest-5.1.2.
To run the programs, in PyCharm,
click File ->  open -> select the project named GraphLibrary;
At the terminal, get into the current directory, and run "pytest".
To run the graph script above, please right-click on GraphScript.py and select "Run GraphScript", and the output will be printed in
the terminal.

References:
1. Default parameter values of functions in Python
   https://www.geeksforgeeks.org/default-arguments-in-python/
2. Python inheritance
   https://www.w3schools.com/python/python_inheritance.asp
3. Python sets
   https://www.w3schools.com/python/python_sets.asp