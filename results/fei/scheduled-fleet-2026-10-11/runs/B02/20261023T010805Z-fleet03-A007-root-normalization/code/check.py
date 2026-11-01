from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import prod
from functools import lru_cache
import json,time,argparse,hashlib

ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
start=time.monotonic(); assertions=0
counts={'functions':0,'implicants':0,'fibers':0,'gradient_vectors':0,'scalar_pairs':0,'boolean_pairs':0}
signed_witnesses={}
def ck(b):
    global assertions
    assert b; assertions+=1
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,c): return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
@lru_cache(maxsize=4096)
def ln(x):
    assert x>0
    if x==1:return Q(0),Q(0)
    j=0; u=x
    while u>=2:u/=2;j+=1
    while u<1:u*=2;j-=1
    def near(v):
        z=(v-1)/(v+1); total=Q(0); term=z
        for k in range(32):total+=2*term/(2*k+1);term*=z*z
        return total,total+2*term/(65*(1-z*z))
    return add(near(u),mul(near(Q(2)),j))
def D(x):return prod(1+a for a in x)-1
def gradcheck(x):
    A=sum(x); d=D(x); ck(A>0 and d>0)
    for i in range(len(x)):
        E=prod(1+x[j] for j in range(len(x)) if j!=i)
        num=A*E-d
        ck(0<=num<=A*d)
    counts['gradient_vectors']+=1
def paircheck(x,y,tag):
    Ax,Ay=sum(x),sum(y); dx,dy=D(x),D(y); loss=Ax-Ay
    ck(all(0<b<=a for a,b in zip(x,y)))
    # Exact prior enumeration is independent of derivative/marginal formulas.
    old={}; new={}
    for mask in range(1,1<<len(x)):
        old[mask]=prod(x[i] for i in range(len(x)) if mask>>i&1)/dx
        new[mask]=prod(y[i] for i in range(len(x)) if mask>>i&1)/dy
    ck(sum(old.values())==sum(new.values())==1)
    mus=[sum(v for m,v in new.items() if m>>i&1) for i in range(len(x))]
    for i in range(len(x)):
        ck(mus[i]==y[i]*prod(1+y[j] for j in range(len(y)) if i!=j)/dy)
        ck(0<=mus[i]-y[i]/Ay<=y[i])
    delta=ln(dx*Ay/(dy*Ax)) # Delta(x)-Delta(y), no unsigned truncation.
    ck(delta[0]>=0 and delta[1]<=loss if loss else dx==dy)
    difference=delta
    kl=ln(dx/dy)
    for i in range(len(x)):
        t=y[i]/x[i]; lt=ln(t)
        difference=add(difference,mul(lt,mus[i]-y[i]/Ay))
        kl=add(kl,mul(lt,mus[i]))
        ck((mul(ln(1/t),y[i]))[1]<=x[i]-y[i] if t<1 else True)
    if loss:ck(difference[0]>=-loss and difference[1]<=loss)
    else:ck(difference==(0,0))
    if new==old:ck(kl==(0,0) or kl[0]<=0<=kl[1])
    else:ck(kl[0]>0)
    if difference[0]>0 and 'positive' not in signed_witnesses:
        signed_witnesses['positive']={'tag':tag,'x':list(map(str,x)),'y':list(map(str,y)),
              'difference_natural_interval':list(map(str,difference))}
    if difference[1]<0 and 'negative' not in signed_witnesses:
        signed_witnesses['negative']={'tag':tag,'x':list(map(str,x)),'y':list(map(str,y)),
              'difference_natural_interval':list(map(str,difference))}

# Derivatives, including unequal activities. Scalar grids are not Boolean spectra.
for N in range(1,3 if args.pilot else 5):
    for x in product([Q(1,64),Q(1,8),Q(1,2)],repeat=N):gradcheck(x)
for N in range(1,3 if args.pilot else 4):
    for x in product([Q(1,64),Q(1,8),Q(1,2)],repeat=N):
        for ts in product([Q(1,4),Q(1,2),Q(1)],repeat=N):
            paircheck(x,tuple(a*t for a,t in zip(x,ts)),f'grid{N}')
            counts['scalar_pairs']+=1

