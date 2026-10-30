"""Full partition graph census with rational packing dual certificates; A010 review."""
from fractions import Fraction as F
from itertools import combinations,product
from math import comb
from pathlib import Path
from time import perf_counter
import json,sys
from star_full import enumerate_runs, mul
from check import fwht,traces,evaluate
BASE=Path(__file__).resolve().parents[1];checks=0
def ck(ok):
    global checks
    checks+=1
    assert ok,checks
def packing_dual(E,n):
    # Enumeration supplies a feasible primal equal to a feasible dual.
    # Weak duality suffices: no reliance on floating LP or half-integrality theorem.
    prices=min((x for x in product([F(0),F(1,2),F(1)],repeat=n)
                if all(x[u]+x[v]>=1 for u,v in E)),key=sum)
    L=sum(prices)
    weight=None
    for z in product([F(0),F(1,2),F(1)],repeat=len(E)):
        if sum(z)==L and all(sum(z[i] for i,e in enumerate(E) if v in e)<=1 for v in range(n)):
            weight=z;break
    ck(weight is not None)
    ck(sum(weight)==sum(prices));return L,weight,prices
def capped_lp(h,caps,v):
    left=F(1);primal_p={T:F(0) for T in h};threshold=None
    for T in sorted(h,key=h.get,reverse=True):
        primal_p[T]=min(caps[T],left);left-=primal_p[T]
        if not left:threshold=h[T];break
    ck(left==0);value=sum(primal_p[T]*h[T] for T in h)
    dual=threshold+sum(caps[T]*max(h[T]-threshold,0) for T in h)
    ck(value==dual and value>=v)
    return value-v,{'threshold':str(threshold),'primal':{str(T):str(z) for T,z in primal_p.items() if z},
                    'primal_value':str(value),'dual_value':str(dual)}
def review_A010():
    rows=[]
    for m in range(2,9):
        D=(1+F(1,4*m))**m-1;delta=F(1,4**m);v=1-delta;I=1+F(m-1,2**m)
        h={T:2*delta*D*(4*m)**T.bit_count()+(4*D*(1-F(1,2**m))**2 if T.bit_count()==1 else 0) for T in range(1,1<<m)}
        caps={T:F(4)**(1-T.bit_count())/T.bit_count()**T.bit_count() for T in h}
        p={T:F(1,(4*m)**T.bit_count())/D for T in h}
        ck(sum(p.values())==1);ck(sum(p[T]*h[T] for T in h)==v);ck(all(p[T]<=caps[T] for T in h))
        gap,cert=capped_lp(h,caps,v);ck(gap<I/6)
        rows.append({'m':m,'Gamma_cap':str(gap),'I':str(I),'certificate':cert})
    (BASE/'out'/'A010_REVIEW_CERTIFICATES.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
def main():
    start=perf_counter();pilot='--pilot' in sys.argv;n=3 if pilot else 4;allE=list(combinations(range(n),2))
    packing={};rows=[];count=0;strict=0
    for mask in range(1,1<<len(allE)):
        E=tuple(e for i,e in enumerate(allE) if mask>>i&1);L,z,y=packing_dual(E,n)
        packing[E]=(L,z,y)
    for E,(L0,z0,y0) in packing.items():
        deg=[sum(v in e for e in E) for v in range(n)];w=[F(1,2*max(deg))]*len(E);D=mul(1+x/4 for x in w)-1
        values=[1 if any(all(x>>v&1 for v in e) for e in E) else -1 for x in range(1<<n)];W=fwht(values)
        P={A:F(a*a,1<<(2*n)) for A,a in enumerate(W) if A and a};v=sum(P.values());I=sum(A.bit_count()*p for A,p in P.items())
        C={};q={};total=F(0)
        for A in range(1,1<<n):
            if any(A>>j&1 and not deg[j] for j in range(n)):ck(W[A]==0);continue
            C[A],runs=enumerate_runs(A,n-1,edges=E);count+=runs
            Ms,_=traces(tuple(j for j in range(n) if A>>j&1),E)
            ck(all(C[A].get(T,0)>=k for T,k in Ms.items()))
            q[A]=evaluate(C[A],w)/D;ck(q[A]>0);total+=q[A]
        ck(total<=1)
        h={T:sum(P[A]*C[A].get(T,F(0))*4**T.bit_count()/q[A] for A in P) for T in range(1,1<<len(E))}
        p={T:mul(w[i]/4 for i in range(len(E)) if T>>i&1)/D for T in h}
        ck(sum(p.values())==1);ck(sum(p[T]*h[T] for T in h)==v)
        caps={};certs={}
        for T in h:
            J=tuple(e for i,e in enumerate(E) if T>>i&1);L,z,y=packing[J];k=len(J)
            caps[T]=min(F(1),F(4)**(1-k)*L**(k-1)/k**k);ck(p[T]<=caps[T])
            certs[str(T)]={'L':str(L),'primal':list(map(str,z)),'vertex_dual':list(map(str,y)),'cap':str(caps[T])}
        gap,cert=capped_lp(h,caps,v);simple=max(h.values())-v;ck(gap<=simple)
        strict+=gap<simple
        rows.append({'edges':E,'weights':list(map(str,w)),'I':str(I),'v':str(v),'actual_output_mass':str(total),
                     'h':{str(T):str(h[T]) for T in h},'uncapped_Gamma':str(simple),'capped_Gamma':str(gap),
                     'bit_gap_over_I':str(2*gap/I),'packing_duals':certs,'cap_LP':cert})
        ck(perf_counter()-start<(55 if pilot else 295))
        (BASE/'out'/'GRAPH_CAP_CHECKPOINT.json').write_text(json.dumps({'rows':rows},indent=2)+'\n',encoding='utf-8')
    review_A010()
    worst=max(rows,key=lambda r:F(r['bit_gap_over_I']))
    result={'status':'PASS','helper_version':'A006-incidence-full-partition-v1','n':n,'tables':len(rows),'actual_distinct_runs':count,
            'strict_cap_improvements':strict,'assertions':checks,'seconds':perf_counter()-start,
            'worst_bit_gap_over_I':worst['bit_gap_over_I'],'worst_edges':worst['edges'],'rows':rows}
    (BASE/'out'/('GRAPH_CAP_PILOT.json' if pilot else 'GRAPH_CAP_FULL.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__':main()
