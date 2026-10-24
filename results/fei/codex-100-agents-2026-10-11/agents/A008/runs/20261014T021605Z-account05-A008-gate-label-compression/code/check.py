from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import itertools as it, math, json, time, sys
B=Path(__file__).resolve().parents[1];checks=0
def ck(t):
    global checks
    checks+=1
    assert t
def enc(x):return [x.numerator,x.denominator]
def lnsmall(x):
    z=(x-1)/(x+1);t=z;lo=F(0)
    for j in range(24):lo+=2*t/(2*j+1);t*=z*z
    return lo,lo+2*t/(49*(1-z*z))
@lru_cache(None)
def logcost(q):
    ck(0<q<=1);x=1/q;k=0
    while x>=2:x/=2;k+=1
    l,h=lnsmall(x);l2,h2=lnsmall(F(2));return F(k)+l/h2,F(k)+h/l2
def matchings(edges,A):
    inside=[e for e in edges if set(e)<=A];out=[]
    for mask in range(1<<len(inside)):
        M=[e for i,e in enumerate(inside) if mask>>i&1];flat=[v for e in M for v in e]
        if len(flat)!=len(set(flat)):continue
        U=A-set(flat)
        if any(set(e)<=U for e in inside):continue
        out.append(M)
    return out
def occupation(edges,lam,A,M):
    V=sorted(v for e in M for v in e);U=sorted(A-set(V));poly={(0,)*len(V):F(1)}
    for u in U:
        factor={}
        for i,e in enumerate(edges):
            if u not in e:continue
            v=next(v for v in e if v!=u);h=[0]*len(V)
            if v in V:h[V.index(v)]=1;weight=lam[i]/8
            else:ck(v not in A);weight=lam[i]/32
            h=tuple(h);factor[h]=factor.get(h,F(0))+weight
        new={}
        for h,x in poly.items():
            for k,y in factor.items():
                z=tuple(a+b for a,b in zip(h,k));new[z]=new.get(z,F(0))+x*y
        poly=new
    total=lower=F(0)
    for h,x in poly.items():
        exact=moment=bound=F(1)
        for v,w in M:
            a,b=h[V.index(v)],h[V.index(w)];c=a+b
            z=F(math.factorial(a)*math.factorial(b),(c+1)**2*(c+2));exact*=z
            moment*=F(1,2)*F(1,c+1)*F(2,(c+1)*(c+2))*math.factorial(a)*math.factorial(b)
            bnd=F(2**max(c-1,0),2*6**c);ck(z>=bnd);bound*=bnd
        ck(exact==moment);total+=x*exact;lower+=x*bound
    pref=math.prod(lam[edges.index(e)]/24 for e in M)
    return pref*total,pref*lower
def assignment_mass(edges,lam,A):
    # Independent coordinate-to-gate assignment; no maximal matching enumeration.
    owners=[[i for i,e in enumerate(edges) if u in e] for u in sorted(A)]
    total=F(0);count=0
    for tau in it.product(*owners):
        used=sorted(set(tau));own={i:set(u for u,k in zip(sorted(A),tau) if k==i) for i in used}
        pair=[i for i in used if len(own[i])==2];matched=set().union(*(own[i] for i in pair)) if pair else set();U=A-matched
        if any(set(e)<=U for e in edges):continue
        parents={};root=[];groups={i:{v:0 for v in own[i]} for i in pair}
        for i in used:
            incoming=[(k,v) for k in used if k!=i for v in own[k] if v in edges[i]]
            if incoming:
                ck(len(incoming)==1 and len(own[i])==1);parents[i]=incoming[0];k,v=incoming[0];ck(k in pair);groups[k][v]+=1
            else:root.append(i)
        mass=math.prod(lam[i] for i in used)*F(1,4)**len(root)
        for i in used:
            s=len(own[i]);ck(s in [1,2]);mass*=F(1,4) if s==1 else F(1,6)
            c=sum(groups[i].values()) if i in pair else 0
            mass*=F(1,(c+1)*(c+2)*math.comb(s+c-1,c))
            if i in pair:mass*=math.prod(math.factorial(h) for h in groups[i].values())
        total+=mass;count+=1
    return total,count
