"""Exact rational certificate for X096; no floating point enters a sign test."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import json
import sympy as sp

HERE=Path(__file__).resolve().parent
RHO=Q(17,20); KAPPA=RHO*RHO
COUNT=0

def check(b):
    global COUNT
    assert b
    COUNT+=1

@lru_cache(None)
def log_unit(x):
    assert 1<=x<=2
    z=(x-1)/(x+1); zz=z*z; term=z; total=Q(0)
    for j in range(20):
        total+=2*term/(2*j+1)
        term*=zz
    return total, total+2*term/(41*(1-zz))

@lru_cache(None)
def log_bounds(x):
    x=Q(x)
    assert x>0
    if x<1:
        l,u=log_bounds(1/x)
        return -u,-l
    k=0
    while x>=2:
        x/=2;k+=1
    l,u=log_unit(x); ll,uu=log_unit(Q(2))
    return l+k*ll,u+k*uu

def delta_max(q):
    return RHO*(RHO-q)/(1-RHO*q)

def fisher(q,delta):
    s=q*q
    return (s*(2-s)+delta*s*s)/(2*(1-s))

def scalar_certificate():
    # Analytic first interval: F <= q^2/(1-q^2), t>=q^2, q<=1/2.
    # All remaining intervals use monotonicity in q and delta separately.
    qmax=2*RHO/(1+KAPPA)
    todo=[(Q(1,2),qmax)]
    leaves=[]; examined=0
    while todo:
        l,u=todo.pop();examined+=1
        tl,_=log_bounds(1/(1-l*l))
        fup=fisher(u,delta_max(l))
        gap=tl-Q(3,5)*fup
        if gap>0:
            leaves.append((l,u,gap))
        else:
            check(u-l>Q(1,10**10))
            mid=(l+u)/2
            todo.extend([(l,mid),(mid,u)])
    leaves.sort()
    check(leaves[0][0]==Q(1,2));check(leaves[-1][1]==qmax)
    for left,right in zip(leaves,leaves[1:]):
        check(left[1]==right[0])
    # Independent replay of each cell and exact domain coverage.
    for l,u,gap in leaves:
        tl,_=log_bounds(1/(1-l*l))
        check(tl-Q(3,5)*fisher(u,delta_max(l))==gap)
        check(gap>0)
    # Elementary lower F/t bound, including radical and logarithm constants.
    a=Q(16,21);s0=Q(8,25)
    check(a*a+KAPPA*KAPPA-1>s0*s0)
    check((a+s0)/(1-KAPPA)==Q(9088,2331))
    check(Q(9088,2331)==4*(1-Q(59,2331)))
    check(Q(25,18)-Q(59,2331)<Q(41,30))
    check(KAPPA+s0-a*Q(41,30)==Q(31,25200))
    # Global allocation and exact positive coefficients.
    aa=Q(3,5);bb=Q(21,16);c=(aa+bb)/2;d=(bb-aa)/2
    r=KAPPA/(1-KAPPA);beta=c-d*r
    check(c==Q(153,160));check(d==Q(57,160))
    check(beta==Q(17,592));check(1-c==Q(7,160))
    check(1-c+beta*(1-KAPPA)==Q(331,6400))
    check(1-r*max(1-aa,bb-1)<0)
    result={'status':'PASS','analytic_interval':['0','1/2'],
            'certified_interval':['1/2',str(qmax)],'examined':examined,
            'cells':len(leaves),'minimum_exact_gap':str(min(t[2] for t in leaves)),
            'leaves':[{'lower':str(l),'upper':str(u),'gap':str(g)} for l,u,g in leaves]}
    (HERE/'scalar_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    return {k:v for k,v in result.items() if k!='leaves'}

def frac(x):
    return Q(int(sp.numer(x)),int(sp.denom(x)))

def sample_check():
    n=4
    U=sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5)],[-sp.Rational(4,5),sp.Rational(3,5)]])
    O=sp.zeros(4);O[:2,2:]=U;O[2:,:2]=U.T
    d=[sp.Rational(1,1000),sp.Rational(-1,500),sp.Rational(1,1000),sp.Rational(1,500)]
    K=sp.eye(4)/2+sp.Rational(21,50)*O+sp.diag(*d)
    check(U*U.T==sp.eye(2))
    check(Q(21,25)+2*max(abs(frac(z)) for z in d)<RHO)
    v=sp.Matrix([1,-2,3,-4]);D=sp.diag(*v)
    atoms={}; J=sp.zeros(n); psecond={}; t=sp.Symbol('t')
    for x in product((0,1),repeat=n):
        M=K-sp.diag(*[1-b for b in x]);R=M.inv()
        p=(-1)**(n-sum(x))*M.det();check(p>0)
        score=sum(v[i]*R[i,i] for i in range(n))
        p1=p*score
        p2=p*(score**2-sp.trace((R*D)**2))
        poly=sp.Poly((-1)**(n-sum(x))*(M+t*D).det(),t)
        check(poly.nth(1)==p1);check(2*poly.nth(2)==p2)
        atoms[x]=p;psecond[x]=p2
        diag=sp.Matrix([R[i,i] for i in range(n)])
        J+=p*(diag*diag.T)
    check(sum(atoms.values())==1);check(sum(psecond.values())==0)
    C=sp.diag(*[J[i,i] for i in range(n)])
    for k in range(1,n+1):
        for ids in combinations(range(n),k):check(J.extract(ids,ids).det()>0)
    for i in range(n):
        check(J[i,i]>=4)
        check(sum(J[i,j] for j in range(n) if i!=j)<=sp.Rational(289,111)*J[i,i])
    accel={x:sp.Rational(0) for x in atoms}; count=0
    for i,j in combinations(range(n),2):
        rem=[k for k in range(n) if k not in (i,j)]
        Fs=sp.Rational(0)
        for y in product((0,1),repeat=n-2):
            xx=[]
            for b,e in product((0,1),repeat=2):
                x=[0]*n;x[i]=b;x[j]=e
                for k,z in zip(rem,y):x[k]=z
                xx.append(tuple(x))
            pp=[atoms[x] for x in xx];m=sum(pp)
            a,b,c,d=[p/m for p in pp];h=b*c-a*d
            F=h*(1/a+1/b+1/c+1/d)
            check(h>=0)
            if h:
                ll,uu=log_bounds(frac(b*c/(a*d)))
                check(ll>=Q(3,5)*frac(F));check(uu<=Q(21,16)*frac(F))
            Fs+=m*F
            for x,sign in zip(xx,(1,-1,-1,1)):
                accel[x]+=2*v[i]*v[j]*m*sign
            count+=1
        check(sp.simplify(Fs-J[i,j])==0)
    check(all(sp.simplify(accel[x]-psecond[x])==0 for x in atoms))
    fi=frac((v.T*J*v)[0]);own=frac((v.T*C*v)[0])
    lower=Q(7,160)*fi+Q(17,592)*own
    curv_l=curv_u=fi
    for x,p in atoms.items():
        ll,uu=log_bounds(frac(p));coeff=frac(psecond[x])
        curv_l+=coeff*(ll if coeff>=0 else uu)
        curv_u+=coeff*(uu if coeff>=0 else ll)
    check(curv_l>lower)
    return {'status':'PASS','n':n,'atoms':len(atoms),'conditional_pairs':count,
            'K':[[str(x) for x in K.row(i)] for i in range(n)],
            'v':[int(z) for z in v],'full_fisher':str(fi),'own_fisher':str(own),
            'proven_hessian_lower':str(lower),
            'direct_minus_H_second_interval':[str(Q((curv_l*10**24).__floor__(),10**24)),str(Q((curv_u*10**24).__ceil__(),10**24))],
            'display_only':{'full_fisher':float(fi),'minus_H_second':float((curv_l+curv_u)/2),
                            'proven_hessian_lower':float(lower)}}

if __name__=='__main__':
    scalar=scalar_certificate()
    print('Scalar certificate:', {k:v for k,v in scalar.items() if k!='minimum_exact_gap'},flush=True)
    witness=sample_check()
    result={'status':'PASS','exact_assertions':COUNT,'scalar':scalar,'witness':witness}
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:',COUNT,'exact assertions;',witness['conditional_pairs'],'physical conditional tables.')
    print('Display only:',witness['display_only'])
