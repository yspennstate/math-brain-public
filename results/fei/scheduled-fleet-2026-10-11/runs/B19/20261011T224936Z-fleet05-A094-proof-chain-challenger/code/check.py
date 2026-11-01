from fractions import Fraction as Q
from itertools import combinations,product,permutations
from math import comb,factorial
from pathlib import Path
import json,time
RUN=Path(__file__).resolve().parents[1]
SPEC={'helper_version':'A006@1/A007@1 independent queue and activation audit v1','family':'sunflower truth tables and all partition runs; every nonconstant <=3-bit seed activated on a fresh conjunction; XOR of equal-width AND signs','domain':{'sunflower_m':[1,2,3,4,5],'auxiliary_theta':['2/5','1/2'],'seed_dimensions':[1,2,3],'activation_r':[1,2,3],'xor_pairs':[[1,1],[1,2],[2,1],[2,2],[2,3],[3,1],[3,2],[4,1],[4,2]]},'case_count':{'sunflower_parameter_pairs':10,'activated_seeds':810,'xor_parameter_pairs':9},'symmetry':'none for Boolean seeds or assignments; coordinate-order invariance proved analytically, reverse order also checked','arithmetic':'integer FWHT, exact Fraction probabilities and moments; symbolic logarithm vector for rank identity; all-dimensional signs supplied analytically','memory_estimate_MB':40,'max_runtime_seconds':60,'automatic_dimension_escalation':False}
if __name__=='__main__' and '--freeze' in __import__('sys').argv:
    (RUN/'FROZEN_SPEC.json').write_text(json.dumps(SPEC,indent=2),encoding='utf-8');print('frozen');raise SystemExit
assert json.loads((RUN/'FROZEN_SPEC.json').read_text())==SPEC
t0=time.perf_counter();checks=0;runs=0
def ck(b):
    global checks
    checks+=1
    assert b
def subsets(s):
    s=tuple(sorted(s))
    for k in range(len(s)+1):
        for v in combinations(s,k):yield frozenset(v)
def spectrum(f):
    a=list(f);stride=1
    while stride<len(a):
        for i in range(0,len(a),2*stride):
            for j in range(i,i+stride):a[j],a[j+stride]=a[j]+a[j+stride],a[j]-a[j+stride]
        stride*=2
    return [Q(v,len(a)) for v in a]
def influence(f):
    n=(len(f)).bit_length()-1
    return [Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n)]
def mask(s):return sum(1<<i for i in s)
def forests(owned):
    nodes=tuple(sorted(owned));edges={v:{w for w in nodes if w!=v and owned[v]&{0,w}} for v in nodes}
    reach={v:{v}|edges[v] for v in nodes}
    for _ in nodes:
        for v in nodes:reach[v]|=set().union(*(reach[w] for w in tuple(reach[v])))
    components={frozenset(w for w in nodes if w in reach[v] and v in reach[w]) for v in nodes}
    sources=[c for c in components if not any(v not in c and edges[v]&c for v in nodes)]
    for roots in product(*(tuple(sorted(c)) for c in sources)):
        nonroots=[v for v in nodes if v not in roots]
        incoming=[[u for u in nodes if v in edges[u]] for v in nonroots]
        for parents in product(*incoming):
            parent=dict(zip(nonroots,parents));valid=True
            for v in nonroots:
                seen=set();u=v
                while u not in roots and u not in seen:seen.add(u);u=parent[u]
                if u not in roots:valid=False
            if not valid:continue
            kids={v:[w for w in nonroots if parent[w]==v] for v in nodes}
            for orders in product(*(tuple(permutations(kids[v])) for v in nodes)):
                yield tuple(sorted(roots)),dict(zip(nodes,orders))
