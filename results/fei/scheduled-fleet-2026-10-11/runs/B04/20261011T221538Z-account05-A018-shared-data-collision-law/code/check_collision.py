"""Frozen exact checker A018-collision-v1; no third-party libraries."""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter()
assertions=0
def ck(condition):
    global assertions
    assertions+=1
    assert condition
    if time.perf_counter()-start>60:
        raise RuntimeError('Frozen 60-second pilot deadline exceeded')

def walsh(v):
    z=list(v); h=1
    while h<len(z):
        for i in range(0,len(z),2*h):
            for j in range(i,i+h):
                x,y=z[j],z[j+h]; z[j],z[j+h]=x+y,x-y
        h*=2
    return z

def direct(v):
    return [sum(z*(-1 if (x&s).bit_count()%2 else 1) for x,z in enumerate(v)) for s in range(len(v))]

@lru_cache(None)
def factors(k):
    ans=[]; d=2
    while d*d<=k:
        e=0
        while k%d==0: e+=1; k//=d
        if e: ans.append((d,e))
        d+=1
    if k>1: ans.append((k,1))
    return tuple(ans)

def plus(*terms):
    z=defaultdict(F)
    for weight,expr in terms:
        for p,c in expr.items(): z[p]+=weight*c
    return {p:c for p,c in z.items() if c}

@lru_cache(None)
def logexpr(q):
    z=defaultdict(F)
    for p,e in factors(q.numerator): z[p]+=e
    for p,e in factors(q.denominator): z[p]-=e
    return dict(z)

def entropy(ps):
    return plus(*[(-p,logexpr(p)) for p in ps if p])

@lru_cache(None)
def ln_interval(q):
    # Reduce q to [1,2); positive atanh series, explicit geometric tail.
    k=0
    while q>=2: q/=2; k+=1
    while q<1: q*=2; k-=1
    def series(r):
        z=(r-1)/(r+1); zz=z*z; power=z; low=F(0)
        for j in range(36):
            low+=2*power/(2*j+1); power*=zz
        return low,low+2*power/(73*(1-zz))
    lo,hi=series(q); l2,h2=series(F(2))
    return (lo+k*l2,hi+k*h2) if k>=0 else (lo+k*h2,hi+k*l2)

@lru_cache(None)
def log2_interval(p):
    if p==2: return F(1),F(1)
    lo,hi=ln_interval(F(p)); l2,h2=ln_interval(F(2))
    return lo/h2,hi/l2  # p prime >=2, numerator nonnegative

def interval(expr):
    lo=hi=F(0)
    for p,c in expr.items():
        l,h=log2_interval(p)
        if c>=0: lo+=c*l; hi+=c*h
        else: lo+=c*h; hi+=c*l
    return lo,hi

