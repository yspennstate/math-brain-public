import time, numpy as np
from feicore import *
polite()
rows = []
def rep(name, tt, n):
    t=time.time(); s = summary(tt, n, tree=(n<=9)); dt=time.time()-t
    print(f"{name:28s} n={n:2d} H={s['H']:.5f} I={s['I']:.5f} H/I={s['HI']:.4f} HC/I={s['HC']:.4f} ({dt:.1f}s)" + (f" tree={s.get('tree')}" if n<=6 else ''), flush=True)
# controls
rep('dictator', np.array([1,-1],dtype=np.int8).repeat(1), 1) if False else None
rep('AND2', and_n(2), 2)
rep('AND3', and_n(3), 3)
rep('AND8', and_n(8), 8)
rep('AND12', and_n(12), 12)
for n in (3,5,7,9,11,13):
    rep(f'Maj{n}', majority(n), n)
rep('recmaj d2', recmaj3(2), 9)
for (w,s) in [(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,2),(3,3),(3,4),(4,2),(4,3)]:
    rep(f'tribes w{w} s{s}', tribes(w,s), w*s)
for m in (2,4,6,8,10,12):
    rep(f'bent{m}', bent(m), m)
for k in (1,2,3):
    rep(f'addr{k}', addressing(k), k+(1<<k))
