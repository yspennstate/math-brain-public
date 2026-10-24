"""Exact full partition-star coefficients, independent ownership enumeration and cap LP."""
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial, comb
from pathlib import Path
from time import perf_counter
import json, sys
BASE=Path(__file__).resolve().parents[1]
checks=0
def ck(ok):
    global checks
    checks+=1
    assert ok, checks
def mul(xs):
    p=F(1)
    for x in xs: p*=x
    return p
def a(k): return F(factorial(k-1),3*8**k*k*(k+1))
def b(k): return F(factorial(k),16*8**k*(k+1)*(k+2))
def formula(A,m):
    B=[j-1 for j in range(1,m+1) if A>>j&1]; T=sum(1<<j for j in B); k=len(B)
    if not A&1: return {T:F(1,32**k)}
    if not k: return {1<<j:F(1,32) for j in range(m)}
    C={T:a(k)}
    for j in range(m):
        if not T>>j&1: C[T|1<<j]=b(k)
    return C
def enumerate_runs(A,m,edges=None):
    # Independent exhaustive coordinate ownership, source components and parent maps.
    E=[{0,j+1} for j in range(m)] if edges is None else list(map(set,edges))
    vertices=[j for j in range(m+1) if A>>j&1]
    choices=[[i for i,e in enumerate(E) if j in e] for j in vertices]
    coefficients={}; seen=set()
    for owner in product(*choices):
        blocks={i:tuple(j for j,o in zip(vertices,owner) if o==i) for i in set(owner)}
        used=tuple(sorted(blocks)); arcs={(i,j) for i in used for j in used if i!=j and set(blocks[i])&E[j]}
        reach={i:{i} for i in used}
        for i,j in arcs: reach[i].add(j)
        for k in used:
            for i in used:
                if k in reach[i]: reach[i]|=reach[k]
        components=[]; left=set(used)
        while left:
            i=min(left); C={j for j in used if j in reach[i] and i in reach[j]}; components.append(C); left-=C
        sources=[C for C in components if not any(i not in C and j in C for i,j in arcs)]
        for roots in product(*(sorted(C) for C in sources)):
            nonroots=[i for i in used if i not in roots]
            options=[[(i,v) for i in used if i!=j for v in blocks[i] if v in E[j]] for j in nonroots]
            for parents in product(*options):
                par=dict(zip(nonroots,parents)); valid=True
                for j in nonroots:
                    path=set(); x=j
                    while x not in roots:
                        if x in path or x not in par: valid=False; break
                        path.add(x); x=par[x][0]
                    if not valid: break
                if not valid: continue
                groups={(i,v):[] for i in used for v in blocks[i]}
                for j,(i,v) in par.items(): groups[i,v].append(j)
                slots=sorted(groups)
                for orders in product(*(list(permutations(groups[s])) for s in slots)):
                    draw=dict(zip(slots,orders)); queue=list(sorted(roots)); visits=[]; prob=F(1,4**len(roots))
                    while queue:
                        i=queue.pop(0); B=blocks[i]; s=len(B)
                        children=tuple((v,j) for v in B for j in draw[i,v]); c=len(children)
                        prob*=F(1,s*(s+1)*comb(2,s)*(c+1)*(c+2)*comb(s+c-1,c))
                        visits.append((i,B,children)); queue.extend(j for v,j in children)
                    key=(tuple(sorted(roots)),tuple(visits))
                    ck(key not in seen); seen.add(key)
                    ck(len(visits)==len(used))
                    T=sum(1<<j for j in used); coefficients[T]=coefficients.get(T,F(0))+prob
    return coefficients,len(seen)
def spectrum_check(m):
    values=[1 if x&1 and x>>1 else -1 for x in range(1<<(m+1))]
    W=list(values); step=1
    while step<len(W):
        for i in range(0,len(W),2*step):
            for j in range(i,i+step): W[j],W[j+step]=W[j]+W[j+step],W[j]-W[j+step]
        step*=2
    P={A:F(v*v,len(W)**2) for A,v in enumerate(W)}; delta=F(1,4**m)
    ck(P[0]==delta and P[1]==(1-F(1,2**m))**2)
    ck(all(P[A]==delta for A in range(2,len(W))))
    edges=sum(values[x]!=values[x^(1<<j)] for x in range(len(W)) for j in range(m+1) if not x>>j&1)
    I=F(edges,1<<m); ck(I==sum(A.bit_count()*p for A,p in P.items()))
    ck(I==1+F(m-1,2**m)); return P
