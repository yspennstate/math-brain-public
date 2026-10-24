import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
import itertools,time,json
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R.parent/'20261014T094139Z-account05-A091-composition-referee'/'code'))
import exact as e
def entropy(values):return e.add(*[(-x,e.logform(x)) for x in values if x])
def packet(x,y):return e.add((1,entropy((x,y))),(-1,entropy((x+y,))))
def fourier(t):
    return tuple(Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
start=time.perf_counter();cases=0
pool=[tuple(1 if mask>>x&1 else -1 for x in range(2)) for mask in range(4)]
for u,v,g in itertools.product(pool,repeat=3):
    for bt in ((0,0,0,0),(0,1,1,0),(0,1,1,1),(1,1,1,1)):
        # Explicit physical construction independent of source compose/FWHT.
        F=tuple(g[(x>>6)&1] if not x&1 else (u[(x>>4)&1] if x&2 else (v[(x>>5)&1] if bt[(x>>2)&3] else g[(x>>6)&1])) for x in range(128))
        co=fourier(F);pp=tuple(x*x for x in co)
        B=e.add(*[(1,packet(pp[s],pp[s+2])) for s in range(128) if not s&2])
        q=Q(1,2);p=Q(sum(bt),4);c=1-p
        m,n,z=[Q(sum(t),2) for t in (u,v,g)];h=p*n+c*z;M=1-m*h
        S=p*(1-n*n)+p*c*(1-z*z+(n-z)**2)
        L=(1-q)*h+q*m;w=q*(m-h)
        rhs=e.add((1,{2:(q-2*q*q)*M+q*q*(1-m*m)}),(S/2,packet((1-q)**2,q*q)),((1-z*z)/4,packet((1+(1-q)*c)**2,q*q*c*c)),((1-z*z)/4,packet(((1-q)*c-1)**2,q*q*c*c)),(Q(1,4),packet((z+L)**2,w*w)),(Q(1,4),packet((L-z)**2,w*w)))
        # Eliminate explicit zero coefficients in the independent reconstruction.
        e.check(B,{k:x for k,x in rhs.items() if x})
        edges=Q(sum(F[x]!=F[x^2] for x in range(128)),128)
        e.check(edges,q*M/2)
        cases+=1
        if time.perf_counter()-start>55:raise RuntimeError('frozen watchdog')
out={'status':'PASS','cases':cases,'exact_assertions':e.COUNT,'runtime_seconds':time.perf_counter()-start,'method':'direct character sums, explicit physical tables, exact prime-log packet identity; no imported FWHT, compose, local or formula implementation'}
(R/'out'/'REPRODUCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
