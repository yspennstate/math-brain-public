from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import json,time,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
phase=sys.argv[1] if len(sys.argv)>1 else 'all'
start=time.perf_counter(); assertions=0
def check(x):
    global assertions
    assertions+=1
    assert x
def guard():
    if time.perf_counter()-start>55: raise RuntimeError('Frozen runtime exceeded; no escalation')
@lru_cache(None)
def chars(N): return tuple(tuple(1-2*((x&s).bit_count()%2) for x in range(N)) for s in range(N))
def walsh(v): return [sum(a*b for a,b in zip(v,row)) for row in chars(len(v))]
def spectrum(v): return [F(w*w,len(v)**2) for w in walsh(v)]
def influence(v):
    N=len(v); n=N.bit_length()-1
    return [F(sum(v[x]!=v[x^(1<<i)] for x in range(N)),N) for i in range(n)]
@lru_cache(None)
def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(*vs):
    out={}
    for v in vs:
        for p,c in v.items():out[p]=out.get(p,F(0))+c
    return {p:c for p,c in out.items() if c}
def scale(v,c):return {p:c*a for p,a in v.items() if c*a}
def log(q):
    assert q>0
    return add(factors(q.numerator),scale(factors(q.denominator),-1))
def term(p):return scale(log(p),-p) if p else {}
def ent(ps):return add(*(term(p) for p in ps))
def restrict(v,U,y):
    n=len(v).bit_length()-1; V=[i for i in range(n) if i not in U]; out=[]
    fixed=sum(((y>>j)&1)<<i for j,i in enumerate(U))
    for z in range(1<<len(V)):
        x=fixed+sum(((z>>j)&1)<<i for j,i in enumerate(V));out.append(v[x])
    return tuple(out)
def project(s,V):return sum(((s>>i)&1)<<j for j,i in enumerate(V))
blocks=0
def block(v,U):
    global blocks
    n=len(v).bit_length()-1; V=[i for i in range(n) if i not in U]; L=1<<len(U)
    p=spectrum(v); q=[F(0)]*(1<<len(V))
    for s,a in enumerate(p):q[project(s,V)]+=a
    children=[restrict(v,U,y) for y in range(L)]; cp=[spectrum(c) for c in children]
    check(all(q[t]==sum(z[t] for z in cp)/L for t in range(len(q))))
    B=add(ent(p),scale(ent(q),-1)); avH=scale(add(*(ent(z) for z in cp)),F(1,L))
    # Conditional erasure computed from explicit posterior probabilities.
    B2={}
    for t,a in enumerate(q):
        if a:B2=add(B2,scale(ent([p[s]/a for s in range(len(p)) if project(s,V)==t]),a))
    check(B==B2)
    J=add(ent(q),scale(avH,-1));D=add(B,J)
    check(D==add(ent(p),scale(avH,-1)))
    ip=influence(v); d=sum(ip[i] for i in U)
    check(sum(ip)==d+sum(sum(influence(c)) for c in children)/L)
    # Direct coherent child coefficient identity for every assignment.
    W=walsh(v); N=len(v)
    for y,c in enumerate(children):
        CW=walsh(c)
        for t,w in enumerate(CW):
            rhs=sum(F(W[s],N)*(1-2*((project(s,U)&y).bit_count()%2)) for s in range(N) if project(s,V)==t)
            check(F(w,len(c))==rhs)
    blocks+=1
    return D,d
def tree(v,early,depth=0,weight=F(1)):
    n=len(v).bit_length()-1
    if n==0 or len(set(v))==1 or (early and n<=2):return ent(spectrum(v)),sum(influence(v)),{},F(0),1
    iv=influence(v);i=max(range(n),key=lambda j:(iv[j],-j)) if depth%2 else min((j for j in range(n) if iv[j]),key=lambda j:(iv[j],j))
    D,d=block(v,[i]); c=[tree(restrict(v,[i],y),early,depth+1) for y in range(2)]
    terminalH=scale(add(c[0][0],c[1][0]),F(1,2)); terminalI=(c[0][1]+c[1][1])/2
    chargeH=add(D,scale(add(c[0][2],c[1][2]),F(1,2)));chargeI=d+(c[0][3]+c[1][3])/2
    check(ent(spectrum(v))==add(terminalH,chargeH));check(sum(iv)==terminalI+chargeI)
    return terminalH,terminalI,chargeH,chargeI,c[0][4]+c[1][4]
identity_cases=0;trees=0;nonzero_terminals=0
for n in (range(4) if phase in ['all','identity'] else []):
    N=1<<n
    for mask in range(1<<N):
        v=tuple(1-2*((mask>>x)&1) for x in range(N))
        for um in range(1,1<<n):block(v,[i for i in range(n) if (um>>i)&1])
        for early in [False,True]:
            r=tree(v,early);trees+=1;nonzero_terminals+=bool(r[0])
        identity_cases+=1
    guard()
