import mpmath as mp
from tower_recompute import PM, T, dual, table
from tower_recompute_mp import compose
mp.mp.dps = 40
g = {"M": PM(3), "D": dual(PM(3)), "P": PM(4), "Pd": dual(PM(4)), "T26": T(2, 6), "T35": T(3, 5), "T36": T(3, 6)}
tab = {k: (table(*v), v[1]) for k, v in g.items()}
words = ["D,M,M,M,M,M,M,M,M,Pd,M,M,T35", "M,D,D,D,D,D,D,D,D,P,P,T26", "D,M,M,M,M,M,M,M,M,Pd,T26"]
for w in words:
    st = (mp.mpf(0), mp.mpf(0), mp.mpf(1), mp.mpf(0), mp.mpf(1))
    for name in w.split(","):
        st, r, err = compose(st, *tab[name])
    print(f"{w}: {mp.nstr(r, 25)}  mean {mp.nstr(st[0], 8)}  err {mp.nstr(err, 3)}", flush=True)
