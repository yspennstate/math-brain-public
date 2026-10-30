import json, time
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache

ROOT = Path(__file__).resolve().parents[1]
START = time.monotonic()
COUNTS = {}

def check(condition, label):
    assert condition, label
    COUNTS[label] = COUNTS.get(label, 0) + 1
    if time.monotonic() - START > 59:
        raise RuntimeError('Frozen 60 second pilot exceeded; no escalation')

def walsh(values):
    a = list(values)
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for k in range(j, j+h):
                x,y=a[k],a[k+h]
                a[k],a[k+h]=x+y,x-y
        h *= 2
    return [Q(x,len(a)) for x in a]

def spectrum(values):
    return [a*a for a in walsh(values)]

def ln_unit_bounds(y, terms=22):
    # 1 <= y <= 2. ln y = 2 sum z^(2j+1)/(2j+1).
    z=(y-1)/(y+1)
    z2=z*z
    power=z
    lo=Q(0)
    for j in range(terms):
        lo += 2*power/(2*j+1)
        power *= z2
    rem=2*power/((2*terms+1)*(1-z2))
    return lo,lo+rem

LN2=ln_unit_bounds(Q(2))

@lru_cache(None)
def log_inv_bounds(p):
    x=1/p
    k=0
    while x >= 2:
        x /= 2
        k += 1
    lo,hi=ln_unit_bounds(x)
    return Q(k)+lo/LN2[1],Q(k)+hi/LN2[0]

def ent(law):
    lo=hi=Q(0)
    for p in law:
        if p:
            a,b=log_inv_bounds(p)
            lo += p*a
            hi += p*b
    return lo,hi

def influence(values, indices):
    return sum((Q(sum(values[x] != values[x^(1<<i)] for x in range(len(values))),len(values)) for i in indices),Q(0))

def overlaps(a,b):
    return max(a[0],b[0]) <= min(a[1],b[1])

def add(a,b):
    return a[0]+b[0],a[1]+b[1]

def scale(a,c):
    return a[0]*c,a[1]*c

cases=0
for m in (1,2,3):
    N=1<<m
    for table in range(1<<N):
        u=[1 if (table>>x)&1 else -1 for x in range(N)]
        au=walsh(u)
        mu=au[0]
        d=1-mu
        v=1-mu*mu
        iu=influence(u,range(m))
        for r in (1,2,3):
            p=Q(1,1<<r)
            # Core coordinates are low bits; activation assignment is z=0.
            f=[u[t&(N-1)] if t>>m==0 else 1 for t in range(1<<(m+r))]
            af=walsh(f)
            law=[a*a for a in af]
            check(sum(law)==1,'Parseval')
            for U in range(1<<r):
                for T in range(N):
                    expected=p*(au[T]-(T==0))
                    if U==0 and T==0:
                        expected+=1
                    check(af[(U<<m)|T]==expected,'activation coefficient')
            iw=influence(f,range(m))
            ic=influence(f,range(m,m+r))
            check(iw==p*iu,'queried influence')
            check(ic==r*p*d,'reserved terminal influence')
            check(sum(Q(s.bit_count())*mass for s,mass in enumerate(law))==iw+ic,'spectral versus physical influence')
            B=(Q(0),Q(0))
            R=[]
            for U in range(1<<r):
                row=law[U<<m:(U+1)<<m]
                mass=sum(row)
                R.append(mass)
                if mass:
                    B=add(B,scale(ent(tuple(x/mass for x in row)),mass))
            check(R[0]==1-2*p*d+2*p*p*d,'empty control fiber')
            check(all(x==2*p*p*d for x in R[1:]),'nonempty control fibers')
            if d:
                shifted=[(au[T]-(T==0))**2/(2*d) for T in range(N)]
                check(sum(shifted)==1,'normalized defect law')
                for U in range(1,1<<r):
                    check([x/R[U] for x in law[U<<m:(U+1)<<m]]==shifted,'exact defect conditional law')
            check(B[1]<=p*(2*d*m+2),'analytic conditional bound certified')
            delta=d/2
            if v:
                L=ent(tuple(x*x/v for x in au[1:]))
                hdelta=ent((delta,1-delta))
                R0=R[0]
                q=p*p*v
                exceptional=scale(ent((q/R0,1-q/R0)),R0/p)
                exact_rhs=add(add(scale(L,v),scale(hdelta,4*delta*(1-p))),exceptional)
                check(overlaps(scale(B,1/p),exact_rhs),'exact core-block transport enclosure')
                if mu>=0:
                    coreH=ent(tuple(x*x for x in au))
                    check(B[1]<=p*(coreH[0]+5*iu),'FEI-to-block transfer certified')
            Dr=[-1]+[1]*((1<<r)-1)
            hd=ent(tuple(spectrum(Dr)))
            idr=influence(Dr,range(r))
            check(idr==2*r*p,'point defect influence')
            check(hd[1]<=4*idr,'terminal entropy certified')
            leafH=scale(hd,d/2)
            fullH=ent(tuple(law))
            marginalH=ent(tuple(R))
            M=(marginalH[0]-leafH[1],marginalH[1]-leafH[0])
            check(overlaps(fullH,add(add(B,M),leafH)),'entropy chain enclosure')
            # Verify exact joint channel law by enumerating physical core leaves.
            channel_marginal=[Q(0)]*(1<<r)
            for value in u:
                child=[value]+[1]*((1<<r)-1)
                for U,mass in enumerate(spectrum(child)):
                    channel_marginal[U]+=mass/N
            check(channel_marginal==R,'physical channel marginal')
            if iu:
                eta=iu/m
                # C = 6/eta + 2/ln2 dominates the terminal constant 4.
                C_lower=6/eta+2/LN2[1]
                check(fullH[1]<=C_lower*(iw+ic),'complete stopping payment certified')
            cases+=1

# Extra fixed coded plateau and bent-splice fixtures; no adaptive increase.
for k in (2,4,6):
    b=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<k)]
    # parity lift b(x_i xor t), uniform on an even-parity spectral code.
    lifted=[b[(x&((1<<k)-1)) ^ (((1<<k)-1) if (x>>k)&1 else 0)] for x in range(1<<(k+1))]
    pl=spectrum(lifted)
    check(all((s.bit_count()%2==0 or mass==0) for s,mass in enumerate(pl)),'coded plateau parity support')
    check(ent(tuple(pl))==(Q(k),Q(k)),'coded plateau full entropy')
    check(influence(lifted,range(k+1))==Q(k+1,2),'coded plateau influence')
    for i in range(k+1):
        check(all(not (pl[s] and pl[s^(1<<i)]) for s in range(len(pl))),'coded plateau zero singleton erasure')
    flipped=b.copy()
    flipped[0]*=-1
    splice=b+flipped
    check(influence(splice,[k])==Q(1,1<<k),'bent marker exact influence')
    check(influence(splice,range(k))==Q(k,2)+Q(k,1<<k),'bent splice core influence')

result={'status':'PASS','activation_cases':cases,'assertions':sum(COUNTS.values()),'checks':COUNTS,'elapsed_seconds':time.monotonic()-START,'arithmetic':'Fraction plus rigorously bounded rational logarithms','log_terms':22,'independent_review':'NOT_PERFORMED'}
(ROOT/'out'/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
