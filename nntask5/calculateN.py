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
        self.diff = np.zeros(self.n)

    def calculate(self):
        for i in range(self.n):
            y = 0
            for j in range(self.m):
                y += self.W[i][j] * self.X[j]

            self.Y[i] = sigmoid(y)
            self.diff[i] = self.Y[i] * (1 - self.Y[i])
        return self.Y

class LayerShapeError(Exception):
    pass

class Network:
    def __init__(self, input_Network, input_Train, input_Params, output):
        weights = load(input_Network)
        self.layers = []
        sorted_layers = sorted(weights.keys())
        for w in sorted_layers:
            self.layers.append(Layer(w, weights[w]))

        self.deltas = [[]] * len(self)
        XY = load(input_Train)

        self.X = np.array(XY['X'])
        self.Y = np.array(XY['Y'])

        train_params = load(input_Params)

        self.iters = int(train_params['iters'])
        self.alpha = float(train_params['alpha'])
        self.eps = float(train_params['eps'])

    def __len__(self):
        return len(self.layers)

    def forward(self, input):
        k = len(self)
        for i in range(k):
            l = self.layers[i]
            if i == 0:
                l.X = input
            new_x = l.calculate()
            if i < k - 1:
                self.layers[i + 1].X = new_x
        return self.layers[-1].Y

    def backward(self, output):
        error = 0
        last_layer = self.layers[-1]
        out_len = len(output)
        self.deltas[-1] = np.zeros(out_len)
        for i in range(out_len):
            e = last_layer.Y[i] - output[i]
            self.deltas[-1][i] = e * last_layer.diff[i]
            error += e * e / 2
        k = len(self)
        for i in range(k - 1, 0, -1):
            layer_i = self.layers[i]
            self.deltas[i - 1] = np.zeros(layer_i.m)
            for a in range(layer_i.m):
                for b in range(layer_i.n):
                    self.deltas[i - 1][a] += layer_i.W[b][a] * self.deltas[i][b]
                self.deltas[i - 1][a] *= self.layers[i - 1].diff[a]
        return error

    def update(self):
        for i in range(len(self)):
            layer = self.layers[i]
            for a in range(layer.n):
                for b in range(layer.m):
                    layer.W[a][b] -= self.alpha * self.deltas[i][a] * layer.X[b]

    def train(self):
        it = 0
        error = 1
        result = ''
        while it < self.iters and error > self.eps:
            it += 1
            errors = []
            for i in range(len(self.X)):
                out = self.forward(self.X[i])
                errors.append(self.backward(self.Y[i]))
                self.update()
                print(f'X: {self.X[i]}, Y: {self.Y[i]}, out: {out}')
                error = np.mean(np.array(errors))
            # print(f'it: {it}, error: {error}')
            result += f'{it}: {error}\n'
            print('---------------------')
        # for i in range(len(self.X)):
        #     print(f'X: {self.X[i]}, Y: {self.Y[i]}, out: {self.forward(self.X[i])}')
        return result

def load(file):
    with open(file, 'r') as f:
        return json.load(f)

def dump(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)
    print(data)
