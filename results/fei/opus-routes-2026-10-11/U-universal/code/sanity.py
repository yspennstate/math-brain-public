import numpy as np
from feilib import *

def tab(fn, n):
    t=[]
    for x in range(1<<n):
        xs=[1-2*((x>>i)&1) for i in range(n)]
        t.append(fn(xs))
    return np.array(t)

# addressing a=1: f(z,y1,y2) = y1 if z=+1 else y2
f = tab(lambda v: v[1] if v[0]==1 else v[2], 3)
s = summary(f); print('addr a=1', round(s['H'],6), round(s['I'],6))
f = tab(lambda v: (v[2+ (1 if v[0]==-1 else 0) + (2 if v[1]==-1 else 0)]), 6)
s = summary(f); print('addr a=2', round(s['H'],6), round(s['I'],6))
for r in [3,6,10]:
    f = tab(lambda v: -1 if all(x==1 for x in v) else 1, r)
    s=summary(f); print('pointdefect r',r, s['H']/s['I'], s['B']/s['I'])
f = tab(lambda v: 1 if sum(v)>0 else -1, 5)
s=summary(f); print('maj5', s['H'], s['I'], s['B'], s['DTC'])
print(exact_total_influence(tab(lambda v: 1 if sum(v)>0 else -1,5)))
