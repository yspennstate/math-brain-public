"""Independent A008 reconstruction and exact/certified PI-J majority pilot."""
from fractions import Fraction as F
from itertools import product, combinations, permutations
from collections import defaultdict, deque
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import json, time
BASE=Path(__file__).resolve().parents[1]
(BASE/'out').mkdir(exist_ok=True)
START=time.perf_counter()
COUNT=0
def ck(ok):
    global COUNT
    COUNT+=1
    assert ok
def save(name,obj):
    (BASE/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')

def ln_unit(x):
    ck(1 <= x <= 2)
    z=(x-1)/(x+1)
    v=2*sum((z**(2*j+1)/F(2*j+1) for j in range(18)),F(0))
    rem=2*z**37/(37*(1-z*z))
    return v,v+rem
LN2=ln_unit(F(2))
@lru_cache(None)
def ln(x):
    ck(x>0)
    if x<1:
        a,b=ln(1/x)
        return -b,-a
    e=0
    y=x
    while y>=2:
        y/=2
        e+=1
    a,b=ln_unit(y)
    return a+e*LN2[0],b+e*LN2[1]
def log2(x):
    a,b=ln(x)
    vals=[u/v for u in (a,b) for v in LN2]
    return min(vals),max(vals)
@lru_cache(None)
def root5(z):
    ck(0<z<=1)
    d=1<<48
    lo,hi=0,d
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**5*z.denominator <= z.numerator*d**5:
            lo=mid
        else:
            hi=mid
    if lo**5*z.denominator==z.numerator*d**5:
        return F(lo,d),F(lo,d)
    return F(lo,d),F(hi,d)
def sum_bounds(terms):
    lo=hi=F(0)
    for z,c in terms.items():
        a,b=root5(z)
        lo+=c*z*a
        hi+=c*z*b
    ck(lo>0)
    return lo,hi
def rounded(a,b):
    d=10**9
    return {'lower':str(F((a*d).numerator//(a*d).denominator,d)),
            'upper':str(F(-((-b*d).numerator//(-b*d).denominator),d))}
def term_export(terms):
    return [{'z':str(z),'coefficient':str(c)} for z,c in sorted(terms.items())]

# Independent dictionary execution: one four-state slot per physical gate.
records=[]
for m in range(1,7):
    kappa={k:F(m+1,m*k*(k+1)) for k in range(1,m+1)}
    ck(sum(kappa.values())==1)
    masses=defaultdict(F)
    count=0
    for slots in product(range(4),repeat=m):
        k=sum(v!=0 for v in slots)
        if not k:
            continue
        q=kappa[k]/(comb(m,k)*3**k)
        A=0
        for i,v in enumerate(slots,1):
            if v in (1,3): A|=1
            if v in (2,3): A|=1<<i
        ck(A!=0)
        masses[A]+=q
        if A==1: ck(q<=F(1,m))
        count+=1
    ck(count==4**m-1)
    ck(sum(masses.values())==1)
    common=sum((kappa[k]/3**k for k in range(1,m+1)),F(0))
    ck(masses[1]==common and common>=F(1,6))
    for mask in range(1,1<<m):
        t=mask.bit_count()
        T=mask<<1
        private=kappa[t]/(comb(m,t)*3**t)
        output=sum((F(comb(m-t,u)*(2**t-(u==0)),1)*kappa[t+u]/(comb(m,t+u)*3**(t+u))
                    for u in range(m-t+1)),F(0))
        ck(masses[T]==private)
        ck(masses[T|1]==output and output>=private)
    rare=8*m*F(1,2**m)-6*m*F(1,4**m)
    ck(rare<=F(13,4))
    records.append({'m':m,'records':count,'normalized_mass':str(sum(masses.values())),
                    'common_mass':str(common),'rare_cost_bound':str(rare)})
for m in range(2,20):
    ck(16*(m-1)*2**m-18*m+6>=46*m-58>0)
save('A008_REVIEW_CHECK.json',{'status':'PASS','verdict':'HOLDS_AT_STATED_SCOPE_NO_REPAIR',
 'assertions_so_far':COUNT,'records':records,'elapsed_seconds':time.perf_counter()-START,
 'independence':'four-state product traces and direct pushforward; no author checker imported'})

def spectrum(n):
    k=(n+1)//2
    coeff=[]
    for s in range(n+1):
        num=sum((1 if j>=k else -1)*sum((-1)**(s-l)*comb(s,l)*comb(n-s,j-l)
                     for l in range(max(0,j-(n-s)),min(s,j)+1)) for j in range(n+1))
        coeff.append(F(num,2**n))
    p=[comb(n,s)*coeff[s]**2 for s in range(n+1)]
    ck(sum(p)==1 and p[0]==0)
    ck(all(p[s]==0 for s in range(0,n+1,2)))
    I=sum((s*p[s] for s in range(n+1)),F(0))
    ck(I==F(n*comb(n-1,(n-1)//2),2**(n-1)))
    ck(I*I<=n)
    if n<=7:
        for mask in range(1<<n):
            direct=sum((1 if x.bit_count()>=k else -1)*(-1)**(mask.bit_count()-(x&mask).bit_count())
                       for x in range(1<<n))
            ck(F(direct,2**n)==coeff[mask.bit_count()])
    return coeff,p,I

def cost(n,gates,selected,roots):
    k=(n+1)//2
    d=comb(n-1,k-1)
    z=F(1)
    for g,B in selected.items():
        A=set().union(*map(set,selected.values()))
        s=len(B)
        kap=len(A&set(gates[g]))
        z*=F(s,kap)**s
        for j in B:
            rank=gates[g].index(j)+1
            pred=sum(i<j for i in A&set(gates[g]))
            z*=F(pred+1,rank)
    ck(0<z<=1)
    return z,F(1,d)**len(selected)*F(1,2**k)**len(roots)

def trace(gates,selected,roots,children):
    work=deque(sorted(roots)); seen=set(); out=set(); tr=[]
    while work:
        g=work.popleft()
        ck(g not in seen)
        seen.add(g)
        B=tuple(sorted(selected[g])); edges=children.get(g,())
        ck(set(B)<=set(gates[g]) and len(B)>0)
        ck(tuple(j for j,h in edges)==tuple(sorted(j for j,h in edges)))
        for j,h in edges:
            ck(j in B and j in gates[h])
            work.append(h)
        tr.append((g,B,edges)); out.update(B)
    ck(seen==set(selected))
    ck(sum(map(len,selected.values()))==len(out))
    return tuple(sorted(roots)),tuple(tr)

def full_forests(n,A,gates):
    eligible=[tuple(g for g,R in enumerate(gates) if j in R) for j in A]
    terms=defaultdict(F); keys=set()
    for assignment in product(*eligible):
        selected=defaultdict(list)
        for j,g in zip(A,assignment): selected[g].append(j)
        V=tuple(sorted(selected))
        outgoing={g:{h for h in V if h!=g and set(selected[g])&set(gates[h])} for g in V}
        reach={g:{g}|outgoing[g] for g in V}
        for _ in V:
            for g in V: reach[g]|=set().union(*(reach[h] for h in tuple(reach[g])))
        components=[]; remaining=set(V)
        while remaining:
            g=min(remaining); comp={h for h in V if h in reach[g] and g in reach[h]}
            components.append(tuple(sorted(comp))); remaining-=comp
        sources=[comp for comp in components if not any(h in comp for g in V if g not in comp for h in outgoing[g])]
        for roots in product(*sources):
            nonroots=[h for h in V if h not in roots]
            choices=[tuple(g for g in V if h in outgoing[g]) for h in nonroots]
            for parents_tuple in product(*choices):
                parents=dict(zip(nonroots,parents_tuple))
                good=True
                for h in nonroots:
                    v=h; walked=set()
                    while v not in roots:
                        if v in walked: good=False; break
                        walked.add(v); v=parents[v]
                    if not good: break
                if not good: continue
                atts=[tuple(sorted(set(selected[parents[h]])&set(gates[h]))) for h in nonroots]
                for att_tuple in product(*atts):
                    groups=defaultdict(list)
                    for h,j in zip(nonroots,att_tuple): groups[(parents[h],j)].append(h)
                    group_keys=sorted(groups)
                    orders=[tuple(permutations(groups[key])) for key in group_keys]
                    for ordered in product(*orders):
                        children=defaultdict(list)
                        for (g,j),order in zip(group_keys,ordered): children[g].extend((j,h) for h in order)
                        children={g:tuple(edges) for g,edges in children.items()}
                        key=trace(gates,selected,roots,children)
                        ck(key not in keys); keys.add(key)
                        z,c=cost(n,gates,selected,roots)
                        terms[z]+=c
    ck(len(keys)>0)
    return terms,len(keys)

exact=[]; constructive=[]
for n in (1,3,5,7):
    coeff,p,I=spectrum(n); k=(n+1)//2
    gates=tuple(combinations(range(n),k)); N=len(gates); d=comb(n-1,k-1)
    D=(1+F(1,d*2**k))**N-1
    Dl,Dh=log2(D)
    rl,rh=Dl,Dh
    cases=[]
    for mask in range(1,1<<n):
        A=tuple(i for i in range(n) if mask>>i&1); s=len(A)
        if n<=3:
            terms,count=full_forests(n,A,gates)
        else:
            terms=defaultdict(F)
            if s<=k:
                for g,R in enumerate(gates):
                    if set(A)<=set(R):
                        trace(gates,{g:A},(g,),{})
                        z,c=cost(n,gates,{g:A},(g,)); terms[z]+=c
                count=comb(n-s,k-s)
                ck(count>0)
            else:
                U,V=A[::2],A[1::2]; j=U[0]
                g=next(g for g,R in enumerate(gates) if set(U)<=set(R))
                h=next(h for h,R in enumerate(gates) if set(V+(j,))<=set(R))
                ck(g!=h)
                trace(gates,{g:U,h:V},(g,),{g:((j,h),)})
                z,c=cost(n,gates,{g:U,h:V},(g,)); terms[z]+=c
                count=1
        sl,sh=sum_bounds(terms)
        a,_=log2(sl); _,b=log2(sh)
        # -log S lies in [-log(sh), -log(sl)].
        lo,hi=-b,-a
        mass=coeff[s]**2
        rl+=mass*lo; rh+=mass*hi
        entry={'mask':mask,'s':s,'runs':count,'terms':term_export(terms),'cost_interval':rounded(lo,hi)}
        if n<=3: cases.append(entry)
    ck(rl<=rh)
    _,loge_hi=log2(F(1)) # log2(e) represented as 1/ln2, no floating constant.
    bound=(F(49,5)+F(6,5)/LN2[0])*I
    ck(rh<=bound)
    row={'n':n,'k':k,'gates':N,'lambda':str(F(1,d)),'D':str(D),'I':str(I),
         'residual_interval':rounded(rl,rh),'residual_over_I_interval':rounded(rl/I,rh/I),
         'scope':'ALL_PARTITION_FORESTS_EXACT_ALGEBRAIC_SUM' if n<=3 else 'CONSTRUCTED_POSTERIOR_UPPER_BOUND',
         'cases':cases}
    (exact if n<=3 else constructive).append(row)
    save('MAJORITY_EXACT.json',{'status':'PASS','exact':exact,'constructive':constructive})

levels=[]
for n in range(1,32,2):
    coeff,p,I=spectrum(n)
    # Exchangeability: E sum F=(I/n)ln(n!)-E ln(|A|!).
    an,bn=ln(F(factorial(n))); lo,hi=I/F(n)*an,I/F(n)*bn
    for s in range(1,n+1):
        a,b=ln(F(factorial(s))); lo-=p[s]*b; hi-=p[s]*a
    ck(lo<=hi)
    ck(hi <= (1+LN2[0])*I)
    levels.append({'n':n,'I':str(I),'level_masses':[str(x) for x in p],
                   'global_rank_mean_over_I':rounded(lo/I,hi/I)})
save('SYMMETRIC_SPECTRA.json',{'status':'PASS','levels':levels,'arithmetic':'exact binomial character sums and certified natural logarithm intervals'})
elapsed=time.perf_counter()-START
save('CHECK_SUMMARY.json',{'status':'PASS','assertions':COUNT,'elapsed_seconds':elapsed,
 'root_precision_bits':48,'log_series_terms':18,'review':'HOLDS_AT_STATED_SCOPE_NO_REPAIR',
 'majority':'exact all-partition residual n=1,3; constructed upper bounds n=5,7; exact spectra through n=31',
 'memory_estimate_bytes':70000000})
ck(elapsed<60)
print(json.dumps({'status':'PASS','assertions':COUNT,'elapsed_seconds':elapsed},indent=2))
