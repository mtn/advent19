#!/usr/bin/env python3

with open("input.txt") as f:
    inp = f.read()

layer_len = 150
num_layers = len(inp) / 150

BLACK = str(0)
WHITE = str(1)
TRANSPARENT = str(2)

top_pixels = [None] * layer_len
for i in range(num_layers):
    layer = inp[i * layer_len : (i + 1) * layer_len]

    for i, l in enumerate(layer):
        if top_pixels[i] is not None:
            continue
        if l == WHITE or l == BLACK:
            top_pixels[i] = l

num_rows = 6
num_cols = 25
for row_num in range(num_rows):
    row = top_pixels[row_num * num_cols : (row_num + 1) * num_cols]
    row = "".join(row).replace("1", "#").replace("0", " ")
    print(row)
