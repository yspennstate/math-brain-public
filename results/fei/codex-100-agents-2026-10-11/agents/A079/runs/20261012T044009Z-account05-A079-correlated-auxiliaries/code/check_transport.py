import json,time
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); ASSERTIONS=0; COUNTS=Counter()

def check(ok):
    global ASSERTIONS
    ASSERTIONS+=1
    assert ok,ASSERTIONS
    if time.perf_counter()-START>60: raise RuntimeError('Frozen 60-second cap')

def walsh(a):
    a=list(a);step=1
    while step<len(a):
        for block in range(0,len(a),2*step):
            for j in range(block,block+step):
                u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
        step*=2
    return a

def sign(z):return (-1)**z.bit_count()

@lru_cache(None)
def primes(z):
    out={};p=2
    while p*p<=z:
        while z%p==0:out[p]=out.get(p,0)+1;z//=p
        p+=1
    if z>1:out[z]=out.get(z,0)+1
    return out

def plus(*terms):
    out={}
    for weight,expr in terms:
        for p,c in expr.items():out[p]=out.get(p,Q(0))+weight*c
    return {p:c for p,c in out.items() if c}

def H(ps):
    out={}
    for p in ps:
        if not p:continue
        for prime,v in primes(p.denominator).items():out[prime]=out.get(prime,Q(0))+p*v
        for prime,v in primes(p.numerator).items():out[prime]=out.get(prime,Q(0))-p*v
    return {p:c for p,c in out.items() if c}

def law(f):
    n=len(f);return [Q(a*a,n*n) for a in walsh(f)]

def erase_index(z,i):return (z&((1<<i)-1))|((z>>(i+1))<<i)

def restrict(f,i,bit):
    n=(len(f).bit_length()-1)
    return [f[(z&((1<<i)-1))|((z>>i)<<(i+1))|(bit<<i)] for z in range(1<<(n-1))]