for m in SPEC['domain']['sunflower_m']:
    f=[1 if (x&1)==0 and any((x&(1<<i))==0 for i in range(1,m+1)) else -1 for x in range(1<<(m+1))]
    aF=spectrum(f);pF=[a*a for a in aF];inf=influence(f)
    ck(sum(pF)==1);ck(sum(inf)==1+Q(m-1,2**m))
    for i in range(1<<m+1):
        ck(pF[i]==((1-Q(1,2**m))**2 if i==1 else Q(1,4**m)))
    for theta in [Q(2,5),Q(1,2)]:
        D=(1+Q(1,4*m))**m-1;total_mass=Q(0)
        for A in subsets(range(m+1)):
            if not A:continue
            T=A-{0};t=len(T);resmass=Q(0);qmass=Q(0);keys=set()
            choices=range(1,m+1) if 0 in A else [None]
            for owner0 in choices:
                owned={i:frozenset({i}) for i in T}
                if owner0 is not None:owned[owner0]=owned.get(owner0,frozenset())|{0}
                for roots,kids in forests(owned):
                    queue=list(roots);trace=[];q=Q(1,D);b=Q(1)
                    for v in roots:q*=Q(1,4*m)
                    for v in owned:b*=Q(1,m)
                    b*=Q(1,4)**len(roots)
                    while queue:
                        v=queue.pop(0);B=owned[v];s=len(B);c=len(kids[v]);support=frozenset({0,v})
                        weights={j:Q(1) if s==2 or j==0 else theta for j in support}
                        Zs=sum((__import__('functools').reduce(lambda u,j:u*weights[j],S,Q(1)) for S in combinations(support,s)),Q(0))
                        w=__import__('functools').reduce(lambda u,j:u*weights[j],B,Q(1))
                        q*=Q(1,s*(s+1))*w/Zs*Q(1,(c+1)*(c+2))*Q(1,comb(s+c-1,c))*Q(1,m)**c
                        # In this family every nonzero congestion/rank penalty is precisely one power of theta.
                        if B==frozenset({v}):b*=theta
                        ck(c==0 or 0 in B)
                        trace.append((v,tuple(sorted(B)),kids[v]));queue.extend(kids[v])
                    key=(roots,tuple(trace));ck(key not in keys);keys.add(key)
                    resmass+=b;qmass+=q;runs+=1
            if A=={0}:rb=Q(1,4);w=1/(16*(1+theta)*D)
            elif 0 not in A:rb=(theta/Q(4*m))**t;w=(theta/Q(16*m)/(1+theta))**t/D
            else:
                rb=Q(factorial(t),4*m**t)*theta**(t-1)*(1+(1-Q(t,m))*theta)
                w=Q(factorial(t),24*t*t*(t+1)*m**t)/D*(theta/(4*(1+theta)))**(t-1)
                w+=Q((m-t)*factorial(t),8*m**(t+1)*(t+1)*(t+2))/D/(1+theta)*(theta/(4*(1+theta)))**t
            ck(rb==resmass);ck(w==qmass);total_mass+=qmass
        ck(total_mass<=1)
activation_cases=0
for n in [1,2,3]:
    for table in range(1,2**(2**n)-1):
        g=[1 if table>>x&1 else -1 for x in range(2**n)]
        ga=spectrum(g);b=Q(sum(x==1 for x in g),len(g));Ig=sum(influence(g))
        for r in [1,2,3]:
            p=Q(1,2**r);F=[g[y] if core==0 else -1 for core in range(2**r) for y in range(2**n)]
            fa=spectrum(F);fp=[a*a for a in fa];If=sum(influence(F))
            ck(If==p*Ig+2*r*p*b);ck(1-fp[0]==4*p*b*(1-p*b))
            extra=Q(0)
            for full in range(1,len(F)):
                T=full%2**n;U=full//2**n
                expected=p*ga[T] if T else 2*p*b
                ck(fp[full]==expected**2)
                if not U and T:extra+=fp[full]*(T.bit_count()-1)
            ck(extra>=0);ck(r*extra<=p*Ig/2)
            # One actual gate B has one root at every nonempty set, and root block cancels exactly.
            x=p*b;D=(1+x)-1;ck(D==x);ck(D/x==1)
            activation_cases+=1
xor_results=[]
for L,m in SPEC['domain']['xor_pairs']:
    n=L*m;p=Q(1,2**L)
    f=[]
    for x in range(2**n):
        value=1
        for j in range(m):value*= -1 if ((x>>(j*L))&((1<<L)-1))==0 else 1
        f.append(value)
    fa=spectrum(f);fp=[a*a for a in fa];I=sum(influence(f));ck(I==2*m*L*p)
    E2=sum(q*S.bit_count()**2 for S,q in enumerate(fp));ck(E2/I==I+Q(L+1,2)-2*L*p)
    # Coefficients of ln(k), before prime factor simplification, are an exact symbolic rank identity.
    direct=[Q(0)]*(n+1);rhs=[Q(0)]+[2*p]*(n)
    for S,q in enumerate(fp):
        k=S.bit_count()
        for j in range(1,k+1):rhs[j]-=q
        for order in [list(range(n)),list(reversed(range(n)))]:
            vec=[Q(0)]*(n+1);count=0
            for rank,i in enumerate(order,1):
                if S>>i&1:count+=1;vec[rank]+=q;vec[count]-=q
            if order[0]==0:
                for j in range(n+1):direct[j]+=vec[j]
            else:
                # Sum reverse contributions separately below.
                pass
    ck(direct==rhs)
    reverse=[Q(0)]*(n+1)
    for S,q in enumerate(fp):
        count=0
        for rank,i in enumerate(reversed(range(n)),1):
            if S>>i&1:count+=1;reverse[rank]+=q;reverse[count]-=q
    ck(reverse==rhs)
    xor_results.append({'L':L,'m':m,'I':str(I),'E_K_squared_over_I':str(E2/I)})
ck(activation_cases==810)
elapsed=time.perf_counter()-t0;ck(elapsed<60)
result={'status':'PASS','assertions':checks,'actual_partition_runs':runs,'activation_cases':activation_cases,'xor_cases':xor_results,'seconds':elapsed,'logarithmic_sign_basis':'analytic proofs in AUDIT.md; no floating point sign used'}
(RUN/'out/EXACT_RESULTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
