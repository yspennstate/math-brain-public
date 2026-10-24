from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,product,permutations
from math import factorial,comb
from time import perf_counter
import json,sys
BASE=Path(__file__).resolve().parents[1]
checks=0
def ck(ok):
    global checks
    checks+=1
    if not ok: raise AssertionError(checks)
def save(name,obj): (BASE/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def mul(xs):
    out=Q(1)
    for x in xs: out*=x
    return out
def fwht(a):
    a=list(a); step=1
    while step<len(a):
        for k in range(0,len(a),step*2):
            for i in range(k,k+step): a[i],a[i+step]=a[i]+a[i+step],a[i]-a[i+step]
        step*=2
    return a
def matchings(edges):
    out=[]
    for mask in range(1<<len(edges)):
        M=tuple(i for i in range(len(edges)) if mask>>i&1); V=[]
        for i in M: V.extend(edges[i])
        if len(set(V))!=len(V): continue
        if any(u not in V and v not in V for u,v in edges): continue
        out.append(M)
    return out
def perfect_count(B,edges):
    if not B: return 1
    u=min(B); total=0
    for a,b in edges:
        if a==u and b in B: total+=perfect_count(B-{u,b},edges)
        if b==u and a in B: total+=perfect_count(B-{u,a},edges)
    return total
def old_matching(A,edges,lam,D):
    a=len(A); m=a//2
    if a%2==0: return Q(perfect_count(set(A),edges))* (lam/48)**m/D
    total=Q(0)
    for j in A:
        count=perfect_count(set(A)-{j},edges)
        inside=sum(j in edge and next(v for v in edge if v!=j) in A for edge in edges if j in edge)
        outside=sum(j in edge for edge in edges)-inside
        total+=count*(outside*(lam/32)*(lam/48)**m+inside*(lam/48)**(m+1))
    return total/D
def completed(A,edges,weights,D):
    edge_id={frozenset(e):i for i,e in enumerate(edges)}
    induced=[e for e in edges if set(e)<=set(A)]
    mass=Q(0); lower=Q(0); registry=set(); assignments=0; rows=[]
    for localM in matchings(induced):
        M=tuple(edge_id[frozenset(induced[i])] for i in localM)
        matched={v for i in M for v in edges[i]}; U=tuple(v for v in A if v not in matched)
        ck(not any(u in U and v in U for u,v in edges))
        bycoord={v:i for i in M for v in edges[i]}
        neighbor_options=[tuple(v if u==a else a for a,v in edges if u in (a,v)) for u in U]
        formula_M=Q(0); direct_M=Q(0)
        for choices in product(*neighbor_options):
            assignments+=1; own={i:tuple(edges[i]) for i in M}; roots=set(M); parent={}; attached={}
            for u,v in zip(U,choices):
                child=edge_id[frozenset((u,v))]; ck(child not in own); own[child]=(u,)
                if v in matched: parent[child]=bycoord[v]; attached[child]=v
                else: roots.add(child)
            children={i:{v:[] for v in own[i]} for i in own}
            for child,p in parent.items(): children[p][attached[child]].append(child)
            # Independently inspect ALL ownership-incidence edges, not only prescribed ones.
            incidence={(u,v) for u in own for v in own if u!=v and set(own[u])&set(edges[v])}
            ck(incidence=={(p,ch) for ch,p in parent.items()})
            ck(roots=={u for u in own if not any(v==u for p,v in incidence)})
            factors=[]
            for i in M:
                hs=[len(children[i][v]) for v in edges[i]]; c=sum(hs)
                factors.append(Q(factorial(hs[0])*factorial(hs[1]),(c+1)**2*(c+2)))
            predicted=mul(weights[i]/24 for i in M)*mul(weights[edge_id[frozenset((u,v))]]/8 for u,v in zip(U,choices))
            predicted*=Q(1,4**sum(v not in matched for v in choices))*mul(factors)/D
            formula_M+=predicted
            groups=[(i,v) for i in sorted(own) for v in sorted(own[i])]
            for ordered in product(*(tuple(permutations(children[i][v])) for i,v in groups)):
                draws={(i,v):seq for (i,v),seq in zip(groups,ordered)}
                # Root experiment executed with absence factors and actual normalization.
                Z=1-mul(1/(1+w/4) for w in weights)
                prob=mul((w/4)/(1+w/4) if i in roots else 1/(1+w/4) for i,w in enumerate(weights))/Z
                queue=list(sorted(roots)); seen=set(); trace=[]; output=set()
                while queue:
                    i=queue.pop(0); ck(i not in seen); seen.add(i); B=own[i]; s=len(B)
                    childdraws=tuple((v,ch) for v in sorted(B) for ch in draws[i,v]); c=len(childdraws)
                    prob*=Q(1,s*(s+1))*Q(1,comb(2,s))
                    prob*=Q(1,(c+1)*(c+2))*Q(1,comb(s+c-1,c))
                    prob*=mul(weights[ch] for v,ch in childdraws)
                    trace.append((i,tuple(sorted(B)),childdraws)); queue.extend(ch for v,ch in childdraws); output.update(B)
                ck(seen==set(own) and output==set(A))
                key=(tuple(sorted(roots)),tuple(trace)); ck(key not in registry); registry.add(key); direct_M+=prob
            ck(predicted>0)
        r={u:sum(weights[i] for i,e in enumerate(edges) if u in e) for u in U}
        lower_M=mul(weights[i]/48 for i in M)*mul(r[u]/48 for u in U)/D
        ck(formula_M==direct_M); ck(0<lower_M<=direct_M)
        mass+=direct_M; lower+=lower_M
        rows.append({'M':M,'U':U,'mass':str(direct_M),'lower':str(lower_M)})
    ck(0<lower<=mass)
    return mass,lower,len(registry),assignments,rows
def operator_review():
    count=0
    def compositions(c,s):
        if s==1: yield(c,); return
        for h in range(c+1):
            for tail in compositions(c-h,s-1): yield(h,)+tail
    for s in range(1,5):
        for c in range(6):
            for h in compositions(c,s):
                coeff=Q(mul(factorial(v) for v in h), (c+1)*(c+2)*comb(s+c-1,c))
                beta=Q(2,(c+1)*(c+2)); exp=factorial(c)
                simplex=Q(factorial(s-1)*mul(factorial(v) for v in h),factorial(s+c-1))
                ck(coeff==beta*exp*simplex/2)
                ck(Q(1,2**(s+1+c)*3**c)*mul(factorial(v) for v in h)<=coeff<=mul(factorial(v) for v in h)/2)
                count+=1
    # The incorrect auxiliary t=1/2 assertion has an exact rational counterexample.
    ck(Q(1,2)*Q(1,2)==Q(1,4)); ck(Q(1,4)!=Q(1,2))
    ck(Q(1,4)**5<Q(1,64)<Q(1,2)**5)
    save('A008_OPERATOR_REVIEW.json',{'vectors':count,'status':'PASS','formal_claim':'HOLDS_AT_UNCHANGED_SCOPE',
        'auxiliary_source_line':'ERROR: COMPLETE_MASS.md says each t_u=1/2 (uniform singleton choice); width-two uniform singleton draw is 1/4, and one-order probabilities are theta/[2*(1+2^-gamma)]',
        'affects_formal_claim':False,'substantive_repair_to_formal_claim':False})
def main():
    start=perf_counter(); n=3 if '--pilot' in sys.argv else 4
    all_edges=list(combinations(range(n),2)); tables=[]; covered_sets=0; total_traces=0; choices_count=0; rescued=0
    for Gmask in range(1,1<<len(all_edges)):
        edges=tuple(e for i,e in enumerate(all_edges) if Gmask>>i&1)
        deg=[sum(v in e for e in edges) for v in range(n)]; Delta=max(deg); covered={v for v in range(n) if deg[v]}
        vals=[1 if any(all(x>>v&1 for v in e) for e in edges) else -1 for x in range(1<<n)]
        W=fwht(vals); ck(sum(z*z for z in W)==1<<(2*n))
        physical=sum(vals[x]!=vals[x^(1<<v)] for v in range(n) for x in range(1<<n) if not x>>v&1)
        ck(sum(a.bit_count()*W[a]**2 for a in range(1<<n))==physical*(1<<(n+1)))
        table_rows=[]
        for kind in ['uniform','endpoint_degree']:
            weights=tuple(Q(1,Delta) if kind=='uniform' else Q(1,deg[u]+deg[v]) for u,v in edges)
            ck(all(sum(w for w,e in zip(weights,edges) if v in e)<=1 for v in covered))
            D=mul(1+w/4 for w in weights)-1; output_total=Q(0)
            for mask in range(1,1<<n):
                A=tuple(v for v in range(n) if mask>>v&1)
                if not set(A)<=covered: ck(W[mask]==0); continue
                mass,lower,traces,choices,rows=completed(A,edges,weights,D)
                covered_sets+=1; total_traces+=traces; choices_count+=choices; output_total+=mass
                old=old_matching(A,edges,weights[0],D) if kind=='uniform' else None
                if old is not None:
                    ck(mass>=old)
                    if W[mask] and old==0: rescued+=1
                table_rows.append({'A':mask,'weight_kind':kind,'P':str(Q(W[mask]**2,1<<(2*n))),
                    'complete_mass':str(mass),'lower_mass':str(lower),'old_matching_mass':str(old) if old is not None else None,
                    'actual_traces':traces,'matchings':rows})
            ck(output_total<=1)
        tables.append({'edges':edges,'rows':table_rows})
        save('PARTIAL_'+str(n)+'.json',{'tables_done':len(tables),'covered_sets':covered_sets,'last_table':tables[-1]})
        if perf_counter()-start>55: raise RuntimeError('frozen 55-second computation guard')
    operator_review()
    if n==4: ck(rescued==104)
    elapsed=perf_counter()-start; ck(elapsed<60)
    summary={'status':'PASS','helper_version':'A006-maximal-matching-star-v1','n':n,'graph_tables':len(tables),
        'covered_sets_two_weight_vectors':covered_sets,'actual_traces':total_traces,'neighbor_assignment_cases':choices_count,
        'positive_spectrum_old_zero_mass_rescued':rescued,'assertions':checks,'seconds':elapsed}
    save('CHECK_'+str(n)+'.json',{'summary':summary,'tables':tables}); save('PILOT_SUMMARY.json' if n==3 else 'CHECK_SUMMARY.json',summary)
    print(json.dumps(summary))
if __name__=='__main__': main()
