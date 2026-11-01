from fractions import Fraction as Q
from pathlib import Path
import itertools, json, sys, time

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
COUNT = 0
PILOT = '--pilot' in sys.argv

def check(v):
    global COUNT
    assert v
    COUNT += 1
    if time.perf_counter()-START > 55:
        raise RuntimeError('frozen runtime limit')

def spectrum(f):
    size = len(f)
    return [Q(sum(v*(-1 if (s & x).bit_count()%2 else 1) for x,v in enumerate(f)),size) for s in range(size)]

def influences(f):
    n = len(f).bit_length()-1
    return [Q(sum(f[x] != f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n)]

def factors(k):
    result = {}
    d = 2
    while d*d <= k:
        while k%d == 0:
            result[d] = result.get(d,0)+1
            k //= d
        d += 1
    if k > 1:
        result[k] = result.get(k,0)+1
    return result

def add(*vs):
    out = {}
    for v in vs:
        for p,c in v.items(): out[p] = out.get(p,Q(0))+c
    return {p:c for p,c in out.items() if c}

def scale(v,c): return {p:q*c for p,q in v.items() if q*c}

def term(mass, arg):
    # mass*ln(arg), exact as rational coefficients of ln(primes)
    if mass == 0: return {}
    assert arg > 0
    return add({p:mass*k for p,k in factors(arg.numerator).items()},
               {p:-mass*k for p,k in factors(arg.denominator).items()})

def Hmass(ps): return add(*(term(-p,p) for p in ps if p))

def entropy(f): return Hmass([a*a for a in spectrum(f)])

def deficit(f,C): return add(entropy(f),{2:-C*sum(influences(f))})

def log_interval(x):
    if x == 1: return Q(0),Q(0)
    k = x.bit_length()-1
    y = Q(x,1<<k)
    def series(y):
        z = (y-1)/(y+1)
        lo = 2*sum((z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
        tail = 2*z**49/(49*(1-z*z))
        return lo,lo+tail
    a,b = series(Q(2))
    c,d = series(y)
    return k*a+c,k*b+d

def enclosure(v):
    lo=hi=Q(0)
    for p,c in v.items():
        a,b=log_interval(p)
        lo += c*(a if c>=0 else b)
        hi += c*(b if c>=0 else a)
    return lo,hi

def bits_enclosure(v):
    a,b=enclosure(v); c,d=log_interval(2)
    vals=[a/c,a/d,b/c,b/d]
    return min(vals),max(vals)

def restrict(f,mask,value):
    n=len(f).bit_length()-1
    free=[i for i in range(n) if not(mask>>i&1)]
    return [f[value|sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free))]

def block_drop(f,mask):
    coords=[i for i in range(len(f).bit_length()-1) if mask>>i&1]
    children=[restrict(f,mask,sum(((x>>j)&1)<<i for j,i in enumerate(coords))) for x in range(1<<len(coords))]
    average=scale(add(*(entropy(c) for c in children)),Q(1,len(children)))
    return add(entropy(f),scale(average,-1))

def activate(g,r):
    return [g[x] if y==0 else 1 for y in range(1<<r) for x in range(len(g))]

def tensor(g,h): return [a*b for b in h for a in g]

def minus_point(r): return [-1]+[1]*((1<<r)-1)

def activation_H(g,r):
    t=Q(1,1<<r); mu=Q(sum(g),len(g)); v=1-mu*mu
    b=1-t+t*mu; c=t*t*(1-mu)**2
    return add(Hmass([b*b]),scale(Hmass([c]),(1<<r)-1),scale(entropy(g),t),
               term(t*mu*mu,mu*mu) if mu else {},{2:2*r*t*v})

activation_cases=tensor_cases=surgery_cases=0
for n in range(3 if PILOT else 4):
    for word in range(1<<(1<<n)):
        g=[-1 if word>>x&1 else 1 for x in range(1<<n)]
        mu=Q(sum(g),len(g)); ig=influences(g)
        for r in ([1,2] if PILOT else [1,2,3]):
            f=activate(g,r); t=Q(1,1<<r); a=spectrum(f); ag=spectrum(g)
            for u in range(1<<r):
                for s in range(1<<n):
                    target=(1-t+t*mu) if u==s==0 else (t*(mu-1) if s==0 else t*ag[s])
                    check(a[s|(u<<n)]==target)
            check(sum(x*x for x in a)==1)
            check(influences(f)==[t*x for x in ig]+[t*(1-mu)]*r)
            check(entropy(f)==activation_H(g,r))
            controls=((1<<r)-1)<<n; data=(1<<n)-1
            Lc=block_drop(f,controls); Lx=block_drop(f,data) if n else {}
            check(Lc==add(entropy(f),scale(entropy(g),-t)))
            check(Lx==add(entropy(f),scale(entropy(minus_point(r)),-(1-mu)/2)))
            C=Q(2)
            df=deficit(f,C); dg=deficit(g,C)
            check(add(Lc,{2:-C*r*t*(1-mu)},scale(df,-1))==scale(dg,-t))
            if r>=2:
                Li=block_drop(f,1<<n)
                child=activate(g,r-1)
                check(add(Li,{2:-C*t*(1-mu)},scale(df,-1))==scale(deficit(child,C),Q(-1,2)))
            activation_cases+=1

words=range(4) if PILOT else range(16)
for u,v in itertools.product(words,repeat=2):
    g=[-1 if u>>x&1 else 1 for x in range(4)]
    h=[-1 if v>>x&1 else 1 for x in range(4)]
    f=tensor(g,h); a=spectrum(f); ag=spectrum(g); ah=spectrum(h)
    check(a==[x*y for y in ah for x in ag])
    check(influences(f)==influences(g)+influences(h))
    check(entropy(f)==add(entropy(g),entropy(h)))
    C=Q(2); df=deficit(f,C)
    check(add(block_drop(f,12),{2:-C*sum(influences(h))},scale(df,-1))==scale(deficit(g,C),-1))
    tensor_cases+=1

for d in ([1] if PILOT else [1,2]):
    for word in range(1<<(1<<d)):
        g=[-1 if word>>x&1 else 1 for x in range(1<<d)]
        for m in ([1] if PILOT else [1,2]):
            core=[1]
            for _ in range(m): core=tensor(core,g)
            f=core+[-a for a in core]; h=f.copy(); h[0]*=-1
            N=d*m+1; p=Q(1,1<<N); a=spectrum(f); b=spectrum(h)
            check(b==[x-2*p*f[0] for x in a])
            check(all(x for x in b))
            check(all((x*(1<<N)).numerator%4==2 for x in b))
            eps=Q(2,1<<N)
            check(influences(h)[-1]==1-eps)
            corr=Q(sum(h[x]*h[x^(1<<(N-1))] for x in range(1<<N)),1<<N)
            check((1-abs(corr))/2==eps)
            inf0=influences(f); inf1=influences(h)
            for i in range(N): check(inf1[i]-inf0[i]==2*p*f[0]*f[1<<i])
            for i in range(N):
                for j in range(i):
                    K0=sum(a[s]*a[s] for s in range(1<<N) if s>>i&1 and s>>j&1)
                    K1=sum(b[s]*b[s] for s in range(1<<N) if s>>i&1 and s>>j&1)
                    ri=f[0]*f[1<<i]; rj=f[0]*f[1<<j]; rij=f[0]*f[(1<<i)|(1<<j)]
                    check(K1-K0==p*(ri+rj-rij))
                    def curvature(t): return Q(sum(t[x]*t[x^(1<<i)]*t[x^(1<<j)]*t[x^(1<<i)^(1<<j)]==-1 for x in range(1<<N)),1<<N)
                    sig=f[0]*f[1<<i]*f[1<<j]*f[(1<<i)|(1<<j)]
                    check(curvature(h)-curvature(f)==4*p*sig)
            # New reconstruction: each nontrivial cut has a rank-two sign matrix.
            for cut in range(1,(1<<N)-1):
                rows=[i for i in range(N) if cut>>i&1]; cols=[i for i in range(N) if not cut>>i&1]
                idx=lambda x,co: sum(((x>>j)&1)<<i for j,i in enumerate(co))
                matrix=[[h[idx(x,rows)|idx(y,cols)] for y in range(1<<len(cols))] for x in range(1<<len(rows))]
                check(any(matrix[x][y]*matrix[0][0]!=matrix[x][0]*matrix[0][y] for x in range(len(matrix)) for y in range(len(matrix[0]))))
            if N>=5:
                # Verify strong singleton-failure payment in natural units at C=1.
                L=block_drop(h,1<<(N-1))
                bound=add(Hmass([eps,1-eps]),{2:0})
                # kappa*eps bits = 2*eps natural units: interval below handles this rational separately.
                lo,hi=enclosure(add(bound,scale(L,-1)))
                check(lo+2*eps>=0)
                lo,hi=enclosure(add({2:1-eps},scale(bound,-1)))
                check(lo-2*eps>0)
            surgery_cases+=1

records=[]
if not PILOT:
    g=minus_point(3); C=Q(2)
    for name,f,block,payment in [
        ('tensor_d3_d3',tensor(g,g),56,sum(influences(g))),
        ('activation_r1_d3',activate(g,1),8,Q(1,8)),
        ('activation_r2_d3',activate(g,2),24,Q(1,8)),
        ('activation_r2_first_control',activate(g,2),8,Q(1,16))]:
        df=deficit(f,C); shortfall=add(df,scale(block_drop(f,block),-1),{2:C*payment})
        dl,du=bits_enclosure(df); sl,su=bits_enclosure(shortfall)
        check(dl>0); check(sl>0)
        records.append({'name':name,'C':'2','deficit_bits_interval':[str(dl),str(du)],'criticality_shortfall_bits_interval':[str(sl),str(su)],'strict_lower_bound':'1/100','margin_check':str(sl>Q(1,100))})
    check(all(r['margin_check']=='True' for r in records))

result={'status':'PASS','helper_version':'A055-check-embeddings-v1','assertions':COUNT,'activations':activation_cases,'tensor_pairs':tensor_cases,'surgeries':surgery_cases,'fixed_witness_records':records,'helper_elapsed_seconds':time.perf_counter()-START,'arithmetic':'integer direct Walsh, Fraction, exact prime-log vectors, rational atanh intervals'}
out=ROOT/'out'/('PILOT.json' if PILOT else 'EXACT_CHECK.json')
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='fixed_witness_records'},indent=2))
