"""Frozen triangle width-exhaustion check; exact compressed signed spectra."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json, math, time, argparse

R=Path(__file__).resolve().parents[1]
CACHE={}
CHECKS=0
def ck(b):
    global CHECKS
    assert b
    CHECKS+=1

def log2q(x):
    x=F(x)
    if x in CACHE:return CACHE[x]
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/F(2)**k
    if y<1:k-=1;y*=2
    assert 1<=y<2
    def ln(z):
        t=(z-1)/(z+1);v=t;total=F(0)
        for j in range(32):total+=v/(2*j+1);v*=t*t
        lo=2*total
        return lo,lo+2*v/(65*(1-t*t))
    l,h=ln(y);l2,h2=ln(F(2))
    ans=(F(k)+l/h2,F(k)+h/l2)
    CACHE[x]=ans
    return ans

def logs(terms):
    lo=hi=F(0)
    for c,x in terms:
        if not c:continue
        l,h=log2q(x)
        if c<0:l,h=h,l
        lo+=c*l;hi+=c*h
    return lo,hi

def add(*vs):return sum(x[0] for x in vs),sum(x[1] for x in vs)
def scale(v,c):return (v[0]*c,v[1]*c) if c>=0 else (v[1]*c,v[0]*c)
def sub(a,b):return add(a,scale(b,-1))
def outward(v):
    d=1<<90
    return [str(F(x.numerator*d//x.denominator,d)) if j==0 else str(F(-((-x.numerator*d)//x.denominator),d)) for j,x in enumerate(v)]

def setup(L):
    # labels a,b,c,x then two length-L private blocks
    P=[1<<3,((1<<L)-1)<<4,((1<<L)-1)<<(4+L)]
    E=[P[0]|1|4,P[1]|1|2,P[2]|2|4]
    U=[]
    for J in range(8):
        u=0
        for j in range(3):
            if J>>j&1:u|=E[j]
        U.append(u)
    def coeff(S):
        return -F(S==0)+sum((2*F((-1)**J.bit_count(),1<<u.bit_count()) for J,u in enumerate(U) if not S&~u),F(0))
    return P,E,coeff

def cells(L,excluded=0):
    P,E,coeff=setup(L)
    masks=[p&~excluded for p in P]
    for flags in product([0,1],repeat=3):
        if any(v and not m for v,m in zip(flags,masks)):continue
        mult=1;private=0
        for v,m in zip(flags,masks):
            if v:mult*=(1<<m.bit_count())-1;private|=m&-m
        for shared in range(8):
            if shared&excluded:continue
            yield mult,private|shared,coeff

def entropy(L,child=None):
    terms=[];total=F(0)
    for m,S,c in cells(L,8 if child is not None else 0):
        a=c(S) if child is None else c(S)+(1 if child==0 else -1)*c(S|8)
        p=a*a;total+=m*p
        if p:terms.append((-m*p,p))
    ck(total==1)
    return logs(terms)

def row(L,i,child=None):
    P,E,c=setup(L);bit=1<<i
    termsM=[];termsB=[];energy=F(0);refmass=F(0);cross=F(0)
    excluded=bit|(8 if child is not None else 0)
    for m,S,c in cells(L,excluded):
        if child is None:u,v=c(S),c(S|bit)
        else:
            sign=1 if child==0 else -1
            u=c(S)+sign*c(S|8);v=c(S|bit)+sign*c(S|bit|8)
        p0,p1=u*u,v*v;r=p0+p1
        energy+=m*p1;refmass+=m*r;cross+=m*u*v
        if p1:termsM.append((m*p1,r/p1));termsB.append((m*p1,r/p1))
        if p0:termsB.append((m*p0,r/p0))
    ck(refmass==1);ck(cross==0)
    return energy,logs(termsM),logs(termsB)

def case(L):
    q=F(1,1<<L);P,E,c=setup(L)
    rows=[row(L,i) for i in [0,1,2,3,4,4+L]]
    epriv=(2-2*q+q*q)/8+2*L*q*(F(3,8)-q/8)
    ck(epriv==rows[3][0]+L*(rows[4][0]+rows[5][0]))
    M=add(*(scale(z[1],F(1) if j<4 else F(L)) for j,z in enumerate(rows)))
    H=entropy(L);Bx=rows[3][2];Bchildren=[];Hchildren=[];CE=[];KLincoming=[]
    # SAME incoming reference Qbar=parent spectrum marginalized over x.
    for s in [0,1]:
        Hs=entropy(L,s);_,_,Ba=row(L,1,s)
        Hchildren.append(Hs);Bchildren.append(Ba)
        CEs=add(Hs,(F(1),F(1)),scale(Ba,-1));CE.append(CEs)
        terms=[];mass=F(0)
        for m,S,c in cells(L,8):
            u,v=c(S),c(S|8);p=(u+(1 if s==0 else -1)*v)**2
            r=u*u+v*v
            if p:ck(r>0);terms.append((m*p,p/r))
            mass+=m*r
        ck(mass==1);KLincoming.append(logs(terms))
    avg=lambda vs:scale(add(*vs),F(1,2))
    avgH=avg(Hchildren);avgCE=avg(CE);JS=avg(KLincoming)
    identity=sub(sub(H,add(Bx,avgH)),JS)
    ck(identity[0]<=0<=identity[1])
    inheritedCE=sub(H,Bx)
    reset=sub(avgCE,inheritedCE)
    bill=add(M,Bx,avgCE)
    margin=sub((17*epriv,17*epriv),bill)
    ck(margin[0]>0)
    # Tail proof uses a fixed three-bit point defect core.
    tailpoly=2*L*L+10*L+548
    if L>=16:
        Hg=entropy_limit();Mg=oriented_limit()
        ck(H[1]<add(Hg,(F((6*L+198)*q),)*2)[0])
        ck(M[1]<add(Mg,(F((2*L*L+4*L+350)*q),)*2)[0])
        ck(JS[0]>F(1,4))
        ck(reset[0]>F(1,4)-q*(L+F(3,2)))
    return {'L':L,'I_private':str(epriv),'H_root':outward(H),'M_old_debit':outward(M),'B_query':outward(Bx),'full_child_H':[outward(z) for z in Hchildren],'full_child_CE':[outward(z) for z in CE], 'incoming_child_KL':[outward(z) for z in KLincoming],'signed_reset_price':outward(reset),'total_bill':outward(bill),'remaining_original_17_bank':outward(margin)}

def entropy_limit():return logs([(-F(9,16),F(9,16)),(-F(7,16),F(1,16))])
def oriented_limit():return logs([(F(3,16),F(10)),(F(9,16),F(2))])

def tail():
    H=entropy_limit();M=oriented_limit()
    # L>=16: q<=2^-16 and polynomial*2^-L decreases.
    P=lambda l:2*l*l+10*l+548
    ck(2*P(16)>P(17));ck(P(16)==1220)
    cap=add(H,M,(F(3,4),F(3,4)),(F(P(16),1<<16),)*2)
    floor=17*(F(1,4)-F(1,4*(1<<16)))
    ck(cap[1]<floor);ck(F(23,32)**2/2>F(1,4))
    return {'tail_start':16,'entropy_core':outward(H),'M_core':outward(M),'all_L_bill_upper':outward(cap),'original_bank_lower':str(floor),'strict_margin_lower':str(floor-cap[1]),'monotonic_polynomial':'2P(L)-P(L+1)=2L^2+6L+536>0'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    start=time.monotonic();domain=[1,2,4] if args.pilot else list(range(1,16))+[16,32,64]
    records=[]
    for L in domain:
        assert time.monotonic()-start<(55 if args.pilot else 180)
        records.append(case(L))
        (R/'out/RESET_CHECKPOINT.json').write_text(json.dumps({'cases':records},indent=2)+'\n',encoding='utf-8')
    result={'cases':records,'tail':tail(),'assertions':CHECKS,'runtime_seconds':time.monotonic()-start,'rung':'author proof plus exact rational certificates; independent-agent review pending'}
    name='PILOT.json' if args.pilot else 'CHECK.json'
    (R/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'file':name,'cases':len(records),'checks':CHECKS,'seconds':result['runtime_seconds'],'reset_signs':[(z['L'],'positive' if F(z['signed_reset_price'][0])>0 else 'negative' if F(z['signed_reset_price'][1])<0 else 'unresolved') for z in records]}))
