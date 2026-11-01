import argparse,json,time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import core as c
R=Path(__file__).resolve().parents[1]
@lru_cache(None)
def ln_bounds(x):
    if x==1:return F(0),F(0)
    if x<1:
        lo,hi=ln_bounds(1/x);return -hi,-lo
    k=x.numerator.bit_length()-x.denominator.bit_length()
    if x<F(2)**k:k-=1
    y=x/F(2)**k; z=(y-1)/(y+1)
    def series(z):
        val=F(0); power=z
        for j in range(24): val+=2*power/(2*j+1);power*=z*z
        return val,val+2*power/(49*(1-z*z))
    lo,hi=series(z); l2,h2=series(F(1,3))
    return lo+k*l2,hi+k*h2
def bounds(expr):
    lo=hi=F(0)
    for p,v in expr.items():
        a,b=ln_bounds(F(p));lo+=v*(a if v>=0 else b);hi+=v*(b if v>=0 else a)
    return lo,hi
def nn(expr):c.ck(bounds(expr)[0]>=0)
def allref(sp,st):
    Z=st['Z1']+st['Zh'];V=st['V']
    return {s:(z['P'] if not s else V*z['W']/Z if V else F(0)) for s,z in sp.items()}
def singleKL(sp,st):
    value={};A=st['A'];Z=st['Z1']
    for s,z in sp.items():
        if s.bit_count()==1 and z['P']:c.logadd(value,z['P']/A/(z['W']/Z),z['P'])
    return c.plus((value,1))
def seed_stats(table,p):
    sp=c.spectrum(table,p);st=c.stats(sp)
    Kh=c.KL(sp,c.paid_reference(sp,st));Ka=c.KL(sp,allref(sp,st));K1=singleKL(sp,st)
    # Critical A041 joint source: J1+ln2 L1 <= ln4(2Delta-R).
    C=2*(st['I']-st['V'])-st['R']
    rhs=2*(C-st['J1']);lo,hi=bounds(st['L1']);c.ck(hi<=rhs)
    nn(c.plus((Ka,1),(Kh,-1)));nn(K1)
    return sp,st,Kh,Ka,K1
def case(table,p,k):
    sp,st,Kh,Ka,K1=seed_stats(table,p);e=F(1,2**k)
    root=c.spectrum(tuple(1 if not x&1 else table[x>>1] for x in range(2*len(table))),(e,)+p)
    rt=c.stats(root);Q=c.paid_reference(root,rt);Kf=c.KL(root,Q)
    A,M,Z1,Zh=st['A'],st['M'],st['Z1'],st['Zh']
    c.ck(rt['M']==e*(M+(1-e)*A));c.ck(rt['Zh']==e*(Zh+(1-e)*Z1))
    mix={}
    if A and M:
        H=rt['M'];s=(1-e)*A/(M+(1-e)*A);t=(1-e)*Z1/(Zh+(1-e)*Z1)
        c.logadd(mix,s/t,H*s);c.logadd(mix,(1-s)/(1-t),H*(1-s))
    c.ck(Kf==c.plus((Kh,e),(K1,e*(1-e)),(mix,1)))
    # Exact ordinary KL plus rigorous signs for concavity chord and monotonicity.
    nn(c.plus((Ka,e),(Kf,-1)))
    nn(c.plus((Kf,1),(Ka,-e*(1-e)),(Kh,-e*e)))
    nn(c.plus((Kf,1),(Kh,-e)))
    nn(c.plus((c.ln4(st['V']),1),(Ka,-1)))
    # The same low/high likelihood split is checked pointwise on every atom.
    for s,z in root.items():
        if not z['P']:continue
        if s.bit_count()<=1:c.ck(Q[s]==z['P']);continue
        T=s>>1;zs=sp[T]
        if T.bit_count()==1:
            c.ck(s&1);c.ck(z['P']/Q[s]==(zs['P']/zs['W'])*(rt['Zh']/rt['M']))
        else:c.ck(z['P']/Q[s]==(zs['P']/zs['W'])*(rt['Zh']/rt['M']))
    c.ck(sum(Q.values())==1)
def fixtures(pilot):
    laws=((F(1,2),F(1,2)),(F(1,3),F(2,5)))
    for p in laws[:1] if pilot else laws:
        for mask in range(16):
            table=tuple(1 if mask>>s&1 else -1 for s in range(4))
            for k in ((1,) if pilot else (1,2,4,10)):yield table,p,k
    if not pilot:
        for mask in range(256):
            table=tuple(1 if mask>>s&1 else -1 for s in range(8))
            for k in (1,2,4,10):yield table,(F(1,2),)*3,k
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args();total=0
    for table,p,k in fixtures(args.pilot):case(table,p,k);total+=1
    result={'status':'PASS','cases':total,'exact_assertions':c.CHECKS,'runtime_seconds':time.perf_counter()-c.START,'arithmetic':'Fraction physical transform, prime-log identities and rigorous24-term atanh enclosures','helper':'core.py (own prior-stage helper copied unchanged)'}
    (R/'out'/('PILOT.json' if args.pilot else 'CHECKS.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
