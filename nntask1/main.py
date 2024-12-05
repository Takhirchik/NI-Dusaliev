import sys
import argparse
from serialization import *
import os

path_to_dir = os.path.dirname(sys.executable)
# path_to_dir, _ = os.path.split(os.path.abspath(__file__))

def format_file_path(file):
    head, tail = os.path.split(file)
    if head:
        return file
    else:
        return os.path.join(path_to_dir, tail)

def get_graph(input_file, output_file):
    formated_input_file = format_file_path(input_file)
    formated_output_file = format_file_path(output_file)
    formated_errors_file = format_file_path(f'errors.txt')
    try:
        serialization(input_file=formated_input_file, output_file=formated_output_file)
        return 1
    except Exception as e:
        with open(formated_errors_file, 'a') as f:
            f.write(f'{formated_input_file} : {formated_output_file}\n{e}\n')
        return -1


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
    input = params.get('input')
    output = params.get('output')

    error_file = format_file_path('errors.txt')
    r = get_graph(input, output)
    dct = {-1 : 'Попытка завершилась с ошибками',
           1 :'Попытка завершилась успешно'
           }
    print(dct[r])
