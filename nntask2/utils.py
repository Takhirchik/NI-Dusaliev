class Vertex:
    def __init__(self, name : str):
        self.name = name
        self.arc_to = 0
        self.arc_from = 0

    def __str__(self):
        return f'Vertex({self.name})'

    def __repr__(self):
        return f'Vertex({self.name})'

class OrderError(Exception):
    pass

class Arc:
    def __init__(self, vertex1 : Vertex, vertex2 : Vertex, order : int):
        self.arc_from = vertex1
        self.arc_to = vertex2
        self.order = order
        self.arc_from.arc_from += 1
        self.arc_to.arc_to += 1
        if self.order != self.arc_to.arc_to:
            raise OrderError(f'OrderError: Порядок дуги ({self.arc_from.name}, {self.arc_to.name}, {self.order}) указан неверно')

    def __str__(self):
        return f'Arc(from: {self.arc_from}, to: {self.arc_to})'

    def __repr__(self):
        return f'Arc(from: {self.arc_from}, to: {self.arc_to})'

    def _get_vertexes(self):
        return self.arc_from, self.arc_to

    def __getitem__(self, value : Vertex):
        if value == self.arc_from:
            return self.arc_to


class QuadMatrixError(Exception):
    pass

class QuadMatrix:
    def __init__(self, args : list):
        if len(args) != len(args[0]):
            raise QuadMatrixError('QuadMatrixError: На вход попал список из которого невозмоно создать квадратную матрицу')
        self.args = args

    def __len__(self):
        return len(self.args)

    def __getitem__(self, index : int):
        return self.args[index]

    def __setitem__(self, index : int, value):
        self.args[index] = value

    def __str__(self):
        return '\n'.join(map(lambda x: ' '.join(map(lambda y: str(y), x)), self.args))

    def __repr__(self):
        return f'Matrix({self.args})'

    def transpose(self):
        self.args = [list(row) for row in zip(*self.args)]
        return self

class GraphHasNotVertex(Exception):
    pass

class Graph:
    def __init__(self, vertexes : list = None, arcs : list = None):
        if vertexes is not None:
            self.vertexes = set(self.from_list(vertexes, Vertex))
        else:
            self.vertexes = set()
        if arcs is not None:
            self.arcs = self.from_list(arcs, Arc)
        else:
            self.arcs = list()

    def from_list(self, li : list, obj):
        if all(map(lambda x: isinstance(x, obj), li)):
            return li

    def has_vertex(self, other : str):
        if other in map(lambda x: x.name, self.vertexes):
            return True
        return False

    def get_vertex(self, other : str):
        if self.has_vertex(other):
            for vertex in self.vertexes:
                if vertex.name == other:
                    return vertex

    def add_vertex(self, other):
        if isinstance(other, Vertex):
            self.vertexes.add(other)
        else:
            raise ValueError('ValueError: На вход попал объект отличный от Vertex')

    def pop_vertex(self, other):
        if isinstance(other, Vertex):
            self.vertexes.discard(other)
            remove_arc_indexes = []
            for index, arc in enumerate(self.arcs):
                vertex1, vertex2 = arc._get_vertexes()
                if vertex1 == other or vertex2 == other:
                    remove_arc_indexes.append(index)
            map(lambda x: self.arcs.pop(x), remove_arc_indexes)
        else:
            raise ValueError('ValueError: На вход попал объект отличный от Vertex')

    def add_arc(self, other):
        if isinstance(other, Arc):
            vertex1, vertex2 = other._get_vertexes()
            if vertex1 not in self.vertexes and vertex2 not in self.vertexes:
                raise GraphHasNotVertex(f'GraphHasNotVertex: Вершины {vertex1} или {vertex2} нет в Graph')
            self.arcs.append(other)
        else:
            raise ValueError('ValueError: На вход попал не объект Arc')

    def pop_arc(self, index : int = -1):
        self.arcs.pop(index)

    def __str__(self):
        dct = {'vertexes' : sorted(self.vertexes, key=lambda x: x.name),
               'arcs' : self.arcs}
        return f'Graph({dct})'

    def __repr__(self):
        dct = {'vertexes' : sorted(self.vertexes, key=lambda x: x.name),
               'arcs' : self.arcs}
        return f'Graph({dct})'

    def get_matrix_adjency(self):
        n = len(self.vertexes)
        self.adj = QuadMatrix([[0 for _ in range(n)] for _ in range(n)])
        dct = dict(map(lambda x: (x[1], x[0]), enumerate(sorted(self.vertexes, key=lambda x: x.name))))

        for arc in self.arcs:
            self.adj[dct[arc.arc_from]][dct[arc.arc_to]] += 1
        return self

    def cycles(self):
        def dfs(vertex : Vertex, visited : set, stack : set):
            visited.add(vertex)
            stack.add(vertex)
            for arc in self.arcs:
                if arc.arc_from == vertex and arc.arc_to not in visited:
                    if dfs(arc.arc_to, visited, stack):
                        return True
                elif arc.arc_from == vertex and arc.arc_to in stack:
                    return True
            stack.remove(vertex)
            return False

        visited = set()
        for vertex in self.vertexes:
            if vertex not in visited:
                if dfs(vertex, visited, set()):
                    return True
        return False
