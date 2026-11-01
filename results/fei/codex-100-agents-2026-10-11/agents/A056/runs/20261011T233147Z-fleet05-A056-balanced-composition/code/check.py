from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from math import lcm
import json,time,sys
RUN=Path(__file__).resolve().parents[1]
def add(a,b,c=Q(1)):
    out=a.copy()
    for k,z in b.items(): out[k]=out.get(k,Q(0))+c*z
    return {k:z for k,z in out.items() if z}
def scale(a,c): return add({},a,c)
@lru_cache(None)
def factors(n):
    d=2; out={}
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out
@lru_cache(None)
def logq(z):
    if z<=0: raise ValueError(z)
    return add({k:Q(e) for k,e in factors(z.numerator).items()},
               {k:Q(e) for k,e in factors(z.denominator).items()},Q(-1))
@lru_cache(None)
def phi(z): return {} if not z else scale(logq(z),-z)
def E(s,t): return add(add(phi(s),phi(t)),phi(s+t),Q(-1))
def D(a,b):
    return add(add(phi(a*a),phi(b*b)),add(phi((a+b)**2),phi((a-b)**2)),Q(-1,2))
def J(a,b): return add(D(a,b),E(a*a,b*b),Q(-1))
def sign(a):
    if not a: return 0
    denom=lcm(*(z.denominator for z in a.values()))
    lhs=rhs=1
    for p,z in a.items():
        e=int(z*denom)
        if e>0: lhs*=p**e
        else: rhs*=p**(-e)
    return (lhs>rhs)-(lhs<rhs)
def serialize(a): return {str(k):str(z) for k,z in sorted(a.items())}
@lru_cache(None)
def table(n,c): return tuple(1 if (c>>x)&1 else -1 for x in range(1<<n))
@lru_cache(None)
def walsh(g):
    return tuple(Q(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(g)),len(g)) for s in range(len(g)))
def spectrum_entropy(g):
    out={}
    for z in walsh(g): out=add(out,phi(z*z))
    return out
def erase(g,i):
    a=walsh(g); out={}
    for u in range(len(a)):
        if not (u>>i)&1: out=add(out,E(a[u]**2,a[u|(1<<i)]**2))
    return out
def dec(g,i):
    a=walsh(g); out={}
    for u in range(len(a)):
        if not (u>>i)&1: out=add(out,D(a[u],a[u|(1<<i)]))
    # Independent truth-table restriction verification of the decrement.
    free=[j for j in range(len(g).bit_length()-1) if j!=i]
    children=[]
    for value in [0,1]:
        t=[]
        for x in range(1<<len(free)):
            idx=value<<i
            for pos,j in enumerate(free): idx|=((x>>pos)&1)<<j
            t.append(g[idx])
        children.append(tuple(t))
    independent=add(spectrum_entropy(g),add(spectrum_entropy(children[0]),spectrum_entropy(children[1])),Q(-1,2))
    assert out==independent
    return out
def inf(g,i): return sum((z*z for u,z in enumerate(walsh(g)) if (u>>i)&1),Q(0))
@lru_cache(None)
def composed(h,a,b):
    return tuple(h[int(a[x&3]==-1)+2*int(b[x>>2]==-1)] for x in range(16))
