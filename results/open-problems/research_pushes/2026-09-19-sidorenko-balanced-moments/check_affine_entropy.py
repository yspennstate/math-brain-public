"""Exact finite-field obstruction to D_5 <= 5 D_3 for star marginals.
Not a Sidorenko counterexample. Python standard library only.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from collections import Counter
import json


def rank(A,q):
    if not A:return 0
    a=[row[:] for row in A];r=0
    for j in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][j]%q),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        inv=pow(a[r][j],-1,q);a[r]=[(x*inv)%q for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                c=a[i][j];a[i]=[(x-c*y)%q for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a):break
    return r


def distribution(r,d,q):
    dist={0:F(1)}
    for _ in range(r):
        new=Counter()
        for s,p in dist.items():
            stay=F(q**s,q**d)
            new[s]+=p*stay
            new[s+1]+=p*(1-stay)
        dist={s:p for s,p in new.items() if p}
    return dist


def rank_formula(r,d,q,s):
    n=F(1)
    for i in range(s):n*=F((q**r-q**i)*(q**d-q**i),q**s-q**i)
    assert n.denominator==1
    return n.numerator


def null_basis(A,q):
    a=[row[:] for row in A];r=0;piv=[]
    for j in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][j]%q),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];iv=pow(a[r][j],-1,q)
        a[r]=[(x*iv)%q for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                c=a[i][j];a[i]=[(x-c*y)%q for x,y in zip(a[i],a[r])]
        piv.append(j);r+=1
        if r==len(a):break
    free=[j for j in range(len(a[0])) if j not in piv];basis=[]
    for j in free:
        v=[0]*len(a[0]);v[j]=1
        for i,k in enumerate(piv):v[k]=-a[i][j]%q
        assert all(sum(x*y for x,y in zip(row,v))%q==0 for row in A)
        basis.append(v)
    return basis


def main():
    q=3;d=3;N=q**d
    ds={}
    for r in [2,4]:
        dist=distribution(r,d,q)
        exact={s:F(rank_formula(r,d,q,s),q**(r*d)) for s in range(min(r,d)+1)}
        assert dist==exact and sum(dist.values())==1
        ds[r]=sum((r-s)*p for s,p in dist.items())
    assert ds[2]==F(106,729) and ds[4]==F(614644,531441)
    gap=ds[4]-5*ds[2]
    assert gap==F(228274,531441)>0
    # Exhaustive independent rank check for the smaller matrix distribution.
    observed=Counter(rank([list(a[:d]),list(a[d:])],q) for a in product(range(q),repeat=2*d))
    assert {s:F(v,q**(2*d)) for s,v in observed.items()}==distribution(2,d,q)
    # The symmetric regular kernel on 81 states: verify every entry/row.
    states=list(product(list(product(range(q),repeat=d)),range(q)))
    def w(s,t):
        a,b=s;u,c=t
        return q if (sum(x*y for x,y in zip(a,u))-b-c)%q==0 else 0
    assert len(states)==81
    assert all(w(s,t)==w(t,s)>=0 for s in states for t in states)
    assert all(sum(w(s,t) for t in states)==len(states) for s in states)
    # Fourier flow formula: enumerate every flow, not vertex assignments.
    edges=[((i+j)%5,i) for i in range(5) for j in range(3)]
    incidence=[[int((v<5 and e[0]==v) or (v>=5 and e[1]==v-5)) for e in edges] for v in range(10)]
    basis=null_basis(incidence,q);assert len(basis)==6
    rc=Counter(); seen=set()
    for coeff in product(range(q),repeat=len(basis)):
        flow=tuple(sum(c*b[i] for c,b in zip(coeff,basis))%q for i in range(15))
        assert flow not in seen;seen.add(flow)
        assert all(sum(x*y for x,y in zip(row,flow))%q==0 for row in incidence)
        M=[[0]*5 for _ in range(5)]
        for t,(i,j) in zip(flow,edges):M[i][j]=t
        rc[rank(M,q)]+=1
    assert len(seen)==q**6 and rc[0]==1 and rc[1]==5*(q-1)
    density=sum(F(c,N**s) for s,c in rc.items())
    assert density>1+F(5*(q-1),N)+F(10*(q-1),N*N)
    out={'status':'ALL_EXACT_CHECKS_PASS','q':q,'d':d,'kernel_states':len(states),
         'D3_over_log3':str(ds[2]),'D5_over_log3':str(ds[4]),'D5_minus_5D3_over_log3':str(gap),
         'smaller_rank_matrices_enumerated':q**(2*d),'flow_dimension':6,'flows_enumerated':len(seen),
         'flow_rank_counts':dict(sorted(rc.items())),'H_density':str(density),
         'Sidorenko_counterexample':False,'full_proof':False,
         'scope':'Counterexample to a sufficient entropy shortcut; separate bipartite Fourier identity.'}
    text=json.dumps(out,indent=2)+'\n';Path(__file__).with_name('affine_entropy_checks.json').write_text(text);print(text,end='')

if __name__=='__main__':main()
