"""Independent replication of the read-once AND/OR beam search (EVIDENCE claims U-G-tight and the G/I plateau).

Population: best H/I formula per bin of the mean; each round combines every pair with AND2 and OR2 (fan-in 2),
leaves capped at 4000.  Reports, for the best formula of each round: H/I, U/I, the Theorem G ratio in both forms
(full: denominator 2(I-Var)+2U-p0 log2(1/p0); weak: 2(I-Var)+2U), and G/I with min/max local U-ratios.
"""
import json, math, sys, time
from rec import var, gate, root_stats, AND2, OR2

NB = 120
LEAVES_MAX = 4000


def binof(mu):
    return min(NB - 1, int((mu + 1) / 2 * NB))


class F:
    __slots__ = ('node', 'leaves', 'ratio', 'mu')


def mk(node, leaves):
    f = F(); f.node = node; f.leaves = leaves
    s = node.summ(); H, U, I, Var = s.full()
    f.ratio = H / I if I > 0 else 0.0; f.mu = s.mu
    return f


x = mk(var(), 1)
pop = {binof(0.0): x}
log = []
t0 = time.time()
for rnd in range(14):
    items = list(pop.values()); new = dict(pop)
    for a in items:
        for b in items:
            if a.leaves + b.leaves > LEAVES_MAX:
                continue
            for g in (AND2, OR2):
                nd = gate(g, [a.node, b.node], symmetric=(a is b))
                s = nd.summ()
                if s.const():
                    continue
                H, U, I, Var = s.full()
                if Var < 1e-6 or I <= 0:
                    continue
                f = F(); f.node = nd; f.leaves = a.leaves + b.leaves; f.ratio = H / I; f.mu = s.mu
                k = binof(s.mu)
                if k not in new or f.ratio > new[k].ratio:
                    new[k] = f
    pop = new
    top = max(pop.values(), key=lambda f: f.ratio)
    st = root_stats(top.node)
    row = dict(round=rnd, leaves=top.leaves, H_over_I=st['H_over_I'], U_over_I=st['U_over_I'], Var=st['Var'],
               thmG_ratio_full=st['thmG_ratio_full'], thmG_ratio_weak=st['thmG_ratio_weak'],
               G_over_I=st['G_over_I'], min_local_U=st['min_local_U'], max_local_U=st['max_local_U'],
               max_U_over_I_in_pop=max(f.node.summ().full()[1] / f.node.summ().full()[2] for f in pop.values()),
               secs=round(time.time() - t0, 1))
    log.append(row)
    print(json.dumps(row), flush=True)
with open('beam_results.json', 'w', encoding='utf-8') as fh:
    json.dump(log, fh, indent=1)
