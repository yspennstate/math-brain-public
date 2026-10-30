"""Frozen two-profile certificate; no numerical signs. Python 3, standard library."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, json, time, hashlib
from functools import lru_cache

ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic()
COUNT=0
def check(v):
    global COUNT
    COUNT+=1
    if not v: raise AssertionError(COUNT)
    if COUNT%100==0 and time.monotonic()-START>55: raise TimeoutError('frozen 55s guard')
def fw(t):
    a=list(t); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h): a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return [Q(v,len(t)) for v in a]
def direct_fw(t):
    return [Q(sum(v*(-1 if (s & x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t))]
def restrict(t,i,b):
    return [v for x,v in enumerate(t) if ((x>>i)&1)==b]
def inf(t,i):
    return Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
def total_inf(t): return sum((inf(t,i) for i in range(len(t).bit_length()-1)),Q(0))
@lru_cache(None)
def factors(n):
    ans=[]; p=2
    while p*p<=n:
        c=0
        while n%p==0: n//=p; c+=1
        if c: ans.append((p,c))
        p+=1
    if n>1: ans.append((n,1))
    return tuple(ans)
def add(*terms):
    z={}
    for m in terms:
        for p,v in m.items(): z[p]=z.get(p,Q(0))+v
    return {p:v for p,v in z.items() if v}
def mul(a,m): return {p:a*v for p,v in m.items() if a*v}
def number(a): return {} if a==0 else {2:Q(a)}
def elog(p):
    if p==0: return {}
    assert p>0
    z={}
    for a,c in factors(p.denominator): z[a]=z.get(a,Q(0))+p*c
    for a,c in factors(p.numerator): z[a]=z.get(a,Q(0))-p*c
    return {a:v for a,v in z.items() if v}
def g(a): return elog(a*a)
@lru_cache(None)
def ln_interval(q):
    assert q>0
    k=0
    while q>=2: q/=2; k+=1
    while q<1: q*=2; k-=1
    t=(q-1)/(q+1)
    lo=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
    hi=lo+2*t**49/(49*(1-t*t))
    if k:
        # ln2 is evaluated directly at t=1/3, avoiding recursion.
        u=Q(1,3); a=2*sum((u**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0)); b=a+2*u**49/(49*(1-u*u))
        lo+=k*(a if k>0 else b); hi+=k*(b if k>0 else a)
    return lo,hi
def interval(m):
    l2,u2=ln_interval(Q(2)); lo=hi=Q(0)
    for p,c in m.items():
        if p==2: l=u=Q(1)
        else:
            l,u=ln_interval(Q(p)); l,u=l/u2,u/l2
        lo+=c*(l if c>=0 else u); hi+=c*(u if c>=0 else l)
    return lo,hi
def entropy(a): return add(*(g(v) for v in a))
def H(t): return entropy(fw(t))
def phi(a,b): return add(elog(a),elog(b),mul(-1,elog(a+b)))
def B(t,i):
    a=fw(t)
    return add(*(phi(a[s]**2,a[s|(1<<i)]**2) for s in range(len(t)) if not s&(1<<i)))
def xi(v,w,e):
    return mul(e,add(*(add(mul(Q(1,2),add(g(a+b),g(a-b))),mul(-1,add(g(a),g(b)))) for a,b in zip(v[1:],w[1:]))))
def wrapper(h,v,w):
    N=len(h)
    return [v[x] if s==0 else w[x] if s==1 else h[s] for x in range(len(v)) for s in range(N)]
def allfunc(n):
    N=1<<n
    return [tuple(1-2*((m>>x)&1) for x in range(N)) for m in range(1<<N)]
def mean(t): return Q(sum(t),len(t))
def baseline(h,v,w):
    """Exact entropy with the two nonempty-private sectors kept separate."""
    e=Q(1,len(h)); d=len(h).bit_length()-1; mu=mean(v); nu=mean(w)
    b=fw(h); vv=fw(v); ww=fw(w)
    E=add(*(g(b[s]+e*(mu-1)+e*(-1 if s&1 else 1)*(nu-1)) for s in range(len(h))))
    return add(E,mul(e,add(H(v),H(w),mul(-1,add(g(mu),g(nu))))),number(2*d*e*(2-mu*mu-nu*nu)))
def pair_root(h,v,w):
    d=len(h).bit_length()-1; n=len(v).bit_length()-1; e=Q(1,len(h)); t=wrapper(h,v,w)
    a=fw(t); vv=fw(v); ww=fw(w); b=fw(h)
    for T in range(len(v)):
        for S in range(len(h)):
            expected=(b[S]+e*(vv[0]-1)+e*(-1 if S&1 else 1)*(ww[0]-1)) if T==0 else e*(vv[T]+(-1 if S&1 else 1)*ww[T])
            check(a[S+(T<<d)]==expected)
    check(H(t)==add(baseline(h,v,w),xi(vv,ww,e)))
    for i in range(n):
        check(inf(t,d+i)==e*(inf(v,i)+inf(w,i)))
        cs=[restrict(t,d+i,z) for z in [0,1]]
        vs=[restrict(v,i,z) for z in [0,1]]; ws=[restrict(w,i,z) for z in [0,1]]
        delta=add(H(t),mul(Q(-1,2),add(*(H(c) for c in cs))))
        main=add(baseline(h,v,w),mul(Q(-1,2),add(*(baseline(h,vs[z],ws[z]) for z in [0,1]))))
        collision=add(xi(vv,ww,e),mul(Q(-1,2),add(*(xi(fw(vs[z]),fw(ws[z]),e) for z in [0,1]))))
        check(delta==add(main,collision))
        check(total_inf(t)==inf(t,d+i)+sum((total_inf(c) for c in cs),Q(0))/2)
    return t
def common_event_review():
    """Separate direct sums reconstruct A076 section7 identity and reserve ownership."""
    roots=queries=0
    for h in allfunc(1):
      for D in allfunc(1):
        A=[int(v==-1) for v in D]; p=Q(sum(A),2)
        for V in allfunc(2):
            roots+=1; mu=mean(V); t=[h[s]*(V[x] if A[s] else 1) for x in range(4) for s in range(2)]
            bh=direct_fw(h); c=direct_fw([h[s]*A[s] for s in range(2)]); vv=direct_fw(V); aa=direct_fw(t)
            for S in range(2):
              for T in range(4): check(aa[S+2*T]==(bh[S]+(mu-1)*c[S] if T==0 else c[S]*vv[T]))
            check(sum((z*z for z in c),Q(0))==p)
            check(sum((bh[i]*c[i] for i in range(2)),Q(0))==p)
            kappa=total_inf(D)/2
            for i in range(2):
                queries+=1; check(inf(t,1+i)==p*inf(V,i))
                R=kappa*(1-mu*mu); mc=[mean(restrict(V,i,z)) for z in [0,1]]
                check(R-sum((kappa*(1-m*m) for m in mc),Q(0))/2==kappa*vv[1<<i]**2)
                delta=add(H(t),mul(Q(-1,2),add(*(H(restrict(t,1+i,z)) for z in [0,1]))))
                dv=add(H(V),mul(Q(-1,2),add(*(H(restrict(V,i,z)) for z in [0,1]))))
                margin=add(mul(p,dv),number(kappa*vv[1<<i]**2+11*p*inf(V,i)),mul(-1,delta))
                if not margin: check(True)
                else: check(interval(margin)[0]>=0)
    return {'roots':roots,'queries':queries,'scope':'A076 v7 section7 Fourier/Parseval/influence/reserve identities only; analytic curvature checked in prose'}
def rare(d):
    e=Q(1,1<<d); v=(1,-1,-1,1); w=(1,1,-1,-1); h=(1,)*(1<<d)
    t=wrapper(h,v,w); c=[restrict(t,d,z) for z in [0,1]]
    check(mean(v)==mean(w)==0)
    check(all(mean(restrict(q,0,z))==0 for q in [v,w] for z in [0,1]))
    check(all(len(set(a))==2 for a in c))
    check(all(len(set(restrict(v,0,z)))==2 and len(set(restrict(w,0,z)))==2 for z in [0,1]))
    check(inf(t,d)==e)
    check(total_inf(t)==(2*d+2)*e)
    check(add(H(t),mul(Q(-1,2),add(*(H(a) for a in c))))==number(4*e))
    check(B(t,d)==number(2*e))
    check(xi(fw(v),fw(w),e)=={})
    check(all(xi(fw(restrict(v,0,z)),fw(restrict(w,0,z)),e)==number(-4*e) for z in [0,1]))
    for i,q in enumerate([v,w]):
        bank=d*e*(1-mean(q)**2)
        check(bank==sum((d*e*(1-mean(restrict(q,0,z))**2) for z in [0,1]),Q(0))/2)
    if d<=3: check(fw(t)==direct_fw(t))
    return {'d':d,'e':str(e),'B_x':str(2*e),'DeltaH':str(4*e),'JS':str(2*e),'Inf_x':str(e),'I':str((2*d+2)*e),'mean_bank_release':'0','H_root':{str(p):str(v) for p,v in H(t).items()},'H_terminals':[{str(p):str(v) for p,v in H(a).items()} for a in c]}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); ap.add_argument('--review',action='store_true'); args=ap.parse_args()
    result={}; roots=queries=0
    if args.review: result=common_event_review()
    else:
        for n in ([1] if args.pilot else [1,2]):
          for d in ([1] if args.pilot else [1,2]):
            carriers=[(1,)*(1<<d)]
            if d==2: carriers.append((1,1,1,-1))
            for h in carriers:
              for v in allfunc(n):
                for w in allfunc(n):
                    pair_root(h,v,w); roots+=1; queries+=n
        result={'roots':roots,'queries':queries,'rare_fixtures':[rare(d) for d in ([1,2] if args.pilot else range(1,9))]}
    result.update({'helper_version':'two-profile-v1','exact_assertions':COUNT,'elapsed_seconds':time.monotonic()-START,'status':'PASS','arithmetic':'integer Walsh, Fraction, exact prime-log equality; no floating sign','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    name='review' if args.review else ('pilot' if args.pilot else 'full')
    (ROOT/'out'/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='rare_fixtures'}))
if __name__=='__main__': main()
