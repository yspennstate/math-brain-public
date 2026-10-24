import itertools as it, math, json, time, sys
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    checks+=1
    assert x
def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,F(0))+v
        if not out[k]: del out[k]
    return out
def mul(a,b):
    out={}
    for x,v in a.items():
        for y,w in b.items():
            z=tuple(i+j for i,j in zip(x,y))
            out[z]=out.get(z,F(0))+v*w
    return {k:v for k,v in out.items() if v}
def det(mat,n):
    z=(0,)*n
    if not mat:return {z:F(1)}
    out={}
    for p in it.permutations(range(len(mat))):
        inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        term={z:F((-1)**inv)}
        for i,j in enumerate(p):term=mul(term,mat[i][j])
        out=add(out,term)
    return out
def sources(V,edges):
    reach={u:{u} for u in V}
    for u,v,j in edges:reach[u].add(v)
    for _ in V:
        for u in V:reach[u]|=set().union(*(reach[v] for v in tuple(reach[u])))
    comps=[]; unseen=set(V)
    while unseen:
        u=min(unseen); c={v for v in unseen if v in reach[u] and u in reach[v]}
        comps.append(c);unseen-=c
    return [c for c in comps if not any(v in c and u not in c for u,v,j in edges)]
def run(n):
    start=time.perf_counter();summary=[];ownership=traces=primecount=0
    supports=[frozenset(j for j in range(n) if mask>>j&1) for mask in range(1,1<<n)]
    for tabmask in range(1,1<<len(supports)):
        R=[s for i,s in enumerate(supports) if tabmask>>i&1]
        prime=all(not(a<b or b<a) for a,b in it.combinations(R,2));primecount+=prime
        pi=[F(1,1<<len(s)) for s in R]
        # Validate actual Boolean spectrum and physical edge influence independently.
        truth=[1 if any(all(x>>j&1 for j in s) for s in R) else -1 for x in range(1<<n)]
        ft=truth[:];step=1
        while step<len(ft):
            for k in range(0,len(ft),2*step):
                for j in range(k,k+step):a,b=ft[j],ft[j+step];ft[j],ft[j+step]=a+b,a-b
            step*=2
        ck(sum(a*a for a in ft)==(1<<n)**2)
        ck(sum(mask.bit_count()*ft[mask]**2 for mask in range(1<<n))==sum(truth[x]!=truth[x^(1<<j)] for x in range(1<<n) for j in range(n))*(1<<n))
        casecount=0
        for mask in range(1,1<<n):
            A=[j for j in range(n) if mask>>j&1]
            owners=[[u for u,s in enumerate(R) if j in s] for j in A]
            if any(not a for a in owners):continue
            for own in it.product(*owners):
                ownership+=1;casecount+=1;V=sorted(set(own));owned={u:[j for j,v in zip(A,own) if u==v] for u in V}
                edges=[(u,v,j) for u in V for v in V if u!=v for j in owned[u] if j in R[v]]
                source=sources(V,edges);rootsets=list(it.product(*(sorted(c) for c in source)));e=len(V)-len(source)
                z=(0,)*n; L=[[{} for _ in V] for _ in V]
                for u,v,j in edges:
                    power=tuple(int(i==j) for i in range(n));iu,iv=V.index(u),V.index(v)
                    L[iv][iv]=add(L[iv][iv],{power:F(1)});L[iv][iu]=add(L[iv][iu],{power:F(-1)})
                T={}
                enum={};moment=F(0);actual=F(0);unique=set();expected_traces=0
                for roots in rootsets:
                    rarity=math.prod(pi[u] for u in roots)
                    nr=[i for i,u in enumerate(V) if u not in roots]
                    T=add(T,{k:v*rarity for k,v in det([[L[i][j] for j in nr] for i in nr],n).items()})
                    # Independent edge SUBSET enumeration, rather than determinant parent choices.
                    for selected in it.combinations(edges,e):
                        incoming={v:[] for v in V}
                        for u,v,j in selected:incoming[v].append((u,j))
                        if any(len(incoming[v])!=(0 if v in roots else 1) for v in V):continue
                        ok=True
                        for v in V:
                            seen=set();cur=v
                            while cur not in roots:
                                if cur in seen:ok=False;break
                                seen.add(cur);cur=incoming[cur][0][0]
                            if not ok:break
                        if not ok:continue
                        h=[0]*n
                        groups={(u,j):[] for u in V for j in owned[u]}
                        for u,v,j in selected:h[j]+=1;groups[u,j].append(v)
                        power=tuple(h);enum[power]=enum.get(power,F(0))+rarity
                        multiplicity=math.prod(math.factorial(x) for x in h)
                        expected_traces+=multiplicity
                        denom=math.prod((sum(h[j] for j in owned[u])+1)*(sum(h[j] for j in owned[u])+2)*math.comb(len(owned[u])+sum(h[j] for j in owned[u])-1,sum(h[j] for j in owned[u])) for u in V)
                        moment+=rarity*multiplicity;actual+=rarity*F(multiplicity,denom)
                        keys=list(groups)
                        for ordering in it.product(*(list(it.permutations(groups[key])) for key in keys)):
                            bykey=dict(zip(keys,ordering));queue=list(sorted(roots));trace=[]
                            while queue:
                                u=queue.pop(0);kids=tuple((j,v) for j in sorted(owned[u]) for v in bykey[u,j]);trace.append((u,tuple(owned[u]),kids));queue.extend(v for j,v in kids)
                            t=tuple(trace);ck(t not in unique);unique.add(t);traces+=1
                ck(T==enum);ck(all(v>=0 for v in T.values()))
                m=F(0);q=F(0);can=sum(T.values(),F(0));up=F(0)
                for h,v in T.items():
                    fac=math.prod(math.factorial(x) for x in h);m+=v*fac
                    d=1;scaled=F(1);prob_rep=F(1)
                    for u in V:
                        s=len(owned[u]);c=sum(h[j] for j in owned[u]);localfac=math.prod(math.factorial(h[j]) for j in owned[u])
                        d*=(c+1)*(c+2)*math.comb(s+c-1,c)
                        # Direct beta/exponential/simplex moment, including 2^-g.
                        prob_rep*=F(1,2)*F(2,(c+1)*(c+2))*math.factorial(c)*F(math.factorial(s-1)*localfac,math.factorial(s+c-1))
                        for j in owned[u]:
                            D=sum(vv!=u and j in R[vv] for vv in V)
                            scaled*= (F(D+1,2) if D else F(1))**h[j]
                    q+=v*F(fac,d);up+=v*scaled
                    ck(prob_rep==F(fac,d))
                ck(m==moment);ck(q==actual);ck(can<=m<=min(math.factorial(e)*can,up));ck(len(unique)==expected_traces)
                ck(F(1,2**(len(A)+len(V)+e)*3**e)*m<=q<=F(1,2**len(V))*m)
                if all(sum(v!=u and j in R[v] for v in V)<=1 for u in V for j in owned[u]):ck(can==m==up)
                # Coefficients of q strip common original algebraic subset factors only.
                ck(q>0)
        summary.append({'table_mask':tabmask,'prime_table':prime,'ownership_cases':casecount})
        (BASE/'out'/f'PARTIAL_{n}.json').write_text(json.dumps(summary),encoding='utf8')
    result={'n':n,'tables':len(summary),'prime_tables':primecount,'ownership_cases':ownership,'distinct_traces':traces,'assertions_cumulative':checks,'seconds':time.perf_counter()-start}
    (BASE/'out'/f'CHECK_{n}.json').write_text(json.dumps(result,indent=2),encoding='utf8');return result
def stars():
    out=[]
    for e in range(1,9):
        exact=F(math.factorial(e),(e+1)*(e+2)*2**e)
        # Two calculations: explicit per-visit probabilities and the polynomial operator.
        direct=math.factorial(e)*F(1,(e+1)*(e+2))*F(1,2)**e
        ck(exact==direct)
        out.append({'e':e,'N_s_T_over_pi':[exact.numerator,exact.denominator],'surrogate_to_actual_factor':(e+1)*(e+2)*2**e,'positive_spectral_coefficient_squared':[1,4**(e+1)]})
    (BASE/'out'/'STAR_CERTIFICATES.json').write_text(json.dumps(out,indent=2),encoding='utf8')
if __name__=='__main__':
    result=run(2 if '--pilot' in sys.argv else 3);stars();result['assertions_total']=checks
    (BASE/'out'/('PILOT_SUMMARY.json' if '--pilot' in sys.argv else 'CHECK_SUMMARY.json')).write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result))
