from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); ASSERTIONS=0; SIGNS=0
PILOT='--pilot' in sys.argv
PREFIX_ONLY='--prefix-only' in sys.argv
def check(x,label=''):
    global ASSERTIONS
    ASSERTIONS+=1
    if not x: raise AssertionError((ASSERTIONS,label))
def plus(*terms):
    z={}
    for k,v in terms:
        for p,a in v.items(): z[p]=z.get(p,F(0))+k*a
    return {p:a for p,a in z.items() if a}
@lru_cache(None)
def factors(n):
    z={}; d=2
    while d*d<=n:
        while n%d==0: z[d]=z.get(d,0)+1; n//=d
        d+=1
    if n>1: z[n]=z.get(n,0)+1
    return z
@lru_cache(None)
def logv(x):
    x=F(x); z=dict(factors(x.numerator))
    for p,a in factors(x.denominator).items(): z[p]=z.get(p,0)-a
    return {p:F(a) for p,a in z.items() if a}
@lru_cache(None)
def phi(x): return {} if not x else plus((-x,logv(x)))
def Phi(a,b): return plus((1,phi(a)),(1,phi(b)),(-1,phi(a+b)))
def pair(a,b): return plus((1,phi(a*a)),(1,phi(b*b)),(-F(1,2),phi((a+b)**2)),(-F(1,2),phi((a-b)**2)))
def fwht(v):
    a=list(v); s=1
    while s<len(a):
        for j in range(0,len(a),2*s):
            for k in range(j,j+s): x,y=a[k],a[k+s]; a[k],a[k+s]=x+y,x-y
        s*=2
    return a
@lru_cache(None)
def core(v):
    coeff=tuple(F(a,len(v)) for a in fwht(v)); p=tuple(a*a for a in coeff)
    H=plus(*[(1,phi(x)) for x in p]); mean=coeff[0]
    n=len(v).bit_length()-1
    ds=tuple(F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(n))
    Is=sum((p[x]*x.bit_count() for x in range(len(v))),F(0))
    check(Is==sum(ds,F(0)),'edge/Walsh influence')
    return H,mean,coeff,ds
@lru_cache(None)
def spectrum_H(v):
    return plus(*[(1,phi(F(a*a,len(v)**2))) for a in fwht(v)])
def child(v,i,b): return tuple(v[x] for x in range(len(v)) if ((x>>i)&1)==b)
@lru_cache(None)
def composed(ctrl,u,v):
    return tuple(u[x] if j==0 else v[y] if j==1 else 1 for j in ctrl for y in range(len(v)) for x in range(len(u)))
def outer(ctrl,u,v,j,i):
    cur=u if j==0 else v; other=v if j==0 else u
    H,m,co,ds=core(cur); mo=core(other)[1]; beta=co[1<<i]
    return outer_values(ctrl,m,mo,j,beta)
@lru_cache(None)
def outer_values(ctrl,m,mo,j,beta):
    t=beta*beta
    av=tuple(m if state==j else mo if state==1-j else F(1) for state in ctrl)
    cv=tuple(F(state==j) for state in ctrl)
    ah=tuple(x/4 for x in fwht(av)); ch=tuple(x/4 for x in fwht(cv))
    M=plus(*[(1,Phi(a*a,t*c*c)) for a,c in zip(ah,ch)])
    J=plus(*[(1,plus((1,phi(a*a+t*c*c)),(-F(1,2),phi((a+beta*c)**2)),(-F(1,2),phi((a-beta*c)**2)))) for a,c in zip(ah,ch)])
    return M,J,pair(m,beta),t
@lru_cache(None)
def lnb(x):
    z=(x-1)/(x+1); n=32
    a=2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    b=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return a,a+b
LN2=lnb(F(2))
@lru_cache(None)
def logb(p):
    k=p.bit_length()-1; a,b=lnb(F(p,2**k)); return F(k)+a/LN2[1],F(k)+b/LN2[0]
def bounds(v): return bounds_tuple(tuple(sorted(v.items())))
@lru_cache(None)
def bounds_tuple(v):
    lo=hi=F(0)
    for p,a in v:
        l,h=logb(p); lo+=a*(l if a>=0 else h); hi+=a*(h if a>=0 else l)
    return lo,hi
def nonnegative(v):
    global SIGNS
    SIGNS+=1
    if not v: return True
    l,h=bounds(v)
    if l>=0: return True
    if h<0: return False
    raise ArithmeticError('32 terms failed to settle a sign')
