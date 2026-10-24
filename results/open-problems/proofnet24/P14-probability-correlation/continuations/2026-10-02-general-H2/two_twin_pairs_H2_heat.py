"""Two distinct positive spoke profiles: full-graph exact H2 verification.

No core contraction or four-terminal transfer. Activities on core/spoke
edges are lambda times conductances. Marked e=01,f=23 are differentiated
before specialization. All decision arithmetic is fractions.Fraction.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from four_twins_full_graph_audit_heat import mul,inv_det


def direct(a,b,core,scales=(F(1),)*4):
    s=len(a);assert s==len(b);n=s+4
    edges=[(4+u,4+v,F(w))for u,v,w in core]
    edges += [(i,4+v,scales[i]*w)for i,profile in enumerate((a,a,b,b))for v,w in enumerate(profile)]
    parent=list(range(n));size=[1]*n;polys=[{}for _ in range(4)]
    def root(v):
        while parent[v]!=v:v=parent[v]
        return v
    def visit(i,k,weight):
        if i==len(edges):
            u,v,x,y=map(root,range(4));e=u!=v;f=x!=y
            for p,ok in zip(polys,[True,e,f,e and f and {u,v}!={x,y}]):
                if ok:p[k]=p.get(k,F(0))+weight
            return
        visit(i+1,k,weight)
        u,v,w=edges[i];ru,rv=root(u),root(v)
        if ru==rv:return
        if size[ru]<size[rv]:ru,rv=rv,ru
        previous=size[ru];parent[rv]=ru;size[ru]+=size[rv]
        visit(i+1,k+1,weight*w)
        size[ru]=previous;parent[rv]=rv
    visit(0,0,F(1));A,B,C,D=polys;R=mul(B,C)
    for k,v in mul(A,D).items():R[k]=R.get(k,F(0))-v
    return polys,{k:v for k,v in sorted(R.items())if v}


def predicted(a,b,core,root=0,scales=(F(1),)*4):
    s=len(a);da=sum(a,F(0));db=sum(b,F(0))
    aa,ab,ba,bb=scales;product=aa*ab*ba*bb
    if s==1:return F(0),product*da**2*db**2
    N=[[F(0)for _ in range(s)]for _ in range(s)]
    for u,v in combinations(range(s),2):
        w=(aa+ab)*a[u]*a[v]/da+(ba+bb)*b[u]*b[v]/db
        N[u][u]+=w;N[v][v]+=w;N[u][v]-=w;N[v][u]-=w
    for u,v,w in core:
        N[u][u]+=w;N[v][v]+=w;N[u][v]-=w;N[v][u]-=w
    indices=[u for u in range(s)if u!=root]
    T,Xi=inv_det([[N[u][v]for v in indices]for u in indices])
    ar=[a[u]for u in indices];br=[b[u]for u in indices];m=s-1
    Pa=[[F(i==j)*ar[i]-ar[i]*ar[j]/da for j in range(m)]for i in range(m)]
    Pb=[[F(i==j)*br[i]-br[i]*br[j]/db for j in range(m)]for i in range(m)]
    value=F(0)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                for l in range(m):value+=Pa[i][j]*T[j][k]*Pb[k][l]*T[l][i]
    tau=product*da**2*db**2*Xi
    H2=product*(aa+ab)*(ba+bb)*da**2*db**2*Xi**2*value
    # Independently evaluate the all-core-pairs adjugate square formula.
    def incidence(u,v):
        return [F(z==u)-F(z==v)for z in indices]
    square_sum=F(0)
    for u,v in combinations(range(s),2):
        z=incidence(u,v)
        for x,y in combinations(range(s),2):
            zz=incidence(x,y)
            bilinear=sum((z[i]*Xi*T[i][j]*zz[j]for i in range(m)for j in range(m)),F(0))
            square_sum+=a[u]*a[v]*b[x]*b[y]*bilinear**2
    assert H2==product*(aa+ab)*(ba+bb)*da*db*square_sum
    return H2,tau


def main():
    cases=[
        ([F(2,3)],[F(5,7)],[]),
        ([F(1),F(2)],[F(3),F(5)],[]),
        ([F(1,2),F(3,4)],[F(2,3),F(5,7)],[(0,1,F(5,7))]),
        ([F(1),F(2),F(3)],[F(2),F(1),F(5)],[(0,1,F(2)),(1,2,F(3))]),
        ([F(1,2),F(2,3),F(3,4)],[F(7,6),F(4,5),F(5,8)],[(0,1,F(5,7)),(1,2,F(7,5)),(0,2,F(4,9))]),
        ([F(1),F(2),F(3)],[F(4),F(2),F(1)],[(0,1,F(4))]),
        ([F(1),F(2),F(1),F(2)],[F(2),F(1),F(2),F(1)],[(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
    ]
    result=[]
    for scales in [(F(1),)*4,(F(2),F(3),F(4),F(5)),(F(1,2),F(2,3),F(3,4),F(4,5))]:
        for a,b,core in cases:
            s=len(a);polys,R=direct(a,b,core,scales);H2,tau=predicted(a,b,core,scales=scales)
            assert R.get(2*s+4,F(0))==0 and R.get(2*s+3,F(0))==0
            assert R.get(2*s+2,F(0))==H2
            assert polys[0][s+3]==tau
            for root in range(s):assert predicted(a,b,core,root,scales)==(H2,tau)
            assert H2>0 if s>1 else not R
            result.append({'s':s,'a':list(map(str,a)),'b':list(map(str,b)),
                           'scales':list(map(str,scales)),
                           'core':[(u,v,str(w))for u,v,w in core],'H2':str(H2),
                           'tau_unmarked':str(tau),'R':{str(k):str(v)for k,v in R.items()},
                           'A_B_C_D':[{str(k):str(v)for k,v in p.items()}for p in polys],
                           'every_grounded_root_agrees':True,'passed':True})
            print('two-profiles passed',s,len(core),'scales',scales,'H2',H2,flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps({'arithmetic':'Fraction exact','independent_method':'full-graph forest subsets + all marked insertion tests','all_passed':True,'cases':result},indent=2))


if __name__=='__main__':main()