def cardinality(m):
    D=(1+F(1,4*m))**m-1; delta=F(1,4**m); P0=(1-F(1,2**m))**2
    h={}
    for t in range(1,m+1):
        v=delta*D*(4*m)**t
        v+=delta*D*4**t*m**t*a(t)/(a(t)+b(t)*F(m-t,m))
        if t>=2:
            v+=t*delta*D*4**t*m**(t-1)*b(t-1)/(a(t-1)+b(t-1)*F(m-t+1,m))
        else: v+=4*D*P0
        h[t]=v
    caps={t:comb(m,t)*F(4)**(1-t)/t**t for t in h}
    actual={t:F(comb(m,t),(4*m)**t)/D for t in h}
    v=1-delta; I=1+F(m-1,2**m)
    ck(sum(actual.values())==1); ck(sum(actual[t]*h[t] for t in h)==v)
    ck(all(actual[t]<=caps[t] for t in h))
    left=F(1); z={t:F(0) for t in h}; threshold=None
    for t in sorted(h,key=h.get,reverse=True):
        z[t]=min(caps[t],left);left-=z[t]
        if not left:threshold=h[t];break
    ck(left==0); primal=sum(z[t]*h[t] for t in h)
    dual=threshold+sum(caps[t]*max(h[t]-threshold,0) for t in h)
    ck(primal==dual); gap=primal-v;ck(gap>=0)
    universal=4*D*(P0+F(2*comb(2*m,m)+comb(2*m,m-1),4**m))-v
    ck(gap<=universal); ck(universal<F(91,48)); ck(2*gap<F(91,24)*I)
    return {'m':m,'D':str(D),'v':str(v),'I':str(I),'h':{str(t):str(h[t]) for t in h},
            'aggregate_caps':{str(t):str(caps[t]) for t in h},'physical_root_law':{str(t):str(actual[t]) for t in h},
            'LP_primal':str(primal),'LP_dual':str(dual),'threshold':str(threshold),
            'aggregate_primal':{str(t):str(z[t]) for t in h},'Gamma_cap':str(gap),'bit_gap_over_I_bound':str(2*gap/I),
            'gap_below_I_over_6':gap<I/6,'universal_natural_gap_upper':str(universal)}
def main():
    start=perf_counter();pilot='--pilot' in sys.argv; top=3 if pilot else 32; enumtop=3 if pilot else 4
    rows=[];enumrows=[];traces=0; spectra=0
    for m in range(2,top+1):
        row=cardinality(m); rows.append(row)
        if m<=enumtop:
            P=spectrum_check(m);spectra+=1; total=F(0); D=F(row['D']); h={T:F(0) for T in range(1,1<<m)}
            for A in range(1,1<<(m+1)):
                C,count=enumerate_runs(A,m); ck(C==formula(A,m));traces+=count
                numerator=sum(k*F(1,m**T.bit_count()) for T,k in C.items()); q=numerator/D;total+=q
                for T,k in C.items():h[T]+=P[A]*k*4**T.bit_count()/q
                # Nonuniform check distinguishes singleton hub monomials from pair-owner monomials.
                w=[F(i+1,m*(m+1)) for i in range(m)]; W=sum(k*mul(w[j] for j in range(m) if T>>j&1) for T,k in C.items())
                ck(W>0)
            ck(total<=1);ck(all(h[T]==F(row['h'][str(T.bit_count())]) for T in h))
            enumrows.append({'m':m,'all_nonempty_outputs':(1<<(m+1))-1,'all_output_mass':str(total),'actual_distinct_runs':'enumerated with complete chronological keys'})
        (BASE/'out'/'STAR_CHECKPOINT.json').write_text(json.dumps({'cardinality_rows':rows,'enumerated':enumrows},indent=2)+'\n',encoding='utf-8')
        ck(perf_counter()-start<(55 if pilot else 295))
    result={'status':'PASS','helper_version':'A006-full-star-v1','m_domain':[2,top],'cardinality_cases':len(rows),
            'enumerated_stars':len(enumrows),'actual_distinct_runs':traces,'FWHT_tables':spectra,'assertions':checks,
            'seconds':perf_counter()-start,'rows':rows,'enumeration':enumrows}
    (BASE/'out'/('STAR_PILOT.json' if pilot else 'STAR_FULL.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','enumeration')}))
if __name__=='__main__':main()
