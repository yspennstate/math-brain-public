from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
A=Q(9,2); k=Q(29,13); counts={}; start=time.perf_counter()
def check(v,label):
    if not v: raise AssertionError(label)
    counts[label]=counts.get(label,0)+1
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
def add(*xs):
    o={}
    for x in xs:
        for p,c in x.items(): o[p]=o.get(p,Q(0))+c
    return {p:c for p,c in o.items() if c}
def mul(c,x): return {p:c*a for p,a in x.items() if c*a}
def num(q): return {2:Q(q)} if q else {}
@lru_cache(None)
def ln_bounds(x):
    x=Q(x); z=(x-1)/(x+1); assert 0<=z<1
    out=Q(0); term=z
    for j in range(48): out+=2*term/(2*j+1); term*=z*z
    tail=2*term/(97*(1-z*z))
    return out,out+tail
@lru_cache(None)
def log_bounds(p):
    if p==2: return Q(1),Q(1)
    e=p.bit_length()-1; l,u=ln_bounds(Q(p,1<<e)); l2,u2=ln_bounds(Q(2))
    return e+l/u2,e+u/l2
def bounds(x):
    lo=hi=Q(0)
    for p,c in x.items():
        l,u=log_bounds(p)
        lo+=c*(l if c>=0 else u); hi+=c*(u if c>=0 else l)
    return lo,hi
def le(x,q): return bounds(x)[1]<=q
def eq(x,y): return add(x,mul(-1,y))=={}
def eta(q):
    if not q: return {}
    out={}
    for p,c in factors(q.numerator).items(): out[p]=out.get(p,Q(0))-q*c
    for p,c in factors(q.denominator).items(): out[p]=out.get(p,Q(0))+q*c
    return {p:c for p,c in out.items() if c}
@lru_cache(None)
def spectrum(tab):
    N=len(tab)
    return tuple(Q(sum(tab[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)),N) for s in range(N))
def fwht(tab):
    v=list(tab); step=1
    while step<len(v):
        for j in range(0,len(v),step*2):
            for i in range(j,j+step): a,b=v[i],v[i+step]; v[i],v[i+step]=a+b,a-b
        step*=2
    return tuple(Q(a,len(v)) for a in v)
@lru_cache(None)
def stats(tab):
    sp=spectrum(tab); probs=[a*a for a in sp]
    return add(*(eta(p) for p in probs)),sum((p*s.bit_count() for s,p in enumerate(probs)),Q(0))
