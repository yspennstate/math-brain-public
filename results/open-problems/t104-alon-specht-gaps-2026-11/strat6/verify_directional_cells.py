"""PROVED: solver-free rational replay of all directional cell certificates."""
import json
from fractions import Fraction as F
from moment_bounds import vertices
from directional_bounds import check

verts=vertices(enhanced=True)
records=json.load(open('directional_moment_cells.json'))
for rec in records:
    assert check(rec,verts)==F(rec['margin'])
print('PROVED:',len(records),'directional cells and every residual matrix verified exactly.')
