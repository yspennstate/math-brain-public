import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
import itertools,time,json
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R.parent/'20261014T094139Z-fleet05-A091-composition-referee'/'code'))
import exact as e
def ent(xs):return e.add(*[(-x,e.logform(x)) for x in xs if x])
def phi(x,y):return e.add((1,ent((x,y))),(-1,ent((x+y,))))
def charsum(t,s):return Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)),len(t))
pool=[tuple(1 if k>>x&1 else -1 for x in range(2)) for k in range(4)]
start=time.perf_counter();cases=zeros=0
for u,v,g in itertools.product(pool,repeat=3):
    for at in ((0,0,0,0),(0,1,1,0),(0,1,1,1),(1,1,1,1)):
        # Y=bit0,A=bits1,2,B=bit3; u/v/G each have one physical bit.
        t=tuple(g[(x>>6)&1] if not x&1 else (u[(x>>4)&1] if at[(x>>1)&3] else (v[(x>>5)&1] if x&8 else g[(x>>6)&1])) for x in range(128))
        f=tuple(charsum(t,s) for s in range(128));pp=tuple(x*x for x in f)
        actual=e.add(*[(1,phi(pp[s],pp[s+8])) for s in range(128) if not s&8])
        a=Q(sum(at),4);c=1-a;q=Q(1,2);m,n,z=[Q(sum(x),2) for x in (u,v,g)]
        M=1-n*z;delta=n-z;K=a*m+c*((1-q)*z+q*n);w=q*c*delta
        rhs=e.add((1,{2:(q-2*q*q)*c*M+q*q*c*(1-n*n)}),(a*c*(1-z*z)/2,phi((1-q)**2,q*q)),(a*c/2,phi((m-z-q*delta)**2,q*q*delta*delta)),((1-z*z)/4,phi((1+c*(1-q))**2,q*q*c*c)),((1-z*z)/4,phi((1-c*(1-q))**2,q*q*c*c)),(Q(1,4),phi((z+K)**2,w*w)),(Q(1,4),phi((K-z)**2,w*w)))
        e.check(actual,{k:v for k,v in rhs.items() if v})
        d=Q(sum(t[x]!=t[x^8] for x in range(128)),128)
        e.check(d,q*c*M/2);zeros+=d==0;cases+=1
        if time.perf_counter()-start>55:raise RuntimeError('frozen watchdog')
out={'status':'PASS','cases':cases,'zero_influence_cases':zeros,'exact_assertions':e.COUNT,'seconds':time.perf_counter()-start,'method':'direct physical tables and character sums; no imported FWHT, local query, compose, grouped formula implementation'}
(R/'out/REPRODUCE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
