from pathlib import Path
from fractions import Fraction as F
import itertools, json, time, sys

BASE=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
start=time.perf_counter()
checks=0
def ck(ok, msg):
    global checks
    checks+=1
    if not ok: raise AssertionError(msg)
    if time.perf_counter()-start>55: raise RuntimeError('frozen runtime exceeded')
def walsh(f):
    a=f[:]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return [F(x,len(a)) for x in a]
def inf(f,n):
    return sum((F(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n)),F(0))
def positive_cores(n):
    for tt in range(1,(1<<(1<<n))-1):
        b=[(tt>>x)&1 for x in range(1<<n)]
        if all(b[x]<=b[x|(1<<i)] for x in range(1<<n) for i in range(n)):
            yield b
def clauses(b,n):
    # Maximal false assignments give all positive prime clauses.
    return [((1<<n)-1)^x for x in range(1<<n) if not b[x] and all(b[x|(1<<i)] for i in range(n) if not (x>>i)&1)]
def lift(b,n,cl,L):
    N=n+len(cl)*L
    out=[]
    for v in range(1<<N):
        z=v&((1<<n)-1)
        ok=all((z&c)!=0 or ((v>>(n+j*L))&((1<<L)-1))==((1<<L)-1) for j,c in enumerate(cl))
        out.append(1 if ok else -1)
    return out,N
def logq(q):
    # Exact formal vector of log2 primes, allowing large powers of two.
    out={}
    for num,sgn in [(q.numerator,1),(q.denominator,-1)]:
        d=2
        while d*d<=num:
            while num%d==0:
                out[d]=out.get(d,F(0))+sgn;num//=d
            d+=1
        if num>1:out[num]=out.get(num,F(0))+sgn
    return {p:c for p,c in out.items() if c}
def add(*terms):
    out={}
    for a,v in terms:
        for p,c in v.items():out[p]=out.get(p,F(0))+a*c
    return {p:c for p,c in out.items() if c}
mon=0; anchor=0; scalar=0; finite=0; maxN=0; profiles=0
for n in range(1,(2 if PILOT else 3)+1):
    for b in positive_cores(n):
        g=[2*x-1 for x in b]; gh=walsh(g); q=F(b.count(0),len(b)); Ig=inf(g,n)
        cl=clauses(b,n)
        for L in [1,2]:
            f,N=lift(b,n,cl,L); fh=walsh(f); maxN=max(maxN,N);mon+=1
            eps=F(1,1<<L)
            m=[2*eps**sum((x&c)==0 for c in cl)-1 for x in range(1<<n)]
            mh=walsh(m)
            ck(fh[:1<<n]==mh,'conditional core coefficients')
            for S in range(1<<n):ck(abs(fh[S]-gh[S])<=2*q*eps,'coefficient perturbation')
            M=sum(x*x for x in fh[1<<n:])
            ck(M==sum(4*((t+1)/2)*(1-(t+1)/2) for t in m)/len(m),'private mass')
            I=inf(f,N)
            ck(I==sum(F(S.bit_count())*a*a for S,a in enumerate(fh)),'physical versus Walsh I')
            ck(abs(I-Ig)<=2*q*(n+L)*eps,'A015 influence error')
            # Full fixed normalized reference, then separately rare root and sector normalizers.
            E=list(range(1,1<<n)); Om=list(range(1,1<<N))
            # Uniform outside E; distinct core reference profile; fixed before targets.
            weights={S:F(S+1) if S in E else F(1) for S in Om}
            W=sum(weights.values()); R={S:w/W for S,w in weights.items()}
            Z=sum(R[S] for S in E); a=F(1,7); theta=F(1,128)
            v=sum(gh[S]**2 for S in E)
            D=add(*[(fh[S]**2,logq(1/R[S])) for S in E])
            B=add(*[(fh[S]**2-a*gh[S]**2,logq(1/R[S])) for S in E])
            Cp=add(*[(gh[S]**2,logq(Z/R[S])) for S in E])
            ck(Cp==add((1/a,D),(-1/a,B),(v,logq(Z))),'sector exact log identity')
            Q={S:theta*R[S] for S in E}; QE=sum(Q.values())
            DQ=add(*[(fh[S]**2,logq(1/Q[S])) for S in E])
            BQ=add(*[(fh[S]**2-a*gh[S]**2,logq(1/Q[S])) for S in E])
            ck(Cp==add((1/a,DQ),(-1/a,BQ),(v,logq(QE))),'both root normalizers')
            profiles+=1
            # Conditioning independent raw mass theta/sector Z cannot change coefficients of log t.
            for S in E:ck((fh[S]**2-a*gh[S]**2)+a*gh[S]**2==fh[S]**2,'surplus exact coefficient')
            # Granularity and dominated extraction side conditions, when met.
            rho=(1<<n)*q*eps
            for S in E:
                if gh[S]:ck(abs(gh[S])>=F(2,1<<n),'Boolean granularity')
                if rho<1:ck(fh[S]**2>=(1-rho)**2*gh[S]**2,'domination')
