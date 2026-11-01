from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import json,time,hashlib

run=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0
def check(x):
    global assertions
    assertions+=1
    if not x:raise AssertionError(assertions)
def combine(*terms):
    ans={}
    for c,d in terms:
        for p,v in d.items():ans[p]=ans.get(p,F(0))+c*v
    return {p:v for p,v in ans.items() if v}
@lru_cache(None)
def logq(q):
    q=F(q); check(q>0); ans={}
    for a,sign in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        # All probability denominators from smoothing are small except 2^m;
        # handle that factor first, leaving the large Mersenne numerator as
        # a whole logarithmic atom instead of factoring an arbitrary integer.
        while a%2==0 and a>1:
            ans[2]=ans.get(2,F(0))+sign; a//=2
        while p<=31 and p*p<=a:
            while a%p==0:ans[p]=ans.get(p,F(0))+sign; a//=p
            p+=1
        if a>1:ans[a]=ans.get(a,F(0))+sign
    return {p:v for p,v in ans.items() if v}
def entropy(p):return combine(*[(-x,logq(x)) for x in p if x])
def ce(p,q):
    check(len(p)==len(q) and sum(p)==sum(q)==1)
    check(all(not x or y>0 for x,y in zip(p,q)))
    return combine(*[(-x,logq(y)) for x,y in zip(p,q) if x])
def ln_bounds(x):
    t=(x-1)/(x+1); check(0<=t<=F(1,3))
    val=sum((2*t**(2*k+1)/F(2*k+1) for k in range(40)),F(0))
    return val,val+2*t**81/(81*(1-t*t))
ln2=ln_bounds(F(2))
@lru_cache(None)
def log_bounds(a):
    k=a.bit_length()-1; l,h=ln_bounds(F(a,2**k))
    return F(k)+l/ln2[1],F(k)+h/ln2[0]
def bounds(d):
    lo=hi=F(0)
    for p,c in d.items():
        a,b=log_bounds(p)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi
def positive(d):return bounds(d)[0]>0
def display(d):return [float(v) for v in bounds(d)]
def walsh(v):
    a=list(v); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return a
def spectrum(v):return [F(x*x,len(v)**2) for x in walsh(v)]
def restrict(v,j,s):return [x for k,x in enumerate(v) if (k>>j)&1==s]
def marginal(p,j):return [p[k]+p[k|(1<<j)] for k in range(len(p)) if not k&(1<<j)]
def erased(p,j):return combine((1,entropy(p)),(-1,entropy(marginal(p,j))))
def inf(v,j):return F(sum(x!=v[k^(1<<j)] for k,x in enumerate(v)),len(v))
def query(v,q,j):
    p=spectrum(v); pm=marginal(p,j); r=marginal(q,j)
    children=[restrict(v,j,s) for s in (0,1)]
    ps=[spectrum(c) for c in children]
    check(all((a+b)/2==x for a,b,x in zip(ps[0],ps[1],pm)))
    E=erased(p,j)
    # R is obtained independently as the exact difference of two KLs.
    R=combine((1,ce(p,q)),(-1,entropy(p)),(-1,ce(pm,r)),(1,entropy(pm)))
    check(not R or bounds(R)[0]>=0)
    check(not combine((1,ce(p,q)),(-1,E),(-F(1,2),ce(ps[0],r)),(-F(1,2),ce(ps[1],r)),(-1,R)))
    return children,ps,r,E,R
def smooth(r):return [F(7,8)*x+F(1,8*len(r)) for x in r]
cap=logq(F(8,7))
def reset(p,r):
    q=smooth(r); check(sum(q)==1 and all(x>0 for x in q))
    check(all(x>=F(7,8)*y for x,y in zip(q,r)))
    tax=combine((1,ce(p,q)),(-1,ce(p,r)))
    check(positive(combine((1,cap),(-1,tax))))
    return q,tax