def baseline_zero(edges,A):
    a=len(A)
    if a%2==0:return not any(len(M)*2==a for M in matchings(edges,A))
    for j in A:
        if any(len(M)*2==a-1 for M in matchings(edges,A-{j})) and any(j in e for e in edges):return False
    return True
def run(n):
    start=time.perf_counter();alledges=list(it.combinations(range(n),2));records=[];rescued=0;ownership=0;cases=0
    for mask in range(1,1<<len(alledges)):
        edges=[e for i,e in enumerate(alledges) if mask>>i&1];covered=set(v for e in edges for v in e);deg=[sum(v in e for e in edges) for v in range(n)]
        truth=[1 if any(all(x>>v&1 for v in e) for e in edges) else -1 for x in range(1<<n)]
        ft=truth[:];s=1
        while s<len(ft):
            for k in range(0,len(ft),2*s):
                for j in range(k,k+s):a,b=ft[j],ft[j+s];ft[j],ft[j+s]=a+b,a-b
            s*=2
        I=F(sum(truth[x]!=truth[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)
        ck(I==F(sum(a.bit_count()*v*v for a,v in enumerate(ft)),4**n));ck(sum(v*v for v in ft)==4**n)
        local=[]
        for scheme in range(2):
            lam=[F(1,max(deg)) if scheme==0 else F(1,deg[u]+deg[v]) for u,v in edges]
            ck(all(sum(lam[i] for i,e in enumerate(edges) if v in e)<=1 for v in covered))
            D=math.prod(1+l/4 for l in lam)-1;qs=F(0);clo=chi=F(0);sector=[]
            for amask in range(1,1<<n):
                A={v for v in range(n) if amask>>v&1}
                if not A<=covered:continue
                cases+=1;q=lower=F(0)
                for M in matchings(edges,A):
                    v,b=occupation(edges,lam,A,M);q+=v;lower+=b
                direct,count=assignment_mass(edges,lam,A);ownership+=count;ck(q==direct);q/=D;lower/=D;ck(0<lower<=q<=1);qs+=q
                p=F(ft[amask]**2,4**n)
                if p:
                    l,h=logcost(q);clo+=p*l;chi+=p*h
                    if scheme==0 and baseline_zero(edges,A):rescued+=1
                sector.append({'A_mask':amask,'P':enc(p),'Q_MS':enc(q),'occupation_lower':enc(lower)})
            ck(qs<=1);ck(chi<5*I)
            local.append({'scheme':scheme,'I':enc(I),'CE_interval':[enc(clo),enc(chi)],'margin_below_5I':enc(5*I-chi),'sectors':sector})
        records.append({'graph_mask':mask,'weights':local})
        (B/'out'/f'CERTIFICATES_{n}.json').write_text(json.dumps(records),encoding='utf8')
    # Exact local collision inequality over a larger fixed integer domain.
    for a in range(17):
        for b in range(17):
            c=a+b;ck(F(math.factorial(a)*math.factorial(b),(c+1)**2*(c+2))>=F(2**max(c-1,0),2*6**c))
    ck(F(1,4)<F(1,2))
    result={'n':n,'graphs':len(records),'weight_vectors':2*len(records),'covered_set_cases':cases,'ownership_events':ownership,'rescued_matching_sectors':rescued,'assertions':checks,'seconds':time.perf_counter()-start,'all_full_CE_lt_5I':True}
    (B/'out'/('PILOT_SUMMARY.json' if n==3 else 'CHECK_SUMMARY.json')).write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result))
if __name__=='__main__':run(3 if '--pilot' in sys.argv else 4)
