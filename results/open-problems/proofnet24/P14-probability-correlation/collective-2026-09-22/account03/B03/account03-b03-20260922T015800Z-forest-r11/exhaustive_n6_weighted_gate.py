#!/usr/bin/env python3
"""Exact n=6 stress test for the one-boundary-edge FOREST Rayleigh gate.

All forest counts and all gate-failure tests are integer exact.  NumPy is used
only to vectorize the 5,591,040 labelled graph/(e,f,g) instances; int64 is far
above the largest integer occurring here.  The displayed rho is diagnostic
floating-point only and is not used to certify absence of a counterexample.
"""
from itertools import combinations
from math import sqrt
import numpy as np

NVERT = 6
EDGES = list(combinations(range(NVERT), 2))
M = len(EDGES)
NSUB = 1 << M

def acyclic(mask):
    parent = list(range(NVERT))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(EDGES):
        if (mask >> i) & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return 0
            parent[ru] = rv
    return 1

forest = np.fromiter((acyclic(mask) for mask in range(NSUB)),
                     dtype=np.int64, count=NSUB)
z = forest.copy()
indices = np.arange(NSUB, dtype=np.int64)
for i in range(M):
    bit = 1 << i
    sel = (indices & bit) != 0
    z[sel] += z[indices[sel] ^ bit]

triple_instances = 0
d0_negative = d1_negative = q_negative = m_negative = 0
best_rho = -1.0
best = None

for e, f in combinations(range(M), 2):
    eb, fb = 1 << e, 1 << f
    for g in range(M):
        if g == e or g == f:
            continue
        gb = 1 << g
        req = eb | fb | gb
        Gs = indices[(indices & req) == req]
        triple_instances += len(Gs)

        G0 = Gs ^ gb
        A = z[G0]
        Z = z[Gs]
        B = Z - A

        G0e, G0f, G0ef = G0 ^ eb, G0 ^ fb, G0 ^ eb ^ fb
        a0 = z[G0] - z[G0e]
        b0 = z[G0] - z[G0f]
        c0 = z[G0] - z[G0e] - z[G0f] + z[G0ef]

        Ge, Gf, Gef = Gs ^ eb, Gs ^ fb, Gs ^ eb ^ fb
        ze = Z - z[Ge]
        zf = Z - z[Gf]
        zef = Z - z[Ge] - z[Gf] + z[Gef]
        a1 = ze - a0
        b1 = zf - b0
        c1 = zef - c0

        D0 = a0*b0 - A*c0
        D1 = a1*b1 - B*c1
        Mix = a0*b1 + a1*b0 - A*c1 - B*c0
        Pe = B*a0 - A*a1
        Pf = B*b0 - A*b1

        d0_negative += int(np.count_nonzero(D0 < 0))
        d1_negative += int(np.count_nonzero(D1 < 0))
        m_negative += int(np.count_nonzero(Mix < 0))

        # Q(w)=D0+Mix*w+D1*w^2 is negative for some w>0 exactly in one
        # of the following integer-detectable cases.
        bad = ((D0 < 0) | (D1 < 0) |
               ((D1 == 0) & (Mix < 0)) |
               ((D1 > 0) & (Mix < 0) & (Mix*Mix > 4*D0*D1)))
        q_negative += int(np.count_nonzero(bad))

        # Diagnostic only: largest floating-point all-weight envelope ratio.
        valid = (D0 > 0) & (D1 > 0) & (Pe*Pf > 0)
        if np.any(valid):
            js = np.where(valid)[0]
            denom = (B[js]*np.sqrt(D0[js].astype(float)) +
                     A[js]*np.sqrt(D1[js].astype(float)))**2
            rho = (Pe[js].astype(float)*Pf[js].astype(float))/denom
            q = int(np.argmax(rho))
            if float(rho[q]) > best_rho:
                k = int(js[q])
                best_rho = float(rho[q])
                best = (int(Gs[k]), e, f, g,
                        int(A[k]), int(B[k]),
                        int(a0[k]), int(a1[k]),
                        int(b0[k]), int(b1[k]),
                        int(c0[k]), int(c1[k]),
                        int(D0[k]), int(D1[k]), int(Mix[k]),
                        int(Pe[k]), int(Pf[k]))

Gmask, e, f, g, A, B, a0, a1, b0, b1, c0, c1, D0, D1, Mix, Pe, Pf = best
graph_edges = [EDGES[i] for i in range(M) if (Gmask >> i) & 1]

print("n_vertices", NVERT)
print("graphs", NSUB)
print("triple_instances", triple_instances)
print("D0_negative", d0_negative)
print("D1_negative", d1_negative)
print("mixed_coefficient_negative", m_negative)
print("Q_negative_for_some_positive_weight", q_negative)
print("diagnostic_largest_observed_rho", format(best_rho, ".15f"))
print("stress_graph_mask", Gmask)
print("stress_graph_edges", graph_edges)
print("stress_marks_e_f_g", EDGES[e], EDGES[f], EDGES[g])
print("stress_A_B_a0_a1_b0_b1_c0_c1",
      (A, B, a0, a1, b0, b1, c0, c1))
print("stress_D0_D1_M_Pe_Pf", (D0, D1, Mix, Pe, Pf))
print("stress_Q", f"{D0} + ({Mix})*w + {D1}*w^2")
print("stress_discriminant", Mix*Mix - 4*D0*D1)
