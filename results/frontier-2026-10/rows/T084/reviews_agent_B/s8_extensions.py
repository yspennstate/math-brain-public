# T084, agent B: single-element extensions of the unbalanced 8-element binary matroid (code 13726). Each contains it as a
# deletion minor, so none is balanced. Question: when the extension's OWN bases are balanced, does the pointwise statement still fail?
import numpy as np, itertools, json, sys
sys.argv = ['x', '0', '0']
from binary_sweep import ranks, run
A = [(13726 >> (4 * c)) & 15 for c in range(4)]; base = [1, 2, 4, 8] + A
out = []
for v in range(1, 16):
    cols = base + [v]; m = 9; rk = ranks(cols, m); R = int(rk[-1])
    X = np.arange(1 << m); pc = np.array([bin(x).count('1') for x in X]); bits = ((X[:, None] >> np.arange(m)) & 1)
    B = bits[(rk == R) & (pc == R)]; n = len(B); s = B.sum(0); P = B.T @ B; V = n * P - np.outer(s, s); np.fill_diagonal(V, -1)
    res = run(cols); fails = [(i, bad) for i, (_, bad) in enumerate(res) if bad]
    out.append({'new_col': v, 'top_balanced': bool(V.max() <= 0), 'pointwise_fail_pairs': len(fails), 'levels': sorted({l for _, b in fails for l in b})})
    print(json.dumps(out[-1]), flush=True)
