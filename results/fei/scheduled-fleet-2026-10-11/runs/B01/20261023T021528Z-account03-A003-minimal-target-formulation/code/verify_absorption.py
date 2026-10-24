from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib

R=Path(__file__).resolve().parents[1]
START=time.perf_counter(); ASSERTS=0
COUNTS={'boolean_paths':0,'generic_candidates':0,'generic_admissible':0,'full_ledgers':0,'retained_nonconstant_siblings':0,'repeated_return_paths':0}

def ck(x):
    global ASSERTS
    ASSERTS+=1
    if not x: raise AssertionError(ASSERTS)
    if time.perf_counter()-START>55: raise TimeoutError('frozen 55 second maximum')

def marg(q,j):
    ans=[F(0)]*(len(q)//2)
    for t,x in enumerate(q): ans[(t&((1<<j)-1))|((t>>(j+1))<<j)]+=x
    return ans

def restrict(f,j,bit):
    return [f[(x&((1<<j)-1))|((x>>j)<<(j+1))|(bit<<j)] for x in range(len(f)//2)]

def spec(f):
    q=list(f);h=1
    while h<len(q):
        for a in range(0,len(q),h*2):
            for b in range(a,a+h): x,y=q[b],q[b+h];q[b],q[b+h]=x+y,x-y
        h*=2
    return [F(x,len(q))**2 for x in q]

def cal(q,p):
    if p==1:return [F(1)]+[F(0)]*(len(q)-1)
    if q[0]==1: raise ValueError('inadmissible nonconstant endpoint')
    return [p]+[(1-p)*x/(1-q[0]) for x in q[1:]]

def ln_interval(q):
    z=(q-1)/(q+1);term=z;low=F(0)
    for k in range(28): low+=2*term/(2*k+1);term*=z*z
    return low,low+2*term/(57*(1-z*z))

LN2=ln_interval(F(2))
@lru_cache(None)
def log(q):
    ck(q>0);k=q.numerator.bit_length()-q.denominator.bit_length();z=q/F(2)**k
    if z<1:z*=2;k-=1
    ck(1<=z<2)
    l,u=ln_interval(z);scale=1<<80
    return F((scale*(k+l/LN2[1])).__floor__(),scale),F((scale*(k+u/LN2[0])).__ceil__(),scale)

def add(a,b): return a[0]+b[0],a[1]+b[1]
def mul(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def sub(a,b): return add(a,mul(-1,b))
def ce(p,q):
    a=(F(0),F(0))
    for x,y in zip(p,q):
        if x: a=add(a,mul(-x,log(y)))
    return a

def generic():
    for a in range(5):
        for b in range(5-a):
            s=[F(a,4),F(b,4),F(4-a-b,4)]
            for x in [F(0),F(1,2),F(1)]:
                for y in [F(0),F(1,2),F(1)]:
                    def M(q):return [q[0]+x*q[1]+y*q[2],(1-x)*q[1]+(1-y)*q[2]]
                    for p in [F(k,4) for k in range(5)]:
                        for r in [F(k,4) for k in range(5)]:
                            COUNTS['generic_candidates']+=1
                            # p=1,r<1 is not a physical constant-parent descendant.
                            if (s[0]==1 and p<1) or (p==1 and r<1):continue
                            old=M(cal(s,p));direct=M(s)
                            if r<1 and (old[0]==1 or direct[0]==1):continue
                            ck(cal(old,r)==cal(direct,r));COUNTS['generic_admissible']+=1

def ledger(f,source,current,depth=0,history=()):
    p=spec(f)
    # Every return uses the ORIGINAL source marginal; compare to current calibration.
    do_reset=(depth>0 and (history[-1]==0 or depth==3))
    if do_reset:
        new=cal(source,p[0]);ck(new==cal(current,p[0]));current=new
        if depth>=2 and history[-2]==0:COUNTS['repeated_return_paths']+=1
    # Stop immediately in the untouched root sibling and in each unreset
    # second-query sibling: their full nonconstant terminal CE is retained.
    if depth==3 or history==(1,) or (depth==2 and history[-1]==1):return ce(p,current)
    j=(sum(history)+depth)%(3-depth)
    mp=marg(p,j);mq=marg(current,j);ms=marg(source,j)
    B=sub(ce(p,p),ce(mp,mp))
    kids=[]
    for bit in [0,1]:
        child=restrict(f,j,bit)
        if depth==0 and bit==1 and len(set(child))==2:COUNTS['retained_nonconstant_siblings']+=1
        kids.append(ledger(child,ms,mq,depth+1,history+(bit,)))
    return add(B,mul(F(1,2),add(*kids)))

def main():
    frozen=json.loads((R/'FROZEN_SPEC.json').read_text(encoding='utf-8'));ck(frozen['search_started'] is False)
    generic();worst_upper=F(-10);worst_mask=None
    for mask in range(256):
        f=[1 if mask>>x&1 else -1 for x in range(8)];p=spec(f)
        ck(sum(p)==1)
        uniform=[F(1,8)]*8
        mix=[(x+y)/2 for x,y in zip(p,uniform)]
        sources=[uniform,[F(k,36) for k in range(1,9)],mix,cal(mix,p[0])]
        for si,s in enumerate(sources):
            ck(sum(s)==1);root=cal(s,p[0])
            for j in range(3):
                sm=marg(s,j);old=marg(root,j)
                for bit in [0,1]:
                    child=restrict(f,j,bit);pc=spec(child);fresh=cal(sm,pc[0])
                    ck(fresh==cal(old,pc[0]));ck(sum(fresh)==1)
                    for k in range(2):
                        inherited=marg(fresh,k);direct=marg(sm,k)
                        for bit2 in [0,1]:
                            grand=restrict(child,k,bit2);pg=spec(grand)
                            ck(cal(inherited,pg[0])==cal(direct,pg[0]));COUNTS['boolean_paths']+=1
            bill=ledger(f,s,s);c=ce(p,s);gap=sub(bill,c)
            # Exact intervals can straddle equality; certify <= using rational margin
            # except all identities at zero-cost constants, which are checked structurally.
            if c==(F(0),F(0)):ck(bill==(F(0),F(0)))
            else:ck(gap[1]<=0)
            COUNTS['full_ledgers']+=1
            if gap[1]>worst_upper:worst_upper=gap[1];worst_mask=[mask,si]
    ck(COUNTS['generic_candidates']==3375);ck(COUNTS['boolean_paths']==24576);ck(COUNTS['full_ledgers']==1024)
    ck(COUNTS['retained_nonconstant_siblings']>0);ck(COUNTS['repeated_return_paths']>0)
    result={'status':'EXACT_PASS','helper_version':frozen['helper_version'],'assertions':ASSERTS,'counts':COUNTS,'runtime_seconds':time.perf_counter()-START,'worst_ledger_minus_initial_CE_upper':str(worst_upper),'worst_mask_source':worst_mask,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite exact evidence; universal identity and stopping-frontier theorem are proved separately in DERIVATION.md.'}
    (R/'out/VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
