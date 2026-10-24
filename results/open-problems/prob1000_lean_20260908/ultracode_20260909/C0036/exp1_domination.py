# Experiment 1: Strassen max-flow test of Conjecture 5.7 (both halves) on small groups,
# plus the two sharper statements used in the proof attempt:
#   (i)  compression inequality  det Q_A >= FK(Q)^{|A|} for every A  (necessary for the conjecture)
#   (ii) the random-order mixture nu_bar = avg over orderings sigma of the product measure with
#        pivot densities d_k(sigma) = det Q_{sigma[k]} / det Q_{sigma[k-1]}  dominates mu_FK,
#        and P_Q dominates nu_bar (sanity of the sequential-coupling step).
import numpy as np, itertools, json, sys, time
import groups as g
import domination as d

rng = np.random.default_rng(20260909)
GROUPS = [('Z2', g.cyclic(2)), ('Z3', g.cyclic(3)), ('Z4', g.cyclic(4)), ('Z2xZ2', g.direct_product(g.cyclic(2), g.cyclic(2))),
          ('Z5', g.cyclic(5)), ('Z6', g.cyclic(6)), ('S3', g.S3()), ('Z7', g.cyclic(7)),
          ('Z8', g.cyclic(8)), ('D4', g.D4()), ('Q8', g.Q8()), ('Z2^3', g.direct_product(g.cyclic(2), g.direct_product(g.cyclic(2), g.cyclic(2)))),
          ('Z2xZ4', g.direct_product(g.cyclic(2), g.cyclic(4)))]
KINDS = ['random', 'full', 'near0', 'near1']
N_PER = int(sys.argv[1]) if len(sys.argv) > 1 else 6
MAX_N_MIX = 7   # orderings enumerated fully up to this size


def pivots(Q, order):
    n = len(Q)
    dets = [1.0]
    for k in range(1, n + 1):
        S = list(order[:k])
        dets.append(np.linalg.det(Q[np.ix_(S, S)]).real)
    return [dets[k] / dets[k - 1] for k in range(1, n + 1)]


def mixture_over_orders(Q):
    n = len(Q)
    N = 2 ** n
    nu = np.zeros(N)
    cnt = 0
    for order in itertools.permutations(range(n)):
        dv = pivots(Q, order)
        dens = np.zeros(n)
        for k, site in enumerate(order):
            dens[site] = dv[k]
        # product measure with site densities
        pm = np.ones(N)
        for m in range(N):
            for i in range(n):
                pm[m] *= dens[i] if (m >> i) & 1 else 1 - dens[i]
        nu += pm
        cnt += 1
    return nu / cnt


def compression_ratio(Q, fk):
    n = len(Q)
    worst = np.inf
    worstA = None
    for m in range(1, 2 ** n):
        S = [i for i in range(n) if (m >> i) & 1]
        r = np.linalg.det(Q[np.ix_(S, S)]).real / fk ** len(S)
        if r < worst:
            worst, worstA = r, S
    return worst, worstA


results = []
t0 = time.time()
for name, T in GROUPS:
    n = len(T)
    for kind in KINDS:
        for rep in range(N_PER):
            Q = g.random_equivariant_contraction(T, rng, kind)
            fk = g.FK(Q)
            fk_c = g.FK(np.eye(n) - Q)
            P = g.determinantal_law(Q)
            Pc = g.determinantal_law(np.eye(n) - Q)
            mu = g.product_law(n, fk)
            muc = g.product_law(n, fk_c)
            lo = d.deficit(P, mu)          # lower half of the conjecture
            up = d.deficit(Pc, muc)        # upper half (complement form)
            comp, compA = compression_ratio(Q, fk)
            row = dict(group=name, n=n, kind=kind, rep=rep, FK=fk, lower_deficit=lo, upper_deficit=up,
                       compression_min_ratio=comp, spec=np.linalg.eigvalsh(Q).tolist())
            if n <= MAX_N_MIX:
                nu = mixture_over_orders(Q)
                row['mix_vs_muFK_deficit'] = d.deficit(nu, mu)
                row['PQ_vs_mix_deficit'] = d.deficit(P, nu)
            results.append(row)
            flag = '' if max(lo, up) < 1e-9 and comp > 1 - 1e-6 else '   <-- VIOLATION?'
            print(f"{name:6s} n={n} {kind:6s} rep={rep} FK={fk:.4f} lower={lo:.2e} upper={up:.2e} compr={comp:.4f}"
                  + (f" mix={row['mix_vs_muFK_deficit']:.2e} PQ>=mix={row['PQ_vs_mix_deficit']:.2e}" if n <= MAX_N_MIX else '') + flag, flush=True)
print('elapsed', time.time() - t0)
with open('exp1_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=1)
worst = max(max(r['lower_deficit'], r['upper_deficit']) for r in results)
print('worst conjecture deficit over all instances:', worst)
print('min compression ratio:', min(r['compression_min_ratio'] for r in results))
mix = [r['mix_vs_muFK_deficit'] for r in results if 'mix_vs_muFK_deficit' in r]
print('worst mixture deficit:', max(mix), ' worst PQ>=mix deficit:', max(r['PQ_vs_mix_deficit'] for r in results if 'PQ_vs_mix_deficit' in r))
