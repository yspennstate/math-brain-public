import psutil; _p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 14, 15])
import sys, itertools, numpy as np
sys.argv = ['x', 'pg23', '0', '0', '0', '0', 'full']
exec(open('run_lines.py', encoding='utf-8').read().split("rng = np.random.default_rng(5)")[0])
from holes_subsetsum import subset_sums
pc = np.array([bin(x).count('1') for x in range(N)])
bal, res = subset_sums(M, vprop, max_k=4)
print('balance of the property (sum c0):', bal, ' candidates:', len(res))
for R, S, I in res[:15]:
    info = [(int(o), int(M.size[o]), sorted(set(pc[M.rep == o].tolist()))) for o in S]
    c = M.c0(np.where(np.isin(np.arange(M.no), S), 0, vprop))
    from holecore import summarize2
    s = summarize2(c, 13)
    print(f"  R={R:.12f} I={I:.6f} holes(orbit,size,weights)={info} ngroups={s["ngroups"]} nvars={s['nvars']}")
