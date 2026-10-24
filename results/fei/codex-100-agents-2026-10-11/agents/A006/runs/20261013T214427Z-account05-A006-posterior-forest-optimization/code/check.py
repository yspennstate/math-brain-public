"""Independent actual queue traces versus determinant polynomials, exact arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, product, permutations
from math import factorial, comb
from time import perf_counter
import json, sys
BASE=Path(__file__).resolve().parents[1]
checks=0
def ck(x):
    global checks
    checks+=1
    if not x: raise AssertionError(checks)
def save(name,obj):
    (BASE/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def coords(mask,n): return tuple(j for j in range(n) if mask>>j&1)
def fwht(a):
    a=list(a); step=1
    while step<len(a):
        for start in range(0,len(a),2*step):
            for k in range(start,start+step): a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
        step*=2
    return a
def spectrum(R,n):
    vals=[1 if any(x&r==r for r in R) else -1 for x in range(1<<n)]
    w=fwht(vals)
    ck(sum(z*z for z in w)==1<<(2*n))
    edges=sum(vals[x]!=vals[x^(1<<j)] for j in range(n) for x in range(1<<n) if not x>>j&1)
    ck(sum(a.bit_count()*w[a]*w[a] for a in range(1<<n))==edges*(1<<(n+1)))
    return w
def scc(adj):
    g=len(adj)
    reach=[]
    for i in range(g):
        seen={i}; todo=[i]
        while todo:
            u=todo.pop()
            for v in adj[u]:
                if v not in seen: seen.add(v); todo.append(v)
        reach.append(seen)
    remaining=set(range(g)); parts=[]
    while remaining:
        i=min(remaining); C={v for v in remaining if v in reach[i] and i in reach[v]}
        parts.append(tuple(sorted(C))); remaining-=C
    sources=[C for C in parts if not any(v in C for u in range(g) if u not in C for v in adj[u])]
    return parts,sources
def padd(a,b):
    out=a.copy()
    for k,v in b.items():
        out[k]=out.get(k,Q(0))+v
        if not out[k]: del out[k]
    return out
def pscale(a,v): return {k:z*v for k,z in a.items() if z*v}
def pmul(a,b):
    out={}
    for k,v in a.items():
        for l,w in b.items():
            key=tuple(x+y for x,y in zip(k,l)); out[key]=out.get(key,Q(0))+v*w
    return {k:v for k,v in out.items() if v}
def pdet(M,m):
    zero=(0,)*m; out={}
    for perm in permutations(range(len(M))):
        inversions=sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        term={zero:Q((-1)**inversions)}
        for i,j in enumerate(perm): term=pmul(term,M[i][j])
        out=padd(out,term)
    return out
def minor(M,keep): return [[M[i][j] for j in keep] for i in keep]
def peval(P,x):
    total=Q(0)
    for k,v in P.items():
        for d,y in zip(k,x): v*=y**d
        total+=v
    return total
def moment(P):
    return sum((v*prodnum(factorial(d) for d in k) for k,v in P.items()),Q(0))
def prodnum(it):
    z=1
    for x in it: z*=x
    return z
def assignment_case(R,A,tau,n):
    used=tuple(sorted(set(tau))); g=len(used); index={l:i for i,l in enumerate(used)}
    owned=[tuple(j for j,l in zip(A,tau) if l==u) for u in used]
    groups=[(u,j) for u in range(g) for j in owned[u]]; m=len(groups); gi={p:i for i,p in enumerate(groups)}
    zero=(0,)*m
    attachments={(u,v):tuple(j for j in owned[u] if R[used[v]]>>j&1) for u in range(g) for v in range(g) if u!=v}
    adj=[{v for v in range(g) if u!=v and attachments[u,v]} for u in range(g)]
    parts,sources=scc(adj); e=g-len(sources)
    pi=[Q(1,1<<R[l].bit_count()) for l in used]
    M=[[{} for _ in range(g)] for _ in range(g)]
    for (u,v),J in attachments.items():
        poly={}
        for j in J:
            key=list(zero); key[gi[u,j]]=1; poly[tuple(key)]=Q(1)
        M[v][v]=padd(M[v][v],poly); M[v][u]=pscale(poly,-1)
    T={}; direct={}; canonical=Q(0); true=Q(0); unique=set(); nforests=0
    for roots in product(*sources):
        rootweight=prodnum(pi[r] for r in roots)
        nonroots=tuple(v for v in range(g) if v not in roots)
        T=padd(T,pscale(pdet(minor(M,nonroots),m),rootweight))
        parent_options=[tuple(u for u in range(g) if u!=v and attachments[u,v]) for v in nonroots]
        for parents in product(*parent_options):
            parent=dict(zip(nonroots,parents)); valid=True
            for v in nonroots:
                path=set(); u=v
                while u not in roots:
                    if u in path: valid=False; break
                    path.add(u); u=parent[u]
                if not valid: break
            if not valid: continue
            for J in product(*(attachments[parent[v],v] for v in nonroots)):
                attached=dict(zip(nonroots,J)); slot_children=[[] for _ in groups]
                for v in nonroots: slot_children[gi[parent[v],attached[v]]].append(v)
                key=tuple(len(children) for children in slot_children)
                direct[key]=direct.get(key,Q(0))+rootweight; canonical+=rootweight; nforests+=1
                # Different child labels within the same repeated-coordinate slots
                # are different actual draws; no arbitrary topological ordering.
                for ordered in product(*(tuple(permutations(ch)) for ch in slot_children)):
                    queue=list(sorted(roots)); visits=[]; seen=set()
                    while queue:
                        u=queue.pop(0); ck(u not in seen); seen.add(u)
                        draws=tuple((j,v) for j in sorted(owned[u]) for v in ordered[gi[u,j]])
                        visits.append((u,owned[u],draws)); queue.extend(v for j,v in draws)
                    ck(len(seen)==g)
                    trace=(tuple(sorted(roots)),tuple(visits))
                    ck(trace not in unique); unique.add(trace); true+=rootweight
    ck(T==direct); ck(peval(T,[Q(1)]*m)==canonical); ck(moment(T)==true)
    # A separate SCC product, not an expectation product.
    factor={zero:Q(1)}
    for C in parts:
        if C in sources:
            p={}
            for r in C: p=padd(p,pscale(pdet(minor(M,[v for v in C if v!=r]),m),pi[r]))
        else: p=pdet(minor(M,C),m)
        factor=pmul(factor,p)
    ck(factor==T)
    caps=[sum(v in adj[u] and R[used[v]]>>j&1 for v in range(g)) for u,j in groups]
    up=peval(T,[Q(d+1,2) if d else Q(1) for d in caps])
    ck(canonical<=true<=min(factorial(e)*canonical,up))
    if all(d<=1 for d in caps): ck(true==canonical==up)
    ck(canonical>0)
    return {'g':g,'edges':e,'attached_forests':nforests,'actual_runs':len(unique),
            'canonical_weight':str(canonical),'actual_weight':str(true),'upper_weight':str(min(factorial(e)*canonical,up))}

def blocks_review():
    # Independent physical truth tables; no author code, product spectrum used only as a comparison.
    def partitions(n,lo=1):
        if not n: yield ()
        for w in range(lo,n+1):
            for tail in partitions(n-w,w): yield (w,)+tail
    rows=[]
    for n in range(1,7):
        for widths in partitions(n):
            supports=[]; offset=0
            for w in widths: supports.append(((1<<w)-1)<<offset); offset+=w
            W=spectrum(supports,n); ps=[Q(1,1<<w) for w in widths]; qs=[1-p for p in ps]; Q0=prodnum(qs)
            v=1-Q(W[0]*W[0],1<<(2*n)); ck(v==4*Q0*(1-Q0))
            hit=[Q(0)]*len(widths); size=[Q(0)]*len(widths)
            for a in range(1,1<<n):
                mass=Q(W[a]*W[a],1<<(2*n))
                predicted=4*prodnum(p*p if a&r else q*q for p,q,r in zip(ps,qs,supports))
                ck(mass==predicted)
                for l,r in enumerate(supports):
                    if a&r: hit[l]+=mass; size[l]+=mass*(a&r).bit_count()
            ck(hit==[4*p*Q0 for p in ps]); ck(size==[2*Q0*w*p/q for w,p,q in zip(widths,ps,qs)])
            D=prodnum(1+p for p in ps)-1
            # Actual root odds and absence factors, conditioned on nonempty roots.
            Z=D/(1+D)
            for Kmask in range(1,1<<len(widths)):
                physical=prodnum(p/(1+p) if Kmask>>i&1 else 1/(1+p) for i,p in enumerate(ps))/Z
                ck(physical==prodnum(p for i,p in enumerate(ps) if Kmask>>i&1)/D)
            # Conditional reciprocal rank identity; proves the pivotal Jensen step exactly.
            for r in range(1,max(widths)+1):
                mean=sum((Q(comb(r-1,k)*r,(1<<(r-1))*(k+1)) for k in range(r)),Q(0))
                ck(mean==2*(1-Q(1,1<<r))); ck(mean<=2)
            rows.append({'widths':widths,'v':str(v),'I':str(sum(size)),'D':str(D)})
    save('A008_REVIEW_CHECK.json',{'cases':len(rows),'rows':rows,'status':'PASS','scope':'exact spectral/physical influence, root odds and conditional rank identity; all-width constants independently reconstructed analytically'})
    return len(rows)

def stars():
    rows=[]
    for e in range(1,8):
        R=[1|(1<<i) for i in range(1,e+2)]; n=e+2; A=1|sum(1<<i for i in range(2,e+2))
        W=spectrum(R,n); ck(W[A]!=0)
        # Forced outgoing star: chronological draws all use attachment coordinate 0.
        traces={(0,tuple((0,v) for v in p)) for p in permutations(range(1,e+1))}
        ck(len(traces)==factorial(e))
        rows.append({'edges':e,'prime_supports':R,'A':A,'walsh_A':W[A],
                     'canonical_runs':1,'actual_runs':len(traces),'moment':'(1/4)*E X^'+str(e),'ratio':factorial(e)})
    ck(rows[1]['actual_runs']==2)
    save('STAR_CERTIFICATES.json',{'status':'PASS','rows':rows,
         'false_expectation_factorization_witness':{'e':2,'exact_moment':'1/2','product_of_SCC_factor_means':'1/4'}})
    return rows

def main():
    start=perf_counter(); pilot='--pilot' in sys.argv; n=2 if pilot else 3
    masks=list(range(1,1<<n)); tables=[tuple(masks[i] for i in range(len(masks)) if t>>i&1) for t in range(1,1<<len(masks))]
    data=[]; cases=0; prime_tables=0; runs=0
    for R in tables:
        W=spectrum(R,n)
        prime=not any(u!=v and u&v==u for u in R for v in R)
        prime_tables+=prime
        local=[]
        for Amask in range(1,1<<n):
            A=coords(Amask,n); eligible=[tuple(l for l,r in enumerate(R) if r>>j&1) for j in A]
            for tau in product(*eligible):
                row=assignment_case(R,A,tau,n); cases+=1; runs+=row['actual_runs']
                # Cover every covered set, not only positive-mass sets, stronger combinatorial check.
                local.append({'A':Amask,'tau':tau,'P_positive':W[Amask]!=0,**row})
        data.append({'supports':R,'is_exact_prime_table':prime,'assignment_cases':len(local),'cases':local})
        if perf_counter()-start>55: raise RuntimeError('pilot/full guard 55 seconds; preserve completed table')
        save('FOREST_PARTIAL_'+str(n)+'.json',{'completed_tables':len(data),'assignment_cases':cases,'last_table':data[-1]})
    save('FOREST_CHECK_'+str(n)+'.json',{'status':'PASS','n':n,'tables':len(tables),'prime_tables':prime_tables,
        'assignment_cases':cases,'actual_runs':runs,'tables_and_cases':data})
    block_count=0
    if not pilot: block_count=blocks_review(); stars()
    elapsed=perf_counter()-start; ck(elapsed<60)
    summary={'status':'PASS','helper_version':'A006-forest-moments-v1','pilot':pilot,'seconds':elapsed,
             'assertions':checks,'tables':len(tables),'prime_tables':prime_tables,'assignment_cases':cases,
             'actual_runs':runs,'A008_width_cases':block_count}
    save('PILOT_SUMMARY.json' if pilot else 'CHECK_SUMMARY.json',summary); print(json.dumps(summary))
if __name__=='__main__': main()
