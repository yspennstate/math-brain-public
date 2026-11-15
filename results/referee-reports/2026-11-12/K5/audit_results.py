"""Independent-equation and exact rank-one audits of the saved results."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import json
import random
import resource
import time
from fractions import Fraction as F
import mpmath as mp
from exact_core import calculate,lump,inverse,leaf_family,save_json


def main():
    start = time.monotonic()
    rng = random.Random(195778)
    maxratio = F(0)
    count = 0
    for trial in range(120):
        w = [[0]*5 for _ in range(5)]
        # Positive complete support, integer loops, wide degree variation.
        for i in range(5):
            for j in range(i,5):
                w[i][j] = w[j][i] = rng.choice([1,2,3,10,100,1000])
        x = calculate(w)
        d,W = x['degrees'],x['total']
        for u in range(5):
            for v in range(u+1,5):
                other = [i for i in range(5) if i != v]
                lap = [[sum(w[i][k] for k in range(5) if k != i) if i==j else -w[i][j]
                        for j in other] for i in other]
                inv = inverse(lap)
                k = [[F(0)]*5 for _ in range(5)]
                for a,i in enumerate(other):
                    for b,j in enumerate(other):
                        k[i][j] = inv[a][b]
                R = k[u][u]
                h = [k[i][u]/R for i in range(5)]
                p = sum(d[i]*h[i] for i in range(5))/W
                hw,groups = lump(w,(u,v))
                y = calculate(hw)
                for a,ga in enumerate(groups):
                    for b,gb in enumerate(groups):
                        for i in ga:
                            for j in gb:
                                assert y['dev'][a][b] == x['dev'][i][j]+W*R*(h[i]-p)*(h[j]-p)
                c = next(a for a,g in enumerate(groups) if len(g)==2)
                assert max(y['dev'][c]) <= x['tmix']
                rat = y['tmix']/x['tmix']
                maxratio = max(maxratio,rat)
                # A finite observed inequality, not a general proof.
                assert rat <= 2
                count += 1
    print(f'Exact random-chain audit: 120 originals, {count} pair quotients, max ratio={float(maxratio):.12f}')
    search_checks = []
    for name in ('search5_best.json','search5_de_best.json'):
        rec = json.load(open(name))
        w = [[F(v) for v in row] for row in rec['weights']]
        x = calculate(w)
        hw,groups = lump(w,rec['pair'])
        y = calculate(hw)
        assert x['tmix'] == F(rec['original'])
        assert y['tmix'] == F(rec['quotient'])
        # Recheck every possible pair, not only the pair selected in search.
        ratios = []
        for u in range(5):
            for v in range(u+1,5):
                hy,_ = lump(w,(u,v))
                ratios.append((calculate(hy)['tmix']/x['tmix'],[u,v]))
        best = max(ratios)
        besthw,_ = lump(w,best[1])
        besty = calculate(besthw)
        search_checks.append(dict(file=name,original=x['tmix'],quotient=besty['tmix'],
                                  selected_ratio=y['tmix']/x['tmix'],
                                  ratio=best[0],best_pair=best[1]))
        if name == 'search5_de_best.json':
            save_json('audited_search5_best.json',dict(weights=w,pair=best[1],
                      original=x['tmix'],quotient=besty['tmix'],ratio=best[0],
                      original_pairs=x['pairs'],quotient_pairs=besty['pairs']))
        print(f'{name}: selected ratio={float(y["tmix"]/x["tmix"]):.14f}, exact all-pairs ratio={float(best[0]):.14f}, pair={best[1]}, X={float(x["tmix"]):.14f}, hX={float(besty["tmix"]):.14f}')
    mp.mp.dps = 80
    for m in (2,3,4,5):
        for t in (2,100,1000000):
            w = leaf_family(m,t)
            d = list(map(sum,w))
            n = len(w)
            lap = mp.matrix([[(sum(w[i][k] for k in range(n) if k != i) if i==j else -w[i][j]) /
                              mp.sqrt(mp.mpf(d[i])*d[j]) for j in range(n)] for i in range(n)])
            vals = mp.eigsy(lap,eigvals_only=True)
            r = mp.mpf(m)/(mp.mpf(t)**5+m)
            S = 1+mp.mpf(1)/t+r
            Q = mp.mpf(1)/(t+1)+r*(1+mp.mpf(1)/(t*(t+1)))
            gap = 2*Q/(S+mp.sqrt(S*S-4*Q))
            assert abs(vals[1]-min(gap,mp.mpf(1)/t)) < mp.mpf('1e-65')
    print('Full normalized-Laplacian eigensystems independently match the two-root spectral formula (12 cases).')
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2
    elapsed = time.monotonic()-start
    print(f'audit wall seconds={elapsed:.3f}; peak resident MB={rss:.2f} (macOS units)')
    save_json('audit_results.json',dict(exact_pair_checks=count,random_max_ratio=maxratio,
                                      search_checks=search_checks,wall_seconds=elapsed,
                                      peak_resident_MB=rss))


if __name__ == '__main__':
    main()