b=[1 if y&7==0 else -1 for y in range(64)]
v=[(1 if (z>>6).bit_count()<=1 else -1) if z%64==0 else b[z%64] for z in range(512)]
p=spectrum(v); H=entropy(p)
expected=combine((F(385,32),{2:F(1)}),(-F(2401,1024),logq(F(7))),(-F(1575,2048),logq(F(15))))
check(not combine((1,H),(-1,expected)))
one_margin=combine((3,{2:F(1)}),(-1,H),(-1,cap))
two_margin=combine((3,{2:F(1)}),(-1,H),(-2,cap))
check(bounds(one_margin)[0]>F(363150,10**6))
check(bounds(two_margin)[0]>F(170505,10**6))
policy_rows=[]
for j in range(9):
    cs,ps,r,E0,R0=query(v,p,j)
    first=[reset(pc,r) for pc in ps]
    for k in range(9):
        if k==j:continue
        jj=k if k<j else k-1
        W=E0; refund=R0; tax=combine((F(1,2),first[0][1]),(F(1,2),first[1][1])); terminal={}
        for s in (0,1):
            gs,pg,r2,E1,R1=query(cs[s],first[s][0],jj)
            W=combine((1,W),(F(1,2),E1)); refund=combine((1,refund),(F(1,2),R1))
            for t in (0,1):
                q2,e2=reset(pg[t],r2)
                tax=combine((1,tax),(F(1,4),e2))
                terminal=combine((1,terminal),(F(1,4),ce(pg[t],q2)))
        bill=combine((1,W),(1,terminal))
        check(not combine((1,bill),(-1,H),(-1,tax),(1,refund)))
        check(positive(combine((1,H),(2,cap),(-1,bill))))
        check(bounds(combine((3,{2:F(1)}),(-1,bill)))[0]>F(170505,10**6))
        policy_rows.append({'first':j,'second':k,'bill':display(bill),'signed_reset_tax':display(tax),'conditional_KL_refund':display(refund)})
        check(time.perf_counter()-start<60)

# Actual Maj5: both children are nonconstant, full-support, nonflat.
maj=[1 if z.bit_count()<=2 else -1 for z in range(32)]
mp=spectrum(maj); cs,ps,r,B,R=query(maj,mp,0)
check(all(len(set(c))==2 for c in cs))
check(all(pc==r for pc in ps))
check(Counter(r)==Counter({F(9,64):6,F(1,64):10}))
check(not B and not R)
check(inf(maj,0)==F(3,8))
I=sum(inf(maj,j) for j in range(5)); check(I==F(15,8))
witnesses=[]
for m in [8,16,32,64,128]:
    q=[F(1,2**m)]+[F(2**m-1,15*2**m)]*15
    check(sum(q)==1 and min(q)>0 and len(set(q))==2)
    fresh=ce(ps[0],q); old=ce(ps[0],r)
    tax=combine((1,fresh),(-1,old))
    bill=combine((1,B),(F(1,2),fresh),(F(1,2),ce(ps[1],r)))
    check(not combine((1,bill),(-1,entropy(mp)),(-F(1,2),tax)))
    check(bounds(bill)[0]>=F(9*m,128))
    if m==128:
        check(bounds(bill)[0]>4*I)
        check(F(9*m,128)>4*I)
    # Fixed-reference reset cap is reached by the appropriate character.
    ratios=[x/y for x,y in zip(r,q)]; maximum=max(ratios)
    for t in range(16):
        character=[-1 if (z&t).bit_count()%2 else 1 for z in range(16)]
        cp=spectrum(character); cost=combine((1,ce(cp,q)),(-1,ce(cp,r)))
        check(not combine((1,cost),(-1,logq(r[t]/q[t]))))
        check(not combine((1,logq(maximum)),(-1,cost)) or bounds(combine((1,logq(maximum)),(-1,cost)))[0]>=0)
    witnesses.append({'m':m,'full_bill_one_child_reset':display(bill),'influence':str(I),'original_rate4_quota':str(4*I),'reference_independent_lower_bill':str(F(9*m,128))})

out={'status':'PASS','assertions':assertions,'policies':len(policy_rows),'witnesses':witnesses,'root_entropy':display(H),'one_frontier_guaranteed_margin':display(one_margin),'two_frontier_guaranteed_margin':display(two_margin),'certified_two_frontier_margin_lower':'170505/1000000','two_reset_policies':policy_rows,'elapsed_seconds':time.perf_counter()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic':'Fraction/log-linear identities and rigorous rational40-term atanh intervals; logarithmic atoms need not be prime'}
(run/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({k:out[k] for k in ['status','assertions','policies','elapsed_seconds','one_frontier_guaranteed_margin','two_frontier_guaranteed_margin','witnesses']},indent=2))