def positive(v):
    global SIGNS
    SIGNS+=1
    if not v: return {}
    lo,hi=bounds(v)
    if lo>0: return v
    if hi<0: return {}
    raise ArithmeticError('32 terms failed in Snell sign')
@lru_cache(None)
def core_reserve(v,C):
    if len(v)==1: return {}
    v0,v1=child(v,0,0),child(v,0,1); H,_,_,ds=core(v)
    D=plus((1,H),(-F(1,2),core(v0)[0]),(-F(1,2),core(v1)[0]))
    return positive(plus((1,D),(-C,{2:ds[0]}),(F(1,2),core_reserve(v0,C)),(F(1,2),core_reserve(v1,C))))
def rarity(ctrl,u,v):
    return plus(*[(F(ctrl.count(j),4)*(1-core(cur)[1]**2),logv(F(4,ctrl.count(j)))) for j,cur in enumerate((u,v)) if ctrl.count(j)])
def candidate(ctrl,u,v,C):
    return plus((F(ctrl.count(0),4),core_reserve(u,C)),(F(ctrl.count(1),4),core_reserve(v,C)),(1,rarity(ctrl,u,v)))
def controlI(ctrl,u,v):
    means=[core(u)[1],core(v)[1],F(1)]; total=F(0)
    for i in range(2):
        for z in range(4):
            a,b=ctrl[z],ctrl[z^(1<<i)]
            if a!=b: total+=(1-means[a]*means[b])/8
    return total
