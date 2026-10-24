import argparse,itertools,json,time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
COUNT=0
def ck(v):
    global COUNT
    COUNT+=1
    if not v: raise AssertionError(COUNT)
def add(a,b,w=Q(1)):
    z=a.copy()
    for p,v in b.items(): z[p]=z.get(p,Q(0))+w*v
    return {p:v for p,v in z.items() if v}
def mul(a,w): return {p:v*w for p,v in a.items() if v*w}
@lru_cache(None)
def factors(n):
    z={};p=2
    while p*p<=n:
        while n%p==0: z[p]=z.get(p,0)+1;n//=p
        p+=1
    if n>1:z[n]=z.get(n,0)+1
    return z
def logform(x):
    z={p:Q(e) for p,e in factors(x.numerator).items()}
    for p,e in factors(x.denominator).items():z[p]=z.get(p,Q(0))-e
    return {p:v for p,v in z.items() if v}
def entropy(prob):
    z={}
    for p in prob:
        if p:z=add(z,logform(p),-p)
    return z
def ln_small(z):
    t=(z-1)/(z+1);v=t;lo=Q(0)
    for j in range(80):lo+=2*v/(2*j+1);v*=t*t
    return lo,lo+2*v/(161*(1-t*t))
LN2=ln_small(Q(2));C=(1/LN2[1],1/LN2[0])
@lru_cache(None)
def loginterval(p):
    if p==2:return Q(1),Q(1)
    k=p.bit_length()-1;l,u=ln_small(Q(p,2**k))
    return k+l/LN2[1],k+u/LN2[0]
def interval(z,c=Q(0)):
    l=u=Q(0)
    for p,v in z.items():
        a,b=loginterval(p);l+=v*(a if v>=0 else b);u+=v*(b if v>=0 else a)
    l+=c*(C[0] if c>=0 else C[1]);u+=c*(C[1] if c>=0 else C[0])
    return l,u
def nonnegative(z,c=Q(0)):
    if not z and not c:ck(True);return
    l,u=interval(z,c);ck(l>=0)
@lru_cache(None)
def matrix(N):return tuple(tuple(-1 if (x&s).bit_count()%2 else 1 for x in range(N)) for s in range(N))
@lru_cache(maxsize=2048)
def rec(tab):
    N=len(tab);n=N.bit_length()-1
    W=[sum(v*t for v,t in zip(row,tab)) for row in matrix(N)]
    P=[Q(w*w,N*N) for w in W];H=entropy(P)
    d=tuple(Q(sum(tab[x]!=tab[x^(1<<i)] for x in range(N)),N) for i in range(n))
    ck(sum(P)==1);ck(sum(d)==sum(s.bit_count()*p for s,p in enumerate(P)))
    return H,sum(d),d,P
