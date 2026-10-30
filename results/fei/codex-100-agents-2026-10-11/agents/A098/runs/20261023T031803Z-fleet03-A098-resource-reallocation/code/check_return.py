from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,time,sys,hashlib
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out';start=time.monotonic();checks=0
def ck(ok):
    global checks
    checks+=1
    assert ok,checks
    assert time.monotonic()-start<55,'frozen runtime cap'
def marg(v,j):return tuple(v[x]+v[x|(1<<j)] for x in range(len(v)) if not x&(1<<j))
def cal(v,z):
    ck(sum(v)==1 and 0<=z<=1)
    if z==1:return (F(1),)+(F(0),)*(len(v)-1)
    ck(v[0]<1)
    return (z,)+tuple(x*(1-z)/(1-v[0]) for x in v[1:])
def unitln(x):
    z=(x-1)/(x+1)
    a=2*sum((z**(2*k+1)/F(2*k+1) for k in range(16)),F(0))
    return a,a+2*z**33/(33*(1-z*z))
L2=unitln(F(2))
@lru_cache(maxsize=8000)
def log(x):
    ck(x>0)
    k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
    if y<1:y*=2;k-=1
    ck(1<=y<2)
    if y==1:return (F(k),F(k))
    lo,hi=unitln(y);return k+lo/L2[1],k+hi/L2[0]
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def mult(c,a):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def ce(p,q):
    ans=(F(0),F(0))
    for a,b in zip(p,q):
        if a:ck(b>0);ans=plus(ans,mult(-a,log(b)))
    return ans
@lru_cache(maxsize=1000)
def spectrum(values):
    a=list(values);size=len(a);h=1
    while h<size:
        for i in range(0,size,2*h):
            for j in range(i,i+h):x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    p=tuple(F(x*x,size*size) for x in a);ck(sum(p)==1)
    return p
def children(v,j):return tuple(v[x] for x in range(len(v)) if not x&(1<<j)),tuple(v[x|(1<<j)] for x in range(len(v)) if not x&(1<<j))
def erasure(p,j):
    ans=(F(0),F(0))
    for x in range(len(p)):
        if x&(1<<j):continue
        a,b=p[x],p[x|(1<<j)]
        if a and b:ans=plus(ans,ce((a,b),(a/(a+b),b/(a+b))))
    return ans
def supplied(p,mode):
    m=p[0];v=1-m;N=len(p)
    if v==0:return p,p,p
    weights=tuple(F((19*x+3)%13+1) for x in range(1,N))
    if mode==0:w=tuple(x/v for x in p[1:])
    elif mode==1:w=tuple(x/sum(weights) for x in weights)
    else:w=tuple((p[x]/v+weights[x-1]/sum(weights))/2 for x in range(1,N))
    D=(m,)+tuple(v*x/2 for x in w)
    rem=1-sum(D);S=tuple(D[x]+rem/F(N) for x in range(N))
    gamma=F(1,2)
    base=(m,)+tuple(gamma*x for x in D[1:]);rest=1-sum(base)
    ghost=tuple(F((7*x+5)%17+1) for x in range(N));z=sum(ghost)
    Q=tuple(base[x]+rest*ghost[x]/z for x in range(N))
    ck(sum(D)<=1 and sum(S)==sum(Q)==1 and D[0]==m)
    ck(all(a>=b for a,b in zip(S,D)))
    ck(Q[0]>=m and all(Q[x]>=gamma*D[x] for x in range(1,N)))
    return D,S,Q
def algebra():
    tuples=0;admissible=0;negative_beta=0
    def compositions(k,n):
        if n==1:yield (k,);return
        for a in range(k+1):
            for b in compositions(k-a,n-1):yield(a,)+b
    for ints in compositions(4,8):
        S=tuple(F(x,4) for x in ints)
        for z,j,w in itertools.product([F(0),F(1,4),F(1,2),F(1)],range(3),[F(0),F(1,3),F(1)]):
            tuples+=1
            if z==1 and w!=1:continue # Constant parent cannot have nonconstant Boolean child.
            if S[0]==1 and z!=1:continue # Finite CE forbids the nonconstant parent.
            V=marg(S,j)
            if V[0]==1 and w!=1:continue # Occupied support propagation forbids this child.
            C=cal(S,z);lhs=cal(marg(C,j),w);rhs=cal(V,w)
            ck(lhs==rhs);ck(sum(lhs)==1 and min(lhs)>=0)
            admissible+=1
            if z<1 and z-(1-z)*S[0]/(1-S[0])<0:negative_beta+=1
    return {'laws':330,'pre_admissibility_tuples':tuples,'admissible_tuples':admissible,'negative_affine_beta':negative_beta}
