"""Controls for the dream's semantic pair step (_top_sem_pairs in dream.py).

 P1 a planted corpus: 5,000 near-duplicate pairs of one series at dot 0.99 crowd the top 4,000; one real pair
    across series at 0.90 is still found, and a linked pair at 0.95 is not (filtering after the top-k loses it)
 P2 against brute force on a small random set: the same pairs, the same order, any block size
 P3 nothing of one series and nothing already linked comes back

The function is compiled out of dream.py alone (importing dream.py would run a dream).

    python test_dream_sem_pairs.py [DREAM_PY]      (a few seconds; ALL PASS at the end)
"""
import ast
import io
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "dream.py")
results = []
N_CHECKS = 5


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


def load():
    tree = ast.parse(io.open(PATH, encoding="utf-8").read())
    fn = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "_top_sem_pairs"]
    if not fn:
        raise LookupError("dream.py has no _top_sem_pairs")
    ns = {}
    exec(compile(ast.Module(body=fn, type_ignores=[]), PATH, "exec"), ns)
    return ns["_top_sem_pairs"]


def unit(v):
    return v / np.linalg.norm(v, axis=-1, keepdims=True)


try:
    f = load()
    rng = np.random.default_rng(11)
    d, npair = 64, 5000
    base = unit(rng.standard_normal((npair, d)))
    rows, pid = [], []
    for k in range(npair):                       # two near-identical rows per series, dot about 0.99
        rows += [base[k], unit(base[k] + 0.1 * unit(rng.standard_normal(d)) * 1.4)]
        pid += [k, k]
    def mix(x, rho):                             # a unit vector at dot rho with x
        r = rng.standard_normal(d)
        r -= (r @ x) * x
        return unit(rho * x + np.sqrt(1 - rho * rho) * unit(r))
    a = unit(rng.standard_normal(d))
    b = mix(a, 0.90)
    c = unit(rng.standard_normal(d))
    e = mix(c, 0.95)
    ia = len(rows)
    rows += [a, b, c, e]
    pid += [npair, npair + 1, npair + 2, npair + 3]
    V = np.array(rows, dtype=np.float32)
    pid = np.array(pid, dtype=np.int64)
    n = len(V)
    codes = np.unique(np.array([(ia + 2) * n + (ia + 3)], dtype=np.int64))      # c-e already linked
    I, J, D = f(V, np.float32(0.8), pid, codes, keep=4000)
    got = set(zip(I.tolist(), J.tolist()))
    check((ia, ia + 1) in got, "P1 the real cross-series pair survives %d same-series duplicates" % npair)
    check((ia + 2, ia + 3) not in got, "P1 the linked pair is not returned")
    check(all(pid[i] != pid[j] for i, j in got) and len(got) <= 4000, "P3 no same-series pair, at most keep")

    W = unit(rng.standard_normal((300, 8))).astype(np.float32)
    wp = rng.integers(0, 120, 300).astype(np.int64)
    lc = np.unique(np.array([i * 300 + j for i in range(0, 300, 7) for j in range(i + 1, 300, 11)], np.int64))
    G = W @ W.T
    want = []
    for i in range(300):
        for j in range(i + 1, 300):
            if G[i, j] >= np.float32(0.5) and wp[i] != wp[j] and (i * 300 + j) not in set(lc.tolist()):
                want.append((-float(G[i, j]), i, j))
    want = [(i, j) for _, i, j in sorted(want)[:50]]
    outs = []
    for blk in (7, 1024):
        I, J, D = f(W, np.float32(0.5), wp, lc, keep=50, block=blk)
        C = D.astype(np.float64)
        order = np.lexsort((J, I, -C))[:50]
        outs.append([(int(I[k]), int(J[k])) for k in order])
    check(outs[1] == want, "P2 equals brute force (%d pairs)" % len(want))
    check(outs[0] == outs[1], "P2 the same with a block of 7 rows")
except Exception as ex:
    check(False, "raised %s: %s" % (type(ex).__name__, ex))

ok = all(results) and len(results) == N_CHECKS
print("ALL PASS" if ok else "FAILED %d of %d" % (N_CHECKS - results.count(True), N_CHECKS))
sys.exit(0 if ok else 1)
