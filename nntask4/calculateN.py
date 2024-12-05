import numpy as np
import json
from math import exp

def sigmoid(x):
    return 1 / (1 + exp(-x))

class Layer:
    def __init__(self, name, W):
        self.name = name
        self.W = np.array(W)
        shape = self.W.shape
        self.n = shape[0]
        self.m = shape[1]
        self.X = np.zeros(self.m)
        self.Y = np.zeros(self.n)

    def set_x(self, X):
        self.X = np.array(X)
        assert(self.X.shape[0] != self.n)

    def calculate(self):
        print(f'{self.name}:\n{self.W}')
        print(('\t' * (self.m // 2)) + '*')
        print('X:' + str(self.X))
        Y = np.dot(self.W, self.X)
        print(('\t' * (self.m // 2)) + '||')
        print('Y:' + str(Y))
        print('Применяется процедура сигмоида на Y')
        for i in range(self.n):
            Y[i] = sigmoid(Y[i])
        print('Y:' + str(Y))
        self.Y = Y
        return self.Y

class LayerShapeError(Exception):
    pass

class Network:
    def __init__(self, input_layers, input_entry, output):
        weights = load(input_layers)
        self.layers = []
        sorted_layers = sorted(weights.keys())
        for w in sorted_layers:
            self.layers.append(Layer(w, weights[w]))
        for w1, w2 in zip(self.layers[:-1], self.layers[1:]):
            if w1.n != w2.m:
                raise LayerShapeError(f'Слой {w1.name} не имеет связности со слоем {w2.name}')
        X = load(input_entry)
        self.layers[0].X = np.array(X['X'])
        dump(output, {'Y' : list(self.calculate())})

    def __len__(self):
        return len(self.layers)

    def calculate(self):
        k = len(self)
        for i in range(k):
            print('-----------------------------------------------')
            l = self.layers[i]
            new_x = l.calculate()
            if i < k - 1:
                self.layers[i + 1].X = new_x
            print('-----------------------------------------------')
        return self.layers[-1].Y

def load(file):
    with open(file, 'r') as f:
        return json.load(f)

def dump(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)
    print(data)
