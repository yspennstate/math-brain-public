"""Frozen exact two-cell validation; no external packages or writes outside this run."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools, json, time, hashlib

RUN=Path(__file__).resolve().parents[1]
START=time.monotonic()
checks=0
def check(value, label):
    global checks
    checks+=1
    if not value: raise AssertionError(label)
    if checks%2048==0 and time.monotonic()-START>55: raise TimeoutError('frozen runtime cap')

def walsh(v):
    a=list(v); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step): a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
        step*=2
    return tuple(a)

def energy(v,n):
    return Q(sum((v[x]-v[x^(1<<i)])**2 for x in range(1<<n) for i in range(n)),4*(1<<n))

def span(basis):
    a={0}
    for b in basis: a|={x^b for x in tuple(a)}
    return frozenset(a)

def basis_for(v):
    b=[]; s={0}
    for x in sorted(v):
        if x not in s:
            b.append(x); s|={z^x for z in tuple(s)}
    return b

def cells(n):
    N=1<<n; spaces=set()
    for mask in range(1<<(N-1)):
        v=frozenset([0]+[i+1 for i in range(N-1) if mask>>i&1])
        if all(x^y in v for x in v for y in v): spaces.add(v)
    seen=set(); out=[]
    for V in spaces:
        for off in range(N):
            A=frozenset(off^v for v in V)
            if A in seen: continue
            seen.add(A); b=basis_for(V); k=len(b)
            coords={off^sumxor([b[i] for i in range(k) if z>>i&1]):z for z in range(1<<k)}
            mon=[0]+[1<<i for i in range(k)]+[(1<<i)|(1<<j) for i in range(k) for j in range(i)]
            for coeff in range(1<<len(mon)):
                vals=[0]*N
                for x,z in coords.items():
                    bit=sum(1 for j,m in enumerate(mon) if coeff>>j&1 and z&m==m)%2
                    vals[x]=1-2*bit
                vals=tuple(vals)
                out.append((A,V,vals,walsh(vals),energy(vals,n)))
    return out

def sumxor(values):
    ans=0
    for v in values: ans^=v
    return ans

@lru_cache(None)
def log2_interval(q):
    q=Q(q)
    if q==1: return Q(0),Q(0)
    e=0
    while q<1: q*=2; e-=1
    while q>=2: q/=2; e+=1
    def ln_int(t):
        z=(t-1)/(t+1); acc=Q(0)
        for j in range(18): acc+=2*z**(2*j+1)/(2*j+1)
        rem=2*z**37/(37*(1-z*z))
        return acc,acc+rem
    a,b=ln_int(q); c,d=ln_int(Q(2))
    return e+a/d,e+b/c

@lru_cache(None)
def atom_entropy(raw,N):
    if raw==0: return Q(0),Q(0)
    p=Q(raw*raw,N*N); lo,hi=log2_interval(1/p)
    return p*lo,p*hi

def entropy_bill(w,N):
    intervals=[atom_entropy(abs(v),N) for v in w]
    return sum(t[0] for t in intervals),sum(t[1] for t in intervals)

def phase_degree(vals):
    a=[(1-v)//2 for v in vals]
    for i in range(len(vals).bit_length()-1):
        for x in range(len(vals)):
            if x>>i&1: a[x]^=a[x^(1<<i)]
    return max([x.bit_count() for x,v in enumerate(a) if v]+[0])

summary=[]; negative_parallel=False; witnesses={}
for n in range(4):
    N=1<<n; rows=cells(n); pair_count=0; parallel_count=0; minimum_ratio=None
    for A,V,a,wa,Ea in rows:
        s=len(A); lo,hi=entropy_bill(wa,N)
        check(Ea==Q(sum(i.bit_count()*w*w for i,w in enumerate(wa)),N*N),'physical versus Fourier component energy')
        check(hi<=4*Ea or lo==hi==4*Ea,'single joint rate4')
        # Flatness and exact quadratic energy interface, independent of polar ranks.
        positive={v*v for v in wa if v}
        check(len(positive)==1,'quadratic flat spectrum')
        count=sum(v!=0 for v in wa)
        check(count&(count-1)==0,'dyadic flat support')
        check(Q(s,N)*(count.bit_length()-1)<=2*Ea,'quadratic normalized entropy')
    for j,(A,V,a,wa,Ea) in enumerate(rows):
        for B,W,b,wb,Eb in rows[j+1:]:
            if A&B: continue
            pair_count+=1
            u=tuple(x+y for x,y in zip(a,b)); wu=tuple(x+y for x,y in zip(wa,wb)); E=energy(u,n); E0=Ea+Eb
            check(walsh(u)==wu,'linear transform replay')
            check(all(w*w<=2*(x*x+y*y) for w,x,y in zip(wu,wa,wb)),'pointwise coherent domination')
            check(sum(w*w for w in wu)==N*(len(A)+len(B)),'exact row norm')
            check(E==Q(sum(i.bit_count()*w*w for i,w in enumerate(wu)),N*N),'physical versus Fourier collision energy')
            if V!=W:
                check(3*E>=E0,'nonparallel energy protection')
                if len(A)==len(B): check(2*E>=E0,'equal nonparallel energy')
                if E0: minimum_ratio=min(minimum_ratio or E/E0,E/E0)
                if E0 and E/E0==Q(1,3) and 'sharp_energy' not in witnesses:
                    witnesses['sharp_energy']={'n':n,'a':a,'b':b,'E0':str(E0),'E':str(E)}
            else:
                parallel_count+=1
                if E0 and 3*E<E0: negative_parallel=True
                C=A|B; off=min(C); U=frozenset(x^off for x in C); basis=basis_for(U)
                check(span(basis)==U,'parallel union affine')
                intrinsic=[u[off^sumxor([basis[i] for i in range(len(basis)) if z>>i&1])] for z in range(1<<len(basis))]
                check(phase_degree(intrinsic)<=3,'parallel cubic glue')
            lo,hi=entropy_bill(wu,N)
            check(hi<=24*E or lo==hi==24*E,'complete joint row rate24')
            mass=Q(len(A)+len(B),N); logmass=log2_interval(1/mass)
            check(hi-mass*logmass[0]<=24*E,'full conditional row entropy rate24')
            if V==W: check(hi<=4*E or lo==hi==4*E,'parallel complete rate4')
            # Every physical restriction has two disjoint affine quadratic pieces.
            for i in range(n):
                for bit in (0,1):
                    aa=[a[x] for x in range(N) if x>>i&1==bit]
                    bb=[b[x] for x in range(N) if x>>i&1==bit]
                    check(all(x*y==0 for x,y in zip(aa,bb)),'restricted disjoint supports')
                    check(all(x+y in (-1,0,1) for x,y in zip(aa,bb)),'restricted unit heights')
    summary.append({'n':n,'signed_cell_rows':len(rows),'disjoint_signed_pairs':pair_count,'parallel_pairs':parallel_count,'minimum_nonparallel_energy_ratio':str(minimum_ratio)})
check(negative_parallel,'negative control rejects unrestricted geometric bound')

# Actual nonproduct Boolean cubic; all sixteen-fourth-order parity derivatives for quartic guard.
cubic=tuple(-1 if x==7 else 1 for x in range(8)); wc=walsh(cubic)
check(phase_degree(cubic)==3,'cubic degree')
check(sorted(w*w for w in wc)==[4]*7+[36],'nonproduct cubic masses')
p=[Q(w*w,64) for w in wc]; marg=[sum(p[x] for x in range(8) if x>>i&1) for i in range(3)]
def prod(it):
    a=Q(1)
    for x in it:a*=x
    return a
check(any(p[x]!=prod(marg[i] if x>>i&1 else 1-marg[i] for i in range(3)) for x in range(8)),'genuine spectral nonproduct')
quartic=tuple(-1 if x==15 else 1 for x in range(16))
check(phase_degree(quartic)==4,'quartic forbidden tensor')
# Sharpness of geometric factor1/3: A is a halfcube, B a quartercube parallel to one face.
# Search was frozen to n<=3 above; record extremum, do not infer global sharpness from it.
witnesses['cubic']={'truth':cubic,'raw_walsh':wc,'influence':str(energy(cubic,3))}
witnesses['quartic']={'truth':quartic,'phase_degree':4}
result={'status':'PASS','checks':checks,'domains':summary,'negative_parallel_control':negative_parallel,'witnesses':witnesses,'runtime_seconds':time.monotonic()-START,'arithmetic':'integer/Fraction; rational logarithm enclosure with 18 atanh terms and explicit geometric remainder','proof_rung':'analytic proof with exact finite validation; not Lean-certified'}
(RUN/'out').mkdir(exist_ok=True)
(RUN/'out'/'validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','domains','runtime_seconds']}))