def marginal(ps,i):
    out=[Q(0)]*(len(ps)//2)
    for s,p in enumerate(ps):out[erase_index(s,i)]+=p
    return out

def erasure(ps,i):return plus((1,H(ps)),(-1,H(marginal(ps,i))))

def Btotal(ps):
    return plus(*[(1,erasure(ps,i)) for i in range(len(ps).bit_length()-1)])

def inf(ps,i):return sum((p for s,p in enumerate(ps) if s>>i&1),Q(0))

def I(ps):return sum((p*s.bit_count() for s,p in enumerate(ps)),Q(0))

def split(f,i):
    ps=law(f);ch=[restrict(f,i,b) for b in [0,1]];cp=[law(g) for g in ch]
    e=erasure(ps,i)
    j=plus((1,H(marginal(ps,i))),(-Q(1,2),H(cp[0])),(-Q(1,2),H(cp[1])))
    d=plus((1,H(ps)),(-Q(1,2),H(cp[0])),(-Q(1,2),H(cp[1])))
    check(d==plus((1,e),(1,j)))
    return e,j,d,inf(ps,i),ch

def phase_values(k,m,rows):
    return [rows[b][x]*sign(a&b) for b in range(1<<m) for a in range(1<<m) for x in range(1<<k)]

def transport_case(k,m,rows,group,seed=None):
    nx,nb=1<<k,1<<m;f=phase_values(k,m,rows);ps=law(f)
    rowlaws=[law(h) for h in rows]
    coreH=plus(*[(Q(1,nb),H(p)) for p in rowlaws])
    coreB=plus(*[(Q(1,nb),Btotal(p)) for p in rowlaws])
    coreI=sum((I(p) for p in rowlaws),Q(0))/nb
    check(H(ps)==plus((1,{2:Q(2*m)}),(1,coreH)))
    check(I(ps)==m+coreI)
    # Build the (V,S) channel directly, independent of the full transform.
    joint=[Q(0)]*(nx*nb)
    for s,p in enumerate(rowlaws):
        for v,mass in enumerate(p):joint[v+nx*s]=mass/nb
    dataA=plus(*[(1,erasure(joint,k+j)) for j in range(m)])
    check(Btotal(ps)==plus((1,{2:Q(m)}),(1,coreB),(1,dataA)))
    for i in range(k):
        check(erasure(ps,i)==plus(*[(Q(1,nb),erasure(p,i)) for p in rowlaws]))
        check(inf(ps,i)==sum((inf(p,i) for p in rowlaws),Q(0))/nb)
    for j in range(m):
        # b_j first: entropy loss 2; full child a_j character has zero entropy.
        eb,jb,db,ib,bchildren=split(f,k+m+j)
        check(eb=={2:Q(1)});check(jb=={2:Q(1)});check(db=={2:Q(2)});check(ib==Q(1,2))
        for bit,g in enumerate(bchildren):
            ea,ja,da,ia,_=split(g,k+j)
            check(ea=={} and ja=={} and da=={})
            check(ia==bit)
        # a_j first: complementary entropy credits of phase multiplexer G.
        gs=[]
        for small in range(nb//2):
            b0=(small&((1<<j)-1))|((small>>j)<<(j+1))
            gs.append(rows[b0]+rows[b0|(1<<j)])
        GB=plus(*[(Q(2,nb),split(g,k)[0]) for g in gs])
        GJ=plus(*[(Q(2,nb),split(g,k)[1]) for g in gs])
        GD=plus(*[(Q(2,nb),split(g,k)[2]) for g in gs])
        ea,ja,da,ia,achildren=split(f,k+j)
        check(ea==plus((1,{2:Q(1)}),(-1,GJ)))
        check(ja==plus((1,{2:Q(1)}),(-1,GB)))
        check(da==plus((1,{2:Q(2)}),(-1,GD)))
        check(ia==Q(1,2))
        # Both a branches have the same entropy drop at the next b query.
        for g in achildren:
            check(split(g,k+m+j-1)[2]==GD)
        check(plus((1,da),(1,GD))=={2:Q(2)})
    # Explicit full b-first paired tree retains actual leaf H, B and I.
    states=[(Q(1),f)]
    paidE={};paidJ={};paidI=Q(0)
    for _ in range(m):
        new=[]
        mm=(len(states[0][1]).bit_length()-1-k)//2
        for weight,g in states:
            e,j,d,iv,children=split(g,k+mm)
            paidE=plus((1,paidE),(weight,e));paidJ=plus((1,paidJ),(weight,j));paidI+=weight*iv
            for child in children:
                e,j,d,iv,grand=split(child,k)
                paidE=plus((1,paidE),(weight/2,e));paidJ=plus((1,paidJ),(weight/2,j));paidI+=weight*iv/2
                for leaf in grand:new.append((weight/4,leaf))
        states=new
    leafH=plus(*[(w,H(law(g))) for w,g in states]);leafB=plus(*[(w,Btotal(law(g))) for w,g in states]);leafI=sum((w*I(law(g)) for w,g in states),Q(0))
    check(paidE=={2:Q(m)} and paidJ=={2:Q(m)})
    check(paidI==m);check(leafH==coreH);check(leafB==coreB);check(leafI==coreI)
    if seed is not None:
        # A034 unit-affine row admission fails: an actual partial row value has 0<abs<1.
        vals=[Q(w,1<<k) for w in walsh(seed)]
        intermediate=any(0<abs(z)<1 for z in vals)
        if not intermediate:
            v=next(v for v,z in enumerate(vals) if not z)
            flipped=seed.copy();flipped[0]*=-1
            intermediate=0<abs(Q(walsh(flipped)[v],1<<k))<1
        check(intermediate)
    COUNTS[group]+=1

def affine_support(support):
    if not support:return False
    base=next(iter(support));v={z^base for z in support}
    return len(v)&(len(v)-1)==0 and all(a^b in v for a in v for b in v)

def a034_control(cycle,sgn):
    # Distinct X labels on four singleton Y cells; all quadratic cell phases allowed.
    labels=[(b+cycle)%4 for b in range(4)]
    f=[sign(x&labels[b])*((-1)**((sgn>>b)&1)) for b in range(4) for x in range(4)]
    p=law(f);check(H(p)=={2:Q(4)})
    py=[sum((p[v+4*t] for v in range(4)),Q(0)) for t in range(4)]
    px=[sum((p[v+4*t] for t in range(4)),Q(0)) for v in range(4)]
    check(H(px)=={2:Q(2)})
    check(plus((1,H(p)),(-1,H(px)))=={2:Q(2)})
    check(sum((p[s]*(s>>2).bit_count() for s in range(16)),Q(0))==1)
    COUNTS['A034_control']+=1

def admission_witnesses():
    # k=1,m=2 tags are admitted; k=1,m=3 loses affinity of a row support.
    for m in [2,3]:
        rows=[[(-1 if b==x else 1) for x in range(2)] for b in range(1<<m)]
        f=phase_values(1,m,rows)
        partial=[[Q(sum(f[x+2*y]*sign(v&x) for x in range(2)),2) for y in range(1<<(2*m))] for v in range(2)]
        check(all(abs(z) in [0,1] for row in partial for z in row))
        admitted=all(affine_support({y for y,z in enumerate(row) if z}) for row in partial)
        check(admitted==(m==2))
        COUNTS['admission_corner']+=1

def receipt():
    out={'status':'PASS','cases':dict(COUNTS),'root_cases':sum(COUNTS.values()),'assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'arithmetic':'integer Walsh / Fraction / exact prime-log entropy expressions','independent_review':False}
    (ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n');return out

for k,m in [(1,1),(2,1)]:
    for mask in range(1<<(2**(k+m))):
        rows=[[(-1)**((mask>>(x+(1<<k)*b))&1) for x in range(1<<k)] for b in range(1<<m)]
        transport_case(k,m,rows,'exhaustive_phase')
receipt()
for j in range(16):
    rows=[[sign(j*x+(j+1)*b+x*b+(x^b)) for x in range(4)] for b in range(4)]
    transport_case(2,2,rows,'deterministic_phase')
receipt()
for mask in range(16):
    seed=[(-1)**((mask>>x)&1) for x in range(4)]
    rows=[[seed[x]*(-1 if b==x else 1) for x in range(4)] for b in range(8)]
    transport_case(2,3,rows,'rare_tag',seed)
receipt()
for cycle in range(4):
    for sgn in range(16):a034_control(cycle,sgn)
admission_witnesses()
print(json.dumps(receipt(),indent=2))
