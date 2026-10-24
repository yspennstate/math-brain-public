#!/usr/bin/env python3
"""Exact finite checker for the degree profiles in KIM-MATTMAN-OH-2026-TFIK22-D34.

A graph in the claimed source residue has 22 edges and every vertex has degree 3
or 4.  If a is the number of degree-4 vertices and b the number of degree-3
vertices, the handshake lemma gives 4*a + 3*b = 44.

This checker was executed in the R01 run on 2026-09-19.  Archived output:

[(2, 12, 14), (5, 8, 13), (8, 4, 12), (11, 0, 11)]

Each tuple is (a, b, a+b).  The 2026 Kim--Mattman--Oh source settles (8,4),
so the three claimed unresolved profiles are (11,0), (5,8), and (2,12).
"""

solutions = []
for a in range(12):
    for b in range(16):
        if 4 * a + 3 * b == 44:
            solutions.append((a, b, a + b))

expected = [(2, 12, 14), (5, 8, 13), (8, 4, 12), (11, 0, 11)]
assert solutions == expected
print(solutions)