selection_counts={};maxima={};witnesses={}
for n in (range(1,5) if phase in ['all','selection'] else []):
    N=1<<n;mx=F(0); witness=None
    for half in range(1<<(N-1)):
        v=(1,)+tuple(1-2*((half>>(x-1))&1) for x in range(1,N)); W=walsh(v)
        ratios=[]
        for i in range(n):
            den=sum(W[s]**2 for s in range(N) if (s>>i)&1)
            if den:
                num=2*sum(abs(W[s]*W[s|(1<<i)]) for s in range(N) if not ((s>>i)&1));ratios.append(F(num,den))
        if ratios:
            r=min(ratios);check(r<=F(7,2))
            if r>=mx:mx=r;witness=half<<1
    check(mx==[None,F(0),F(2),F(3),F(7,2)][n]);maxima[n]=str(mx);witnesses[n]=witness;selection_counts[n]=1<<(N-1);guard()
activation_cases=0;node_checks=0
for mask in (range(16) if phase in ['all','activation'] else []):
    seed=tuple(1-2*((mask>>x)&1) for x in range(4))
    if sum(seed):continue
    for t in [1,2]:
        core=[]
        for x in range(1<<(2*t)):
            val=1
            for j in range(t):val*=seed[(x>>(2*j))&3]
            core.append(val)
        h=ent(spectrum(core));ic=sum(influence(core));check(h==scale(ent(spectrum(seed)),t));check(ic==t*sum(influence(seed)))
        for k in [1,2,3,4]:
            q=F(1,1<<k);f=tuple(core[x>>k] if x% (1<<k)==0 else 1 for x in range(1<<(k+2*t)))
            boundary=add({2:(4*q-2*q*q)*k},term((1-q)**2))
            check(ent(spectrum(f))==add(scale(h,q),boundary));check(sum(influence(f))==q*(ic+k))
            paid=F(0);charge={};blind=F(0);Jtree={}
            for s in range(k,0,-1):
                u=F(1,1<<s);w=q/u;g=tuple(core[x>>s] if x%(1<<s)==0 else 1 for x in range(1<<(s+2*t)))
                gp=restrict(g,[0],0);gm=restrict(g,[0],1);ap=[F(a,len(gp)) for a in walsh(gp)];am=[F(a,len(gm)) for a in walsh(gm)]
                Q=[(a*a+b*b)/2 for a,b in zip(ap,am)];m=[(abs(a)-abs(b))**2/4 for a,b in zip(ap,am)]
                check(sum(m)==u);check(Q[0]==1-2*u+2*u*u);check(m[0]==u*u)
                residual=add(*(scale(log(a/b),b) for a,b in zip(Q,m) if b))
                predicted=add({2:u-u*u},scale(log(Q[0]/(u*u)),u*u));check(residual==predicted)
                lam={}; Wg=walsh(g)
                for r in range(len(g)):
                    if not r&1:
                        aa=F(Wg[r],len(g));bb=F(Wg[r+1],len(g)); mass=aa*aa+bb*bb
                        if bb:lam=add(lam,scale(log(mass/(bb*bb)),bb*bb))
                check(lam==residual)
                D=add(ent(spectrum(g)),scale(add(ent(spectrum(gp)),ent(spectrum(gm))),-F(1,2)))
                d=influence(g)[0];check(d==u);paid+=w*d;charge=add(charge,scale(D,w));Jtree=add(Jtree,scale(residual,w));blind+=w*u*s;node_checks+=1
            check(paid==k*q);check(charge==boundary);check(blind==q*k*(k+1)/2)
            A={}
            for s in range(1,k+1):
                u=F(1,1<<s);A=add(A,scale(add({2:2*s-1},log(1-2*u+2*u*u)),u))
            check(Jtree==scale(add({2:k},A),q));activation_cases+=1;guard()
# Independently reconstruct the symmetric witness by counting characters on each level.
n=32;r=24; W=[]
for j in range(n+1):
    val=sum((1 if weight>=r else -1)*sum((-1)**z*comb(j,z)*comb(n-j,weight-z) for z in range(max(0,weight-(n-j)),min(j,weight)+1)) for weight in range(n+1))
    W.append(val)
num=2*sum(comb(n-1,j)*abs(W[j]*W[j+1]) for j in range(n));den=sum(comb(n-1,j)*W[j+1]**2 for j in range(n))
ratio=F(num,den);check(ratio==F(2220940451,536870912));check(ratio>4)
check(F(den,1<<(2*n))==F(comb(31,23),1<<31))
result={'status':'PASS','phase':phase,'assertions':assertions,'identity_functions':identity_cases,'block_checks_including_tree_rechecks':blocks,'adaptive_trees':trees,'nonzero_terminal_entropy_trees':nonzero_terminals,'selection_counts':selection_counts,'selection_maxima':maxima,'selection_witness_masks':witnesses,'activation_cases':activation_cases,'active_node_checks':node_checks,'threshold_amplitude_ratio':str(ratio),'runtime_seconds':time.perf_counter()-start,'entropy_arithmetic':'rational prime-log vectors','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
ROOT.joinpath('out/check_results_'+phase+'.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
