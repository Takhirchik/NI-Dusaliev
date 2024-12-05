import sys
import os
from calculate import prefix_function
import argparse

path_to_dir = os.path.dirname(sys.executable)
# path_to_dir, _ = os.path.split(os.path.abspath(__file__))

def format_file_path(file):
    head, tail = os.path.split(file)
    if head:
        return file
    else:
        return os.path.join(path_to_dir, tail)

def get_prefix_notation(input_file, input_oper_file, output_file):
    formated_input_file = format_file_path(input_file)
    formated_input_oper_file = format_file_path(input_oper_file)
    formated_output_file = format_file_path(output_file)
    formated_errors_file = format_file_path('errors_.txt')
    try:
        prefix_function(formated_input_file, formated_input_oper_file, formated_output_file)
        return 1
    except Exception as e:
        with open(formated_errors_file, 'a') as f:
            f.write(f'{formated_input_file} : {formated_output_file}\n{e}\n')
        return 0

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
    r = get_prefix_notation(input1, input2, output)
    dct = {-1 : 'Попытка завершилась с ошибками',
           1 :'Попытка завершилась успешно'
           }
    print(dct[r])
