"""Independent polynomial and original-graph check of adjacent marks.

Polynomial keys are Kronecker-encoded integers in base32, unlike the author
tuple representation. C is regenerated via raw (I,P,Q) multiplication,
not the author's explicit cluster formula. Total degree <=20 ensures no
encoding carry. The graph checker literally enumerates all unmarked edges.
"""
from fractions import Fraction as Q
from pathlib import Path
from functools import reduce
from operator import mul
import json

N=11
BASE=32
POWERS=[BASE**i for i in range(N)]


def add(*polys):
    result={}
    for p in polys:
        for k,v in p.items():
            result[k]=result.get(k,0)+v
    return {k:v for k,v in result.items() if v}


def scale(p,c):
    return {k:v*c for k,v in p.items() if v*c}


def times(p,q):
    result={}
    for i,a in p.items():
        for j,b in q.items():
            result[i+j]=result.get(i+j,0)+a*b
    return {k:v for k,v in result.items() if v}


def product(*polys):
    return reduce(times,polys,{0:1})


def decode(k):
    return tuple((k//x)%BASE for x in POWERS)


def polynomial_certificate():
    a,b,c,b1,b2,b3,p,q,r,U,G=[{x:1} for x in POWERS]
    one={0:1}
    B=add(b1,b2,b3)
    J=product(b1,b2,b3)
    S=add(one,p,q,r,product(p,q),product(p,r),product(q,r))
    L=add(product(b1,b2),product(b1,b3),product(b2,b3),
          product(p,b3,add(b1,b2)),product(q,b2,add(b1,b3)),product(r,b1,add(b2,b3)))
    def multiply(v,w):
        v0,vP,vQ=v
        w0,wP,wQ=w
        return (product(v0,w0),add(product(v0,wP),product(vP,w0)),
                add(product(v0,wQ),product(vQ,w0),scale(product(B,vP,wP),2)))
    def terminal(x):
        return (add(one,product(B,x)),product(x,x),product(x,x,x))
    def forest(rows):
        state=(one,U,add(G,product(B,U,U)))
        for x in rows:
            state=multiply(state,terminal(x))
        return add(product(S,state[0]),product(L,state[1]),product(J,state[2]))
    A=forest([a,b,c])
    E=forest([add(a,b),c])
    F=forest([a,add(b,c)])
    EF=forest([add(a,b,c)])
    R=add(product(E,F),scale(product(A,EF),-1))
    assert len(R)==11063 and min(R.values())>0
    assert all(sum(decode(k))<=20 for k in R)
    assert all(decode(k)[0]>0 and decode(k)[2]>0 for k in R)
    for i in (3,4,5):
        assert R[POWERS[0]+POWERS[2]+2*POWERS[i]]==1
    original=json.loads(Path(__file__).with_name("forest_adjacent_terminal_core3_coefficient_certificate.json").read_text())
    expected={sum(e*x for e,x in zip(row["exponents"],POWERS)):row["coefficient"] for row in original["coefficients"]}
    assert expected==R
    slices={}
    for k,v in R.items():
        key=str(decode(k)[9:])
        item=slices.setdefault(key,dict(terms=0,minimum_coefficient=v))
        item["terms"]+=1
        item["minimum_coefficient"]=min(item["minimum_coefficient"],v)
    return R,slices


def merge(parent,u,v):
    def root(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    ru,rv=root(u),root(v)
    if ru==rv:
        return None
    out=list(parent)
    out[ru]=rv
    return tuple(out)


def original_graph(rows,columns,core,background):
    m=len(rows)
    edges=[(m,m+1,core[0]),(m,m+2,core[1]),(m+1,m+2,core[2])]
    edges += [(j,m+i,a*b) for j,a in enumerate(rows) for i,b in enumerate(columns)]
    edges += background
    edges=[(u,v,Q(w).numerator,Q(w).denominator) for u,v,w in edges if w]
    denominator=reduce(mul,(d for u,v,n,d in edges),1)
    totals=[0,0,0,0]
    forests=0
    def walk(k,parent,weight):
        nonlocal forests
        if k==len(edges):
            forests+=1
            totals[0]+=weight
            e=merge(parent,0,1)
            f=merge(parent,1,2)
            if e is not None:
                totals[1]+=weight
                if merge(e,1,2) is not None:
                    totals[3]+=weight
            if f is not None:
                totals[2]+=weight
            return
        u,v,n,d=edges[k]
        walk(k+1,parent,weight*d)
        included=merge(parent,u,v)
        if included is not None:
            walk(k+1,included,weight*n)
    walk(0,tuple(range(m+3)),1)
    return [Q(x,denominator) for x in totals],forests


def raw_reduction(rows,columns,core,background):
    B=sum(columns)
    J=reduce(mul,columns,Q(1))
    p,q,r=core
    b1,b2,b3=columns
    S=1+p+q+r+p*q+p*r+q*r
    L=b1*b2+b1*b3+b2*b3+p*b3*(b1+b2)+q*b2*(b1+b3)+r*b1*(b2+b3)
    def multiply(v,w):
        a,b,c=v
        d,e,f=w
        return (a*d,a*e+b*d,a*f+c*d+2*B*b*e)
    def terminal(x):
        return (1+B*x,x*x,x**3)
    raw=[Q(0)]*3
    for mask in range(1<<len(background)):
        parent=tuple(range(len(rows)))
        weight=Q(1)
        for j,(u,v,w) in enumerate(background):
            if mask>>j&1:
                parent=merge(parent,u,v)
                if parent is None:
                    break
                weight*=w
        if parent is None:
            continue
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        clusters={}
        for j,a in enumerate(rows[3:],3):
            clusters[root(j)]=clusters.get(root(j),Q(0))+a
        value=(Q(1),Q(0),Q(0))
        for a in clusters.values():
            value=multiply(value,terminal(a))
        raw=[x+weight*y for x,y in zip(raw,value)]
    D=raw[0]
    U=raw[1]/D
    G=raw[2]/D-B*U*U
    assert D>0 and U>=0 and G>=0
    values=[]
    a,b,c=rows[:3]
    for groups in ([a,b,c],[a+b,c],[a,b+c],[a+b+c]):
        value=tuple(raw)
        for x in groups:
            value=multiply(value,terminal(x))
        values.append(S*value[0]+L*value[1]+J*value[2])
    return values,(D,U,G)


def evaluate(poly,values):
    return sum((c*reduce(mul,(v**e for v,e in zip(values,decode(k))),Q(1)) for k,c in poly.items()),Q(0))


def main():
    R,slices=polynomial_certificate()
    report=dict(status="PASS",polynomial_terms=len(R),all_coefficients_identical_to_author=True,
                representation="Base32 integer monomials; raw (I,P,Q) transfer products",
                coefficient_slices=slices,direct_graph_checks=[],degenerate_checks=[])
    cases=[([1,2,3,4,5,6],[2,3,5],[2,3,5],[(3,4,2),(4,5,3),(3,5,5)]),
           ([1,0,2,3,4,5],[1,0,2],[0,1,2],[(3,4,1),(4,5,2),(3,5,3)])]
    for aa,bb,pp,bg in cases:
        aa,bb,pp=[list(map(Q,x)) for x in (aa,bb,pp)]
        bg=[(i,j,Q(w)) for i,j,w in bg]
        direct,forests=original_graph(aa,bb,pp,bg)
        reduced,(D,U,G)=raw_reduction(aa,bb,pp,bg)
        assert direct==reduced
        rayleigh=direct[1]*direct[2]-direct[0]*direct[3]
        assert rayleigh==D*D*evaluate(R,aa[:3]+bb+pp+[U,G])>0
        report["direct_graph_checks"].append(dict(rows=list(map(str,aa)),columns=list(map(str,bb)),
            core=list(map(str,pp)),background=[[i,j,str(w)] for i,j,w in bg],
            original_forests=forests,A_Be_Bf_C=list(map(str,direct)),rayleigh=str(rayleigh)))
    for aa,bb,expected_strict in (([1,0,1],[1,0,0],True),([1,0,1],[0,0,0],False),
                                  ([0,2,3],[1,2,3],False),([1,2,0],[1,2,3],False)):
        aa,bb=list(map(Q,aa)),list(map(Q,bb))
        values,(D,U,G)=raw_reduction(aa,bb,[Q(0)]*3,[])
        rayleigh=values[1]*values[2]-values[0]*values[3]
        assert rayleigh==evaluate(R,aa+bb+[Q(0)]*3+[U,G])
        assert rayleigh>0 if expected_strict else rayleigh==0
        report["degenerate_checks"].append(dict(rows=list(map(str,aa)),columns=list(map(str,bb)),rayleigh=str(rayleigh)))
    Path(__file__).with_name("adjacent_terminal_ant_independent_checks.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