def masktab(mask):return tuple(1 if mask>>x&1 else -1 for x in range(4))
def product(g,h):return tuple(x*y for x,y in zip(g,h))
def gamma(g,h):return Q(sum(x!=y for x,y in zip(g,h)),len(g))
def switch(g,h,s):return tuple(h[x] if y==0 else g[x] for y in range(1<<s) for x in range(len(g)))
def split(tab,i,b):
    n=len(tab).bit_length()-1
    return tuple(tab[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(1<<(n-1)))
def erasure(tab,i):
    H,_,_,P=rec(tab);N=len(tab);n=N.bit_length()-1
    marg=[P[(x&((1<<i)-1))|((x>>i)<<(i+1))]+P[(x&((1<<i)-1))|((x>>i)<<(i+1))|(1<<i)] for x in range(1<<(n-1))]
    return add(H,entropy(marg),-1)
def oneblock(g,h,s):
    a=Q(1,2**s);gam=gamma(g,h);tab=switch(g,h,s);n=len(g).bit_length()-1
    H,I,ds,_=rec(tab);Hg,Ig,dg,_=rec(g);Hh,Ih,dh,_=rec(h)
    Is=2*s*a*gam;It=(1-a)*Ig+a*Ih;Ht=add(mul(Hg,1-a),Hh,a)
    ck(I==Is+It);ck(ds[:n]==tuple((1-a)*u+a*v for u,v in zip(dg,dh)))
    for d in ds[n:]:ck(d==2*a*gam)
    _,Ip,dp,_=rec(product(g,h));R=2*a*(1-a)*Ip
    for u,v,w in zip(dp,dg,dh):ck(u<=v+w)
    ck(R<=2*It)
    EB={};decrement={};Jtree={};mutree=Q(0);node=tab;w=Q(1)
    for j in range(s,0,-1):
        rho=Q(1,2**(j-1));B=erasure(node,n)
        _,In,dn,_=rec(node);ch0=split(node,n,0);ch1=split(node,n,1)
        H0,I0,*_=rec(ch0);H1,I1,*_=rec(ch1);Hn=rec(node)[0]
        ck(In-(I0+I1)/2==rho*gam)
        delta=add(add(Hn,H0,-Q(1,2)),H1,-Q(1,2))
        nonnegative(add(delta,B,-1));nonnegative(add(mul({2:rho*gam},0),add(delta,B,-1),-1),2*rho*gam)
        N=len(ch0)
        W0=[sum(v*t for v,t in zip(row,ch0)) for row in matrix(N)]
        W1=[sum(v*t for v,t in zip(row,ch1)) for row in matrix(N)]
        J={};mu=Q(0)
        for u,v in zip(W0,W1):
            minority=Q((abs(u)-abs(v))**2,4*N*N);q=Q(u*u+v*v,2*N*N)
            mu+=minority
            if minority:J=add(J,logform(q/minority),minority)
        nonnegative(add(B,J,-1));ck(mu<=rho*gam)
        Jtree=add(Jtree,J,w);mutree+=w*mu
        EB=add(EB,B,w);decrement=add(decrement,delta,w)
        node=ch0;w/=2
    ck(decrement==add(H,Ht,-1))
    rhs={2:2*(1-2*a)*Is}
    if gam:rhs=add(rhs,logform(gam),-4*a*gam*(1-a))
    nonnegative(add(rhs,EB,-1),4*a*gam*(1-a))
    nonnegative(add({2:Q(11,2)*Is+R},decrement,-1))
    nonnegative(add({2:Q(5,2)*Is+R},EB,-1))
    # This also independently verifies a sufficient full-minority bound using J<=B,mu<=d.
    nonnegative(add({2:7*Is+R},EB,-1),-3*Is)
    nonnegative(add({2:Q(5,2)*Is+R},Jtree,-1))
    nonnegative(add({2:7*Is+R},Jtree,-1),-3*mutree)
    return gam
def nested(g0,g1,g2,r,s):
    a,b=Q(1,2**r),Q(1,2**s);pi=(1-a,a*(1-b),a*b)
    h=switch(g1,g2,s);g0pad=g0*(1<<s);tab=switch(g0pad,h,r)
    H,I,ds,_=rec(tab);core=[rec(g) for g in (g0,g1,g2)]
    IsB=2*s*b*gamma(g1,g2)
    IsA=2*r*a*((1-b)*gamma(g0,g1)+b*gamma(g0,g2));Is=IsA+a*IsB
    Ht={};It=Q(0)
    for p,z in zip(pi,core):Ht=add(Ht,z[0],p);It+=p*z[1]
    ck(I==Is+It)
    IP=[rec(product(g,h))[1] for g,h in ((g0,g1),(g0,g2),(g1,g2))]
    Rdata=2*a*(1-a)*((1-b)*IP[0]+b*IP[1])+2*a*b*(1-b)*IP[2]
    Rp=rec(product(g0pad,h))[1]
    Rcontrol=2*a*(1-a)*IsB
    ck(2*a*(1-a)*Rp+2*a*b*(1-b)*IP[2]==Rdata+Rcontrol)
    Rstar=2*(pi[0]*pi[1]*IP[0]+pi[0]*pi[2]*IP[1]+pi[1]*pi[2]*IP[2])
    ck(Rdata-Rstar==2*a*(1-a)*b*(1-b)*IP[2]);ck(Rstar<=2*It)
    caps=(2*a,2*(1-a+b),2*(2-a-b))
    for i in range(2):
        Iij=[rec(product(g,h))[2][i] for g,h in ((g0,g1),(g0,g2),(g1,g2))]
        Ri=2*a*(1-a)*((1-b)*Iij[0]+b*Iij[1])+2*a*b*(1-b)*Iij[2]
        cap=sum(p*c*z[2][i] for p,c,z in zip(pi,caps,core));ck(Ri<=cap)
        ck(ds[i]==sum(p*z[2][i] for p,z in zip(pi,core)))
    decrement=add(H,Ht,-1)
    nonnegative(add({2:Q(11,2)*Is+Rdata+Rcontrol},decrement,-1))
    # Actual signed inequality checked at three prices; no individual negative child is dropped.
    for K in (Q(2),Q(11,2),Q(8)):
        Droot=add({2:K*I},H,-1);Dterm=add({2:K*It},Ht,-1)
        lower=add(Dterm,{2:(K-Q(11,2))*Is-Rdata-Rcontrol})
        nonnegative(add(Droot,lower,-1))
    return Rdata,Rstar
def compositions(n):
    if n==0:yield ();return
    for k in range(1,n+1):
        for rest in compositions(n-k):yield (k,)+rest
def chains():
    rows=[]
    for n in range(1,9):
        for ts in compositions(n):
            aa=[Q(1,2**t) for t in ts];p=Q(1,2**n)
            reserve=2*p*sum(1-a for a in aa);fold=2*p*(1-p)
            ck(reserve>=fold)
            if len(ts)==2:ck(reserve-fold==2*p*(1-aa[0])*(1-aa[1]))
            if all(t==1 for t in ts):ck(reserve/p==n)
            rows.append({'widths':ts,'terminal_I':str(p),'split_data_R':str(reserve),'fold_data_R':str(fold),'refund':str(reserve-fold)})
    (BASE/'out'/'chains.json').write_text(json.dumps(rows,indent=2));return len(rows)
def scalar():
    c=Q(81,56)
    for s in range(1,6):
        a=Q(1,2**s)
        if s<=4:ck(2*(1-2*a)+2*c+2*c*(1-a)/s<Q(11,2))
        ck(2*(1-2*a)+2*c*(1-a)/s<Q(5,2))
    ck(2+Q(12,5)*c<Q(11,2));ck(2+c/3<Q(5,2));ck(Q(5,2)+3*c<7)
def main(pilot):
    start=time.monotonic();masks=[0,1,6,15] if pilot else range(16);pairs=triples=0
    scalar()
    for m,n in itertools.product(masks,repeat=2):
        for s in ((1,2) if pilot else (1,2,3)):
            oneblock(masktab(m),masktab(n),s);pairs+=1
    elapsed=time.monotonic()-start
    (BASE/'out'/('pilot_pairs.json' if pilot else 'pairs.json')).write_text(json.dumps({'status':'PASS','cases':pairs,'assertions':COUNT,'seconds':elapsed},indent=2))
    print('PAIR_SCOPE_PASS',pairs,COUNT,elapsed,flush=True)
    for m,n,t in itertools.product(masks,repeat=3):
        for r,s in itertools.product((1,2),repeat=2):nested(masktab(m),masktab(n),masktab(t),r,s);triples+=1
    ch=chains()
    result={'status':'PASS','pilot':pilot,'pair_cases':pairs,'triple_cases':triples,'width_compositions':ch,'assertions':COUNT,'seconds':time.monotonic()-start,'arithmetic':'Direct integer Walsh/Fraction edges/prime-log forms and80-term rational intervals','review_scope':'A023@3 whole-block only; no repair contribution','maximum_dimension':6,'memory_estimate_mb':160}
    (BASE/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');main(p.parse_args().pilot)