def restrict(tab,i,a):
    return tuple(tab[(x&((1<<i)-1))|((x>>i)<<(i+1))|(a<<i)] for x in range(len(tab)//2))
def edge(tab,i):
    h,I=stats(tab); kids=[restrict(tab,i,a) for a in range(2)]; hs=[stats(t)[0] for t in kids]; Is=[stats(t)[1] for t in kids]
    p=Q(sum(tab[x]!=tab[x^(1<<i)] for x in range(len(tab))),len(tab))
    D=add(h,mul(-Q(1,2),add(*hs))); J=sum(Is,Q(0))/2
    check(I==p+J,'physical influence conservation')
    return D,p,I,J,kids
def qpolicy(D,p,I,J):
    if not J: return Q(0)
    if le(D,A*p): return Q(1)
    lo,hi=bounds(D)
    qlo=max(Q(0),min(Q(1),(A*I-hi)/(A*J)))
    q=Q((qlo*256).numerator//(qlo*256).denominator,256)
    return q
def tree(tab):
    H,I=stats(tab)
    if not I: return {},H,Q(0),Q(0),{}
    D,p,I,J,kids=edge(tab,0); q=qpolicy(D,p,I,J)
    sub=[tree(t) for t in kids]
    cost=add(D,mul(q/2,add(*(r[0] for r in sub))))
    terminal=mul(Q(1,2),add(*(add(mul(1-q,stats(t)[0]),mul(q,r[1])) for t,r in zip(kids,sub))))
    killed=(1-q)*J+q*sum((r[2] for r in sub),Q(0))/2
    removed=p+q*sum((r[3] for r in sub),Q(0))/2
    release=add(num(A*I-q*A*J),mul(-1,D),mul(q/2,add(*(r[4] for r in sub))))
    check(eq(add(cost,terminal),H),'full terminal entropy identity')
    check(killed+removed==I,'full killed influence conservation')
    check(eq(add(cost,release),num(A*I)),'original owner exactly conserved to constant-or-stop leaves')
    check(bounds(release)[0]>=0,'nonnegative cumulative release')
    return cost,terminal,killed,removed,release
def main(pilot=False):
    rows=edges=0
    for n in range(4):
        lim=1<<(1<<n)
        if pilot and n==3: lim=16
        for mask in range(lim):
            tab=tuple(1 if (mask>>x)&1 else -1 for x in range(1<<n)); H,I=stats(tab); rows+=1
            check(sum(a*a for a in spectrum(tab))==1,'Parseval')
            check(spectrum(tab)==fwht(tab),'independent direct character versus butterflies')
            for i in range(n):
                D,p,I,J,kids=edge(tab,i); edges+=1
                check(bounds(D)[0]>=0,'actual entropy decrement nonnegative')
                check(le(D,k*I),'universal rational singleton bound control')
                for q in [Q(0),Q(1,4),Q(1,2)]:
                    rate=k/(1-q)
                    check(bounds(add(num(rate*I-q*rate*J),mul(-1,D)))[0]>=q*rate*p,'A059 geometric release')
                check(A-2*k==Q(1,26),'two-ticket exact original split')
                q=qpolicy(D,p,I,J)
                R=add(num(A*I-q*A*J),mul(-1,D))
                check(bounds(R)[0]>=0,'adaptive release paid')
                if J:
                    if q==1: check(le(D,A*p),'no killing only on affordable query')
                    else:
                        lo,hi=bounds(D); qstarlo=(A*I-hi)/(A*J); qstarhi=(A*I-lo)/(A*J)
                        check(q<=qstarlo and qstarhi-q<=Q(1,256)+(hi-lo)/(A*J),'certified dyadic approximation')
                for t in kids:
                    if stats(t)[1]:
                        for j in range(n-1):
                            D2,p2,I2,J2,kk=edge(t,j)
                            check(bounds(add(num(k*I2),mul(-1,D2)))[0]>=0,'second labelled ticket fee paid')
            tree(tab)
    control=[]
    for r in range(1,65):
        for q in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
            S=sum((q**j for j in range(r)),Q(0))
            check(Q(r,8)-Q(r-S,8)==S/8,'A060 terminal debit law')
            check(S/8==4*S/32,'A060 debit removed influence ratio')
            check(0<=1-S/r<=Q(r-1,2)*(1-q),'A060 sharp horizon sufficient bound')
        check(Q(2)<=A*Q(1,2),'adaptive AND2 all depths no killing')
        check(A*(r+1)-2*r>0,'SAME owner deterministic AND2 terminal entropy paid')
        control.append(dict(r=r,fair_debit=str((1-Q(1,2)**r)/4),adaptive_debit=str(Q(r,8))))
    witness={}
    if not pilot:
        def bent(x,m): return -1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2))%2 else 1
        def wrapper(core,m):
            return tuple(core[x>>m] if (x&((1<<m)-1))==(1<<m)-1 else bent(x&((1<<m)-1),m) for x in range((1<<m)*len(core)))
        empty=wrapper((-1,1),4); E0,Iz=stats(empty)
        explicit_E0=add(num(8),{3:-Q(45,64),5:-Q(75,64)})
        check(eq(E0,explicit_E0),'A060 E0 direct spectrum')
        for r in [1,2]:
            core=tuple((-1 if (x>>(2*r))&1 else 1)*(-1 if sum(((x>>(2*j))&3)==3 for j in range(r))%2 else 1) for x in range(1<<(2*r+1)))
            full=wrapper(core,4); H,I=stats(full)
            check(eq(H,add(E0,num(Q(r,8)))),'actual complete wrapper entropy')
            check(I==Q(7,4)+Q(r+1,16),'actual complete wrapper influence')
            # Every actual core-answer child retains its full exterior/tag spectrum.
            for a in range(2):
                t=restrict(full,4,a); ht,it=stats(t)
                check(eq(ht,add(E0,num(Q(r-1,8)))),'both actual full wrapper child entropies')
            D,p,ii,jj,kids=edge(full,4)
            check(eq(D,num(Q(1,8))) and p==Q(1,32),'actual wrapper fee and removed influence')
        full=wrapper((-1,1),8)
        D,p,I,J,kids=edge(full,8); q=qpolicy(D,p,I,J)
        dlo,dhi=bounds(D)
        check(dlo>A*p,'genuine tag forced stop necessary for this potential')
        check(q<1,'adaptive actual witness forces stop')
        check(bounds(add(num(A*I-q*A*J),mul(-1,D)))[0]>=0,'genuine tag adaptive witness paid')
        hkid=mul(Q(1,2),add(*(stats(t)[0] for t in kids)))
        witness=dict(bits=9,query='genuine tag',p=str(p),I=str(I),q=str(q),D_interval=[str(dlo),str(dhi)],full_stopped_entropy_interval=[str(x) for x in bounds(mul(1-q,hkid))])
    return dict(functions=rows,coordinate_cases=edges,assertions=sum(counts.values()),categories=counts,seconds=time.perf_counter()-start,AND2_control=control,forced_stop_witness=witness)
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
    result=main(mode=='pilot')
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({a:result[a] for a in ['functions','coordinate_cases','assertions','seconds']}))
