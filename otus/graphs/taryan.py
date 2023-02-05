from collections import defaultdict


class OrGraphNode:
    def __init__(self):
        self.incoming = []
        self.outgoing = []


class OrGraph:
    def __init__(self):
        self.graph = defaultdict(OrGraphNode)
        self.root = self.graph[0]
        self.res = []

    def add_edge(self, from_vertex: int, to_vertex: int, direction: str) -> None:
        """
        Добавление ребра в граф
        """
        another_direction = "incoming" if direction == "outgoing" else "outgoing"
        getattr(self.graph[from_vertex], direction).append(to_vertex)
        getattr(self.graph[to_vertex], another_direction).append(from_vertex)

    def taryan_sorting(self) -> None:
        while len(self.graph) != len(self.res):
            self.sort()

    def sort(self, key=None) -> None:
        """
        Топологическая сортировка Тарьяна
        """
        from random import choice

        if key:
            item = self.graph[key]
        else:
            key, item = choice(list(self.graph.items()))

        if item.outgoing:
            for vertex in item.outgoing:
                self.demukron_sorting(vertex)

        if key not in self.res:
            self.res.append(key)
        return
