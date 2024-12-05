import xml.etree.ElementTree as ET
from utils import Graph, Arc, Vertex
import os.path
import re
from math import exp

class FileExtensionError(Exception):
    pass

_NUMBER_MATCH = re.compile(
    r"-?\b\d+\.?\d*|\.\d+\b"
)

_INT_MATCH = re.compile(
    r"-?\b\d+"
)

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

def summarize(*args):
    res = 0
    for ch in args:
        res += ch
    return res

def multiplie(*args):
    res = 1
    for ch in args:
        res *= ch
    return res

def my_exp(*args):
    res = []
    for ch in args:
        res.append(exp(ch))
    return res

def get_number(s):
    if _NUMBER_MATCH.match(s):
        if _INT_MATCH.match(s):
            return int(s)
        else:
            return float(s)

def get_operations(input_file, graph : Graph):
    try:
        with open(input_file, 'r') as f:
            operations_data = f.read()
    except:
        raise FileNotFoundError(f"FileNotFoundError: Файл {input_file} не был найден")
    match = map(lambda x: x, re.findall(r'(\b\w+\d+)\s*:\s*([+*]|exp|(-?\b\d+\.?\d*|\.\d+\b))', operations_data))
    if not match:
        raise ValueError(f'ValueError: В файле {input_file} не указаны или неверно заданы данные')
    operations_dct = {
        '+' : summarize,
        '*' : multiplie,
        'exp' : my_exp,
        'NUMBER' : get_number
    }
    for raw_data in match:
        vertex = raw_data[0]
        v = graph.get_vertex(vertex)
        if v is None:
            raise ValueError(f'ValueError: Вершины {vertex} не существует в графе')
        operation = raw_data[1]
        if operation in operations_dct.keys():
            v.init_operation((operation, operations_dct[operation]))
        else:
            v.init_value(operations_dct['NUMBER'](operation))
    return graph

class HasCyclesError(Exception):
    pass

class RootVertexNotFoundError(Exception):
    pass

def prefix_function(input_graph_file, input_oper_file, output_file):
    graph = unpack(input_graph_file)
    has_cycles = graph.cycles()
    if has_cycles:
        raise HasCyclesError(f'HasCyclesError: В графе присутствуют циклы')

    root_vertex = None
    for vertex in graph.vertexes:
        if vertex.arc_to == 0:
            root_vertex = vertex

    if root_vertex is None:
        raise RootVertexNotFoundError(f'RootVertexNotFoundError: В графе отсутствуют вершины без входящих в них дуг')

    graph = get_operations(input_oper_file, graph)

    prefix_notation = build_prefix_notation(graph, root_vertex)
    str_oper_prefix_notation = strfprefix(prefix_notation)
    result = calculate_prefix(prefix_notation, root_vertex)
    if os.path.exists(output_file):
        raise FileExistsError(f"FileExistsError: Файл {output_file} уже существует")
    with open(output_file, 'w') as f:
        f.write(str_oper_prefix_notation + ' = ' + str(result))

def calculate_prefix(prefix_notation, root_vertex : Vertex):
    result = None
    if root_vertex.value is not None:
        result = root_vertex.value
    else:
        tmp = []
        for key in prefix_notation[root_vertex].keys():
            x = calculate_prefix(prefix_notation[root_vertex], key)
            if isinstance(x, list):
                tmp.extend(x)
            else:
                tmp.append(x)
        result = root_vertex.operation[1](*tmp)
    return result

def build_prefix_notation(graph : Graph, root_vertex : Vertex):
    result = {root_vertex : {}}
    for arc in graph.arcs:
        if arc.arc_from == root_vertex:
            result[root_vertex].update(build_prefix_notation(graph, arc.arc_to))
    return result

def strfprefix(prefix_notation : dict):
    result = []
    for key, value in prefix_notation.items():
        if key.operation is not None:
            result.append(key.operation[0])
        else:
            result.append(str(key.value))
        if value == {}:
            continue
        result[-1] += f'({strfprefix(value)})'
    return ', '.join(result)
