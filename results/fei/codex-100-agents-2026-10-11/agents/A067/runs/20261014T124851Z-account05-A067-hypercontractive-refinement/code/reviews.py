import itertools,json,math,time
from fractions import Fraction as Q
from functools import lru_cache
import check as h
START=time.perf_counter();COUNT=0
def ck(b):
    global COUNT
    COUNT+=1;assert b;assert time.perf_counter()-START<600
def pos(p):ck(not p or h.lower(p)>=0)
def lg(x):return h.combine((h.ns['factors'](x.numerator),Q(1)),(h.ns['factors'](x.denominator),Q(-1)))
def Hval(v):return h.H(h.fwht(v))
def restrict(v,i,value):
    return tuple(v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(value<<i)] for x in range(len(v)//2))
@lru_cache(None)
def oriented(v,i):
    a=h.fwht(v);den=len(v)**2;p={}
    for t in range(len(a)):
        if t>>i&1:continue
        d=a[t|(1<<i)]**2
        if d:p=h.combine((p,Q(1)),(lg(Q(a[t]**2+d,d)),Q(d,den)))
    return p
@lru_cache(None)
def potential(b,q):
    d=len(b).bit_length()-1;r=len(q).bit_length()-1;delta=Q(1,len(b));mean=Q(sum(q),len(q));var=1-mean*mean
    v=tuple(b[x]+(q[z]-b[0] if x==0 else 0) for z in range(len(q)) for x in range(len(b)))
    for i in range(r):
        e=h.physical(v,[d+i]);beta=Q(h.fwht(q)[1<<i],len(q));ck(e==delta*h.physical(q,[i]))
        M=oriented(v,d+i);quot=h.combine((oriented(q,i),delta))
        if beta:
            rho=1-delta+delta*(mean*mean+beta*beta)
            quot=h.combine((quot,Q(1)),(lg(rho/(delta*(mean*mean+beta*beta))),delta*beta*beta))
        pos(h.combine((quot,Q(1)),(M,Q(-1))))
    return v,h.combine((Hval(q),delta)),delta*d*var,delta,var
@lru_cache(None)
def tree(b,q,order,depth):
    v,G,R,delta,var=potential(b,q);d=len(b).bit_length()-1
    if depth==0:return {},Q(0),Q(0),G,R
    i=order[0];rest=tuple(j-1 if j>i else j for j in order[1:]);children=[]
    for bit in [0,1]:
        if i<d:
            bb=restrict(b,i,bit);qq=q if bit==0 else tuple([bb[0]]*len(q))
        else:bb=b;qq=restrict(q,i-d,bit)
        children.append(tree(bb,qq,rest,depth-1))
    M=h.combine(*((c[0],Q(1,2)) for c in children));Pc=sum(c[1] for c in children)/2;DR=sum(c[2] for c in children)/2
    GL=h.combine(*((c[3],Q(1,2)) for c in children));RL=sum(c[4] for c in children)/2
    if i<d:DR+=delta*var
    else:M=h.combine((M,Q(1)),(oriented(v,i),Q(1)));Pc+=h.physical(v,[i])
    return M,Pc,DR,GL,RL
EL=sum((Q(1,math.factorial(j)) for j in range(13)),Q(0));EU=EL+Q(1,math.factorial(13))/(1-Q(1,14));kappa_low=2/(EU*h.ns['LN2'][1])
roots=histories=0
for bc in range(16):
    b=tuple(1 if bc>>x&1 else -1 for x in range(4))
    for qc in range(16):
        q=tuple(1 if qc>>x&1 else -1 for x in range(4));v,G,R,delta,var=potential(b,q);roots+=1
        for order in itertools.permutations(range(4)):
            for depth in [2,4]:
                M,Pc,DR,GL,RL=tree(b,q,order,depth)
                budget=h.combine((G,Q(1)),(GL,Q(-1)),(h.linear(R-RL-DR+kappa_low*Pc),Q(1)))
                pos(h.combine((budget,Q(1)),(M,Q(-1))));histories+=1

# A069: direct complete final-reference price and one inherited Y query.
weights={1:Q(1,4),2:Q(1,4),3:Q(1,16),'tail0':Q(7,20),'tail1':Q(7,80)};ck(sum(weights.values())==1)
def CE(v,m,ref,corebits):
    a=h.fwht(v);den=len(v)**2;width=1<<corebits;alpha=Q(sum(c*c for s,c in enumerate(a) if s>=width),den);p={}
    for s,c in enumerate(a):
        if not c:continue
        T=s&(width-1);D=s>>corebits
        if D==0:r=1-alpha
        elif D<4:r=alpha*weights[D]
        else:r=alpha*weights['tail1' if D&2 else 'tail0']/ (2*((1<<m)-1))
        p=h.combine((p,Q(1)),(lg(1/(ref[T]*r)),Q(c*c,den)))
    return p,alpha
def hb(a):
    if not a or a==1:return {}
    return h.combine((lg(1/a),a),(lg(1/(1-a)),1-a))
corecases=0
for m in [1,2]:
    for hs in itertools.product(range(4),repeat=4):
        for ref in [(Q(1,2),Q(1,2)),(Q(1,3),Q(2,3))]:
            v=[]
            for control in range(1<<(m+2)):
                c=control&1;u=(control>>1)&1;Z=control>>2;state=c+2*u;sign=-1 if c==0 and Z==0 else 1
                v.extend(sign*(1 if hs[state]>>y&1 else -1) for y in range(2))
            full,alpha=CE(v,m,ref,1);B={}
            for code in hs:
                core=tuple(1 if code>>y&1 else -1 for y in range(2));a=h.fwht(core)
                for T,c in enumerate(a):B=h.combine((B,Q(1)),(lg(1/ref[T]),Q(c*c,16)))
            Iy=h.physical(v,[0]);Icu=h.physical(v,[1,2]);Iz=h.physical(v,range(3,m+3))
            bound=h.combine((B,Q(1)),(h.linear(2*Iy+4*Icu+4*Iz),Q(1)),(lg(Q(20,7)),Iz));pos(h.combine((bound,Q(1)),(full,Q(-1))))
            children=[CE(restrict(tuple(v),0,bit),m,(Q(1),),0) for bit in [0,1]]
            delta=h.combine((full,Q(1)),*((c[0],Q(-1,2)) for c in children))
            rhs=h.combine((B,Q(1)),(hb(alpha),Q(1)),*((hb(c[1]),Q(-1,2)) for c in children))
            ck(not h.combine((delta,Q(1)),(rhs,Q(-1))));corecases+=1

# A068: independent invertible label map, actual two-face reserve and geometry.
def stars(n):
    edges=list(itertools.permutations(range(n),2));out=[]
    for code in range(1<<len(edges)):
        chosen=[edges[j] for j in range(len(edges)) if code>>j&1];centers={c for c,l in chosen};leaves=[l for c,l in chosen]
        if not centers.intersection(leaves) and len(set(leaves))==len(leaves):out.append(chosen)
    return out
starcases=0
for n in [1,2,3]:
    for truth in range(1<<(1<<n)):
        b=tuple(1 if truth>>x&1 else -1 for x in range(1<<n))
        if any(len({(b[x]-b[x^(1<<i)])//2 for x in range(1<<n) if not(x>>i&1)}-{0})>1 for i in range(n)):continue
        a=h.fwht(b);den=len(b)**2
        for edges in stars(n):
            def mapping(x):
                out=x
                for c,l in edges:out^=((x>>l)&1)<<c
                return out
            G=tuple(b[mapping(x)] for x in range(len(b)));ck(len({mapping(x) for x in range(len(b))})==len(b))
            reserve=Q(0)
            for c,l in edges:
                p=Q(sum(w*w for s,w in enumerate(a) if s>>c&1 and s>>l&1),den)
                r=h.physical(b,[c])-2*p;ck(r>=0)
                both=Q(sum(b[x]!=b[x^(1<<c)] and b[x^(1<<l)]!=b[x^(1<<l)^(1<<c)] for x in range(len(b))),len(b));ck(r==both);reserve+=r
            ck(h.physical(G,range(n))==h.physical(b,range(n))+reserve);starcases+=1

majority=lambda x:1 if x.bit_count()<=1 else -1
G=tuple(majority((x&~1)|(((x&1)^((x>>1)&1)))) for x in range(8))
# Coordinate0 is a star center, coordinate1 its leaf.
ck(h.H(h.fwht(G))=={2:Q(2)});ck(h.physical(G,range(3))==Q(3,2))
nonunate=any(len({(G[x]-G[x^(1<<i)])//2 for x in range(8) if not(x>>i&1)}-{0})>1 for i in range(3));ck(nonunate)
orderfails=0
for order in itertools.permutations(range(3)):
    for orientation in range(8):
        fail=False
        for step,i in enumerate(order):
            before=order[:step];after=order[step+1:]
            for vals in range(1<<len(after)):
                points=[]
                for u in range(1<<len(before)):
                    x=sum(((vals>>j)&1)<<k for j,k in enumerate(after))+sum((((u>>j)&1)^((orientation>>k)&1))<<k for j,k in enumerate(before))
                    if G[x]!=G[x^(1<<i)]:points.append(u)
                if any(a!=b and a&b==a for a in points for b in points):fail=True
        ck(fail);orderfails+=1

out={'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'A066_roots':roots,'A066_full_and_early_histories':histories,'A066_unique_states':potential.cache_info().currsize,'A069_complete_reference_core_queries':corecases,'A068_unate_star_cases':starcases,'A068_order_orientation_failures':orderfails,'A088_obstruction_validation':'in primary CHECK_FULL.json, four physical parent/child dimensions'}
(h.ROOT/'out/REVIEWS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
