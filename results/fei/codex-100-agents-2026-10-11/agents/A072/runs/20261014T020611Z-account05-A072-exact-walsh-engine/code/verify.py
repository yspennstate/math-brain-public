import sys, json, time, math, importlib.util
from pathlib import Path
from fractions import Fraction as Q
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
old=ROOT.parent/'20261013T222130Z-account05-A072-exact-walsh-engine/code/check.py'
sp=importlib.util.spec_from_file_location('prior',old); e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
B=e.BASE
H=tuple(-1 if x in (0,1,2,4,8,16,32,6,17,40) else 1 for x in range(64))
J=tuple(-H[x^1] for x in range(64))
def dump(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2,default=str)+'\n',encoding='utf-8')
def log(x):
    a,b=e.logint(x.numerator);c,d=e.logint(x.denominator)
    return Q(a-d,e.SCALE),Q(b-c,e.SCALE)
def ent(s):
    lo=hi=Q(0)
    for x in s:
        if x:
            a,b=log(x);lo-=x*b;hi-=x*a
    return lo,hi
def fast(table):
    n=B.validate(table);N=len(table);W=B.fwht(table)
    assert sum(w*w for w in W)==N*N
    assert B.fwht(W)==[N*x for x in table]
    edges=[sum(table[x]!=table[x^(1<<i)] for x in range(N) if not x>>i&1) for i in range(n)]
    inf=[Q(2*z,N) for z in edges]
    assert inf==[sum((Q(W[s]**2,N*N) for s in range(N) if s>>i&1),Q(0)) for i in range(n)]
    return W,inf,edges
def grid(p):
    bc=B.biased_certificate(J,(p,)*6);s=bc['spectrum'];qs=bc['pivotal_probabilities'];v=4*p*(1-p)
    assert sum(qs)>=Q(11,4)
    assert all(min(q,1-q)<=5*p for q in qs)
    sigma=4*p-10*p*p+18*p**3-19*p**4+10*p**5-2*p**6
    actual=sum((p**x.bit_count()*(1-p)**(6-x.bit_count()) for x in range(64) if J[x]<0),Q(0))
    assert actual==sigma and 3*p<sigma<4*p
    terminal=e.subtract(ent(s),tuple(sum(qs)*x for x in ent((1-v,v))))
    upper=120*p*p*(Q(3,2)-log(5*p)[0])
    assert terminal[1]<upper
    rows=[];t=4*p*p;m=1-2*p
    for j,q in enumerate(qs):
        cost=e.phi(m*m,t);mlo=mhi=Q(0)
        for S in range(64):
            if not S>>j&1:
                a,b=e.phi(s[S],t*s[S|(1<<j)]/v);mlo+=a;mhi+=b
        r=e.subtract((mlo,mhi),tuple(q*x for x in cost))
        loss_cap=2*p*(Q(3,2)-log(4*p*p)[0])
        assert r[0]/(q*2*p)>-loss_cap
        rows.append({'block':j,'q':q,'reserve_bounds':r})
    dump('bias_'+str(p.denominator)+'.json',{'p':p,'sigma':sigma,'spectrum':s,'q':qs,'reserve_rows':rows,'terminal_bounds':terminal,'terminal_upper_cap':upper})
def compose(mask):
    g=tuple(1-2*((mask>>x)&1) for x in range(4));gc=B.uniform_certificate(g)
    p=Q(sum(x<0 for x in g),4);bc=B.biased_certificate(J,(p,)*6)
    table=tuple(J[sum((g[(x>>(2*j))&3]<0)<<j for j in range(6))] for x in range(4096))
    W,inf,edges=fast(table)
    for s in range(4096):
        occupied=0;prod=Q(1)
        for j in range(6):
            sub=(s>>(2*j))&3
            if sub:occupied|=1<<j;prod*=Q(-gc['walsh'][sub],8)
        predicted=bc['centered_coefficients'][occupied]*prod
        assert predicted==Q(W[s],4096)
    qs=bc['pivotal_probabilities']
    assert inf==[qs[j]*gc['influences'][i] for j in range(6) for i in range(2)]
    dump('composition_'+str(mask)+'.json',{'core_mask':mask,'p':p,'walsh':W,'edges':edges,'influences':inf,'coefficient_matches':4096,'parseval':True,'sign_inverse':True})
def main():
    pilot='--pilot' in sys.argv;start=time.perf_counter();cap=55 if pilot else 120
    gate=B.uniform_certificate(J)
    counts=[sum(J[x]<0 and x.bit_count()==k for x in range(64)) for k in range(7)]
    assert counts==[0,4,10,18,15,6,1]
    pivotal=[j for j in range(6) if J[0]!=J[1<<j]]
    assert len(pivotal)==4
    dump('gate.json',{'negative_weight_counts':counts,'dominant_pivotal_directions':pivotal,'uniform_certificate':gate})
    for d in ([16] if pilot else [16,32,64,128,256]):
        grid(Q(1,d));assert time.perf_counter()-start<cap
    for mask in ([1] if pilot else [1,14,6,10]):
        compose(mask);assert time.perf_counter()-start<cap
    dump('pilot.json' if pilot else 'validation.json',{'passed':True,'biases':1 if pilot else 5,'reserves':6 if pilot else 30,'compositions':1 if pilot else 4,'coefficient_matches':4096 if pilot else 16384,'runtime_seconds':time.perf_counter()-start})
    print(json.dumps({'passed':True,'pilot':pilot,'runtime_seconds':time.perf_counter()-start}))
if __name__=='__main__':main()
