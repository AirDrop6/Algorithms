from graph import Graph, Edge
from prim import prim
from dijkstra import dijkstra
import time

ITERATIONS = 100_000


class GraphBenchmark:
    @staticmethod
    def run():
        GraphBenchmark.dijkstra_bench()
        GraphBenchmark.prim_bench()

    @staticmethod
    def dijkstra_bench():
        print("Dijkstra:")
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

        start = time.time()

        for i in range(ITERATIONS):
            answer, cost = dijkstra(graph, "A", "E")

        end = time.time()

        print(f"Path: {answer} with cost: {cost}")
        print(f'Time spent on {ITERATIONS} iterations: {end - start} sec \n')

    @staticmethod
    def prim_bench():
        print("Prim:")
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

        start = time.time()

        for i in range(ITERATIONS):
            ostov: Graph[str] = prim(graph, "C")

        end = time.time()

        print("---------Vertexes-----------")
        ostov.print_all_vertexes()
        print("---------Edges-----------")
        ostov.print_all_edges()
        print(f'Time spent on {ITERATIONS} iterations: {end - start} sec \n')


if __name__ == "__main__":
    GraphBenchmark.run()
