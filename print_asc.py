#!/usr/bin/env python

num_cols = 6
num_rows = (127 - 32 + 1) // num_cols  
# print(num_rows)
for i in range(num_cols):
    print('|DEC|HEX|  ', end='\t')
print()
for i in range(num_cols):
    print('-----------', end='\t')
print()
for i in range(num_rows):
    for j in range(num_cols):
        ascii_val = 32 + i + j * num_rows
        print(f"|{ascii_val:3}|{ascii_val:3X}: {chr(ascii_val)}", end='\t')
    print()
for i in range(num_cols):
    print('-----------', end='\t')