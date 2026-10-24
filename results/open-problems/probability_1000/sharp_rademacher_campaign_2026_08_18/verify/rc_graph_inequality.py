"""RC reduced to one graph inequality - test it on every graph I can enumerate.

Chain established today:
    c = log2 Z,   Z = < prod_e (1 - x_u x_v/3) > = (2/3)^E < 2^{cut(X)} >
    d_cb <= |V| - b   (b = number of BIPARTITE components), by the pair-sum residual family
    RC  <=  c <= beta (k - d_cb)

With k = E (every triangle carrying two shared coordinates), RC follows from

    ***   Z  <=  (4/3)^{E - V + b}   ***

i.e. Z is at most 4/3 to the CYCLE RANK, less one when the component is non-bipartite. Note
E - V + comps is the cycle rank, so the exponent is (cycle rank) - (number of non-bipartite
components).

Sanity of the shape: on an odd cycle the exponent is 0, so the claim is Z <= 1 - and indeed
Z = 1 - 3^-m, only just. On an even cycle the exponent is 1 and Z = 1 + 3^-m, miles inside 4/3.
So the inequality is TIGHT exactly on odd cycles, which is where tightness -> 1.

This enumerates all connected graphs up to isomorphism-ish on small vertex counts (by brute force
over edge subsets of K_V, deduplicated by a cheap canonical form) and checks the inequality exactly.
Reports the WORST ratio Z / (4/3)^{E-V+b} found, and any violation with its graph.

A violation is the useful outcome: it would be an RC counterexample candidate (subject to d_cb
actually attaining the pair-sum bound, which is only an upper bound).
"""
import itertools
import sys
from fractions import Fraction

VMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7


def components_and_bipartite(V, edges):
    adj = {v: [] for v in range(V)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = {}
    comps = 0
    bip_comps = 0
    for s in range(V):
        if s in seen:
            continue
        comps += 1
        seen[s] = 0
        st = [s]
        isbip = True
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in seen:
                    seen[v] = 1 - seen[u]
                    st.append(v)
                elif seen[v] == seen[u]:
                    isbip = False
        if isbip:
            bip_comps += 1
    return comps, bip_comps


def Z_numer(V, edges):
    """integer numerator N with Z = N / (3^E 2^V). All-integer, no Fraction in the hot loop."""
    tot = 0
    for bits in range(1 << V):
        p = 1
        for (a, b) in edges:
            p *= 4 if ((bits >> a) ^ (bits >> b)) & 1 else 2   # 3 - x_u x_v: 4 when DIFFERENT
        tot += p
    return tot          # note 3 - x_u x_v is 4 when different, 2 when same


def Z_exact(V, edges):
    return Fraction(Z_numer(V, edges), 3 ** len(edges) * 2 ** V)


worst = None
violations = []
checked = 0
for V in range(3, VMAX + 1):
    alledges = list(itertools.combinations(range(V), 2))
    for mask in range(1, 1 << len(alledges)):
        edges = [alledges[i] for i in range(len(alledges)) if (mask >> i) & 1]
        # require every vertex used, else it is really a smaller graph
        if len({v for e in edges for v in e}) != V:
            continue
        E = len(edges)
        comps, b = components_and_bipartite(V, edges)
        if comps != 1:
            continue                     # connected only; c and d_cb both add over components
        d = E - V + b
        N = Z_numer(V, edges)
        lhs = N * 3 ** d
        rhs = 4 ** d * 3 ** E * 2 ** V
        checked += 1
        ratio = Fraction(lhs, rhs)
        if worst is None or ratio > worst[0]:
            worst = (ratio, V, E, b, tuple(edges),
                     Fraction(N, 3 ** E * 2 ** V), Fraction(4, 3) ** d)
        if lhs > rhs:
            violations.append((V, E, b, tuple(edges),
                               Fraction(N, 3 ** E * 2 ** V), Fraction(4, 3) ** d))

print("connected graphs checked (exact rationals): %d   up to V = %d" % (checked, VMAX))
print()
if violations:
    print("*** VIOLATIONS: %d" % len(violations))
    for V, E, b, edges, Z, bound in violations[:10]:
        print("   V=%d E=%d bip=%d  Z=%s > bound=%s   %s" % (V, E, b, Z, bound, edges))
else:
    print("NO VIOLATION FOUND. The inequality Z <= (4/3)^{E-V+b} held on every connected graph.")
print()
ratio, V, E, b, edges, Z, bound = worst
print("worst ratio Z / (4/3)^{E-V+b} = %.9f" % float(ratio))
print("   attained at V=%d E=%d bipartite=%s  edges=%s" % (V, E, "yes" if b else "no", edges))
print("   Z = %s = %.9f     bound = %s = %.9f" % (Z, float(Z), bound, float(bound)))
