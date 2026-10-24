"""Battery of symmetry hosts: for each group G and each anti-map pi in N(G)/G (brute-force normaliser for m <= 10,
known normalisers otherwise), search G-invariant, A-anti-invariant cores with optimal coins."""
import sys, os, itertools, time, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from groups import close, affine_line, psl2_p_on_line, pgl2_p_on_line, grid_group, graph_edge_group, sym_gens, \
    normaliser_elements, coset_reps
from symsearch import run

MAXREP = 6
DONE10 = {'S5 on 2-sets', 'A5 on 2-sets', 'AGL(1,5) on 2-sets', 'C10', 'D10', 'S2xS5 grid', 'C2xD5 grid'}
LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')


def f9_groups():
    # F_9 = F_3[i], point a + b i <-> index 3a + b
    def idx(a, b): return 3 * (a % 3) + (b % 3)
    def mul(z, w):
        a, b = z; c, d = w
        return ((a * c - b * d) % 3, (a * d + b * c) % 3)
    pts = [(a, b) for a in range(3) for b in range(3)]
    def P(f): return tuple(idx(*f(p)) for p in pts)
    tr1 = P(lambda p: ((p[0] + 1) % 3, p[1]))
    tri = P(lambda p: (p[0], (p[1] + 1) % 3))
    om = (1, 1)  # 1 + i, order 8
    mw = P(lambda p: mul(om, p))
    mw2 = P(lambda p: mul(mul(om, om), p))
    mw4 = P(lambda p: mul(mul(mul(om, om), mul(om, om)), p))
    frob = P(lambda p: (p[0], (-p[1]) % 3))
    out = {
        'AGL(1,9)': [tr1, tri, mw],
        'AGammaL(1,9)': [tr1, tri, mw, frob],
        'F9:C4': [tr1, tri, mw2],
        'F9:C2': [tr1, tri, mw4],
        'F9:C4:frob': [tr1, tri, mw2, frob],
        'F9:C2:frob': [tr1, tri, mw4, frob],
        'ASL(2,3)': [tr1, tri, P(lambda p: ((p[0] + p[1]) % 3, p[1])), P(lambda p: (p[0], (p[0] + p[1]) % 3))],
    }
    return out


def m9_battery():
    B = {}
    B.update(f9_groups())
    B['C9'] = [tuple((i + 1) % 9 for i in range(9))]
    B['D9'] = B['C9'] + [tuple((-i) % 9 for i in range(9))]
    B['Z9:Z9*'] = affine_line(9, [2])
    B['Z9:C3'] = affine_line(9, [4])
    B['S3xS3'] = grid_group(3, 3)
    B['C3xC3:transp'] = grid_group(3, 3, transpose=True, rowgens='C', colgens='C')
    B['S3xC3'] = grid_group(3, 3, rowgens='S', colgens='C')
    B['C3wrC3'] = [tuple([1, 2, 0] + list(range(3, 9))), tuple(list(range(3, 9)) + [0, 1, 2])]
    B['S3wrC3'] = B['C3wrC3'] + [tuple([1, 0, 2] + list(range(3, 9)))]
    B['C3wrS2xC3?'] = [tuple([1, 2, 0] + list(range(3, 9))), tuple(list(range(3, 9)) + [0, 1, 2]),
                       tuple([3, 4, 5, 0, 1, 2, 6, 7, 8])]
    return B


def m10_battery():
    B = {}
    E5 = list(itertools.combinations(range(5), 2))
    B['S5 on 2-sets'] = graph_edge_group(5, E5, sym_gens(5))
    B['A5 on 2-sets'] = graph_edge_group(5, E5, [tuple((i + 1) % 5 for i in range(5)), (1, 2, 0, 3, 4)])
    B['AGL(1,5) on 2-sets'] = graph_edge_group(5, E5, [tuple((i + 1) % 5 for i in range(5)), tuple((2 * i) % 5 for i in range(5))])
    B['C10'] = [tuple((i + 1) % 10 for i in range(10))]
    B['D10'] = B['C10'] + [tuple((-i) % 10 for i in range(10))]
    B['S2xS5 grid'] = grid_group(2, 5)
    B['C2xD5 grid'] = grid_group(2, 5, rowgens='C', colgens='C') + [tuple(a * 5 + (-b) % 5 for a in range(2) for b in range(5))]
    B['S5wrS2'] = grid_group(2, 5)  # placeholder replaced below
    B['S5wrS2'] = [tuple([1, 2, 3, 4, 0] + list(range(5, 10))), tuple([1, 0] + list(range(2, 10))),
                   tuple(list(range(5, 10)) + list(range(5)))]
    B['C5wrC2'] = [tuple([1, 2, 3, 4, 0] + list(range(5, 10))), tuple(list(range(5, 10)) + list(range(5)))]
    B['D5wrC2'] = B['C5wrC2'] + [tuple([0, 4, 3, 2, 1] + list(range(5, 10)))]
    B['AGL(1,5)wrC2'] = B['C5wrC2'] + [tuple([(2 * i) % 5 for i in range(5)] + list(range(5, 10)))]
    return B


def m11_battery():
    B = {}
    B['AGL(1,11)'] = affine_line(11, [2])
    B['C11:C5'] = affine_line(11, [3])
    B['D11'] = affine_line(11, [10])
    B['C11'] = [tuple((i + 1) % 11 for i in range(11))]
    return B


def m11_anti(name):
    # normaliser of these subgroups of AGL(1,11) is AGL(1,11): anti-map multipliers
    return [tuple((a * x) % 11 for x in range(11)) for a in range(1, 11)]


if __name__ == '__main__':
    which = sys.argv[1]
    logf = open(os.path.join(LOG, f'groups_{which}.log'), 'a')
    if which in ('m9', 'm10'):
        m = 9 if which == 'm9' else 10
        B = m9_battery() if m == 9 else m10_battery()
        for name, gens in B.items():
            G = close(gens, m)
            t = time.time()
            if which == 'm10' and name in DONE10:
                continue
            Nel = normaliser_elements(G, m, gens=[tuple(g) for g in gens])
            reps = coset_reps(Nel, G, m)
            logf.write(f"# {name}: |G|={len(G)} |N(G)|={len(Nel)} anti-map classes={len(reps)} ({time.time()-t:.0f}s)\n")
            logf.flush()
            print(f"# {name}: |G|={len(G)} |N(G)|={len(Nel)} reps={len(reps)}", flush=True)
            # anti-maps: prefer pi with pi^2 in G (involutive on orbits); at most MAXREP classes per group
            Gs = set(G)
            inv = [p for p in reps if tuple(p[p[i]] for i in range(m)) in Gs]
            rest = [p for p in reps if p not in inv]
            sel = (inv + rest)[:MAXREP]
            for pi in sel:
                try:
                    run(name, G, m, pi, topk=5, log=logf, anneal_iters=60000, restarts=6)
                except Exception as e:
                    logf.write(f"   {name} pi={pi} error {e}\n")
    elif which == 'm11':
        m = 11
        for name, gens in m11_battery().items():
            if name == 'C11':
                continue
            G = close(gens, m)
            Nel = close(affine_line(11, [2]), m)
            reps = coset_reps([p for p in Nel if all(tuple(p[g[[p.index(i) for i in range(m)][k]]] for k in range(m)) in set(G) for g in gens)], G, m)
            logf.write(f"# {name}: |G|={len(G)} anti-map classes={len(reps)}" + chr(10)); logf.flush()
            for pi in reps:
                run(name, G, m, pi, topk=5, log=logf, anneal_iters=40000, restarts=6)
    logf.close()
