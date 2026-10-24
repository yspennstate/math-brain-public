import itertools, json, time, hashlib
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
N=24
assertions=0
def check(x):
    global assertions
    assertions+=1
    assert x

def series(x):
    z=(x-1)/(x+1)
    check(0<=z<=F(1,3))
    low=sum((2*z**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    tail=2*z**(2*N+1)/F(2*N+1)/(1-z*z)
    return low,low+tail
L2=series(F(2))
@lru_cache(None)
def ln(x):
    check(x>=1)
    k=0
    while x>=2:
        x/=2; k+=1
    lo,hi=series(x)
    return lo+k*L2[0],hi+k*L2[1]

def product(a):
    r=F(1)
    for x in a:r*=x
    return r

def spectrum(mask,p):
    values=[F(1 if mask>>x&1 else -1) for x in range(8)]
    a=[]
    for s in range(8):
        a.append(sum(((-1)**((s^u).bit_count())*values[u]
                      for u in range(8) if u&s==u),F(0)))
    v=[4*t*(1-t) for t in p]
    c=[]; mass=[]
    for s in range(8):
        c.append(sum((a[u]*product(p[j] for j in range(3) if u>>j&1 and not s>>j&1)
                      for u in range(8) if u&s==s),F(0))/2**s.bit_count())
        moment=sum((values[x]*product(p[j] if x>>j&1 else 1-p[j] for j in range(3))*
                    product(F((x>>j)&1)-p[j] for j in range(3) if s>>j&1)
                    for x in range(8)),F(0))
        direct=moment*moment/product(p[j]*(1-p[j]) for j in range(3) if s>>j&1)
        closed=product(v[j] for j in range(3) if s>>j&1)*c[-1]**2
        check(direct==closed)
        check(abs(c[-1])<=1)
        mass.append(direct)
    check(sum(mass)==1)
    # Independent signed-derivative variance and the summed degree identity.
    reserve=F(0)
    for j in range(3):
        dd=[]
        for x in range(8):
            if x>>j&1:continue
            prob=product(p[k] if x>>k&1 else 1-p[k] for k in range(3) if k!=j)
            d=(values[x|(1<<j)]-values[x])/2
            dd.append((prob,d))
        mean=sum((r*d for r,d in dd),F(0))
        var=sum((r*d*d for r,d in dd),F(0))-mean*mean
        check(mean==c[1<<j])
        check(var>=abs(mean)*(1-abs(mean)))
        reserve+=v[j]*var
    check(reserve==sum((s.bit_count()*mass[s] for s in range(8) if s.bit_count()>=2),F(0)))
    return c,mass,reserve

def energy(c,mass,indices):
    lo=hi=F(0)
    for s in indices:
        if not mass[s]:continue
        l,h=ln(1/(c[s]*c[s]))
        lo+=mass[s]*l;hi+=mass[s]*h
    return lo,hi

L4=ln(F(4));L9=ln(F(9))
def case(mask,p):
    c,m,r=spectrum(mask,p)
    delta=sum(((s.bit_count()-1)*m[s] for s in range(1,8)),F(0))
    T=m[7]
    E=energy(c,m,range(1,8))
    singles=energy(c,m,(1,2,4))
    check(singles[1]<=2*r)
    check(2*r==4*delta-2*T)
    bound=4*delta+L4[0]*delta
    if mask==22:bound-=L9[1]*T
    if mask==232:bound+=(1-L4[1])*T
    check(E[1]<bound)
    # Check the exact normalized coefficient forms used in the proof.
    p0,p1,p2=p
    if mask==22:
        expected=[1-2*p1-2*p2+3*p1*p2,1-2*p0-2*p2+3*p0*p2,1-2*p0-2*p1+3*p0*p1]
        check([c[s] for s in (1,2,4)]==expected)
        for s,k in ((3,2),(5,1),(6,0)):
            check(c[s]==-1+F(3,2)*p[k])
            check(energy(c,m,[s])[1]<=L4[0]*m[s]+F(2,3)*T)
        check(c[7]==F(3,4))
    if mask==129:
        check(c[7]==0)
        check(all(c[s]==F(1,2) for s in (3,5,6)))
    if mask==25:
        check((c[1],c[2],c[4],c[3],c[5],c[6],c[7])==
              (-1+2*p1-p1*p2,-1+2*p0-p0*p2,-p0*p1,1-p2/2,-p1/2,-p0/2,F(-1,4)))
        check(energy(c,m,[3])[1]<=L4[0]*m[3]-2*T)
        for s in (5,6):check(energy(c,m,[s])[1]<=L4[0]*m[s]+2*T)
    if mask==232:
        means=[2*t-1 for t in p]
        check(all(c[s]==-means[k]/2 for s,k in ((3,2),(5,1),(6,0))))
        for s in (3,5,6):check(energy(c,m,[s])[1]<=L4[0]*m[s]+T)
        check(c[7]==F(-1,2))
    if mask==228:
        q=p0;v0=4*p1*(1-p1);v1=4*p2*(1-p2);d=abs(2*(p2-p1))
        check(m[1]==q*(1-q)*d*d)
        check(m[2]==(1-q)**2*v0 and m[4]==q*q*v1)
        check(m[3]==q*(1-q)*v0 and m[5]==q*(1-q)*v1)
        check(m[6]==m[7]==0)
        check(delta==q*(1-q)*(v0+v1))
        check(v0+v1>=d*(2-d))
    return E[0]/delta/L2[1],E[1]/delta/L2[0]

grid=[F(1,16),F(1,8),F(1,4),F(1,2),F(3,4),F(7,8),F(15,16)]
records=[]
for mask in (22,232,129,25,228):
    winner=None
    for p in itertools.product(grid,repeat=3):
        lo,hi=case(mask,p)
        if winner is None or lo>winner[0]:winner=(lo,hi,p)
    records.append({'mask':mask,'cases':343,'best_grid_ratio_interval':[str(winner[0]),str(winner[1])],
                    'display_only':float(winner[0]),'probabilities':[str(x) for x in winner[2]]})
paths=[]
for k in range(2,11):
    t=F(1,2**k)
    for mask,p in ((22,(1-t**3,t,t)),(232,(1-t**3,t,t)),(129,(t,t,t)),
                   (25,(t,t,1-t**3)),(228,(t,t*t,1-t**4))):
        lo,hi=case(mask,p)
        paths.append({'mask':mask,'k':k,'ratio_interval':[str(lo),str(hi)],'display_only':float(lo)})
out={'helper':'A043-ternary-continuum-proof-check-v1','cases':1760,'assertions':assertions,
     'runtime_seconds':time.perf_counter()-START,'log_terms':N,
     'log_error_proof':'2 sum_{j=0}^{N-1} z^(2j+1)/(2j+1); remaining tail <= 2 z^(2N+1)/((2N+1)(1-z^2)), z in [0,1/3]; normalize x by exact powers of two',
     'unique_log_arguments':ln.cache_info().currsize,'all_passed':True,'grid':records,'boundary_paths':paths}
(ROOT/'out'/'proof_checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('grid','boundary_paths','log_error_proof')}))
print('boundary k=10 displays:',[(r['mask'],r['display_only']) for r in paths if r['k']==10])
