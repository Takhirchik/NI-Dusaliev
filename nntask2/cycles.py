import xml.etree.ElementTree as ET
from utils import Graph, Arc, Vertex
import os.path

class FileExtensionError(Exception):
    pass


def unpack(input_file):
    _, extension = os.path.splitext(input_file)
    if extension != '.xml':
        raise FileExtensionError(f'FileExtensionError: Входящий файл должен быть формата XML-документа')
    try:
        with open(input_file, 'r') as f:
            xml_data = f.read()
    except:
        raise FileNotFoundError(f"FileNotFoundError: Файл {input_file} не был найден")
    tree = ET.fromstring(xml_data)
    graph = Graph()
    for vertex in tree.findall('vertex'):
        graph.add_vertex(Vertex(vertex.text))

    for arc in sorted(tree.findall('arc'), key = lambda x: int(x.findall('order')[0].text)):
        from_vertex = graph.get_vertex(arc.findall('from')[0].text)
        to_vertex = graph.get_vertex(arc.findall('to')[0].text)
        order = int(arc.findall('order')[0].text)
        graph.add_arc(Arc(from_vertex, to_vertex, order))
    return graph

class HasCyclesError(Exception):
    pass

class RootVertexNotFoundError(Exception):
    pass

def prefix_function(input_file, output_file):
    graph = unpack(input_file)
    has_cycles = graph.cycles()
    if has_cycles:
        raise HasCyclesError(f'HasCyclesError: В графе присутствуют циклы')

    root_vertex = None
    for vertex in graph.vertexes:
        if vertex.arc_to == 0:
            root_vertex = vertex

    if root_vertex is None:
        raise RootVertexNotFoundError(f'RootVertexNotFoundError: В графе отсутствуют вершины без входящих в них дуг')

    prefix_notation = build_prefix_notation(graph, root_vertex)
    if os.path.exists(output_file):
        raise FileExistsError(f"FileExistsError: Файл {output_file} уже существует")
    with open(output_file, 'w') as f:
        f.write(strfprefix(prefix_notation))

def build_prefix_notation(graph : Graph, root_vertex : Vertex):
    result = {root_vertex : {}}
    for arc in graph.arcs:
        if arc.arc_from == root_vertex:
            result[root_vertex].update(build_prefix_notation(graph, arc.arc_to))
    return result

def strfprefix(prefix_notation : dict):
    result = []
    for key, value in prefix_notation.items():
        result.append(key.name)
        if value == {}:
            continue
        result[-1] += f'({strfprefix(value)})'
    return ', '.join(result)
