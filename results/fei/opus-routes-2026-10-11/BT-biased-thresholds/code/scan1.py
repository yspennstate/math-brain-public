import numpy as np, math, time, json
import mpmath as mp
from biased import ltf_table, metrics
from levels import spectrum_2groups, spectrum_1group
mp.mp.dps = 40
# 1. cross-check against brute force: weights (2,2,1,1,1) theta 4, biases q0 on group0 (weight 2), q1 on group1
q0, q1 = 0.3, 0.15
T = ltf_table([2,2,1,1,1], 4)
m = metrics(T, [q0,q0,q1,q1,q1])
s = spectrum_2groups(lambda a,b: int(2*a+b>=4), 2, q0, 3, q1)
print('check', m['E'], s['E'], m['I'], s['I'], m['V'], s['V'], s['parseval_err'])
# 2. symmetric thresholds T_{t,m} under bias p: max ratio over t, p for m up to 40
t0=time.time()
res=[]
for mm in [2,3,4,6,8,12,16,24,32,40]:
    best=(0,None)
    for t in range(1, mm+1):
        for p in [0.5,0.3,0.1,0.03,0.01,0.001,0.7,0.9,0.97,0.99,0.999]:
            r = spectrum_1group(lambda a: int(a>=t), mm, p)
            if r['ratio_HD']==r['ratio_HD'] and r['ratio_HD']>best[0]:
                best=(r['ratio_HD'],(t,p))
    res.append((mm,best))
    print('sym m',mm,'best H+/Delta',round(best[0],4),best[1], round(time.time()-t0,1),'s',flush=True)
