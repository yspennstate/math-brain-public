"""Exact finite dyadic checks and independent constants for PROOF.md."""

from fractions import Fraction as F
from pathlib import Path
import math
import os
import resource
import time

started = time.monotonic()
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

# All integrals below are exact integrals against step-function inputs.
# w(u)=u^2(1-u)^2(u-1/2); its integral is zero by reflection.
coeff = [F(0), F(0), F(-1, 2), F(2), F(-5, 2), F(1)]
A = sum(abs(c) for c in coeff) + sum(j * abs(c) for j, c in enumerate(coeff))
assert A == 28


def primitive(x):
    return sum((c * x**(j + 1) / (j + 1) for j, c in enumerate(coeff)), F(0))


assert primitive(F(1)) == primitive(F(0)) == 0
for k in range(21):
    u = F(k, 20)
    value = sum((c * u**j for j, c in enumerate(coeff)), F(0))
    assert value == u**2 * (1-u)**2 * (u-F(1, 2))

grid_depth = 6
leaves = 2**grid_depth
supports = [(s, left, 2**(grid_depth-s))
            for s in range(4)
            for left in range(0, leaves, 2**(grid_depth-s))]
carriers = [
    [F(1 if j % 2 else -1) for j in range(leaves)],
    [F([1, -1, 0, 1, -1, 1, 0][j % 7], 2) for j in range(leaves)],
]


def bump_average(s, left, width, depth):
    """E_depth(w_I), represented on the fine grid; depth>=s."""
    depth = min(depth, grid_depth)
    cell_width = 2**(grid_depth-depth)
    result = [F(0)] * leaves
    for start in range(left, left + width, cell_width):
        u, v = F(start-left, width), F(start+cell_width-left, width)
        mean = (primitive(v)-primitive(u)) / (v-u)
        result[start:start+cell_width] = [mean] * cell_width
    return result


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0)) / leaves


pieces = {}
for h in range(1, grid_depth + 1):
    pieces[h] = []
    for s, left, width in supports:
        fine = bump_average(s, left, width, s+h)
        coarse = bump_average(s, left, width, s+h-1)
        pieces[h].append([x-y for x, y in zip(fine, coarse)])

gram_checks = 0
for h, vectors in pieces.items():
    for i, (si, li, wi) in enumerate(supports):
        assert dot(vectors[i], vectors[i]) / F(wi, leaves) <= 4*A*A*F(1, 4)**h
        for j in range(i):
            assert dot(vectors[i], vectors[j]) == 0
            gram_checks += 1
print(f'exact fixed-carrier martingale orthogonality checks: {gram_checks}')

tests = [[F(int(j == k)) for j in range(leaves)] for k in range(leaves)]
tests += [[F(((j*j + 3*k*j + k) % 7)-3, 3) for j in range(leaves)]
          for k in range(12)]
physical_checks = augmented_checks = 0
for h, vectors in pieces.items():
    for f in tests:
        norm2 = dot(f, f)
        output2 = F(0)
        augmented2 = F(0)
        private = [list(reversed(f)), [(-x if j % 3 else x) for j, x in enumerate(f)]]
        augmented_input2 = norm2 + sum(dot(z, z) for z in private)
        for v, carrier in enumerate(carriers):
            for (_, _, width), q in zip(supports, vectors):
                length = F(width, leaves)
                physical = dot(q, [x*m for x, m in zip(f, carrier)])
                output2 += physical**2 / length
                augmented2 += (physical + dot(q, private[v]))**2 / length
        assert output2 <= 4*A*A*len(carriers)*F(1, 4)**h*norm2
        assert augmented2 <= 4*A*A*(len(carriers)+1)*F(1, 4)**h*augmented_input2
        physical_checks += 1
        augmented_checks += 1
print(f'exact physical contraction checks: {physical_checks}; augmented checks: {augmented_checks}')

