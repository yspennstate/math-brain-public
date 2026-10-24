"""Independent exact matrix/ladder checks and numerical gradient audit.

Exact checks have no author helper imports. Numerical checks intentionally
load the search implementations to compare their gradients with differences.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import importlib.util
import json
import numpy as np


def multiply(A,B):
    return [[sum(a*b for a,b in zip(row,column)) for column in zip(*B)] for row in A]


def power(A,n):
    answer=[[Q(i==j) for j in range(len(A))] for i in range(len(A))]
    factor=A
    while n:
        if n&1:
            answer=multiply(answer,factor)
        factor=multiply(factor,factor)
        n//=2
    return answer


def act(A,v):
    return [sum(a*b for a,b in zip(row,v)) for row in A]


def exact_rank(columns):
    rows=[list(row) for row in zip(*columns)]
    rank=0
    for col in range(len(columns)):
        pivot=next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        d=rows[rank][col]
        rows[rank]=[v/d for v in rows[rank]]
        for i in range(len(rows)):
            if i!=rank:
                f=rows[i][col]
                rows[i]=[a-f*b for a,b in zip(rows[i],rows[rank])]
        rank+=1
    return rank


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    states=list(product(range(3),repeat=2))
    index={x:i for i,x in enumerate(states)}
    S=[[Q(x==(y[1],y[0])) for y in states] for x in states]
    B=[[Q(1)-Q(3,20)*Q(x==y)+Q(17,20)*S[i][j]
        for j,y in enumerate(states)] for i,x in enumerate(states)]
    assert all(x>0 for row in B for x in row)
    assert B==[list(x) for x in zip(*B)] and multiply(B,S)==multiply(S,B)
    def e(i,j):
        v=[Q(0)]*9
        v[index[i,j]]=Q(1)
        return v
    def lin(*terms):
        return [sum(c*v[i] for c,v in terms) for i in range(9)]
    sym=lambda i,j:lin((1,e(i,j)),(1,e(j,i)))
    basis=[([Q(1)]*9,Q(97,10))]
    basis += [(lin((1,e(0,0)),(-1,e(1,1))),Q(7,10)),
              (lin((1,e(1,1)),(-1,e(2,2))),Q(7,10)),
              (lin((1,sym(0,1)),(-1,sym(0,2))),Q(7,10)),
              (lin((1,sym(0,2)),(-1,sym(1,2))),Q(7,10)),
              (lin((2,e(0,0)),(-1,sym(0,1))),Q(7,10))]
    basis += [(lin((1,e(i,j)),(-1,e(j,i))),Q(-1)) for i,j in ((0,1),(0,2),(1,2))]
    assert exact_rank([v for v,l in basis])==9
    for v,l in basis:
        assert act(B,v)==[l*x for x in v]
    fifth=power(B,5)
    trace=sum(B[i][i] for i in range(9))
    tail5=sum(fifth[i][i] for i in range(9))-Q(97,10)**5
    assert trace==Q(51,5) and trace-Q(97,10)==Q(1,2)
    assert tail5==Q(-43193,20000)
    pairs=((0,1),(0,2),(1,2))
    symmetric,antisymmetric=[],[]
    for i,j in pairs:
        srow,arow=[],[]
        for k,l in pairs:
            entries=[B[index[u,v]][index[x,y]] for u,v in ((i,j),(j,i)) for x,y in ((k,l),(l,k))]
            srow.append(sum(entries)/2)
            arow.append((entries[0]-entries[1]-entries[2]+entries[3])/2)
        symmetric.append(srow)
        antisymmetric.append(arow)
    assert antisymmetric==[[-Q(i==j) for j in range(3)] for i in range(3)]
    assert all(symmetric[i][j]>=abs(antisymmetric[i][j]) for i in range(3) for j in range(3))
    assert B[index[0,1]][index[1,0]]==Q(37,20)>Q(17,10)
    report=dict(status="PASS",exact_eigenbasis_rank=9,trace=str(trace),excluded_trace="1/2",
                shortest_tail="-3/10",excluded_fifth_moment=str(tail5),
                symmetric_pair_principal_block=[[str(v) for v in row] for row in symmetric],
                antisymmetric_block=[[str(v) for v in row] for row in antisymmetric],
                product_family_obstruction=dict(exchange_entry="37/20",allowed_geometric_maximum="17/10"),
                ladder_normalization_checks=[],numerical_gradient_checks=[])
    W=[[1,4],[4,9]]
    roots=[[1,2],[2,3]]
    ix=list(product(range(2),repeat=2))
    M=[[Q(W[i][l]*W[k][j]*roots[i][j]*roots[k][l]) for k,l in ix] for i,j in ix]
    for m in (3,4,5,6):
        hom=0
        for bits in product(range(2),repeat=2*m):
            xs,ys=bits[:m],bits[m:]
            weight=1
            for r in range(m):
                for q in (-1,0,1):
                    weight*=W[xs[r]][ys[(r+q)%m]]
            hom+=weight
        mp=power(M,m)
        assert hom==sum(mp[i][i] for i in range(4))
        assert hom<=sum(x**3 for row in W for x in row)**m
        report["ladder_normalization_checks"].append(dict(m=m,hom=str(hom),normalized_density=str(Q(hom,2**(2*m)))))
    folder=Path(__file__).parent
    spectral=load_module("spectral_gradient_under_audit",folder/"continuation_20261002_spectral_obstruction_search.py")
    radial=load_module("radial_gradient_under_audit",folder/"continuation_20261002_regular_radial_search.py")
    rng=np.random.default_rng(27931)
    for kind,k in (("majorization",2),("majorization",4),("pseudo",2)):
        n=4
        z=rng.normal(0,.6,n*(n+1)//2)
        args=(n,1/3,kind,k,1.0,1.25)
        value,gradient=spectral.objective(z,*args)
        errors=[]
        for j in range(len(z)):
            change=np.zeros_like(z);change[j]=1e-5
            finite=(spectral.objective(z+change,*args)[0]-spectral.objective(z-change,*args)[0])/2e-5
            errors.append(abs(finite-gradient[j]))
        assert max(errors)<1e-7
        report["numerical_gradient_checks"].append(dict(objective=kind,k=k,n=n,max_absolute_error=max(errors),value=value))
    n=4
    z=rng.normal(0,.6,n*(n+1)//2)
    value,gradient=radial.objective(z,n,.8)
    errors=[]
    for j in range(len(z)):
        change=np.zeros_like(z);change[j]=1e-5
        finite=(radial.objective(z+change,n,.8)[0]-radial.objective(z-change,n,.8)[0])/2e-5
        errors.append(abs(finite-gradient[j]))
    assert max(errors)<1e-7
    report["numerical_gradient_checks"].append(dict(objective="radial",n=n,max_absolute_error=max(errors),value=value))
    Path(__file__).with_name("operator_boundaries_ant_independent_checks.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":
    main()
