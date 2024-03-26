from graph import Graph, Edge
from prim import prim
from dijkstra import dijkstra
import unittest


class TestGraph(unittest.TestCase):
    def test_init(self):
        graph = Graph()
        self.assertIsInstance(graph, Graph)

    def test_adding(self):
        vertexes: list[Edge[str]] = [
                Edge("A", "B", 8),
                Edge("A", "C", 5),
                Edge("B", "D", 1),
                Edge("B", "E", 13),
                Edge("C", "F", 14),
                Edge("C", "D", 10),
                Edge("F", "D", 9),
                Edge("F", "E", 6),
                Edge("D", "E", 8),
            ]
        graph: Graph[str] = Graph[str]()
        for it in vertexes:
            graph.add_edge(it.start_edge, it.finish_edge, it.weight)
        self.assertEqual(graph.amount_edges(), 9)
        self.assertEqual(graph.amount_vertexes(), 6)

    def test_dijkstra(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B", 8),
            Edge("A", "C", 5),
            Edge("B", "D", 1),
            Edge("B", "E", 13),
            Edge("C", "F", 14),
            Edge("C", "D", 10),
            Edge("F", "D", 9),
            Edge("F", "E", 6),
            Edge("D", "E", 8),
        ]

        graph: Graph[str] = Graph[str]()
        for it in vertexes:
            graph.add_edge(it.start_edge, it.finish_edge, it.weight)

        path, cost = dijkstra(graph, "E", "A")

        self.assertEqual(path, ['E', 'D', 'B', 'A'])
        self.assertEqual(cost, 17)

    def test_prim(self):
        vertexes: list[Edge[str]] = [
            Edge("A", "B", 13),
            Edge("A", "C", 6),
            Edge("A", "F", 4),
            Edge("B", "C", 7),
            Edge("B", "F", 7),
            Edge("B", "E", 5),
            Edge("C", "E", 1),
            Edge("C", "F", 8),
            Edge("E", "F", 9),
        ]

        graph: Graph[str] = Graph[str]()

        for it in vertexes:
            graph.add_edge(it.start_edge, it.finish_edge, it.weight)

        ostov: Graph[str] = prim(graph, "C")

        self.assertEqual(graph.amount_vertexes(), ostov.amount_vertexes())
        self.assertEqual(ostov.amount_edges(), 4)
