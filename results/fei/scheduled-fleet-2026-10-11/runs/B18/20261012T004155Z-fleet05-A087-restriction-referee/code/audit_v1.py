from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations,product
from math import factorial
from pathlib import Path
import json,sys,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
ROOT.joinpath('out').mkdir(exist_ok=True)
phase=sys.argv[1];start=time.perf_counter();count=0
def ck(x):
    global count
    count+=1
    assert x
def guard():
    if time.perf_counter()-start>55:raise RuntimeError('Frozen phase runtime cap; no dimension escalation')
@lru_cache(None)
def character(N):return tuple(tuple(1-2*((s&x).bit_count()%2) for x in range(N)) for s in range(N))
@lru_cache(None)
def W(v):return tuple(sum(a*b for a,b in zip(v,row)) for row in character(len(v)))
def coef(v):return [F(w,len(v)) for w in W(v)]
def spectrum(v):return [a*a for a in coef(v)]
@lru_cache(None)
def factor(n):
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def add(*vs):
    d={}
    for v in vs:
        for p,a in v.items():d[p]=d.get(p,F(0))+a
    return {p:a for p,a in d.items() if a}
def scale(v,a):return {p:c*a for p,c in v.items() if a*c}
def log(q):return add(factor(q.numerator),scale(factor(q.denominator),-1))
def entropy(ps):return add(*(scale(log(p),-p) for p in ps if p))
def raw(v):return entropy([a*a for a in v])
def H(v):return entropy(spectrum(v))
def child(v,i,b):
    out=[];n=len(v).bit_length()-1
    for y in range(1<<(n-1)):
        x=(y&((1<<i)-1))+((y>>i)<<(i+1))+(b<<i);out.append(v[x])
    return tuple(out)
def inf(v,i):return F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def I(v):return sum(inf(v,i) for i in range(len(v).bit_length()-1))
def B(v,i):
    p=spectrum(v)
    return add(*(add(entropy([p[s],p[s|(1<<i)]]),scale(entropy([p[s]+p[s|(1<<i)]]),-1)) for s in range(len(p)) if not ((s>>i)&1)))
def D(v,i):return add(H(v),scale(add(H(child(v,i,0)),H(child(v,i,1))),-F(1,2)))
@lru_cache(None)
def ln_small(q):
    z=(q-1)/(q+1);partial=2*sum((z**(2*j+1))/F(2*j+1) for j in range(32));tail=2*z**65/(65*(1-z*z))
    return partial,partial+tail
@lru_cache(None)
def ln(q):
    q=F(q);k=0
    while q>=2:q/=2;k+=1
    while q<1:q*=2;k-=1
    a,b=ln_small(q);l,u=ln_small(F(2))
    return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def interval(v):
    lo=hi=F(0)
    for p,c in v.items():
        a,b=ln(p)
        if c>=0:lo+=c*a;hi+=c*b
        else:lo+=c*b;hi+=c*a
    return lo,hi
def sign_nonnegative(v):
    if not v:return True
    return interval(v)[0]>=0
