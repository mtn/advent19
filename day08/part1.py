#!/usr/bin/env python3

with open("input.txt") as f:
    inp = f.read()

layer_len = 150
num_layers = len(inp) / 150

min_zeros = None
least_zeros_layer = None
for i in range(num_layers):
    layer = inp[i * layer_len : (i + 1) * layer_len]
    num_zeros = layer.count("0")

    if min_zeros is None or num_zeros < min_zeros:
        min_zeros = num_zeros
        least_zeros_layer = i

least_zeros_layer = inp[
    least_zeros_layer * layer_len : (least_zeros_layer + 1) * layer_len
]
print(least_zeros_layer.count("1") * least_zeros_layer.count("2"))