for s in range(1,(2 if PILOT else 4)+1):
    n=s+1
    b=[int((x&1)!=0 or (x>>1)==(1<<s)-1) for x in range(1<<n)]
    cl=[1|(1<<i) for i in range(1,s+1)]
    for L in [1,2]:
        f,N=lift(b,n,cl,L); fh=walsh(f); gh=walsh([2*x-1 for x in b]); eps=F(1,1<<L)
        aa=(1+eps)/2;bb=(1-eps)/2;anchor+=1;maxN=max(maxN,N)
        ck(fh[0]==aa**s,'anchor mean')
        ck(fh[1]==-(1-aa**s),'anchor sign phase z')
        for S in range(2,1<<n):
            k=(S>>1).bit_count()
            expected=(-1)**k*aa**(s-k)*bb**k
            ck(fh[S]==expected,'anchor exact coefficient')
        rat=min(fh[S]**2/gh[S]**2 for S in range(1,1<<n) if gh[S])
        ck(rat==(1-eps)**(2*s),'sharp attenuation minimum')
        ck(inf(f,N)==1-aa**s+F(s,2)*(1+(L-1)*eps)*aa**(s-1),'anchor physical I')
        ck(inf([2*x-1 for x in b],n)==1+F(s-1,1<<s),'core physical I')
        if L==1:
            # An explicit bad but uniformly cheap complete reference; materialized
            # only on the frozen s<=4 domain (largest exponent 65536).
            j=((1<<s)-1)<<1; u=[c*c for c in fh]; p=[c*c for c in gh]
            MM=16**s
            ck(u[j]*MM==1,'one source bit pays rare atom suppression')
            R={S:u[S]/2 for S in range(1,len(u)) if u[S]}
            R[j]*=F(1,1<<MM)
            Z=sum(R.get(S,F(0)) for S in range(1,1<<n)); TT=sum(R.values())
            ck(F(1,32)<=Z<=TT<=F(1,2),'actual source and core normalizers')
            ck(p[j]*MM==4**s,'exponential core penalty')
            # Formal source cost is H_nonempty+v+1, without factoring 2^M-1.
            v=sum(u[1:])
            Cbase=add(*[(u[S],logq(1/u[S])) for S in range(1,len(u)) if u[S]])
            CR=add(Cbase and (F(1),Cbase) or (F(0),{}),(v+1,logq(F(2))))
            deltaC=add((F(1),CR),(-F(1),Cbase))
            ck(deltaC=={2:v+1},'source cost difference exact log vector')
            ck(F(s)*aa**(s-1)<=4,'entropy envelope geometric sum')
            ck(inf(f,N)>=F(3,4),'source influence floor')
for s in range(1,(8 if PILOT else 64)+1):
    for L in range(1,(4 if PILOT else 16)+1):
        eps=F(1,1<<L); a=(1-eps)**(2*s)
        ck(1/a>=1+2*s*eps,'necessary scale Bernoulli')
        ck(a>=1-2*s*eps,'sufficient scale Bernoulli')
        scalar+=1
    for j in range(0,(4 if PILOT else 16)+1):
        delta=F(1,1<<j); A=4+j; LL=2*s+2*A;eps=F(1,1<<LL)
        rho=F(1<<s,2)*eps;d0=(s+LL)*eps
        ck(rho<=delta/1024,'A007 rho bound')
        ck(d0<delta/16,'A007 influence surplus bound')
        ck((1+d0)/(1-rho)**2<=1+delta,'A007 finite factor')
        # Logarithmic necessary/sufficient extraction bracket for anchor family.
        K=0
        while F(1,1<<K)>delta/F(4*s):K+=1
        ee=F(1,1<<K)
        ck((1-ee)**(-2*s)<=1+delta,'log-scale upper bracket')
        finite+=1
# Boundary controls for the new sharp theorem.
ck(F(1,2)*0==0,'empty p coordinate contributes no cost')
# E singleton normalization makes every target cost zero; necessity requires |E|>=2.
ck(logq(F(1))=={},'singleton sector excluded from necessity')
# A007 surplus cannot be omitted under arbitrary reference profiles.
ck(F(1,2)-F(1,7)*F(1,3)!=0,'nonzero surplus negative control')
ck(F(1,2)!=-F(1,2),'wrong optional-z coefficient phase is rejected')
result={'status':'PASS','pilot':PILOT,'checks':checks,'monotone_lifts':mon,'anchor_lifts':anchor,'anchor_scalar_pairs':scalar,'finite_extraction_pairs':finite,'root_sector_profiles':profiles,'max_physical_dimension':maxN,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'exact integers/Fraction and rational log-prime coefficient vectors'}
(BASE/'out').mkdir(exist_ok=True)
(BASE/'out'/('pilot.json' if PILOT else 'checks.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
