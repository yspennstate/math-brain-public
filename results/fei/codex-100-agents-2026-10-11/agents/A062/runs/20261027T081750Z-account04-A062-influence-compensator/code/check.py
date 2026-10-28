"""Frozen exact finite verification; no floating-point entropy or search escalation."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json, time, random, hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
checks=0
def ck(ok):
    global checks
    checks+=1
    assert ok, checks
    if time.monotonic()-start>60:
        raise RuntimeError('frozen runtime limit')
def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h):
                x,y=a[i],a[i+h]; a[i],a[i+h]=x+y,x-y
        h*=2
    return a
def table(m,L):
    mask=(1<<m)-1
    out=[]
    for x in range(1<<(m*L)):
        z=sum(((x>>(j*m))&mask)==0 for j in range(L))
        out.append((-1)**z)
    out[0]*=-1
    return out
def basis4(prefix=(),span=frozenset({0})):
    if len(prefix)==4:
        yield prefix; return
    for v in range(1,16):
        if v not in span:
            yield from basis4(prefix+(v,),span|frozenset(x^v for x in span))
def rank(cols):
    piv={}
    for x in cols:
        while x:
            k=x.bit_length()-1
            if k in piv: x^=piv[k]
            else: piv[k]=x; break
    return len(piv)

cases=[]; bases_count=0; directions=0
for m,L in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:
    n=m*L; size=1<<n; f=table(m,L); w=fwht(f)
    d=Q(2,1<<m); u=Q(2,size); a=d-u
    D={}
    for v in range(1,size):
        t=sum(bool((v>>(j*m))&((1<<m)-1)) for j in range(L))
        count=sum(f[x]!=f[x^v] for x in range(size))
        exact=(1-(1-2*d)**t)/2+(-1)**t*u
        ck(Q(count,size)==exact)
        spectral=sum(w[s]**2 for s in range(size) if (s&v).bit_count()%2)
        ck(spectral==count*size)  # independent Walsh/autocorrelation route
        ck(a<=exact<=1-a)
        D[v]=count
        directions+=1
    ck(sum(Q(D[1<<i],size) for i in range(n))==n*a)
    if L>=2 and n>=3:
        ck(sum(x<0 for x in f)%2==1)
        ck(all(x%4==2 for x in w))
    if n==4:
        bases=basis4()
    else:
        rng=random.Random(620022+n+m)
        generated=[]
        for _ in range(256):
            cols=[1<<i for i in range(n)]
            for j in range(4*n):
                v,widx=rng.sample(range(n),2); cols[v]^=cols[widx]
            generated.append(tuple(cols))
        bases=iter(generated)
    countbases=0
    for cols in bases:
        ck(rank(cols)==n)
        ck(all(min(D[v],size-D[v])>=a*size for v in cols))
        if countbases<16:
            # Compute transformed truth table directly; confirm marginals, not just rank.
            trans=[]
            for y in range(size):
                x=0
                for j,v in enumerate(cols):
                    if y>>j&1: x^=v
                trans.append(f[x])
            what=fwht(trans)
            ck(sorted(x*x for x in what)==sorted(x*x for x in fwht(f)))
            for j,v in enumerate(cols):
                ck(sum(what[s]**2 for s in range(size) if s>>j&1)==D[v]*size)
        countbases+=1
    bases_count+=countbases
    if n==4: ck(countbases==20160)
    # All translations of one nontrivial shear; derivative counts are invariant.
    cols=[1<<i for i in range(n)]; cols[0]^=cols[1]
    for b in range(size):
        for v in cols:
            ck(sum(f[x^b]!=f[x^b^v] for x in range(size))==D[v])
    cases.append({'m':m,'L':L,'N':n,'directions':size-1,'bases':countbases})

compressed=[]
for m in range(8,41):
    d=Q(2,1<<m); L=(1<<(m-1))//m; N=m*L
    ck(m*d<=Q(1,16)); ck(Q(15,16)<=N*d<=1)
    ck(L>=16 and N>=128); ck(N>m)
    ck(Q(2*m+1,1)*2*d*L<=Q(17,4))
    # For N>=32 the uniform perturbation bound follows from a decreasing sequence.
    ck(Q(100,97)**2<2); ck(Q(97,2)*Q(1,1<<15)<Q(1,16))
    if m<=12:
        u=Q(2,1<<N); a=d-u; total=Q(0); infl=Q(0)
        for r in range(L+1):
            amp=(1-d)**(L-r)*(-d)**r-(-1)**L*u
            mult=comb(L,r)*((1<<m)-1)**r
            p=mult*amp**2
            total+=p
            infl+=p*Q(r*m*(1<<(m-1)),(1<<m)-1)
            ck(amp!=0)
        ck(total==1); ck(infl==N*a); ck(Q(7,8)<infl<Q(17,16))
        compressed.append({'m':m,'L':L,'N':N,'rank_cells':L+1})

ck(directions==1162); ck(bases_count==21440)
result={'status':'PASS','checks':checks,'cases':cases,'directions':directions,
        'bases':bases_count,'compressed':compressed,'parameter_m':[8,40],
        'arithmetic':'integers and exact rational; no float entropy',
        'elapsed_seconds':time.monotonic()-start,
        'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/'CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