def test(h,child,other,i,j=0):
    aa=walsh(child); m=aa[0]; v=1-m*m; beta=aa[1<<i]; t=beta*beta
    mo=walsh(other)[0]; vo=1-mo*mo; hh=walsh(h)
    # Expand h=A+y_j B and then center the other output.
    oj=1-j
    A0=hh[0]; A1=hh[1<<oj]; B0=hh[1<<j]; B1=hh[3]
    d=[B0+mo*B1,B1]; c=[A0+mo*A1+m*d[0],A1+m*d[1]]
    weights=[Q(1),vo]
    q=sum((w*z*z for w,z in zip(weights,d)),Q(0))
    M={}; N={}; Mv={}
    for w,cc,dd in zip(weights,c,d):
        M=add(M,E(cc*cc,t*dd*dd),w)
        N=add(N,J(cc,beta*dd),w)
        Mv=add(Mv,E(cc*cc,v*dd*dd),w)
    Bc=erase(child,i); Dc=dec(child,i)
    emptyB=E(m*m,t); emptyD=D(m,beta); emptyJ=J(m,beta)
    Bstar=add(Bc,emptyB,Q(-1)); Dstar=add(Dc,emptyD,Q(-1))
    L=add(M,emptyB,-q); K=add(N,emptyJ,-q)
    f=composed(h,child,other) if j==0 else composed(h,other,child)
    phys=i+2*j
    Bf=erase(f,phys); Df=dec(f,phys)
    assert Bf==add(scale(Bc,q),L)
    assert Bf==add(scale(Bstar,q),M)
    assert Df==add(add(scale(Dc,q),L),K)
    assert Df==add(scale(Dstar,q),add(M,N))
    assert inf(f,phys)==q*inf(child,i)
    assert sign(Bstar)>=0 and sign(Dstar)>=0 and sign(M)>=0 and sign(N)>=0
    assert sign(add({2:4*q*t},N,Q(-1)))>=0
    if v:
        assert t<=v
        assert sign(add(Mv,M,Q(-1)))>=0
        envelope=scale(Mv,t/v)
        if t: envelope=add(envelope,logq(v/t),q*t)
        assert sign(add(envelope,M,Q(-1)))>=0
    else:
        assert t==0 and not M and not N and not Bf and not Df
    return {'mean':str(m),'variance':str(v),'beta':str(beta),'q':str(q),
            'B_F':serialize(Bf),'D_F':serialize(Df),'L_signed':serialize(L),'J_signed':serialize(K),
            'M_positive':serialize(M),'N_positive':serialize(N),'B_child_empty':serialize(emptyB),
            'D_child_empty':serialize(emptyD),'I_coordinate_F':str(inf(f,phys)),
            'L_sign':sign(L),'J_sign':sign(K)}
def main():
    start=time.perf_counter(); pilot='--pilot' in sys.argv
    count=0; negativeL=negativeJ=0; firstL=firstJ=None
    for hc in range(16):
        for ac in (range(1) if pilot else range(16)):
            for bc in (range(1) if pilot else range(16)):
                for j in range(2):
                    for i in range(2):
                        a,b=table(2,ac),table(2,bc)
                        z=test(table(2,hc),a if j==0 else b,b if j==0 else a,i,j)
                        count+=1
                        if z['L_sign']<0:
                            negativeL+=1
                            if firstL is None: firstL={'codes':[hc,ac,bc],'block':j,'coordinate':i,**z}
                        if z['J_sign']<0:
                            negativeJ+=1
                            if firstJ is None: firstJ={'codes':[hc,ac,bc],'block':j,'coordinate':i,**z}
    and2=table(2,1); or2=table(2,7)
    fixtures=[]
    # The physical x=+1 restriction of majority_3 produces OR_2.
    for i in range(2): fixtures.append({'name':'AND(restricted_Maj3,dictator)','i':i,**test(and2,or2,(1,1,-1,-1),i)})
    for i in range(2): fixtures.append({'name':'AND(OR2,OR2)','i':i,**test(and2,or2,or2,i)})
    out={'helper_version':'A056-biased-erasure-v1','pilot':pilot,'physical_splits':count,'fixtures':fixtures,
         'negative_L_cases':negativeL,'negative_J_cases':negativeJ,'first_negative_L':firstL,'first_negative_J':firstJ,
         'all_exact_assertions_passed':True,'runtime_seconds':time.perf_counter()-start}
    (RUN/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:z for k,z in out.items() if k not in ['fixtures','first_negative_L','first_negative_J']},indent=2))
if __name__=='__main__': main()