def structural(n):
    roots=0;transitions=0
    for table in range(1<<(1<<n)):
        values=tuple(-1 if table&(1<<x) else 1 for x in range(1<<n));p=spectrum(values)
        for mode in range(3):
            _,S,_=supplied(p,mode);roots+=1
            def walk(v,raw,current):
                nonlocal transitions
                pv=spectrum(v);ck(current==cal(raw,pv[0]))
                for j in range((len(v)).bit_length()-1):
                    a,b=children(v,j);pa,pb=spectrum(a),spectrum(b)
                    ck(tuple((x+y)/2 for x,y in zip(pa,pb))==marg(pv,j))
                    direct=F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
                    ck(direct==sum(pv[x] for x in range(len(v)) if x&(1<<j)))
                    rawchild=marg(raw,j);inherited=marg(current,j)
                    for child,pc in [(a,pa),(b,pb)]:
                        target=cal(rawchild,pc[0]);ck(cal(inherited,pc[0])==target)
                        ck(all(q>0 for u,q in zip(pc,target) if u))
                        transitions+=1
                        # Two query levels suffice here; all deeper maps are covered by algebra.
                        if len(v)>(1<<(n-1)):walk(child,rawchild,target)
            walk(values,S,cal(S,p[0]))
    return {'Boolean_tables':1<<(1<<n),'source_roots':roots,'physical_transitions':transitions}
FIRST_POS=0;LATER_NEG=0;OLD_NONCONST=0;POLICIES=0
def ledger(v,S,Q,policy,depth=0,path=0,seen=False):
    global FIRST_POS,LATER_NEG,OLD_NONCONST
    p=spectrum(v);q=Q
    reset= (policy==0 and depth>=1) or (policy==1 and depth%2==1) or (policy==2 and depth>=1 and path%2==0)
    if reset:
        target=cal(S,p[0])
        if seen:
            ck(cal(q,p[0])==target)
            if target!=q:LATER_NEG+=1
        else:
            old,new=ce(p,q),ce(p,target)
            if new[0]>old[1]:FIRST_POS+=1
        q=target;seen=True
    stop=len(v)==1 or (policy==2 and depth==1 and path%2==1)
    if stop:
        if p[0]<1 and not reset:OLD_NONCONST+=1
        return ce(p,q)
    n=len(v).bit_length()-1;j=(depth+sum(x<0 for x in v))%n
    a,b=children(v,j);sm=marg(S,j);qm=marg(q,j)
    return plus(erasure(p,j),mult(F(1,2),plus(ledger(a,sm,qm,policy,depth+1,path*2,seen),ledger(b,sm,qm,policy,depth+1,path*2+1,seen))))
def global_cases(pilot):
    global POLICIES
    fixtures=[(2,t) for t in range(16)]
    if not pilot:fixtures += [(3,t) for t in [1,3,7,15,22,23,27,30,63,85,105,127,128,150,232,254]]
    for n,t in fixtures:
        v=tuple(-1 if t&(1<<x) else 1 for x in range(1<<n));p=spectrum(v)
        for mode in range(3):
            D,S,Q=supplied(p,mode);c=ce(p,D);m=p[0]
            for policy in range(4):
                bill=ledger(v,S,Q,policy)
                ck(bill[1]<=c[0]+1-m*m or bill==(F(0),F(0)))
                POLICIES+=1
    return {'Boolean_fixtures':len(fixtures),'policies':POLICIES,'positive_first_resets':FIRST_POS,'later_nonidentity_calibrations':LATER_NEG,'old_nonconstant_terminals':OLD_NONCONST}
pilot='--pilot' in sys.argv
stats={}
if not pilot:stats['algebra']=algebra()
stats['structural']=structural(2 if pilot else 3)
stats['global']=global_cases(pilot)
# Guard: conditional-NONEMPTY replacement is outside the free-return identity.
old=(F(0),F(1,4),F(1,4),F(1,2));returned=(F(0),F(1,3),F(1,3),F(1,3));actual=(F(0),F(0),F(0),F(1))
z=ce(actual,returned);u=ce(actual,old);ck(z[0]-u[1]>F(1,2));ck(3**2>2**3)
stats['changed_profile_guard']={'actual':'parity3 queried once gives nonconstant parity2 in BOTH children','old_occupied_atom':'1/2','returned_occupied_atom':'1/3','reset_bill':'log2(3)-1 > 1/2 bit','bound_scope':'not an FEI counterexample; free-return theorem excludes this nonempty-profile modification'}
ck(L2[0]>F(2,3))
result={'status':'PASS','pilot':pilot,'assertions':checks,'runtime_seconds':time.monotonic()-start,'stats':stats,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'Lean':'separate admission and compiler receipt required','full_FEI':'OPEN'}
(OUT/('PILOT_RESULT.json' if pilot else 'RESULT.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
