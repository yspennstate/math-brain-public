"""Independent stage-2 Boolean/reference checks. No upstream code is imported."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import json,time

out=Path(__file__).resolve().parents[1]/'out'
start=time.perf_counter(); assertions=0
def ck(v):
    global assertions
    assert v
    assertions+=1
    assert time.perf_counter()-start<60

def walsh(t):
    a=list(t); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j],a[j+h]=x+y,x-y
        h*=2
    return [F(x,len(a)) for x in a]

@lru_cache(None)
def factor(n):
    D={}; k=2
    while k*k<=n:
        while n%k==0: D[k]=D.get(k,0)+1; n//=k
        k+=1
    if n>1: D[n]=D.get(n,0)+1
    return D
def plus(D,E,c=F(1)):
    for k,v in E.items():
        D[k]=D.get(k,F(0))+c*v
        if not D[k]: del D[k]
    return D
def logformal(q):
    return plus({k:F(v) for k,v in factor(q.numerator).items()},
                {k:F(v) for k,v in factor(q.denominator).items()},F(-1))
def ent(P):
    D={}
    for p in P:
        if p: plus(D,logformal(p),-p)
    return D
def cross(P,Q):
    D={}
    for p,q in zip(P,Q):
        if p:
            ck(q>0); plus(D,logformal(q),-p)
    return D
def h2(q): return ent([q,1-q])
def Aformal(r):
    p=F(1,1<<r)
    return plus(ent([(1-p)**2]),{2:F(1)},2*r*p*(2-p))

activation_records=[]; posterior_by_r={}; case_count=0
for m in [1,2,3]:
    for mask in range(1<<(1<<m)):
        if mask.bit_count()!=(1<<m)//2: continue
        core=[-1 if mask>>x&1 else 1 for x in range(1<<m)]
        corea=walsh(core); coreP=[x*x for x in corea]; coreI=sum(F(S.bit_count())*q for S,q in enumerate(coreP))
        # Build the full (stopping leaf, output S) coupling from actual child coefficients.
        joint={(0,S):q for S,q in enumerate(coreP) if q}
        child=core
        Bsum={}
        for r in [1,2,3,4]:
            parent=child+[1]*len(child)
            a=walsh(child)
            new={}; bit=1<<(m+r-1)
            rows=[(J,S,q/2) for (J,S),q in joint.items()]+[(r,0,F(1,2))]
            for J,S,q in rows:
                x=a[S]; y=F(S==0)
                theta=(x-y)**2/(2*(x*x+y*y))
                for U,prob in [(S,1-theta),(S|bit,theta)]:
                    if prob: new[J,U]=new.get((J,U),F(0))+q*prob
            joint=new; child=parent
            P=[x*x for x in walsh(parent)]
            marg=[F(0)]*len(P)
            Jmass={}
            for (J,S),q in joint.items(): marg[S]+=q; Jmass[J]=Jmass.get(J,F(0))+q
            ck(marg==P); ck(sum(joint.values())==1)
            p=F(1,1<<r); D=2*(1-p)
            ck(ent(Jmass.values())=={2:D})
            expectedI=p*(coreI+r)
            ck(sum(F(S.bit_count())*q for S,q in enumerate(P))==expectedI)
            # R_g = P_g/2: complete subprobability core bill = H(g)+1.
            Q=[]
            for S in range(len(P)):
                T=S&((1<<m)-1); U=S>>m
                Q.append(p*p*coreP[T]/2 if T else (p*p if U else (1-p)**2))
            ck(sum(Q)==1-p+p/2)
            CE=cross(P,Q); target=plus(Aformal(r),ent(coreP),p); plus(target,{2:F(1)},p)
            ck(CE==target)
            ck(plus(dict(CE),ent(P),F(-1))=={2:p})
            # Explicit stopping posterior formula, independently evaluated from the joint law.
            for J in range(1,r+1):
                depth=r-J+1
                for Uraw in range(1<<r):
                    inds=[i for i in range(1,r+1) if Uraw>>(r-i)&1]
                    if not inds:
                        val=F(1,1<<depth)
                        for i in range(1,depth+1):
                            k=r-i+1; s=F(1,1<<(k-1)); b=1-s
                            eps=s*s/(2*(1+b*b)); val*=1-eps
                    else:
                        last=max(inds)
                        if depth<last: val=F(0)
                        else:
                            k=r-last+1; s=F(1,1<<(k-1)); b=1-s
                            eps=s*s/(2*(1+b*b))
                            val=F(1,1<<depth)*eps*F(1,1<<(last-1))
                            for i in range(last+1,depth+1):
                                k=r-i+1; s=F(1,1<<(k-1)); b=1-s
                                val*=1-s*s/(2*(1+b*b))
                    ck(joint.get((J,Uraw<<m),F(0))==val)
            s=F(1,1<<(r-1)); b=1-s; q=(1+b*b)/2; eps=s*s/(2*(1+b*b))
            B=plus({2:(1-b*b)/2},h2(eps),q)
            # Existing levels halve their visit probability; new root has weight one.
            Bsum={k:v/2 for k,v in Bsum.items()}; plus(Bsum,B)
            post=plus(ent(joint.values()),ent(P),F(-1))
            formula=plus({2:D},Bsum); plus(formula,Aformal(r),F(-1))
            ck(post==formula)
            if r in posterior_by_r: ck(post==posterior_by_r[r])
            else: posterior_by_r[r]=post
            case_count+=1
            activation_records.append({'m':m,'core_id':mask,'r':r,'I':str(expectedI),'Q_mass':str(sum(Q)),
                                       'posterior_log2_prime_coefficients':{str(k):str(v) for k,v in post.items()}})

ck(case_count==312)

def ln_interval(q,terms=28):
    ck(q>0)
    k=0
    while q>=2: q/=2; k+=1
    while q<1: q*=2; k-=1
    def series(y):
        z=(y-1)/(y+1); z2=z*z; term=z; total=F(0)
        for j in range(terms): total+=term/(2*j+1); term*=z2
        lo=2*total; error=2*term/((2*terms+1)*(1-z2))
        return lo,lo+error
    L,U=series(q); a,b=series(F(2))
    if k>=0: return L+k*a,U+k*b
    return L+k*b,U+k*a
@lru_cache(None)
def log_interval(q):
    L,U=ln_interval(q); a,b=ln_interval(F(2))
    if L>=0: low,high=L/b,U/a
    elif U<=0: low,high=L/a,U/b
    else: low,high=L/a,U/a
    grid=1<<64
    # Integer floor/ceiling are outward, including signed intervals.
    return F((low*grid).__floor__(),grid),F((high*grid).__ceil__(),grid)
def c_interval(r):
    p=F(1,1<<r); L,U=log_interval(1/(1-p)); scale=2*(1-p)**2/(r*p)
    return 4-2*p+scale*L,4-2*p+scale*U
cis={r:c_interval(r) for r in [1,2,3,4,5]}
ck(cis[3][0]>F(9,2))
for r in [1,2,4,5]: ck(cis[r][1]<cis[3][0])
ck(cis[3][0]>F(4536,1000)); ck(cis[3][1]<F(4537,1000))

mux_records=[]
for r in [1,2,3,4,5,6,7]:
    n=r+2; p=F(1,1<<r); N=1<<(n-1); pi=F(1,1<<n)
    table=[]
    for x in range(1<<n):
        y=1 if x&1 else -1; z=1 if x&2 else -1
        table.append(z if x>>2==0 else y)
    a=walsh(table); P=[x*x for x in a]
    expected=[F(0)]*len(P); expected[1]=(1-p)**2
    for U in range(1<<r):
        expected[2|(U<<2)]=p*p
        if U: expected[1|(U<<2)]=p*p
    ck(P==expected); ck(sum(P)==1); ck(P[0]==0)
    I=sum(F(S.bit_count())*q for S,q in enumerate(P)); ck(I==1+r*p)
    for j in range(n):
        inf=sum(P[S] for S in range(len(P)) if S>>j&1)
        ck(inf==(1-p if j==0 else p))
    target=plus(ent([(1-p)**2]),{2:F(1)},2*r*(2*p-p*p)); ck(ent(P)==target)
    eta=pi/((1+pi/N)**N-1); ck(0<eta<=1); ck(eta>=1-pi)
    sym=[F(0)]*len(P); ordered=[F(0)]*len(P)
    # Rational rank-exponent-two local subset laws; common order y,z,controls.
    for s in range(1,n+1):
        theta=[min(F(1),F(s,j)**2) for j in range(1,n+1)]
        polys=[F(1)]+[F(0)]*s
        for w in theta:
            for k in range(s,0,-1): polys[k]+=w*polys[k-1]
        Z=polys[s]
        for A in range(1,len(P)):
            if A.bit_count()!=s: continue
            weight=F(1)
            for j in range(n):
                if A>>j&1: weight*=theta[j]
            sym[A]=eta/F(2*s*(s+1)*comb(n,s))
            ordered[A]=eta*weight/(2*s*(s+1)*Z)
    mass=eta*F(n,2*(n+1))
    ck(sum(sym)==mass); ck(sum(ordered)==mass)
    W1=sum(P[S] for S in range(len(P)) if S.bit_count()==1)
    ck(W1==(1-p)**2+p*p)
    # Physical name lower bound and complete symmetric cost formula, interval-certified.
    # Bound the common large-integer root factor analytically; only small local ratios
    # enter the atanh series. This avoids unneeded huge-denominator log arithmetic.
    root_upper=log_interval(1/(1-pi))[1]
    lo=olo=F(0); hi=ohi=root_upper
    for S,prob in enumerate(P):
        if not prob: continue
        L,U=log_interval(eta/sym[S]); lo+=prob*L; hi+=prob*U
        L,U=log_interval(eta/ordered[S]); olo+=prob*L; ohi+=prob*U
    ck(olo<=ohi and lo<=hi)
    ck(ohi < F(639,80)*I)
    mux_records.append({'r':r,'n':n,'I':str(I),'eta':str(eta),'reference_mass':str(mass),
                        'W1':str(W1),'sym_CE_lower':str(lo),'sym_CE_upper':str(hi),
                        'ordered_CE_lower':str(olo),'ordered_CE_upper':str(ohi)})

for r in range(1,65):
    n=r+2; p=F(1,1<<r)
    ck(factorial(n)>=n+1)
    ck(F(n+1)<=factorial(n)) # proves 2^-r log(n!) is nonincreasing.
    ck((1-p)**2+p*p>0)
ck(18**5<2**21); ck(6**5<2**13)

result={'status':'PASS','helper_version':'A015-stage2-posterior-and-location-v1','exact_assertions':assertions,
        'balanced_activation_cases':case_count,'rare_mux_truth_tables':7,'symbolic_mux_parameters':64,
        'elapsed_seconds':time.perf_counter()-start,'imported_upstream_code':False,
        'A012_sharp_constant_intervals':{str(r):[str(x) for x in v] for r,v in cis.items()},
        'posterior_by_r':{str(r):{str(k):str(v) for k,v in D.items()} for r,D in posterior_by_r.items()},
        'activation_records':activation_records,'mux_records':mux_records}
(out/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['activation_records','mux_records','A012_sharp_constant_intervals','posterior_by_r']},indent=2))
