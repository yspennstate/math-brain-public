from fractions import Fraction as F
from pathlib import Path
from itertools import product
from functools import lru_cache
import json, sys, time

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
PILOT='--pilot' in sys.argv
LIMIT=55 if PILOT else 180
COUNT=0
TRUTH=0
EVENTS=0
def ck(test,msg=''):
    global COUNT
    COUNT+=1
    if not test: raise AssertionError(msg)
    if COUNT%500==0 and time.perf_counter()-START>LIMIT: raise RuntimeError('frozen cap')

@lru_cache(None)
def ln_unit(x):
    z=(x-1)/(x+1); s=F(0); p=z
    for j in range(24):
        s+=p/F(2*j+1); p*=z*z
    lo=2*s
    return lo,lo+2*p/(49*(1-z*z))

@lru_cache(None)
def log2(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(F(2)**k)
    if y<1: k-=1; y*=2
    assert 1<=y<2
    l,h=ln_unit(y); l2,h2=ln_unit(F(2))
    low=F(k)+l/h2; high=F(k)+h/l2
    den=1<<40
    return F(low.numerator*den//low.denominator,den),F(-((-high.numerator*den)//high.denominator),den)

def cost(P,Q):
    lo=hi=F(0)
    for A,p in enumerate(P):
        if A and p:
            ck(Q.get(A,F(0))>0,'missing support')
            l,h=log2(1/Q[A]); lo+=p*l; hi+=p*h
    return lo,hi

def spectrum(n,predicate):
    global TRUTH
    vals=[1 if predicate(x) else -1 for x in range(1<<n)]; TRUTH+=len(vals)
    a=vals[:]; h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]; a[j]=x+y; a[j+h]=x-y
        h*=2
    P=[F(x*x,(1<<n)**2) for x in a]
    ck(sum(P)==1)
    I=sum((p*A.bit_count() for A,p in enumerate(P)),F(0))
    direct=F(sum(vals[x]!=vals[x^(1<<i)] for x in range(1<<n) for i in range(n)),1<<n)
    ck(I==direct,'physical influence mismatch')
    return P,I

def subsets(E):
    out=[0]; s=E
    while s: out.append(s); s=(s-1)&E
    return out

def law(supports,oracle=False):
    global EVENTS
    beta=[F(1,1<<E.bit_count()) for E in supports]; rho=sum(beta)
    tables=[]
    for E,b in zip(supports,beta):
        tables.append([(A,(1-b) if not A else b*b/(1-b)) for A in subsets(E)])
    state={0:(F(1),F(0))}
    for table in tables:
        nxt={}
        for A,(a,b) in state.items():
            for S,m in table:
                C=A|S; aa,bb=nxt.get(C,(F(0),F(0)))
                nxt[C]=(aa+a*m,bb+(b+bool(S)*a)*m)
        state=nxt
    Q={A:b/rho for A,(a,b) in state.items() if A}
    ck(sum(Q.values())==1,'normalization')
    if oracle:
        direct={}
        for j,E in enumerate(supports):
            for tup in product(*tables):
                if not tup[j][0]: continue
                mass=beta[j]/rho/F((1<<E.bit_count())-1)
                A=0
                for i,(s,m) in enumerate(tup):
                    A|=s
                    if i!=j: mass*=m
                direct[A]=direct.get(A,F(0))+mass; EVENTS+=1
        ck(Q==direct,'conditional-anchor oracle')
    return Q

def profile(k,widths):
    Z=(1<<k)-1; pos=k; blocks=[]
    for w in widths:
        blocks.append(((1<<w)-1)<<pos); pos+=w
    P,I=spectrum(pos,lambda x: bool(x&Z) or all(x&B for B in blocks))
    Q=law([Z|B for B in blocks],PILOT)
    R={A:q/2 for A,q in Q.items()}
    for A in subsets(Z):
        if A: R[A]+=F(1,2*((1<<k)-1))
    ck(sum(R.values())==1)
    t=F(1,1<<k); eps=[F(1,1<<w) for w in widths]
    a=F(1)
    for e in eps: a*=1-e
    S=sum(eps); J=a*sum(w*e/(1-e) for w,e in zip(widths,eps))
    ck(I==2*t*(k*(1-a)+J),'core physical identity')
    ck(a*S<=1-a)
    ck(sum(P[A] for A in range(len(P)) if A and not A&~Z)==4*t*(1-t)*(1-a)**2)
    for B,e in zip(blocks,eps): ck(sum(p for A,p in enumerate(P) if A&B)==4*t*a*e)
    rho=t*S
    for A in Q:
        private=A&~Z
        if private:
            Bparts=[private&B for B in blocks]; L=sum(bool(B) for B in Bparts)
            base=F(L)/rho
            for B,e in zip(Bparts,eps):
                b=t*e; base*=b*b/(1-b) if B else 1-b
            ck(Q[private]==base)
            ck(Q[A]>=base,'allocation injection')
    l,h=cost(P,R); ck(h<=F(17,2)*I,'17/2 core bound')
    # Independent review of A008's ORIGINAL k=1 bound and exact core atom.
    if k==1:
        ck(h<=F(29,2)*I)
        qz=Q[Z]
        beta=[t*e for e in eps]; c=[b*b/(1-b) for b in beta]
        core=F(0)
        for j in range(len(beta)):
            m=c[j]
            for i in range(len(beta)):
                if i!=j: m*=1-beta[i]+c[i]
            core+=m
        ck(qz==core/rho)
    return {'k':k,'widths':widths,'n':pos,'I':str(I),'cost_interval':[str(l),str(h)]}

def two_stars(w,r):
    z=1; y=1<<1; blocks=[]; pos=2
    for _ in range(2*r): blocks.append(((1<<w)-1)<<pos); pos+=w
    P,I=spectrum(pos,lambda x:(bool(x&z) or all(x&B for B in blocks[:r])) and (bool(x&y) or all(x&B for B in blocks[r:])))
    supports=[z|B for B in blocks[:r]]+[y|B for B in blocks[r:]]
    Q=law(supports,PILOT)
    R={A:q/3 for A,q in Q.items()}; R[z]+=F(1,3); R[y]+=F(1,3)
    e=F(1,1<<w); a=(1-e)**r; Is=1-a+a*r*w*e/(1-e)
    ck(I==(1+a)*Is)
    ck(P[z|y]==(1-a)**4/4)
    b=e/2; c=b*b/(1-b); d=1-b+c
    ck(Q[z|y]==c/b*d**(r-1)*(d**r-(1-b)**r))
    ck(R[z|y]==Q[z|y]/3)
    # A genuinely different paid sector reference; both-sector retains joint cores.
    components=[]
    for core,bb in [(z,blocks[:r]),(y,blocks[r:])]:
        qq=law([core|B for B in bb]); rr={A:q/2 for A,q in qq.items()}; rr[core]+=F(1,2)
        components.append(rr)
    sector={}
    for rr in components:
        for A,q in rr.items(): sector[A]=sector.get(A,F(0))+q/3
    for A,q in components[0].items():
        for B,s in components[1].items(): sector[A|B]=sector.get(A|B,F(0))+q*s/3
    ck(sum(sector.values())==1)
    l,h=cost(P,sector); ck(h<11*I,'sector repaired bound')
    ls,hs=cost(P,R)
    return {'w':w,'r':r,'n':pos,'I':str(I),'joint_atom':str(P[z|y]),'Q_joint':str(Q[z|y]),'failed_reference_cost':[str(ls),str(hs)],'paid_sector_cost':[str(l),str(h)]}

profiles=[(k,ww) for k in ([1,2] if PILOT else [1,2,3]) for ww in ([[1],[2],[1,1]] if PILOT else [[1],[2],[3],[1,1],[1,2],[2,2],[1,1,1]])]
rows=[profile(k,ww) for k,ww in profiles]
pairs=[two_stars(w,r) for w in ([1] if PILOT else [1,2]) for r in [1,2]]
if not PILOT:
    # Analytic induction antecedents; not physical truth-table claims at huge r,w.
    for r in range(4,129):
        a=F(3,4)**r; Is=1-a+F(r,2)*F(3,4)**(r-1)
        ck(a<F(1,2)); ck(Is<2); ck((1+a)*Is<3)
        ck((1-a)**4/4>F(1,64))
        b=F(1,8); c=F(1,56); d=F(25,28)
        ck(c/b*d**(r-1)*(d**r-F(7,8)**r)<=d**(2*r-1)/7)
        # Source A008 exact singleton law and the physical bounded entropy payment.
        ck(F(1,7)*d**(r-1)>0)
    for w in range(8,129):
        ck(F(w*w,1<<w)/(1-F(1,1<<w))<=F(64,255))
        ck(F(35,8)>=4+F(3,w))
        ck((1-F(1,1<<w))**2>F(1,2))
    for k in range(1,129): ck((1-F(1,1<<k))*(1+F(1,k))<=F(5,4))
    ck(log2(F(28,25))[0]>F(3,28))
elapsed=time.perf_counter()-START
ck(elapsed<LIMIT,'runtime cap')
out={'status':'PASS','helper_version':'A006-core-closure-v1','pilot':PILOT,'assertions':COUNT,'truth_inputs':TRUTH,'actual_anchor_oracle_events':EVENTS,'profiles':rows,'two_stars':pairs,'seconds':elapsed,'log_certificate':'24-term atanh; omitted tail <=2 z^49/[49(1-z^2)]; ratio endpoints use independent ln2 interval; outward 40-bit dyadics'}
path=ROOT/'out'/('PILOT.json' if PILOT else 'CHECK.json')
path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','pilot','assertions','truth_inputs','actual_anchor_oracle_events','seconds']}))
