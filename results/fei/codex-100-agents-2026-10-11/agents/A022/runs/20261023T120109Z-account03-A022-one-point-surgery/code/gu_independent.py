"""Distinct GU representation; direct characters AND direct upper-set summation.
Shares only the standalone replay's separately written rational-log primitives.
No production exact.py/FWHT/zeta code is imported.
"""
from pathlib import Path
prefix=(Path(__file__).with_name('independent.py')).read_text(encoding='utf-8').split('\nstart=time.monotonic()')[0]
exec(compile(prefix,'independent.py arithmetic prefix','exec'))
@lru_cache(None)
def upper(a):
    P=spectrum(a)
    return add(*(times(log(sum(P[T] for T in range(len(P)) if T&S==S)/p),p) for S,p in enumerate(P) if p))
def cut(a,i,b):return tuple(x for z,x in enumerate(a) if z>>i&1==b)
def drift(a,coordinates):
    return add(*(add(upper(a),times(add(upper(cut(a,i,0)),upper(cut(a,i,1))),-F(1,2))) for i in coordinates))
def influence(a,coordinates):return sum(F(sum(x!=a[z^(1<<i)] for z,x in enumerate(a)),len(a)) for i in coordinates)
start=time.monotonic();fixtures=[(0,(-1,1,1,1)),(63,(-1,1,-1,1)),(0,(1,1,1,1)),(63,(-1,-1,-1,1))]
for v,a in fixtures:
    delta=F(1,64);k=6;seed=tuple((-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1) for x in range(64))
    f=tuple(seed[x]*(a[z] if x==v else 1) for z in range(4) for x in range(64))
    Ua=upper(a);Ga=drift(a,range(2));Id=influence(f,range(k));Ia=influence(a,range(2))
    # Direct paired spectrum and all upward rows, rather than the producer zeta.
    amps=chars(seed);s=F(sum(a),4)
    pp=tuple((c+delta*seed[v]*(-1 if (S&v).bit_count()%2 else 1)*(s-1))**2 for S,c in enumerate(amps))
    ee=add(*(times(log(sum(pp[T]+delta*delta*(1-s*s) for T in range(64) if T&S==S)/p),p) for S,p in enumerate(pp) if p))
    ph=times(log(s*s),-s*s) if s else {}
    Qb=add(ee,times(ph,-delta),num(delta*k*(1-s*s)/2))
    same(upper(f),add(times(Ua,delta),Qb))
    gd=drift(f,range(6));gc=drift(f,range(6,8))
    ge(add(num(198),times(gd,-1)));ge(add(times(Ga,delta),num(6*delta*Ia+F(21,2)),times(gc,-1)))
    ge(add(times(Ga,delta),num(6*delta*Ia+256*Id),times(add(gd,gc),-1)))
    for i in range(k):
        qchild=add(upper(cut(f,i,v>>i&1)),times(Ua,-2*delta),times(upper(cut(seed,i,v>>i&1)),-1))
        ge(add(num(20),qchild));ge(add(num(20),times(qchild,-1)))
    assert time.monotonic()-start<120
out={'status':'PASS','cases':4,'assertions':tests,'elapsed_seconds':time.monotonic()-start,'representation':'direct character sums/direct upward sums/separate48-term log enclosure','review':'author reconstruction; shared standalone arithmetic only, not external review'}
(ROOT/'out/gu_independent.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
