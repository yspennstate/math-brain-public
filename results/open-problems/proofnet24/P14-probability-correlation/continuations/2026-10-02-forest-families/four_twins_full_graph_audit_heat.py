"""Independent full-graph audit; no contraction or terminal partition transfer.

Enumerate all acyclic subsets of the unmarked graph on s+4 vertices. Determine
whether adding each marked edge/both marked edges preserves acyclicity. This
directly obtains A,B,C,D as exact Fraction polynomials in lambda.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def mul(p,q):
    out={}
    for i,x in p.items():
        for j,y in q.items():out[i+j]=out.get(i+j,F(0))+x*y
    return out


def direct_polynomials(a,core):
    s=len(a);n=s+4
    edges=[(4+u,4+v,F(w))for u,v,w in core]
    edges += [(i,4+v,F(w))for i in range(4)for v,w in enumerate(a)]
    parent=list(range(n));size=[1]*n
    polys=[{}for _ in range(4)]
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    def count_leaf(k,weight):
        r0,r1,r2,r3=map(root,range(4))
        eok=r0!=r1;fok=r2!=r3
        # If both edges separately connect components, adding both fails
        # precisely when their unordered pairs of component labels coincide.
        both=eok and fok and {r0,r1}!={r2,r3}
        for poly,ok in zip(polys,[True,eok,fok,both]):
            if ok:poly[k]=poly.get(k,F(0))+weight
    def visit(i,k,weight):
        if i==len(edges):count_leaf(k,weight);return
        visit(i+1,k,weight)
        u,v,w=edges[i];ru,rv=root(u),root(v)
        if ru==rv:return
        if size[ru]<size[rv]:ru,rv=rv,ru
        oldsize=size[ru];parent[rv]=ru;size[ru]+=size[rv]
        visit(i+1,k+1,weight*w)
        size[ru]=oldsize;parent[rv]=rv
    visit(0,0,F(1))
    A,B,C,D=polys;assert B==C
    R=mul(B,C)
    for k,v in mul(A,D).items():R[k]=R.get(k,F(0))-v
    return polys,{k:v for k,v in sorted(R.items())if v}


def inv_det(matrix):
    n=len(matrix);w=[row[:]+[F(i==j)for j in range(n)]for i,row in enumerate(matrix)]
    det=F(1)
    for i in range(n):
        j=next(j for j in range(i,n)if w[j][i])
        if i!=j:w[i],w[j]=w[j],w[i];det=-det
        pivot=w[i][i];det*=pivot;w[i]=[x/pivot for x in w[i]]
        for j in range(n):
            if j==i:continue
            factor=w[j][i];w[j]=[x-factor*y for x,y in zip(w[j],w[i])]
    return [row[n:]for row in w],det


def sos(a,core):
    s=len(a);M=[[F(0)for _ in range(s)]for _ in range(s)]
    for i,x in enumerate(a):M[i][i]=4*x
    for u,v,w in core:
        w=F(w);M[u][u]+=w;M[v][v]+=w;M[u][v]-=w;M[v][u]-=w
    inverse,W=inv_det(M);d=sum(a,F(0))
    return sum((a[u]*a[v]*(4*d*W*inverse[u][v]-W)**2/F(64)
                for u in range(s)for v in range(s)),F(0))


def main():
    cases=[
        ([F(2,3)],[]),
        ([F(1),F(2)],[]),
        ([F(1,2),F(3,4)],[(0,1,F(5,7))]),
        ([F(1),F(2),F(3)],[(0,1,F(2)),(1,2,F(3))]),
        ([F(1,2),F(2,3),F(3,4)],[(0,1,F(5,7)),(1,2,F(7,5)),(0,2,F(4,9))]),
        ([F(1),F(2),F(3)],[(0,1,F(4))]),
        ([F(1),F(1),F(1),F(1)],[(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
    ]
    report=[]
    for a,core in cases:
        s=len(a);polys,R=direct_polynomials(a,core);prediction=sos(a,core)
        assert R.get(2*s+4,F(0))==0 and R.get(2*s+3,F(0))==0
        assert R.get(2*s+2,F(0))==prediction
        if s==1:assert not R
        else:assert prediction>0
        record={'s':s,'a':list(map(str,a)),'core':[(u,v,str(w))for u,v,w in core],
                'H2':str(prediction),'R':{str(k):str(v)for k,v in R.items()},
                'A_B_C_D':[{str(k):str(v)for k,v in p.items()}for p in polys],
                'all_passed':True}
        report.append(record)
        print('full-graph passed',s,len(core),'H2',prediction,flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps({'method':'full unmarked edge-subset enumeration with marked-edge insertion tests; Fraction exact','cases':report,'all_passed':True},indent=2))


if __name__=='__main__':main()