# Verify the original integral by integrating the polynomial, independently
# of its telescoping expression, on schedules which vary with both s and y.
# Four singleton blocks admit amplitudes <=1/2. The initial-piece
# class s=0,3 includes two distinct support depths in the same class.
decomposition_checks = residue_checks = 0
h_initial = 2
for trial in range(12):
    schedule = [[F(((j*j + 3*s*j + trial*j + s) % 5)-2, 4)
                 for j in range(leaves)] for s in range(4)]
    assert all(4*x*x <= 1 for row in schedule for x in row)
    outputs = {h: [] for h in [0, *range(h_initial+1, grid_depth+1)]}
    for v, carrier in enumerate(carriers):
        for row_index, (s, left, width) in enumerate(supports):
            operand = [a*b for a, b in zip(schedule[s], carrier)]
            original = dot(bump_average(s, left, width, grid_depth), operand)
            initial = dot(bump_average(s, left, width, s+h_initial), operand)
            outputs[0].append((s, F(width, leaves), initial))
            reconstructed = initial
            for h in range(h_initial+1, grid_depth+1):
                piece = dot(pieces[h][row_index], operand)
                reconstructed += piece
                outputs[h].append((s, F(width, leaves), piece))
            assert original == reconstructed
            decomposition_checks += 1
    for h, values in outputs.items():
        offset = h_initial if h == 0 else h
        direct = sum((value*value / length for _, length, value in values), F(0))
        separate = [sum((value*value / length for s, length, value in values
                         if s % (offset+1) == residue), F(0))
                    for residue in range(offset+1)]
        assert direct == sum(separate)
        assert direct <= (offset+1)*max(separate)
        residue_checks += 1
print(f'exact scheduled bump decompositions: {decomposition_checks}; residue square sums: {residue_checks}')

# Two independent derivations of the infinite weighted geometric sums:
# finite rational summation with an exact remainder, and closed forms.
for n in range(51):
    upper = n + 64
    tail_mass = sum((F(1, 2)**h for h in range(n+1, upper+1)), F(0))
    tail_moment = sum(((h+1)*F(1, 2)**h for h in range(n+1, upper+1)), F(0))
    assert tail_mass + F(1, 2)**upper == F(1, 2)**n
    assert tail_moment + (upper+3)*F(1, 2)**upper == (n+3)*F(1, 2)**n
assert F(40, 3)*F(21, 2) == 140
assert F(10, 3)**2 > 11 and F(7, 2)**2 > 12
assert 3*F(10, 3) + F(1, 50)*F(7, 2) < F(21, 2)
assert F(1, 2)**19 < F(1, 100)
print('weighted tail: 51 exact finite-sum/remainder checks; rational 140-constant proof: passed')

for d in list(range(2, 2050)) + [2**j for j in range(12, 101)]:
    ell = math.log2(2*d)
    h0 = math.ceil(10*ell)
    cd = (8/3)*math.sqrt(9+(1+math.ceil(5*math.log2(d)))**2)
    assert h0+1 <= 11*ell and h0+3 <= 12*ell
    assert math.sqrt(d)*2**(-h0) < .01
    for b, a in [(1, 0), (0, 1)]:
        refined = cd*(math.sqrt(h0+1)*(b+3*a)
                      +2*a*math.sqrt(d)*math.sqrt(h0+3)*2**(-h0))
        assert refined <= 140*(b+a)*ell**1.5
print('supplementary floating-point constant checks: 2137 catalog sizes, B-only and A-only')

here = Path(__file__).resolve().parent
for n in range(1, 4):
    source = (here/'sources'/f'candidate{n}-introduction.tex').read_text()
    begin = source.index(r'\begin{theorem}\label{thm:main}')
    end = source.index(r'\end{theorem}', begin) + len(r'\end{theorem}')
    if (here/'VERIFY.md').exists():
        assert source[begin:end] in (here/'VERIFY.md').read_text()
print('main-theorem source extracts readable; quotation checks run when VERIFY.md exists')
print(f'nice={os.getpriority(os.PRIO_PROCESS, 0)}')
print(f'peak RSS (macOS bytes)={resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}')
print(f'elapsed seconds={time.monotonic()-started:.3f}')
