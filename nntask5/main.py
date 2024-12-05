import sys
import os.path
from calculateN import *
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
    input3 = params.get('input3')
    output = params.get('output')
    error_file = format_file_path('errors.txt')

    try:
        network = Network(format_file_path(input1), format_file_path(input2), format_file_path(input3), format_file_path(output))
        result = network.train()
        with open(format_file_path(output), 'w') as f:
            f.write(result)
    except Exception as e:
        print(e)
        with open(error_file, 'a') as f:
            f.write(f'{datetime.now()} : {e}\n')