def check_case(v,n,a,direct_check=False):
    N=1<<a; D=1<<(n-a); L=1<<n
    w=walsh(v)
    if direct_check: ck(w==direct(v))
    p=[F(t*t,L*L) for t in w]
    ck(sum(p)==1)
    # selectors occupy low bits; branches indexed by x, data by y
    branches=[[v[x+N*y] for y in range(D)] for x in range(N)]
    c=[[F(t,D) for t in walsh(b)] for b in branches]
    R=[]; B={}; M={}; avg={}; common=True; character_rows=True
    for x in range(N): avg=plus((1,avg),(F(1,N),entropy([t*t for t in c[x]])))
    for t in range(D):
        row=[c[x][t] for x in range(N)]
        r=sum(z*z for z in row)/N
        R.append(r)
        if not r: continue
        post=[z*z/(N*r) for z in row]
        amplitudes=walsh(row)
        nu=[z*z/(N*N*r) for z in amplitudes]
        ck(sum(post)==1 and sum(nu)==1)
        ck(all(F(w[s+N*t],L)==amplitudes[s]/N for s in range(N)))
        B=plus((1,B),(r,entropy(nu)))
        M=plus((1,M),(r,{2:F(a)}),( -r,entropy(post)))
        common=common and all(z*z==row[0]*row[0] for z in row)
        character_rows=character_rows and sum(z!=0 for z in amplitudes)==1
    HF=entropy(p)
    ck(HF==plus((1,avg),(1,B),(1,M)))
    ck(HF==plus((1,entropy(R)),(1,B)))
    Iw=sum(p[s]*((s&(N-1)).bit_count()) for s in range(L))
    Id=sum(p[s]*((s>>a).bit_count()) for s in range(L))
    physical=[F(sum(v[x]!=v[x^(1<<j)] for x in range(L)),L) for j in range(n)]
    ck(Iw==sum(physical[:a]) and Id==sum(physical[a:]))
    ck(Id==sum(sum(z*z*t.bit_count() for t,z in enumerate(c[x])) for x in range(N))/N)
    ck((not M)==common)
    ck((not B)==character_rows)
    ck(bool(B) or not M)  # zero conditional Walsh entropy forces common magnitudes
    ml,mh=interval(M)
    l2,h2=ln_interval(F(2))
    ck(ml>=0 and mh<=2*Iw/h2) if Iw else ck(not M)
    return {'HF':HF,'B':B,'M':M,'Iw':Iw,'Id':Id,'common':common,'zero':not B}

counts={}; zero_counts={}; common_counts={}
for n in range(4):
    for a in range(n+1):
        key=f'n={n},a={a}'; counts[key]=zero_counts[key]=common_counts[key]=0
        for table in range(1<<(1<<n)):
            v=[1 if (table>>x)&1 else -1 for x in range(1<<n)]
            z=check_case(v,n,a,True); counts[key]+=1
            zero_counts[key]+=z['zero']; common_counts[key]+=z['common']

phase_hist={}
for a in (1,2,3):
    hist=defaultdict(int)
    for phase in range(1<<(1<<a)):
        signs=[1 if (phase>>x)&1 else -1 for x in range(1<<a)]
        v=signs+[-z for z in signs]
        z=check_case(v,a+1,a)
        ck(not z['M'])
        ck(z['HF']==entropy([F(w*w,1<<(2*a)) for w in walsh(signs)]))
        hist['character' if z['zero'] else 'positive_coherent_entropy']+=1
    phase_hist[str(a)]=dict(hist)

bent=[]
for m in (2,4,6,8,10,12):
    N=1<<m; delta=F(1,N); root=F(1,1<<(m//2))
    b=[-1 if sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,m,2))%2 else 1 for y in range(N)]
    bp=b.copy(); bp[0]=-1
    v=[v for y in range(N) for v in (b[y],bp[y])]
    z=check_case(v,m+1,1)
    ck(z['Iw']==delta)
    coeff=[F(w,N) for w in walsh(b)]
    ck(all(abs(c)==root for c in coeff))
    ck(all(((c-delta)**2+delta**2)/delta**2>=1/(2*delta) for c in coeff))
    bl,bh=interval(z['B']); dl,dh=interval(plus((1,z['B']),(1,z['M'])))
    ck(bl>=delta*(m-1))
    bent.append({'m':m,'Iw':str(delta),'B_over_I_interval':[str(bl/delta),str(bh/delta)],'deltaH_over_I_interval':[str(dl/delta),str(dh/delta)],'numeric_B_over_I_for_display':float(bl/delta)})

out={'helper_version':'A018-collision-v1','status':'PASS','assertions':assertions,'block_cases':sum(counts.values()),'block_case_counts':counts,'zero_increment_counts':zero_counts,'common_spectrum_counts':common_counts,'signed_literal_cases':276,'phase_histograms':phase_hist,'bent_splices':bent,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer/Fraction, exact formal prime-log identities, rational outward log intervals','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out'/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','assertions','block_cases','signed_literal_cases','elapsed_seconds','phase_histograms')},indent=2))
