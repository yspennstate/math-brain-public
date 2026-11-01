"""On sampled K2 functions (same sampler as validate_relax.py): compute H - c*I exactly-ish (floats) and
Phi = sum_T w_T ebar_T with ebar_T = delta L + 2 kappa (1 - log2 nu') - sum G_i - c|T| (G at alpha = m).
Check H - c*I <= Phi + 1e-12 and Phi <= 1e-12."""
import sys, math, random, itertools
import numpy as np
from collections import defaultdict
sys.path.insert(0, ".")
import rows_v2 as RV, check_identity as CI
C = 16/3 - 1.5*math.log2(3); KAP = C/2 - 1; DEL = 2 - C/2
def h(t): return 0.0 if t<=0 or t>=1 else -t*math.log2(t)-(1-t)*math.log2(1-t)
def G(p,q):
    S=p*p+q*q; s=math.log2(S); m=q*q/S
    return KAP*(s-2)+C*m-h(m)
def run(m, pkl=None):
    rows = RV.product_rows(m, pkl); N = 1<<m; Hm = RV.hadamard(m)
    half, two = RV.masks_arr(rows, m)
    by_half = defaultdict(list)
    for i in range(len(rows)): by_half[int(half[i])].append(i)
    full=(1<<N)-1; rng=random.Random(7); worst_gap=-1e9; worst_phi=-1e9; cnt=0
    info = {}
    for r0i in RV.orbit_reps(rows, m):
        r0=rows[r0i]; h0=int(half[r0i]); z0=full&~h0&~int(two[r0i])
        cand=[ci for ci in by_half.get(h0,[]) if not (int(two[ci])&~z0)]
        bt=defaultdict(list)
        for ci in cand: bt[int(two[ci])].append(ci)
        keys=list(bt); hp=[x for x in range(N) if h0>>x&1]
        combos=[(S1,S2,z0&~S1&~S2) for S1 in keys for S2 in keys if not (S2 & ~(z0&~S1)) and (z0&~S1&~S2) in bt]
        if len(combos)>150: combos=rng.sample(combos,150)
        for S1,S2,S3 in combos:
            for _ in range(20):
                rr=(r0,rows[rng.choice(bt[S1])],rows[rng.choice(bt[S2])],rows[rng.choice(bt[S3])])
                if any(rr[0][x]*rr[1][x]*rr[2][x]*rr[3][x]!=-1 for x in hp): continue
                Hs=0.0; Is=0.0; Phi=0.0
                for T in range(4):
                    V=np.array(rr[T]); w=(V*V).sum()/(4.0*N)
                    if w==0: continue
                    W=Hm@V; Q=(W*W).astype(float); Q/=Q.sum()
                    Hq=-sum(x*math.log2(x) for x in Q if x>0)
                    Iq=sum(Q[U]*bin(U).count("1") for U in range(N))
                    t=[0,1,1,2][T]
                    Hs+=w*(-math.log2(w)+Hq); Is+=w*(t+Iq)
                    key=rr[T]
                    if key not in info: info[key]=CI.analyse(key,m)
                    r,pq,nup,odd=info[key]
                    eb=DEL*(-math.log2(w))+2*KAP*(1-math.log2(nup))-sum(G(p,q) for p,q in pq if (p,q)!=(1,1))-C*t
                    Phi+=w*eb
                cnt+=1
                worst_gap=max(worst_gap,(Hs-C*Is)-Phi); worst_phi=max(worst_phi,Phi)
    print("m",m,"functions",cnt,"max (H-c*I) - Phi =",worst_gap,"(must be <= 0)  max Phi =",worst_phi,"(must be <= 0)")
run(3); run(4,"../data/prod3_wide.pkl")