def table(n,x): return tuple(1 if (x>>i)&1 else -1 for i in range(2**n))
allcores=[table(2,x) for x in range(16)]
named=[table(2,x) for x in (0,15,7,6)]
controllers=list(product(range(3),repeat=4))
if PILOT: controllers=controllers[:8]; roots=named
else: roots=[] if PREFIX_ONLY else named
root_count=0;face_count=0
for ctrl in controllers:
    for u,v in product(roots,repeat=2):
        root_count+=1; HF=spectrum_H(composed(ctrl,u,v)); q=[F(ctrl.count(j),4) for j in range(2)]
        check(nonnegative(plus((2,{2:controlI(ctrl,u,v)}),(-1,rarity(ctrl,u,v)))),'owned rarity')
        for j,cur in enumerate((u,v)):
            for i in range(2):
                M,J,P,t=outer(ctrl,u,v,j,i); Dcore=plus((1,core(cur)[0]),(-F(1,2),core(child(cur,i,0))[0]),(-F(1,2),core(child(cur,i,1))[0]))
                children=[composed(ctrl,child(u,i,b),v) if j==0 else composed(ctrl,u,child(v,i,b)) for b in range(2)]
                DF=plus((1,HF),(-F(1,2),spectrum_H(children[0])),(-F(1,2),spectrum_H(children[1])))
                check(DF==plus((q[j],Dcore),(-q[j],P),(1,M),(1,J)),'A087 exact signed query')
                check(nonnegative(P),'pair refund positive')
                check(nonnegative(J),'unnormalized sector gap')
                e_ne=plus((1,core(cur)[0]),(-1,phi(core(cur)[1]**2)))
                e_child=plus(*[(F(1,2),plus((1,core(ch)[0]),(-1,phi(core(ch)[1]**2)))) for ch in (child(cur,i,0),child(cur,i,1))])
                check(plus((1,Dcore),(-1,P))==plus((1,e_ne),(-1,e_child),(-1,phi(t))),'nonempty signed ledger')
                if q[j]:
                    # Rational alpha increment 11/2 dominates the reconstructed cap+J rate.
                    upper=plus((F(11,2)*q[j],{2:core(cur)[3][i]}),(q[j]*t,logv(1/q[j])))
                    check(nonnegative(plus((1,upper),(-1,M),(-1,J))),'positive outer local bank')
                else: check(not M and not J,'zero selector')
                face_count+=1
        if time.perf_counter()-START>(58 if PILOT else 595): raise TimeoutError('Frozen execution cap')
    (ROOT/'out'/'CHECKPOINT_PREFIX_INIT.json').write_text(json.dumps({'controllers_finished':controllers.index(ctrl)+1,'roots_finished':root_count,'faces_finished':face_count,'exact_assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START,'status':'IN_PROGRESS'},indent=2)+'\n',encoding='utf-8')

TREECOUNT=0;NODECOUNT=0
@lru_cache(None)
def prefix_tree(ctrl,u,v,order,C,level=0):
    global NODECOUNT
    NODECOUNT+=1
    R=candidate(ctrl,u,v,C)
    if not order:
        check(not R,'constant data reserve zero')
        return {},spectrum_H(composed(ctrl,u,v))
    j=order[0]; cur=u if j==0 else v; q=F(ctrl.count(j),4); alpha=C+F(11,2)
    vals=[]; leafs=[]; rs=[]
    for b in range(2):
        un,vn=(child(u,0,b),v) if j==0 else (u,child(v,0,b))
        value,leaf=prefix_tree(ctrl,un,vn,order[1:],C,level+1)
        vals.append(value);leafs.append(leaf);rs.append(candidate(ctrl,un,vn,C))
    HF=spectrum_H(composed(ctrl,u,v))
    un0,vn0=(child(u,0,0),v) if j==0 else (u,child(v,0,0))
    un1,vn1=(child(u,0,1),v) if j==0 else (u,child(v,0,1))
    D=plus((1,HF),(-F(1,2),spectrum_H(composed(ctrl,un0,vn0))),(-F(1,2),spectrum_H(composed(ctrl,un1,vn1))))
    need=positive(plus((1,D),(-alpha*q,{2:core(cur)[3][0]}),(F(1,2),vals[0]),(F(1,2),vals[1])))
    check(nonnegative(plus((1,R),(-1,need))),'least nonnegative prefix reserve dominated')
    check(nonnegative(plus((alpha*q,{2:core(cur)[3][0]}),(1,R),(-F(1,2),rs[0]),(-F(1,2),rs[1]),(-1,D))),'candidate drift')
    return need,plus((F(1,2),leafs[0]),(F(1,2),leafs[1]))

for ctrl in controllers:
    for u,v in product(named,repeat=2):
        for order in ((0,1,0,1),(1,0,1,0)):
            for C in (F(0),F(2),F(4)):
                value,leaf=prefix_tree(ctrl,u,v,order,C);TREECOUNT+=1
        if time.perf_counter()-START>(58 if PILOT else 595): raise TimeoutError('Frozen execution cap')
    (ROOT/'out'/'PREFIX_CHECKPOINT.json').write_text(json.dumps({'controllers_finished':controllers.index(ctrl)+1,'trees_finished':TREECOUNT,'distinct_prefix_states':NODECOUNT,'exact_assertions':ASSERTIONS,'elapsed_seconds':time.perf_counter()-START,'status':'IN_PROGRESS'},indent=2)+'\n',encoding='utf-8')

# Independent boundary and growing-branch witnesses.
witness=[]
for h in allcores:
    ctrl=tuple(0 if x==1 else 1 for x in h); u=v=(1,-1)
    leafH={};leafI=F(0)
    for y0,y1 in product((1,-1),repeat=2):
        leaf=tuple(y0 if j==0 else y1 for j in ctrl)
        leafH=plus((1,leafH),(F(1,4),spectrum_H(leaf)))
        leafI+=sum(core(leaf)[3],F(0))/4
    check(leafH==plus((F(1,2),core(h)[0])),'arbitrary seed terminal H retained')
    check(leafI==sum(core(h)[3],F(0))/2==controlI(ctrl,u,v),'terminal control influence')
    for C in (F(0),F(2),F(4)):
        expected=plus(*[(F(1,4),core_reserve(tuple(y0 if j==0 else y1 for j in ctrl),C)) for y0,y1 in product((1,-1),repeat=2)])
        check(expected==plus((F(1,2),core_reserve(h,C))),'sign-translated boundary reserve')
ctrl=(0,2,2,2);u=(1,1,1,-1);v=(1,)
R0=candidate(ctrl,u,v,F(4));R1=candidate(ctrl,child(u,0,1),v,F(4));delta=plus((1,R1),(-1,R0))
check(nonnegative(delta) and bounds(delta)[0]>0,'growing rare branch')
witness.append({'name':'biased active child','root_R':{str(p):str(x) for p,x in R0.items()},'child_R':{str(p):str(x) for p,x in R1.items()},'increase_interval':[str(x) for x in bounds(delta)]})
out={'status':'PASS','mode':'pilot' if PILOT else 'full','root_cases':root_count,'root_data_faces':face_count,'prefix_trees':TREECOUNT,'distinct_prefix_states':NODECOUNT,'exact_assertions':ASSERTIONS,'certified_sign_decisions':SIGNS,'runtime_seconds':time.perf_counter()-START,'witnesses':witness,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'max_table_dimension':6,'H_cache_entries':spectrum_H.cache_info().currsize,'composed_cache_entries':composed.cache_info().currsize,'no_floating_signs':True}
name='PILOT.json' if PILOT else 'PREFIX_VALIDATION.json' if PREFIX_ONLY else 'VALIDATION.json'
(ROOT/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
