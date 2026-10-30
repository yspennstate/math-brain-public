"""A023-separator-v1: independent exact witness and separator reserve."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,time
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();CHECKS=0;SIGNS={}
def ck(x):
    global CHECKS
    assert x
    CHECKS+=1
def cap():
    if time.perf_counter()-START>60:raise RuntimeError('frozen 60 second pilot cap')
@lru_cache(None)
def factors(n):
    out=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return tuple(out)
def term(o,n,c):
    if not n or not c:return
    for p,e in factors(n):
        o[p]=o.get(p,0)+c*e
        if not o[p]:del o[p]
def combine(*args):
    o={}
    for scale,v in args:
        for p,c in v.items():
            o[p]=o.get(p,F(0))+scale*c
            if not o[p]:del o[p]
    return o
@lru_cache(None)
def walsh(v):
    w=list(v);s=1
    while s<len(w):
        for j in range(0,len(w),2*s):
            for i in range(j,j+s):a,b=w[i],w[i+s];w[i],w[i+s]=a+b,a-b
        s*=2
    return tuple(w)
@lru_cache(None)
def entropy(v):
    N=len(v);o={}
    for w in walsh(v):
        if w:term(o,N*N,w*w);term(o,w*w,-w*w)
    return {p:F(c,N*N) for p,c in o.items()}
@lru_cache(None)
def influence(v):
    N=len(v);n=N.bit_length()-1
    return F(sum(v[x]!=v[x^(1<<i)] for x in range(N) for i in range(n)),N)
def ln_series(x,T):
    z=(x-1)/(x+1);v=z;s=F(0)
    for j in range(T):s+=v/F(2*j+1);v*=z*z
    lo=2*s;hi=lo+2*v/F(2*T+1)/(1-z*z)
    return lo,hi
@lru_cache(None)
def log_bound(p,T):
    k=p.bit_length()-1;a,b=ln_series(F(p,1<<k),T);l,h=ln_series(F(2),T)
    return k+a/h,k+b/l
def sign(v):
    key=tuple(sorted(v.items()))
    if key in SIGNS:return SIGNS[key]['bad']
    if not v:SIGNS[key]={'vector':{},'bad':False,'exact_equal':True};return False
    for T in [24,48]:
        lo=hi=F(0)
        for p,c in v.items():
            a,b=log_bound(p,T);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
        if lo>0 or hi<0:
            SIGNS[key]={'vector':{str(p):str(c) for p,c in v.items()},'bad':lo>0,'lower':str(lo),'upper':str(hi),'terms':T};return lo>0
    raise AssertionError('unresolved sign')
@lru_cache(None)
def node(v):
    cap();N=len(v);w=walsh(v);ck(sum(x*x for x in w)==N*N)
    d=F(sum(w[i]**2 for i in range(1,N,2)),N*N);B={};J={};mu=F(0)
    for i in range(0,N,2):
        A,D=w[i]**2,w[i+1]**2
        term(B,A+D,A+D);term(B,A,-A);term(B,D,-D)
        mm=min(A,D);mu+=F(mm,N*N);term(J,A+D,mm);term(J,mm,-mm)
    B={p:F(c,N*N) for p,c in B.items()};J={p:F(c,N*N) for p,c in J.items()}
    gap=combine((1,B),(-4,{2:d}));bad=sign(gap)
    a,b=v[::2],v[1::2];cost=influence(tuple(x*y for x,y in zip(a,b)))/2
    ck(influence(v)==d+(influence(a)+influence(b))/2);ck(mu<=d)
    return d,B,J,mu,bad,cost,gap
def controller_fixed(v,c):
    block=1<<c
    return c==0 or all(all(t==v[j] for t in v[j:j+block]) for j in range(0,len(v),block))
@lru_cache(None)
def stopping(v,c):
    if controller_fixed(v,c):return F(0),F(0),influence(v),entropy(v),{},F(0),F(0)
    d,B,J,mu,bad,cost,gap=node(v);a=stopping(v[::2],c-1);b=stopping(v[1::2],c-1)
    return ((cost if bad else F(0))+(a[0]+b[0])/2,d+(a[1]+b[1])/2,(a[2]+b[2])/2,combine((F(1,2),a[3]),(F(1,2),b[3])),combine((1,J),(F(1,2),a[4]),(F(1,2),b[4])),mu+(a[5]+b[5])/2,cost+(a[6]+b[6])/2)
def reorder(v,order):return tuple(v[sum(((x>>j)&1)<<i for j,i in enumerate(order))] for x in range(len(v)))
def bent_core(k):
    b=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<k))
    h=b+tuple(-v if x==0 else v for x,v in enumerate(b))
    return h+tuple(-v for v in h)
def build(L,R,T,g):
    # positive point literals: W starts at bit0, separator X at bit L
    WW=list(range(L));XX=[L];UU=list(range(L+1,L+1+R));VV=list(range(L+1+R,L+1+R+T));nc=L+1+R+T
    A=[]
    for z in range(1<<nc):
        w=all((z>>i)&1 for i in WW);x=(z>>L)&1;u=all((z>>i)&1 for i in UU);v=all((z>>i)&1 for i in VV)
        A.append(int((x and(u or v)) or (w and u and v)))
    f=tuple(g[y] if A[z] else 1 for y in range(len(g)) for z in range(1<<nc))
    return f,tuple(A),XX+WW+UU+VV,list(range(nc,nc+(len(g)-1).bit_length()))
def main():
    rows=[]
    cases=[(L,R,T,(1,-1),'dictator') for L,R,T in itertools.product([1,2,3],repeat=3)]
    cases +=[(L,R,T,bent_core(4),'balanced-bent4-flip') for L,R,T in itertools.product([1,2],repeat=3)]
    for L,R,T,g,label in cases:
        cap();f,A,order,coreorder=build(L,R,T,g);nc=len(order)
        p,q,r=F(1,1<<L),F(1,1<<R),F(1,1<<T);beta=q+r-q*r;eta=p*q*r;pi=(beta+eta)/2;e=beta-eta;d=e/2
        ja0=(L+R+T)*eta;ja1=R*q*(1-r)+T*r*(1-q);rem=(ja0+ja1)/2;jctrl=d+rem
        ck(F(sum(A),len(A))==pi);ck(influence(tuple(1-2*a for a in A))/2==jctrl)
        v=reorder(f,order+coreorder);nd=node(v);ck(nd[0]==d);ck(nd[5]==rem+e*influence(g)/2)
        tr=stopping(v,nc);ck(tr[1]==jctrl);ck(tr[2]==pi*influence(g));ck(tr[3]==combine((pi,entropy(g))))
        ck(tr[0]==(nd[5] if nd[4] else 0));ck(tr[0]<=rem+pi*influence(g));ck(influence(f)==jctrl+pi*influence(g))
        # The reserve's downstream sum has no bad node, exactly.
        ck((stopping(v[::2],nc-1)[0]+stopping(v[1::2],nc-1)[0])/2==0)
        row={'L':L,'R':R,'T':T,'core':label,'pi':str(pi),'control_I':str(jctrl),'remaining_control_reserve':str(rem),'root_d':str(d),'root_bad':nd[4],'root_face_credit':str(nd[5]),'terminal_I':str(tr[2]),'terminal_H':{str(p):str(c) for p,c in tr[3].items()},'bad_credit':str(tr[0]),'bad_credit_over_I':str(tr[0]/influence(f)),'J_tree':{str(p):str(c) for p,c in tr[4].items()},'minority_mass_sum':str(tr[5])}
        rows.append(row);(ROOT/'out/results.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
    # Independently replay A021's original five-bit witness, x0 first.
    f,A,order,coreorder=build(1,1,1,(1,-1));n=node(f)
    expected={2:F(192,256),3:F(-432,256),5:F(60,256),7:F(-98,256),13:F(52,256),41:F(82,256)}
    ck(n[6]==expected);ck(n[4]);ck(n[0]==F(1,16));ck(F(sum(A),len(A))==F(7,16));ck(influence(tuple(1-2*a for a in A))/2==F(3,4))
    ck(n[5]==F(1,4))
    witness={'controller':'x1x2 OR x1x3 OR x0x2x3','pi':'7/16','controller_J':'3/4','bad_x0_d':'1/16','bad_x0_face_credit':'1/4','gap_log_vector':{str(p):str(c) for p,c in n[6].items()},'fixed_order_bad_credit':str(stopping(f,4)[0]),'separator_order_bad_credit':str(stopping(reorder(f,order+coreorder),4)[0]),'gap_certificate':SIGNS[tuple(sorted(n[6].items()))]}
    (ROOT/'out/witness.json').write_text(json.dumps(witness,indent=2),encoding='utf-8')
    # Balanced-core transfer for the witness, independently of controller spelling.
    for g in [(1,-1),bent_core(4)]:
        f,_,_,_=build(1,1,1,g);n2=node(f);ck(n2[1]==n[1]);ck(n2[0]==n[0]);ck(n2[6]==n[6])
    cc=F(81,56);ck(5+2*cc<8);ck(5+3*cc<10)
    (ROOT/'out/sign_certificates.json').write_text(json.dumps(list(SIGNS.values()),indent=2),encoding='utf-8')
    out={'status':'PASS','roots':len(rows),'checks':CHECKS,'unique_spectral_nodes':node.cache_info().currsize,'sign_certificates':len(SIGNS),'root_bad_count':sum(x['root_bad'] for x in rows),'policy_max_bad_credit_over_I':str(max(F(x['bad_credit_over_I']) for x in rows)),'elapsed_seconds':time.perf_counter()-START,'witness_review':'HOLDS at witness/balanced-control-transfer scope only; whole A021 claim not independently accepted'}
    (ROOT/'out/validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
