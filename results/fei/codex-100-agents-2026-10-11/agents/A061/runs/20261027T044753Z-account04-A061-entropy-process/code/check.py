"""Exact point spectra, full-reference terminals, and selected-policy cuts."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, math, hashlib
R=Path(__file__).resolve().parents[1]
COUNT=0
def ck(b,label):
    global COUNT
    COUNT+=1
    if not b: raise AssertionError(label)
def plus(*terms):
    z={}
    for c,a in terms:
        for k,v in a.items(): z[k]=z.get(k,F())+c*v
    return {k:v for k,v in z.items() if v}
def log(x):
    x=F(x); assert x>0
    z={}
    for a,sign in [(x.numerator,1),(x.denominator,-1)]:
        p=2
        while p*p<=a:
            while a%p==0: z[p]=z.get(p,F())+sign; a//=p
            p+=1
        if a>1:z[a]=z.get(a,F())+sign
    return {p:F(v) for p,v in z.items() if v}
def const(q):return {2:F(q)} if q else {}
@lru_cache(None)
def ln_unit(x):
    z=(x-1)/(x+1);term=z;s=F()
    for k in range(48): s+=term/F(2*k+1);term*=z*z
    return 2*s,2*s+2*term/(97*(1-z*z))
@lru_cache(None)
def log_interval(n):
    e=n.bit_length()-1;x=F(n,2**e)
    lo,hi=ln_unit(x);l2,u2=ln_unit(F(2))
    return F(e)+lo/u2,F(e)+hi/l2
def interval(a):
    lo=hi=F()
    for n,c in a.items():
        l,u=log_interval(n)
        lo+=c*(l if c>=0 else u);hi+=c*(u if c>=0 else l)
    return lo,hi
def nn(a,label):ck(not a or interval(a)[0]>=0,label)
def maximum(a,b):
    d=plus((1,a),(-1,b))
    if not d:return a
    l,u=interval(d)
    ck(l>=0 or u<=0,'separated exact interval maximum')
    return a if l>=0 else b
def entropy(p):
    return plus(*[(-x,log(x)) for x in p if x])
def kl(p,q):
    return plus(*[(x,log(x/y)) for x,y in zip(p,q) if x])
def walsh(t):
    a=list(t);step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
        step*=2
    return tuple(F(x,len(t)) for x in a)
def stats(t):
    a=walsh(t);p=tuple(x*x for x in a);n=len(t).bit_length()-1
    ds=tuple(sum(p[s] for s in range(len(p)) if s>>i&1) for i in range(n))
    q=tuple(math.prod(ds[i] if s>>i&1 else 1-ds[i] for i in range(n)) for s in range(len(p)))
    H=entropy(p);M=plus(*[(1,entropy((d,1-d))) for d in ds])
    return p,ds,H,M,q
def child(t,i,b):
    return tuple(t[(x&((1<<i)-1))+((x>>i)<<(i+1))+(b<<i)] for x in range(len(t)//2))
def point(s):return tuple(-1 if x==0 else 1 for x in range(2**s))
@lru_cache(None)
def H(s):
    if s==1:return {}
    d=F(1,2**(s-1));return plus((-(1-d)**2,log((1-d)**2)),(-(2**s-1)*d*d,log(d*d)))
@lru_cache(None)
def M(s):
    d=F(1,2**(s-1));return plus((s,entropy((d,1-d))))
def V(s,r):return maximum(H(s),plus((F(1,2**(s-r)),M(r))))
def value(a):return float(sum(float(v)*math.log2(p) for p,v in a.items()))
def show(a):return {str(p):str(v) for p,v in a.items()}
def run(pilot):
    global COUNT
    COUNT=0;start=time.perf_counter();rows=[];nstate=0;queries=0;resets=0
    maxm=4 if pilot else 8
    for m in range(2,maxm+1):
        t=point(m);p,ds,h,mm,q=stats(t);d=F(1,2**(m-1))
        ck(h==H(m),'direct labelled Walsh H');ck(mm==M(m),'direct marginal M')
        ck(p[0]==(1-d)**2 and all(x==d*d for x in p[1:]),'complete spectrum')
        ck(all(x==d for x in ds),'direct influence spectrum')
        for i in range(m):
            edge=F(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
            ck(edge==d,'independent physical edge influence')
            hs=[]
            for b in [0,1]:
                c=child(t,i,b);hs.append(stats(c)[2])
                ck(c==point(m-1) or len(set(c))==1,'both actual children')
            nn(plus((1,h),(F(-1,2),hs[0]),(F(-1,2),hs[1])),'nonnegative entropy release')
        ck(kl(p,q)==plus((1,mm),(-1,h)),'actual reset KL M-H with all atoms')
        nn(plus((1,mm),(-1,h)),'nonnegative reset KL')
        nn(plus((1,const(4*m*d)),(-1,h)),'analytic H<=4I control')
        for r in range(1,m+1):
            N=2**(m-1);K=plus((2**(r-1),M(r)));root=maximum(plus((N,h)),K)
            ck(root==plus((N,V(m,r))),'exact tensor initial potential')
            nn(plus((1,K),(-1,const(r*(r-1)))),'K lower boundary')
            nn(plus((1,const(F(r*(2*r+1),2))),(-1,K)),'K upper boundary')
            ck(plus((N*F(1,2**(m-r)),M(r)))==K,'terminal full CE')
            for s in range(r,m+1):
                vv=V(s,r);nn(plus((1,vv),(-1,H(s))),'full CE domination')
                if s==r:
                    ck(vv==M(r),'reset boundary no extra reserve');resets+=1
                else:
                    nn(plus((1,vv),(F(-1,2),V(s-1,r))),'exact physical supermartingale');queries+=1
            A=maximum(plus((N,h),(1,const(2))),K)
            if r<=math.isqrt(m):nn(plus((1,const(4*(m+1))),(-1,A)),'same original rate4 suffices')
            rows.append({'m':m,'r':r,'K':show(K),'A':show(A),'A_over_I_display_only':value(A)/(m+1)})
    # Two-block states: literal tables, actual whole reference and every legal action.
    for m in range(2,5):
      for r in range(1,m+1):
        states=[('dead',0)]+[('live',s) for s in range(r,m+1)]+[('frozen',r)]
        nstate+=len(states)**2
        def local(state):
            typ,s=state
            if typ=='dead':return (1,), (F(1),),{},{}
            t=point(s);p,ds,h,mm,q=stats(t)
            return t, q if typ=='frozen' else p, mm if typ=='frozen' else h,V(s,r)
        for st0 in states:
          for st1 in states:
            st=[st0,st1];parts=[local(x) for x in st];n0=len(parts[0][0]);n1=len(parts[1][0])
            t=tuple(parts[0][0][x%n0]*parts[1][0][x//n0] for x in range(n0*n1))
            q=tuple(parts[0][1][x%n0]*parts[1][1][x//n0] for x in range(n0*n1))
            p,ds,h,mm,unused=stats(t);ce=plus((1,h),(1,kl(p,q)))
            ck(ce==plus((1,parts[0][2]),(1,parts[1][2])),'FULL tensor reference CE incl frozen atoms')
            vv=plus((1,parts[0][3]),(1,parts[1][3]));nn(plus((1,vv),(-1,ce)),'all mixed states CE dominated')
            for j,(typ,s) in enumerate(st):
                if typ!='live':continue
                if s==r:
                    new=list(st);new[j]=('frozen',r);cp=[local(x) for x in new]
                    nn(plus((1,vv),(-1,cp[0][2]),(-1,cp[1][2])),'actual permitted reset dominated')
                    continue
                for i in range(s):
                    ii=i+(0 if j==0 else n0.bit_length()-1)
                    nvar=len(t).bit_length()-1
                    groups=[];O=[];childvs=[]
                    for b in [0,1]:
                        pc=stats(child(t,ii,b))[0];ref=[];prediction=F()
                        for z in range(len(pc)):
                            z0=(z&((1<<ii)-1))+((z>>ii)<<(ii+1));z1=z0+(1<<ii)
                            mass=p[z0]+p[z1]
                            kernel=pc[z]/(2*mass) if mass else F(1,2)
                            rr=(q[z0]+q[z1])*kernel;ref.append(rr);prediction+=rr
                        ck(prediction==F(1,2),'actual coherent prediction fair incl source-zero rows')
                        ref=tuple(x/prediction for x in ref)
                        other=1-j
                        ctyp='dead' if b==1 else 'live'
                        cstate=(ctyp,0 if b==1 else s-1);expected=local(cstate)
                        childce=plus((1,entropy(pc)),(1,kl(pc,ref)))
                        ck(childce==plus((1,expected[2]),(1,parts[other][2])),'exact inherited data reference CE')
                        childvs.append(plus((1,expected[3]),(1,parts[other][3])))
                    nn(plus((1,vv),(F(-1,2),childvs[0]),(F(-1,2),childvs[1])),'every labelled mixed-reference query drift')
    # Independently enumerate global adapted stopping cuts through Bellman maxima.
    bellman_rows=0
    for m in range(2,5):
      for r in range(1,m+1):
        @lru_cache(None)
        def bell(st):
            costs=[]
            for typ,s in st:
                costs.append(M(s) if typ=='frozen' else H(s) if typ=='live' else {})
            best=plus(*[(1,c) for c in costs])
            for j,(typ,s) in enumerate(st):
                if typ!='live':continue
                if s==r:
                    ns=list(st);ns[j]=('frozen',s);candidate=bell(tuple(ns))
                else:
                    branches=[]
                    for new in [('dead',0),('live',s-1)]:
                        ns=list(st);ns[j]=new;branches.append(bell(tuple(ns)))
                    candidate=plus((F(1,2),branches[0]),(F(1,2),branches[1]))
                best=maximum(best,candidate)
            return best
        actual=bell((('live',m),('live',m)))
        target=plus((2,V(m,r)))
        ck(actual==target,'all adapted cuts/two-block initial sharpness')
        bellman_rows+=bell.cache_info().currsize
    elapsed=time.perf_counter()-start
    ck(elapsed<(55 if pilot else 120),'frozen runtime limit')
    out={'status':'PASS','pilot':pilot,'predicates':COUNT,'seconds':elapsed,'parameter_pairs':len(rows),'mixed_states':nstate,'Bellman_states':bellman_rows,'scalar_query_states':queries,'scalar_resets':resets,'rows':rows,'arithmetic':'exact Fraction Walsh/edges, prime-log equalities, 48-term outward rational signs; display ratios NOT certificates'}
    (R/'out'/('PILOT.json' if pilot else 'MAIN.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
    print({k:v for k,v in out.items() if k!='rows'},flush=True)
if __name__=='__main__':
    run(True);run(False)
