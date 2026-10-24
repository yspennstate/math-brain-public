"""A074 v4: binary Moebius polynomials; no external helper or source spectra."""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json, math, time, sys, hashlib

RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'
NEG={0,1,2,4,8,16,32,6,17,40}
TABLE=[-1 if x in NEG else 1 for x in range(64)]
CHECKS=0
SCALE=1<<160
TERMS=180

def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def check(v):
    global CHECKS
    CHECKS+=1
    assert v, CHECKS
def mobius(a):
    c=list(map(F,a)); n=(len(c)-1).bit_length()
    for i in range(n):
        for s in range(len(c)):
            if s>>i&1:c[s]-=c[s^(1<<i)]
    return c
def centered(c,p):
    # h(x)=sum c_T x_T, x_i=p+(x_i-p).
    b=c.copy(); n=(len(c)-1).bit_length()
    for i in range(n):
        for s in range(len(c)):
            if not s>>i&1:b[s]+=p*b[s|(1<<i)]
    return b
def masses(c,p):
    b=centered(c,p); w=p*(1-p)
    return [v*v*w**s.bit_count() for s,v in enumerate(b)]
def ceildiv(a,b):return -(-a//b)
def ln_from_t(lo,hi):
    # All values scaled by SCALE. Outward powers bound every Taylor term.
    a=b=SCALE; lower=upper=0
    for j in range(1,TERMS+1):
        a=a*lo//SCALE; b=ceildiv(b*hi,SCALE)
        lower+=a//j; upper+=ceildiv(b,j)
    # sum_{j>N} t^j/j <= 2^-N/(N+1), t<=1/2.
    upper+=ceildiv(SCALE,(1<<TERMS)*(TERMS+1))
    return lower,upper
LN2=ln_from_t(SCALE//2,SCALE//2)
LOGCACHE={}
def log2_bounds(x):
    if x in LOGCACHE:return LOGCACHE[x]
    assert x>0
    a,b=x.numerator,x.denominator
    k=a.bit_length()-b.bit_length()
    if k>=0:
        if a < b<<k:k-=1
    elif a<<(-k)<b:k-=1
    if k>=0:yn,yd=a,b<<k
    else:yn,yd=a<<(-k),b
    check(yd<=yn<2*yd)
    tnum=yn-yd
    if tnum==0:
        LOGCACHE[x]=(F(k),F(k))
        return LOGCACHE[x]
    low=tnum*SCALE//yn; high=ceildiv(tnum*SCALE,yn)
    check(0<=low<=high<=SCALE//2)
    ll,lh=ln_from_t(low,high)
    l=F(k)+F(ll,LN2[1]); h=F(k)+F(lh,LN2[0])
    LOGCACHE[x]=(l,h)
    return l,h
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,c):
    return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def xlx(x):return (F(0),F(0)) if x==0 else mul(log2_bounds(x),x)
def entropy(xs):
    ans=(F(0),F(0))
    for x in xs:ans=sub(ans,xlx(x))
    return ans
def phi(x,y):
    if x==0 or y==0:return F(0),F(0)
    return sub(sub(xlx(x+y),xlx(x)),xlx(y))
def pack(a):
    if isinstance(a,F):return str(a)
    if isinstance(a,tuple):return {'exact':[str(x) for x in a],'display':[float(x) for x in a]}
    return a
def record(label,n,p,d,t,E,H,extra=None):
    out={k:pack(v) for k,v in dict(label=label,physical_bits=n,p=p,minority=min(p,1-p),coordinate_influence=d,singleton_square=t,E=E,H=H,H_over_I=mul(H,1/(n*d))).items()}
    if extra:out.update({k:pack(v) for k,v in extra.items()})
    return out
def sections(j):
    other=[i for i in range(6) if i!=j]
    aa=[];dd=[]
    for z in range(32):
        x=sum(((z>>k)&1)<<i for k,i in enumerate(other))
        a,b=TABLE[x],TABLE[x|(1<<j)]
        aa.append(F(a+b,2));dd.append(F(a-b,2))
    return mobius(aa),mobius(dd)

def verify_symmetry():
    pairs=[(1,2),(0,4),(3,5)]; orbit=set(); count=0
    for perm in permutations(range(3)):
        for flips in product(range(2),repeat=3):
            mapping={}
            for j in range(3):
                for k in range(2):mapping[pairs[j][k]]=pairs[perm[j]][k^flips[j]]
            mapped={sum(((x>>i)&1)<<mapping[i] for i in range(6)) for x in NEG}
            check(mapped==NEG); orbit.add(mapping[0]);count+=1
    check(orbit==set(range(6)));check(count==48)
    return count

def seed():
    w=[F(sum(TABLE[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(64)),64) for s in range(64)]
    mu=[x*x for x in w];check(sum(mu)==1)
    E0=None;d0=None
    for i in range(6):
        d=F(sum(TABLE[x]!=TABLE[x^(1<<i)] for x in range(64)),64)
        check(d==sum(mu[s] for s in range(64) if s>>i&1));check(w[1<<i]**2==d*d)
        B=(F(0),F(0))
        for s in range(64):
            if not s>>i&1:B=add(B,phi(mu[s],mu[s|(1<<i)]))
        Ei=mul(B,1/d)
        if E0 is None:E0,d0=Ei,d
        else:check(Ei==E0);check(d==d0)
    p=F(len(NEG),64);H=entropy(mu)
    check(masses(mobius(TABLE),F(1,2))==mu)
    return (6,p,d0,d0*d0,E0,H)

def compose(state,sign,label):
    n,p,d,t,E,H=state
    if sign==-1:p=1-p
    m=1-2*p;v=4*p*(1-p)
    a,der=sections(0)
    c=[x+m*y for x,y in zip(a,der)]
    U=masses(c,p);D=masses(der,p);q=sum(D)
    check(q==2*p*(1-p)**3*(2-p))
    # Direct edge polynomial has values D(y)^2; independently compare all six.
    for j in range(6):
        aj,dj=sections(j)
        check(centered(dj,p)[0]==-q)
        check(sum(masses(dj,p))==q)
    mean=centered(mobius(TABLE),p)[0]
    newp=(1-mean)/2
    check(newp==(1-p)**4*(1+4*p-2*p*p))
    law=[*U,*[v*x for x in D]];check(sum(law)==1)
    full=masses(mobius(TABLE),p)
    check(sorted(full)==sorted(law))
    check(sum(F(s.bit_count())*x for s,x in enumerate(full))==6*v*q)
    R=(F(0),F(0))
    for x,y in zip(U,D):R=add(R,phi(x,t*y))
    R=sub(R,mul(phi(m*m,t),q))
    Cp=sub(entropy(full),mul(entropy([v,1-v]),6*q))
    En=add(E,mul(R,1/(q*d)))
    Hn=add(mul(H,6*q),Cp)
    result=(6*n,newp,q*d,q*q*t,En,Hn)
    check(result[3]==result[2]**2)
    extra={'chosen_sign':sign,'chosen_p':p,'q':q,'reserve':R,'Cp':Cp,'E_increment':mul(R,1/(q*d)),'H_over_I_increment':mul(Cp,1/(6*q*n*d))}
    return result,record(label,*result,extra=extra)

def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv
    verify_symmetry();st=seed();rows=[record('seed',*st)]
    save('PILOT_PARTIAL.json' if pilot else 'ORBIT_PARTIAL.json',rows)
    for k,sign in enumerate([1,-1,1],1):
        if pilot and k>1:break
        st,row=compose(st,sign,'g'+str(k));rows.append(row)
        check(F(row['reserve']['exact'][0])>0)
        save('PILOT_PARTIAL.json' if pilot else 'ORBIT_PARTIAL.json',rows)
    if not pilot:
        check(st[4][0]>F(669,200));check(0<min(st[1],1-st[1])<F(1,16))
        for sign in [1,-1]:
            child,row=compose(st,sign,'child_'+str(sign));rows.append(row)
            check(child[4][1]<F(669,200));check(F(row['reserve']['exact'][1])<0)
            check(0<min(child[1],1-child[1])<=12*min(st[1],1-st[1])**2)
            save('ORBIT_PARTIAL.json',rows)
    result={'status':'PASS','helper':'A074-binary-Moebius-v4','pilot':pilot,'assertions':CHECKS,'runtime_seconds':time.perf_counter()-start,'log_scale_bits':160,'positive_log_terms':TERMS,'rows':rows,'independence':'Fresh truth table character sums and binary Moebius polynomials; no external code or spectrum loaded'}
    save('PILOT.json' if pilot else 'VALIDATION.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__':main()
