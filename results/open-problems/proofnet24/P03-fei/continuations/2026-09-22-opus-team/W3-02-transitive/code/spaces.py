"""Named transitive permutation groups used by the W3-02 searches (generators on [n])."""
import numpy as np
import tlib


def psl2_gens(q):
    """PSL(2,q) acting on the projective line F_q u {inf} (q prime): points 0..q-1, inf = q."""
    inf = q

    def mob(a, b, c, d):
        g = []
        for x in range(q + 1):
            if x == inf:
                g.append(inf if c % q == 0 else (a * pow(c, -1, q)) % q)
            else:
                num = (a * x + b) % q
                den = (c * x + d) % q
                g.append(inf if den == 0 else (num * pow(den, -1, q)) % q)
        return g
    return [mob(1, 1, 0, 1), mob(0, q - 1, 1, 0)]


def k33_doubled():
    """Aut(K_{3,3}) acting diagonally on two copies A (0..8) and B (9..17) of the edge set, plus the
    swap A <-> B.  Transitive on 18 points; contains the symmetry of Numaro's g on core+coins
    (coin j of g sits at edge j after relabelling) only if relabelled; used for a symmetric search."""
    g9, n9 = tlib.bipartite_gens(3, 3, transpose=True)
    gens = []
    for g in g9:
        gens.append(list(g) + [9 + v for v in g])
    swap = [9 + i for i in range(9)] + [i for i in range(9)]
    gens.append(swap)
    return gens, 18


def get(name):
    """Return (gens, n) for a named group."""
    if name.startswith('Z'):
        n = int(name[1:]); return tlib.cyclic_gens(n), n
    if name.startswith('D') and name[1:].isdigit():
        n = int(name[1:]); return tlib.dihedral_gens(n), n
    if name.startswith('K') and name[1:].isdigit() and len(name) == 2:
        g, n, _ = tlib.graph_gens(int(name[1])); return g, n
    if name.startswith('H3_'):
        g, n, _ = tlib.hypergraph3_gens(int(name[3:])); return g, n
    if name.startswith('B') and len(name) == 3:
        a, b = int(name[1]), int(name[2]); return tlib.bipartite_gens(a, b, transpose=(a == b))
    if name.startswith('W') and len(name) == 3:
        w, s = int(name[1]), int(name[2]); return tlib.wreath_gens(w, s)
    if name.startswith('AGL'):
        p = int(name[3:]); return tlib.affine_line_gens(p), p
    if name.startswith('T') and name[1:].isdigit():
        k = int(name[1:]); return tlib.translations_F2(k), 1 << k
    if name.startswith('PSL'):
        q = int(name[3:]); return psl2_gens(q), q + 1
    if name == 'K33x2':
        return k33_doubled()
    raise ValueError(name)


def space(name):
    gens, n = get(name)
    return tlib.InvariantSpace(gens, n, name)
