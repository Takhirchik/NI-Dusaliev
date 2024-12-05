import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import re
import os.path
from utils import *

__all__ = ['serialization']

def get_data(file):
    try:
        with open(file, 'r') as f:
            all_data = f.read()
    except:
        raise FileNotFoundError(f'FileNotFoundError: Файл {file} не найден')
    match = re.findall(r"\(\s*?\w+\d+\s*?,\s*?\w+\d+\s*?,\s*?\d+\s*?\)", re.sub(r'\s*', '', all_data))
    if not match:
        raise ValueError(f'ValueError: В файле {file} не указаны или неверно заданы данные')
    graph = Graph()
    sorted_match = sorted(match, key = lambda x: int(x.split(',')[2].strip(')')))
    arcs = []
    for raw_data in sorted_match:
        str_vertex1, str_vertex2 = re.findall(r"\b\w+\d+", raw_data)
        vertex1 = graph.get_vertex(str_vertex1)
        if vertex1 is None:
            vertex1 = Vertex(str_vertex1)
            graph.add_vertex(vertex1)
        vertex2 = graph.get_vertex(str_vertex2)
        if vertex2 is None:
            vertex2 = Vertex(str_vertex2)
            graph.add_vertex(vertex2)
        arcs.append(Arc(vertex1, vertex2, int(re.search(r'\b\d+', raw_data)[0])))
    for raw_data in match:
        str_vertex1, str_vertex2 = re.findall(r"\b\w+\d+", raw_data)
        vertex1 = graph.get_vertex(str_vertex1)
        vertex2 = graph.get_vertex(str_vertex2)
        for arc in arcs:
            if arc.arc_from == vertex1 and arc.arc_to == vertex2 and arc.order == int(re.search(r'\b\d+', raw_data)[0]):
                graph.add_arc(arc)
                break
    return graph

def pretty_print(xml_elem):
    rough_string = ET.tostring(xml_elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent='    ', encoding='utf-8')

class FileExtensionError(Exception):
    pass

def serialization(input_file, output_file):
    if os.path.exists(output_file):
        raise FileExistsError(f'FileExistsError: Файл {output_file} уже существует')
    _, extension = os.path.splitext(output_file)
    if extension != '.xml':
        raise FileExtensionError(f'FileExtensionError: Выходной файл должен быть формата XML-документа')


    graph = get_data(input_file)
    # vertexes, arcs = get_data(input_file)
    data_xml = ET.Element('graph')
    for v in sorted(graph.vertexes, key=lambda x: x.name):
        vertex_xml = ET.SubElement(data_xml, 'vertex')
        vertex_xml.text = v.name
    for arc in graph.arcs:
        arc_xml = ET.SubElement(data_xml, 'arc')
        arc_xml_from = ET.SubElement(arc_xml, 'from')
        arc_xml_from.text = arc.arc_from.name
        arc_xml_to = ET.SubElement(arc_xml, 'to')
        arc_xml_to.text = arc.arc_to.name
        arc_xml_order = ET.SubElement(arc_xml, 'order')
        arc_xml_order.text = str(arc.order)

    str_xml = pretty_print(data_xml)
    with open(output_file, 'wb') as f:
        f.write(str_xml)
