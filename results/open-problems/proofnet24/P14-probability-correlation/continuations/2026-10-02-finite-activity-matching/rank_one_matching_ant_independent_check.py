"""Independent exact checks of rank-one spokes plus arbitrary matching.

No author imports. Original-graph enumeration includes an unselected third
matching edge. A second route uses coefficients in the nilpotent basis
(I,P,Q), rather than logarithms or the claimed gamma-margin inequality.
"""
from fractions import Fraction as Q
from functools import reduce
from operator import mul
from pathlib import Path
import json
import random


def product(items):
    return reduce(mul,items,1)


def merge(parent,u,v):
    def root(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    ru,rv=root(u),root(v)
    if ru==rv:
        return None
    answer=list(parent)
    answer[ru]=rv
    return tuple(answer)


def original_graph(rows,cols,core,other):
    m=len(rows)
    edges=[(m,m+1,core[0]),(m,m+2,core[1]),(m+1,m+2,core[2])]
    edges += [(j,m+i,a*b) for j,a in enumerate(rows) for i,b in enumerate(cols)]
    edges += [(i,j,w) for i,j,w in other]
    edges=[(i,j,Q(w).numerator,Q(w).denominator) for i,j,w in edges if w]
    denominator=product(d for _,_,_,d in edges)
    numerators=[0,0,0,0]
    forests=0

    def walk(k,parent,weight):
        nonlocal forests
        if k==len(edges):
            forests+=1
            numerators[0]+=weight
            pe=merge(parent,0,1)
            pf=merge(parent,2,3)
            if pe is not None:
                numerators[1]+=weight
                if merge(pe,2,3) is not None:
                    numerators[3]+=weight
            if pf is not None:
                numerators[2]+=weight
            return
        u,v,n,d=edges[k]
        walk(k+1,parent,weight*d)
        included=merge(parent,u,v)
        if included is not None:
            walk(k+1,included,weight*n)
    walk(0,tuple(range(m+3)),1)
    return [Q(x,denominator) for x in numerators],forests


def data(cols,core):
    b,c,d=cols
    p,q,r=core
    B,J=b+c+d,b*c*d
    S=1+p+q+r+p*q+p*r+q*r
    L=b*c+b*d+c*d+p*d*(b+c)+q*c*(b+d)+r*b*(c+d)
    return B,J,S,L


def algebra_coefficients(rows,cols,core,other):
    B,J,S,L=data(cols,core)
    def multiply(v,w):
        a,b,c=v
        d,e,f=w
        return (a*d,a*e+b*d,a*f+c*d+2*B*b*e)
    def terminal(x):
        return (1+B*x,x*x,x**3)
    def forest(contract_e,contract_f):
        value=(Q(1),Q(0),Q(0))
        used=set()
        for (i,j),contract in zip(((0,1),(2,3)),(contract_e,contract_f)):
            used.update((i,j))
            group=terminal(rows[i]+rows[j]) if contract else multiply(terminal(rows[i]),terminal(rows[j]))
            value=multiply(value,group)
        for i,j,w in other:
            used.update((i,j))
            delete=multiply(terminal(rows[i]),terminal(rows[j]))
            contract=terminal(rows[i]+rows[j])
            group=tuple(a+w*b for a,b in zip(delete,contract))
            value=multiply(value,group)
        for i,a in enumerate(rows):
            if i not in used:
                value=multiply(value,terminal(a))
        c0,cP,cQ=value
        return S*c0+L*cP+J*cQ
    return [forest(False,False),forest(True,False),forest(False,True),forest(True,True)]


def response(rows,cols,core,other,strict=True):
    B,J,S,L=data(cols,core)
    d=lambda x:1+B*x
    alpha=lambda x:x*x/d(x)
    gamma=lambda x:x**3/d(x)**2
    D,U,G=Q(1),Q(0),Q(0)
    used=set()
    for i,j,w in other:
        a,b=rows[i],rows[j]
        used.update((i,j))
        k0,k1=d(a)*d(b),d(a+b)
        K=k0+w*k1
        theta=w*k1/K
        u0,u1=alpha(a)+alpha(b),alpha(a+b)
        g0,g1=gamma(a)+gamma(b),gamma(a+b)
        delta=u1-u0
        # Independently test every stated merge-gap bound, including zero rows.
        assert 0<=delta<=a/(B*d(a)) and delta<=b/(B*d(b))
        assert u0/B-g0>=B*delta*delta and u1/B-g1>=B*delta*delta
        uh=(1-theta)*u0+theta*u1
        gh=(1-theta)*g0+theta*g1+B*theta*(1-theta)*delta*delta
        assert 0<=gh<=uh/B
        D*=K
        U+=uh
        G+=gh
    for i,a in enumerate(rows):
        if i not in used:
            D*=d(a)
            U+=alpha(a)
            G+=gamma(a)
    F=S+L*U+J*G+B*J*U*U
    changes=[]
    for i,j in ((0,1),(2,3)):
        a,b=rows[i],rows[j]
        de=alpha(a+b)-alpha(a)-alpha(b)
        ep=gamma(a+b)-gamma(a)-gamma(b)
        ce=d(a+b)/(d(a)*d(b))
        xe=de*(L+2*B*J*U)+J*ep+B*J*de*de
        assert de>=0 and ep>=0
        if strict:
            assert de>0 and ep>0
        changes.append((de,ce,xe))
    de,ce,xe=changes[0]
    df,cf,xf=changes[1]
    values=[D*F,D*ce*(F+xe),D*cf*(F+xf),D*ce*cf*(F+xe+xf+2*B*J*de*df)]
    rayleigh=D*D*ce*cf*(xe*xf-2*B*J*de*df*F)
    assert values[1]*values[2]-values[0]*values[3]==rayleigh
    assert 0<=G<=U/B
    assert L*L-2*B*J*S>0 and B*L>J
    assert (L+2*B*J*U)**2-2*B*J*F>0
    assert rayleigh>0 if strict else rayleigh>=0
    return values,rayleigh


def encode(rows,cols,core,other,rayleigh,forests=None):
    answer=dict(m=len(rows),rows=list(map(str,rows)),columns=list(map(str,cols)),
                core=list(map(str,core)),other_matching=[[i,j,str(w)] for i,j,w in other],rayleigh=str(rayleigh))
    if forests is not None:
        answer["enumerated_original_forests"]=forests
    return answer


def main():
    report=dict(status="PASS",direct=[],algebra_checks=[],zero_endpoint_checks=[])
    direct_cases=[
        ([1,2,3,4,5,6],[2,3,5],[2,3,5],[(4,5,2)]),
        ([Q(1,2),Q(2,3),Q(3,4),Q(4,5),0,2],[Q(1,2),Q(2,3),Q(3,4)],[Q(1,3),Q(2,5),0],[(4,5,Q(7,3))]),
    ]
    for aa,bb,pp,other in direct_cases:
        aa,bb,pp=[list(map(Q,x)) for x in (aa,bb,pp)]
        other=[(i,j,Q(w)) for i,j,w in other]
        direct,forests=original_graph(aa,bb,pp,other)
        expected,rayleigh=response(aa,bb,pp,other)
        assert direct==algebra_coefficients(aa,bb,pp,other)==expected
        report["direct"].append(encode(aa,bb,pp,other,rayleigh,forests))
    rng=random.Random(31415926535)
    for m in (4,6,8,10,25,100):
        for _ in range(6):
            aa=[Q(rng.randrange(1,20),rng.randrange(1,15)) for _ in range(4)]
            aa += [Q(rng.randrange(0,20),rng.randrange(1,15)) for _ in range(m-4)]
            bb=[Q(rng.randrange(1,20),rng.randrange(1,15)) for _ in range(3)]
            pp=[Q(rng.randrange(0,20),rng.randrange(1,15)) for _ in range(3)]
            other=[(i,i+1,Q(rng.randrange(0,20),rng.randrange(1,15))) for i in range(4,m-1,2)]
            expected,rayleigh=response(aa,bb,pp,other)
            assert algebra_coefficients(aa,bb,pp,other)==expected
            report["algebra_checks"].append(encode(aa,bb,pp,other,rayleigh))
    for pivot in range(4):
        aa=list(map(Q,[1,2,3,4,0,2,3,4]))
        aa[pivot]=Q(0)
        bb=list(map(Q,[2,3,5]))
        pp=list(map(Q,[0,3,1]))
        other=[(4,5,Q(2)),(6,7,Q(3))]
        expected,rayleigh=response(aa,bb,pp,other,strict=False)
        assert algebra_coefficients(aa,bb,pp,other)==expected
        assert rayleigh==0
        report["zero_endpoint_checks"].append(encode(aa,bb,pp,other,rayleigh))
    report["direct_cases"]=len(report["direct"])
    report["algebra_cases"]=len(report["algebra_checks"])
    report["zero_endpoint_cases"]=len(report["zero_endpoint_checks"])
    Path(__file__).with_name("rank_one_matching_ant_independent_checks.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k not in ("direct","algebra_checks","zero_endpoint_checks")},indent=2))
    print(json.dumps(report["direct"],indent=2))


if __name__ == "__main__":
    main()