e_lower=sum(F(1,factorial(j)) for j in range(25));e_upper=e_lower+F(26,25*factorial(25))
ln2=ln(F(2))
def save(result):
    result.update({'status':'PASS','phase':phase,'assertions':count,'runtime_seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    ROOT.joinpath('out',phase+'.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
def inner_tables():
    return [tuple(1-2*(x&1) for x in range(8)),tuple(1-2*(x.bit_count()%2) for x in range(8)),tuple(1 if x.bit_count()<=1 else -1 for x in range(8)),tuple((1-2*(x&1))*(1-2*(((x>>1)&1)*((x>>2)&1))) for x in range(8))]
def cases():
    inners=inner_tables()
    for mask in range(16):
        g=tuple(1-2*((mask>>x)&1) for x in range(4))
        for h,k in product(inners,repeat=2):
            f=tuple(g[(h[x&7]==-1)+2*(k[x>>3]==-1)] for x in range(64))
            yield g,h,k,f
def outer_vectors(g,j):
    a=coef(tuple(F(x+y,2) for x,y in zip(child(g,j,0),child(g,j,1))));b=coef(tuple(F(x-y,2) for x,y in zip(child(g,j,0),child(g,j,1))))
    return a,b
if phase=='npn':
    cases_n={};transforms=0
    for n in range(4):
        N=1<<n;c=0
        for mask in range(1<<N):
            f=tuple(1-2*((mask>>x)&1) for x in range(N));wf=W(f);ivs=[inf(f,i) for i in range(n)]
            for perm in permutations(range(n)):
                for neg in range(N):
                    for eps in [-1,1]:
                        v=tuple(eps*f[sum((((x>>perm[j])&1)^((neg>>j)&1))<<j for j in range(n))] for x in range(N));wv=W(v)
                        for s in range(N):
                            t=sum(((s>>j)&1)<<perm[j] for j in range(n));ck(wv[t]==eps*(1-2*((neg&s).bit_count()%2))*wf[s])
                        for j in range(n):ck(inf(v,perm[j])==ivs[j])
                        transforms+=1;c+=1
            if mask%32==0:guard()
        cases_n[n]=c
    ck(transforms==24852);save({'NPN_transformations':transforms,'counts_by_n':cases_n,'nonphysical_affine_transform_not_admitted':True})
elif phase=='composition':
    splits=0;interference_nonzero=0;endpoint_counts={'x0':0,'x1':0,'q0':0,'M0':0}
    margins={'L_upper':None,'J_upper':None,'alpha_log':None}
    for g,h,k,f in cases():
        ck(sum(h)==sum(k)==0)
        for i in range(6):
            j=i//3;loc=i%3;inner=[h,k][j];a,b=outer_vectors(g,j);q=sum(t*t for t in b);alpha=coef(inner)[1<<loc];x=alpha*alpha;t=q*x
            s=[aa*aa+x*bb*bb for aa,bb in zip(a,b)];plus=[aa+alpha*bb for aa,bb in zip(a,b)];minus=[aa-alpha*bb for aa,bb in zip(a,b)];M=1-q+t
            ck(sum(z*z for z in plus)==sum(z*z for z in minus)==sum(s)==M)
            L=add(raw(a),scale(raw(b),x),scale(log(F(1,x)),t) if x else {},scale(entropy(s),-1))
            J=add(entropy(s),scale(add(raw(plus),raw(minus)),-F(1,2)));R=add(L,J)
            ck(B(f,i)==add(scale(B(inner,loc),q),L))
            ck(D(f,i)==add(scale(D(inner,loc),q),R))
            jsf=add(D(f,i),scale(B(f,i),-1));jsinner=add(D(inner,loc),scale(B(inner,loc),-1))
            ck(jsf==add(scale(jsinner,q),J));ck(inf(f,i)==q*inf(inner,loc));ck(abs(alpha)<=inf(inner,loc))
            Lgap=add(scale(B(g,j),x),scale(log(F(1,x)),t) if x else {},scale(L,-1))
            ck(sign_nonnegative(Lgap));ck(sign_nonnegative(J));ck(sign_nonnegative(L))
            Jlo,Jhi=interval(J);ck(Jhi<=2*t)
            bank=scale(log(F(1,x)),t) if x else {};banklo,bankhi=interval(bank)
            ck(bankhi<=2*inf(f,i)/e_upper)
            # Certified per-child other-block interference is retained.
            other=[k,h][j];Aother=H(other)
            if Aother and any(alpha*aa*bb for aa,bb in zip(a,b)):interference_nonzero+=1
            endpoint_counts['x0']+=x==0;endpoint_counts['x1']+=x==1;endpoint_counts['q0']+=q==0;endpoint_counts['M0']+=M==0
            for name,val in [('L_upper',interval(Lgap)[0]),('J_upper',2*t-Jhi),('alpha_log',2*inf(f,i)/e_upper-bankhi)]:
                if val>0 and (margins[name] is None or val<margins[name]):margins[name]=val
            splits+=1
        if splits%96==0:guard()
    ck(splits==1536);save({'composition_functions':256,'physical_splits':splits,'nonzero_other_block_interference_splits':interference_nonzero,'endpoints':endpoint_counts,'minimum_positive_certified_margins':{k:str(v) for k,v in margins.items()},'interval_terms':32})
elif phase=='trees':
    nodes=represented=nonzero_terminal=0;max_ratio=F(0)
    def walk(v,depth=0):
        global nodes,represented
        n=len(v).bit_length()-1
        if depth==2 or len(set(v))==1:return H(v),I(v),{},F(0),{},0
        i=0 if depth==0 else max(range(n),key=lambda j:(inf(v,j),-j));d=inf(v,i);nodes+=1
        bank={}
        if sum(v)==0:
            alpha=coef(v)[1<<i];x=alpha*alpha;bank=scale(log(F(1,x)),x) if x else {};represented+=1
            ck(interval(bank)[1]<=2*d/e_upper)
        r=[walk(child(v,i,b),depth+1) for b in [0,1]]
        termH=scale(add(r[0][0],r[1][0]),F(1,2));termI=(r[0][1]+r[1][1])/2
        chargedH=add(D(v,i),scale(add(r[0][2],r[1][2]),F(1,2)));paidI=d+(r[0][3]+r[1][3])/2
        logbank=add(bank,scale(add(r[0][4],r[1][4]),F(1,2)))
        ck(H(v)==add(termH,chargedH));ck(I(v)==termI+paidI)
        ck(interval(logbank)[1]<=2*paidI/e_upper)
        return termH,termI,chargedH,paidI,logbank,1
    trees=0
    for g,h,k,f in cases():
        r=walk(f);trees+=1;nonzero_terminal+=bool(r[0]);guard()
    save({'stopped_trees':trees,'queried_nodes':nodes,'certified_balanced_actual_node_representations':represented,'nonzero_terminal_entropy_trees':nonzero_terminal,'biased_nodes_omitted_from_bank':nodes-represented,'representation':'identity outer at balanced actual nodes; no automatic biased closure'})
elif phase=='correction':
    results=[]
    for k in range(1,7):
        q=F(1,1<<k)
        # Natural remainder: b_nat(q)-2q+3q².
        lo,hi=ln(1-q);bnat=(-2*(1-q)**2*hi,-2*(1-q)**2*lo)
        lower=bnat[0]-2*q+3*q*q;upper=bnat[1]-2*q+3*q*q
        bound=F(2,3)*q**3/(1-q)
        ck(lower>0);ck(upper<=bound)
        results.append({'k':k,'q':str(q),'natural_remainder_lower':str(lower),'natural_remainder_upper':str(upper),'natural_upper_bound':str(bound)})
    ck(ln2[0]>F(1,2));save({'corrected_entropy_remainder_certificates':results,'withdrawn_component':'A021 v1 R<=0 and positive G_s; prior A087 acceptance narrowed','positive_endpoint_proof':'R(1/2)=(2ln2-1)/(4ln2)>0','all_parameter_proof':'positive series coefficients, documented in CORRECTION_CONSUMED.md'})
else:raise ValueError(phase)
