import json
import re
import os.path

def serialization_network(input_file):
    try:
        with open(input_file, 'r') as f:
            data = f.read()
    except:
        raise FileNotFoundError(f'Файл {input_file} не найден')

    match = re.findall(r'\[(\[.*\])\]', data)
    if match[0] is None:
        raise ValueError(f'Файл {input_file} не содержит данных')

    k = 1
    Network = dict()
    for raw_data in match:
        W = re.findall(r'\[[^\]]*\]', raw_data)
        new_W = list()
        for layer in W:
            numbers = re.findall(r'(-?\b\d+\.?\d*|\.\d+\b)', layer)
            new_W.append(list(map(lambda x: float(x), numbers)))
        k_len = len(str(k))
        layer_num = str(k)
        if k_len < len(match) // 10:
            layer_num = '0' * (len(match) // 10 - k_len) + str(k)
        Network[f'W{layer_num}'] = new_W
        k += 1

    filename, _ = os.path.splitext(input_file)
    output_file = filename + '.json'
    i = 1
    while os.path.exists(output_file):
        output_file = filename + f' ({i})' + '.json'
        i += 1

    with open(output_file, 'w') as f:
        json.dump(Network, f)

    return output_file

def serialization_entry(input_file):
    try:
        with open(input_file, 'r') as f:
            data = f.read()
    except:
        raise FileNotFoundError(f'Файл {input_file} не найден')

    match = re.findall(r'(-?\b\d+\.?\d*|\.\d+\b)', data)
    if match[0] is None:
        raise ValueError(f'Файл {input_file} не содержит данных')

    Entry = {'X' : list(map(lambda x: float(x), match))}

    filename, _ = os.path.splitext(input_file)
    output_file = filename + '.json'
    i = 1
    while os.path.exists(output_file):
        output_file = filename + f' ({i})' + '.json'
        i += 1

    with open(output_file, 'w') as f:
        json.dump(Entry, f)

    return output_file
