import sys
import os.path
from calculateN import *
from serializationN import *
import argparse
from datetime import datetime

path_to_dir = os.path.dirname(sys.executable)
# path_to_dir, _ = os.path.split(os.path.abspath(__file__))

def format_file_path(file):
    head, tail = os.path.split(file)
    if head:
        return file
    else:
        return os.path.join(path_to_dir, tail)

def parse_value(value : str):
    parts = value.split('=')
    if len(parts) != 2:
        raise argparse.ArgumentTypeError('Неверный формат введённых данных')
    return parts[0], parts[1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('params', nargs='+', type=parse_value)
    args = parser.parse_args()
    params = dict(args.params)
    input1 = params.get('input1')
    input2 = params.get('input2')
    output = params.get('output')

    error_file = format_file_path('errors.txt')
    try:
        Name_network = serialization_network(format_file_path(input1))
        Name_entry = serialization_entry(format_file_path(input2))
        Network(Name_network, Name_entry, format_file_path(output))
    except Exception as e:
        print(e)
        with open(error_file, 'a') as f:
            f.write(f'{datetime.now()} : {e}\n')
