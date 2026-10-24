# Numerical check of the down-set lemma and of the restriction step it gives for monotone DNFs of width <= w.
# For each function: q = Pr[f = 0]; eps_v = Inf_v/(4q) (down-set side), eps'_v = Inf_v/(4(1-q)) (up-set side);
# lemma: B_v <= 1.75 Inf_v + log2(5e)(4 min(q,1-q) - Inf_v) at EVERY coordinate;
# step:  at v* = argmax_v Inf_v, Delta_{v*}/Inf_{v*} <= 2/ln2 + 1.75 + log2(5e)(4 min(q,1-q)/Inf_{v*} - 1).
# Also reports max_v Inf_v / min(q,1-q) (the "relative influence" gamma), which the width argument bounds below by
# 2/3 (width 2, via an edge) and 2^(1-w) (width w, via a shortest minterm).
import sys, random, itertools, numpy as np
from gdnf import truth_table, analyse
from gdnf_battery import (path, cycle, star, complete, kab, grid, hypercube, petersen, paley, crown, matching,
                          random_regular, gnp)

L5E = np.log2(5 * np.e); C0 = 2 * np.exp(-0.5) / np.log(2); JS = 2 / np.log(2)

def check(n, terms, name):
    f = truth_table(n, terms)
    r = analyse(n, f)
    q = 1.0 - f.mean()
    qm = min(q, 1 - q)
    Inf, B, D = r['Inf'], r['B'], r['Delta']
    rel = Inf > 1e-14
    if not rel.any():
        return None
    lem = np.where(rel, B - (C0 * Inf + L5E * (4 * qm - Inf)), -np.inf)
    vs = int(np.argmax(Inf))
    gamma = Inf[vs] / qm
    step = D[vs] / Inf[vs]
    stepbound = JS + C0 + L5E * (4 * qm / Inf[vs] - 1)
    return dict(name=name, n=n, q=q, HI=r['H'] / r['I'], gamma=gamma, step=step, stepbound=stepbound,
                lemma_worst=float(lem.max()), rho0=float(np.min(np.where(rel, D / np.where(rel, Inf, 1), np.inf))))

def random_width_dnf(n, m, w, rng):
    return [tuple(rng.sample(range(n), rng.randint(1, w))) for _ in range(m)]

if __name__ == '__main__':
    rng = random.Random(7)
    fams = []
    for n in (8, 12, 16, 20): fams += [('path%d' % n, n, path(n)), ('cycle%d' % n, n, cycle(n))]
    for k in (3, 7, 12, 19): fams.append(('star%d' % k, k + 1, star(k)))
    for n in (5, 8, 12, 16, 20): fams.append(('K%d' % n, n, complete(n)))
    for a, b in ((3, 3), (2, 10), (5, 5), (3, 12), (8, 8), (10, 10)): fams.append(('K%d,%d' % (a, b), a + b, kab(a, b)))
    for rr, cc in ((3, 3), (4, 4), (4, 5)): fams.append(('grid%dx%d' % (rr, cc), rr * cc, grid(rr, cc)))
    for d in (3, 4): fams.append(('Q%d' % d, 1 << d, hypercube(d)))
    fams.append(('petersen', 10, petersen()))
    for q in (13, 17): fams.append(('paley%d' % q, q, paley(q)))
    for k in (4, 8, 10): fams.append(('crown%d' % k, 2 * k, crown(k)))
    for m in (4, 8, 10): fams.append(('matching%d' % m, 2 * m, matching(m)))
    for n, d in ((16, 3), (20, 3), (20, 5), (20, 8)):
        e = random_regular(n, d, rng)
        if e: fams.append(('rr%d_d%d' % (n, d), n, e))
    for n, p in ((16, 0.1), (20, 0.1), (20, 0.3), (20, 0.5)): fams.append(('gnp%d_%.2f' % (n, p), n, gnp(n, p, rng)))
    # graphs with singleton terms (the restriction class)
    for n in (10, 14, 18):
        e = gnp(n, 0.25, rng); s = rng.sample(range(n), 2)
        fams.append(('gnp%d+2single' % n, n, e + [(v,) for v in s]))
    # width-3 and width-4 random monotone DNFs
    for (n, m, w) in ((12, 6, 3), (14, 10, 3), (16, 20, 3), (18, 30, 3), (16, 8, 4), (18, 25, 4), (20, 60, 3)):
        for s in range(3):
            fams.append(('w%d_n%d_m%d_s%d' % (w, n, m, s), n, random_width_dnf(n, m, w, rng)))
    worst_step_frac = 0.0; worst_lemma = -np.inf; min_gamma2 = np.inf
    print('%-18s %3s %9s %7s %7s %8s %9s %8s %10s' % ('function', 'n', 'q', 'H/I', 'gamma', 'step', 'stepbound', 'rho0', 'lemma_max'))
    for name, n, t in fams:
        terms = [tuple(x) for x in t]
        o = check(n, terms, name)
        if o is None: continue
        worst_lemma = max(worst_lemma, o['lemma_worst'])
        worst_step_frac = max(worst_step_frac, o['step'] / o['stepbound'])
        if all(len(x) <= 2 for x in terms): min_gamma2 = min(min_gamma2, o['gamma'])
        print('%-18s %3d %9.3e %7.4f %7.4f %8.4f %9.4f %8.4f %10.3e' % (name, n, o['q'], o['HI'], o['gamma'], o['step'],
              o['stepbound'], o['rho0'], o['lemma_worst']), flush=True)
    print('max over all of (lemma lhs - rhs): %.3e  (must be <= 0)' % worst_lemma)
    print('max over all of step/stepbound:    %.4f  (must be <= 1)' % worst_step_frac)
    print('min relative influence gamma on width-2 functions: %.4f  (proved >= 2/3)' % min_gamma2)