# Full physical fibers of all signed conjunction implicants, not a spectral proxy.
for n in range(1,3 if args.pilot else 4):
    size=1<<n
    faces=[]
    for signs in product([-1,0,1],repeat=n):
        R=[i for i,s in enumerate(signs) if s]
        if not R:continue
        points=[z for z in range(size) if all(bool(z>>i&1)==(signs[i]==1) for i in R)]
        faces.append((R,signs,points))
    for bits in range(1,(1<<size)-1):
        truth=[bool(bits>>z&1) for z in range(size)]
        false=Q(size-sum(truth),size); variance=4*false*(1-false)
        influences=[Q(sum(truth[z]!=truth[z^(1<<i)] for z in range(size)),size) for i in range(n)]
        I=sum(influences); ck(I>0 and 0<false<1)
        implicants=[]
        for R,signs,points in faces:
            if not all(truth[z] for z in points):continue
            implicants.append((R,signs,points)); w=len(R)
            ck(sum(influences[i] for i in R)>=2*false*w/(2**w-1))
            outside=[i for i in range(n) if i not in R]
            for o in range(1<<len(outside)):
                zs=[]
                for b in range(1<<w):
                    z=sum(((o>>j)&1)<<i for j,i in enumerate(outside))
                    z+=sum(((b>>j)&1)<<i for j,i in enumerate(R)); zs.append(z)
                B=[not truth[z] for z in zs]
                edges=sum(B[z]!=B[z^(1<<i)] for z in range(1<<w) for i in range(w) if not (z>>i&1))
                ck(sum(B)<1<<w); ck(edges>=w*Q(sum(B),2**w-1))
                if sum(B):ck(edges>=w)
                counts['fibers']+=1
            counts['implicants']+=1
        # Chosen once from f's table, independent of every sampled Fourier set.
        chosen=sorted(implicants,key=lambda z:(len(z[0]),z[1]))[:3]
        N=len(chosen); ck(1<=N<=3)
        read=max(sum(i in R for R,s,points in chosen) for i in range(n))
        lam=[Q(1,read)]*N
        ck(all(sum(l for l,(R,s,pts) in zip(lam,chosen) if i in R)<=1 for i in range(n)))
        k=min(len(R) for R,s,pts in chosen); ak=Q(1-Q(1,2**k),k)
        for eps in [Q(1),Q(1,2),Q(1,8),Q(1,64),Q(1,512)]:
            activities=tuple(eps*l/Q(2**len(R)) for l,(R,s,pts) in zip(lam,chosen))
            S=sum(activities); ck(S<=ak*I/(2*false))
            d=D(activities)
            if d>1:ck(variance*ln(d)[1]<=2*ak*(1-false)*I)
            else:ck(d>0)
            ts=tuple(Q(1,2) if i%2==0 else Q(3,4) for i in range(N))
            y=tuple(a*t for a,t in zip(activities,ts))
            lost=sum(activities)-sum(y)
            debit=sum(influences[i]*sum(eps*l*(1-t)*Q(1-Q(1,2**len(R)),len(R))
                       for l,t,(R,s,pts) in zip(lam,ts,chosen) if i in R) for i in range(n))
            ck(variance*lost<=2*(1-false)*debit)
            paircheck(activities,y,f'boolean-n{n}-f{bits}-eps{eps}')
            counts['boolean_pairs']+=1
        counts['functions']+=1
        ck(time.monotonic()-start<55)

# Sharp endpoints of A008; its coefficient is sharp for S, not the looser log step.
for w in range(1,129):
    pi=Q(1,2**w); q=1-pi; I=2*w*pi
    ck(pi==Q(1-pi,w)*I/(2*q))
# Explicit failed hypotheses: no implication, no packing, incorrect rarity.
q=Q(7,8); I=Q(3,4)
ck(Q(1,2)>Q(1,2)*I/(2*q))
ck(Q(1,2)+Q(1,4)+Q(1,4)>Q(1,2))
ck(Q(1,2)>Q(7,24)*I/(2*q))
# Coordinatewise shrinkage cannot be replaced by arbitrary increase.
e=Q(1,2**64); x=(e,e); y=(Q(1,2),Q(1,2)); dx,dy=D(x),D(y)
mu=Q(3,5); kl=add(ln(dx/dy),mul(ln(Q(1,2)/e),2*mu))
ck(kl[0]>sum(abs(a-b) for a,b in zip(x,y)))
# Inherited OR2 guard: arbitrary forced two-root posterior is not the new prior.
for j in [1,2,8,32,128]:
    e=Q(1,2**j); cost_argument=(2*e+e*e)/(e*e)
    ck(cost_argument>2**j)
ck(bool(signed_witnesses.get('positive')))
if not args.pilot:ck(bool(signed_witnesses.get('negative')))
out={'status':'PASS','assertions':assertions,'counts':counts,'pilot':args.pilot,
     'seconds':time.monotonic()-start,'signed_witnesses':signed_witnesses,
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'log_certificate':'32 atanh terms; exact rational remainder; signed intervals'}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/('pilot.json' if args.pilot else 'checks.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['signed_witnesses']}))
