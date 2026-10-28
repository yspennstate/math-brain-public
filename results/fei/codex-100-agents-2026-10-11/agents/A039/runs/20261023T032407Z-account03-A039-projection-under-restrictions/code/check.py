"""A039 coherent a-child factor-reset v1. Exact algebra; bounded log signs."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, sys, time, math

R=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
START=time.monotonic(); CHECKS=0; SCALE=1<<130
def ck(value, label):
    global CHECKS
    CHECKS+=1
    if not value: raise AssertionError(label)
    if time.monotonic()-START>55: raise RuntimeError('frozen55secondguard')
def floor(x): return x.numerator//x.denominator
def ceil(x): return -floor(-x)
class IV:
    def __init__(self,lo=0,hi=None): self.lo,self.hi=lo,lo if hi is None else hi
    def __add__(self,b):
        if not isinstance(b,IV): b=iv(b)
        return IV(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,b): return self+-b
    def __mul__(self,b):
        b=F(b); a,c=self.lo*b,self.hi*b
        return IV(floor(min(a,c)),ceil(max(a,c)))
    __rmul__=__mul__
    def json(self): return [str(F(self.lo,SCALE)),str(F(self.hi,SCALE))]
def iv(x):
    a=F(x)*SCALE
    return IV(floor(a),ceil(a))
def atanh(z):
    a=sum((z**(2*k+1)/F(2*k+1) for k in range(28)),F(0))*2
    tail=2*z**57/(57*(1-z*z))
    return a,a+tail
LN2=atanh(F(1,3))
@lru_cache(None)
def log2(x):
    x=F(x)
    assert x>0
    k=0
    while x<1: x*=2;k-=1
    while x>=2: x/=2;k+=1
    a,b=atanh((x-1)/(x+1))
    return IV(floor((a/LN2[1]+k)*SCALE),ceil((b/LN2[0]+k)*SCALE))
def KL(p,q):
    return sum((log2(a/b)*a for a,b in zip(p,q) if a),IV())
def entropy(p): return -sum((log2(a)*a for a in p if a),IV())
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def amp(table):
    out=list(table);n=len(out)
    width=1
    while width<n:
        for j in range(0,n,2*width):
            for k in range(width):
                a,b=out[j+k],out[j+k+width]
                out[j+k],out[j+k+width]=a+b,a-b
        width*=2
    return [F(x,n) for x in out]
def spectrum(table): return [a*a for a in amp(table)]
def influence(table):
    n=(len(table)-1).bit_length()
    return sum(F(sum(table[x]!=table[x^(1<<j)] for x in range(len(table))),len(table)) for j in range(n))
def restrict(table,j,y):
    return [table[(k&((1<<j)-1))|((k>>j)<<(j+1))|(y<<j)] for k in range(len(table)//2)]
def erase(a,j):
    return [a[(k&((1<<j)-1))|((k>>j)<<(j+1))]+a[(k&((1<<j)-1))|((k>>j)<<(j+1))|(1<<j)] for k in range(len(a)//2)]
def channel(table,ref,j):
    p=spectrum(table);pb=erase(p,j);rb=erase(ref,j)
    children=[];outs=[];kernels=[]
    for y in [0,1]:
        t=restrict(table,j,y);py=spectrum(t)
        k=[a/(2*b) if b else F(1,2) for a,b in zip(py,pb)]
        raw=[a*b for a,b in zip(rb,k)];r=sum(raw)
        ck(r>0,'positive outcome normalizer')
        ry=[a/r for a in raw]
        ck(sum(ry)==1 and sum(py)==1,'normalized child')
        children.append((t,py,ry));outs.append(r);kernels.append(k)
    ck(sum(outs)==1,'reference outcome mass')
    ck(all(a+b==1 for a,b in zip(*kernels)),'common physical kernel')
    return children,outs,pb,rb,kernels
def factor(w,active=True,beta=F(5,6)):
    if not active or w==0: return [F(1)]+[F(0)]*((1<<w)-1)
    p=[F((1-2*F(1,1<<w))**2)]+[F(4,1<<(2*w))]*((1<<w)-1)
    if w==1:return p
    q=[p[0]]+[beta*a for a in p[1:]]
    q[-1]+=(1-beta)*(1-p[0])
    ck(sum(q)==1 and q[0]==p[0],'factor normalized and empty calibrated')
    return q
def tensor(arrays):
    q=[F(1)]
    for a in arrays:q=[x*y for y in a for x in q]
    return q
def point(x,w):return -1 if x&((1<<w)-1)==0 else 1
def coretable(widths,sign=1):
    n=sum(widths);out=[]
    for x in range(1<<n):
        val=sign;off=0
        for w in widths:val*=point(x>>off,w);off+=w
        out.append(val)
    return out
def selectortable(widths,epsilon=1,sign=1):
    core=coretable(widths,sign)
    return [epsilon if x%2==0 else core[x>>1] for x in range(2*len(core))]
def lift(table,q):
    p=spectrum(table)
    ck(len(p)==2*len(q),'lift dimension')
    out=[p[i] if i>>1==0 else q[i>>1]/4 for i in range(len(p))]
    ck(sum(out)==1,'lift normalized')
    return out
def ratios(q,p):return [a/b if b else F(1) for a,b in zip(q,p)]
def runlocal(w,sp,eps,sign):
    widths=[w]+sp;table=selectortable(widths,eps,sign);p=spectrum(table)
    pv=factor(w,beta=F(1));pu=tensor([factor(v,beta=F(1)) for v in sp])
    qv=factor(w);qu=tensor([factor(v) for v in sp]);q=tensor([qv,qu]);ref=lift(table,q)
    l=ratios(qv,pv);s=ratios(qu,pu)
    ll=[l[(i>>1)&((1<<w)-1)] for i in range(len(p))]
    ss=[s[i>>(w+1)] for i in range(len(p))]
    ck(all(a==b*c*d for a,b,c,d in zip(ref,p,ll,ss)),'exact parent likelihood factorization')
    B=[a*b for a,b in zip(p,ll)];C=[a*b for a,b in zip(p,ss)]
    ck(sum(B)==1 and sum(C)==1,'single-likelihood references normalized')
    children,outs,pb,rb,k=channel(table,ref,1)
    Bbar=erase(B,1);Cbar=erase(C,1)
    bb=ratios(Bbar,pb);sss=[s[i>>w] for i in range(len(pb))]
    ck(all(a==b*c for a,b,c in zip(rb,Bbar,sss)),'erased spectator factorization')
    ck(all(dot(Cbar,ky)==F(1,2) for ky in k),'baseline outcome exactly fair')
    ck(all(r>=F(5,12) for r in outs),'actual outcome lower bound')
    ck(all(a>=F(5,6)*b for a,b in zip(ref,C)),'pointwise domination by paid beta')
    sigma=IV();newterm=IV();factorKL=IV();rows=[]
    for y,(t,py,old) in enumerate(children):
        qvy=factor(w-1,y==0,F(4,5));pvy=factor(w-1,y==0,F(1))
        new=lift(t,tensor([qvy,qu]));ln=ratios(qvy,pvy)
        lnfull=[ln[(i>>1)&((1<<(w-1))-1)] for i in range(len(py))]
        ck(all(a==b*c*d/(2*outs[y]) for a,b,c,d in zip(old,py,sss,bb)),'exact inherited likelihood with outcome normalizer')
        ck(all(a==b*c*d for a,b,c,d in zip(new,py,sss,lnfull)),'exact fresh likelihood retains spectators')
        # These two pointwise identities and exact mean-child identity prove (4).
        ck(all((children[0][1][i]+children[1][1][i])/2==pb[i] for i in range(len(pb))),'mean physical spectrum equals erasure')
        # Compare coefficients of each log in the derived expression, before evaluating signs.
        for i,a in enumerate(py):
            if a:ck(old[i]/new[i]==bb[i]/(2*outs[y]*lnfull[i]),'exact old/new likelihood quotient')
        d=KL(py,new)-KL(py,old);sigma+=d*F(1,2)
        factorKL+=KL(pvy,qvy)*F(1,4)
        newterm+=sum((-log2(lnfull[i])*a for i,a in enumerate(py) if a),IV())*F(1,2)
    # Extra1/2 for selector then1/2 for outcome.
    er=KL(pb,Bbar);o=KL([F(1,2)]*2,outs);rhs=factorKL-er+o
    ck(max(sigma.lo,rhs.lo)<=min(sigma.hi,rhs.hi),'interval consistency of exact identity (not equality proof)')
    ck(max(newterm.lo,factorKL.lo)<=min(newterm.hi,factorKL.hi),'factor coefficient consistency')
    cap=log2(F(5,4))*F(1,4)+log2(F(36,35))*F(1,2)
    ck(sigma.hi<=cap.hi and sigma.hi<SCALE//8,'rigorous local reset upper bound')
    ck(o.hi<iv(F(1,24)).lo,'rigorous coherent outcome correction cap')
    return {'w':w,'spectators':sp,'epsilon':eps,'core_sign':sign,'sigma':sigma.json(),'erasure_correction':er.json(),'outcome_correction':o.json(),'outcomes':list(map(str,outs))}
def root_table(m,r):
    h=coretable([r]*m)
    return [(-1 if z&2 else 1) if not z&1 else (h[z>>3] if z&4 else 1) for z in range(1<<(3+m*r))]
def root_ref(table,m,r):
    p=spectrum(table);q=tensor([factor(r,beta=F(7,8))]*m)
    out=[p[i] if i>>3==0 else (q[i>>3]/16 if i&7 in [0,1,4,5] else F(0)) for i in range(len(p))]
    ck(sum(out)==1,'original root reference normalized')
    return out
def runroot(m,r,policy):
    table=root_table(m,r);p=spectrum(table);q=root_ref(table,m,r)
    A0=KL(p,q);H0=entropy(p);I0=influence(table)
    ck(I0==sum(F(i.bit_count())*a for i,a in enumerate(p)),'root edge/spectral influence equality')
    bch,_,_,_,_=channel(table,q,2)
    terminals=[(F(1,2),bch[0][0],bch[0][2])];sigma1=IV();sigma2=IV()
    ach,_,_,_,_=channel(bch[1][0],bch[1][2],1)
    old_second=[]
    for a,(t,py,old) in enumerate(ach):
        ref=lift(t,tensor([factor(r)]*m))
        sigma1+=(KL(py,ref)-KL(py,old))*F(1,4)
        if policy=='both' or a==0:
            dch,outs,_,_,_=channel(t,ref,1)
            for y,(td,pd,od) in enumerate(dch):
                nr=lift(td,tensor([factor(r-1,y==0,F(4,5))]+[factor(r)]*(m-1)))
                sigma2+=(KL(pd,nr)-KL(pd,od))*F(1,8)
                terminals.append((F(1,8),td,nr))
        else:terminals.append((F(1,4),t,ref))
    ck(sum(a for a,_,_ in terminals)==1,'complete physical terminal mass')
    Hf=sum((entropy(spectrum(t))*w for w,t,ref in terminals),IV())
    If=sum(w*influence(t) for w,t,ref in terminals)
    Kf=sum((KL(spectrum(t),ref)*w for w,t,ref in terminals),IV())
    S=iv(4*If)-Hf;e=H0-Hf-iv(4*(I0-If));bill=A0+e+sigma1+sigma2
    paid=S-IV(max(0,bill.lo),max(0,bill.hi))-iv(F(1,4))
    ck(S.lo>=SCALE,'actual terminal surplus >=1')
    ck(sigma2.hi<SCALE//16,'global actual second reset <1/16')
    ck(paid.lo>11*SCALE//16,'same original owner retains >11/16')
    ck((iv(4*I0)-H0-A0-sigma1).lo>SCALE,'same original headroom after first reset >1')
    return {'m':m,'r':r,'policy':policy,'sigma1':sigma1.json(),'sigma2':sigma2.json(),'old_booking':'1/4','complete_terminal_KL':Kf.json(),'terminal_entropy':Hf.json(),'terminal_influence':str(If),'S':S.json(),'remaining':paid.json(),'terminal_count':len(terminals)}
def main():
    ck(5**3<2*4**3,'exact new factor logarithm certificate')
    ck(36**12<2*35**12,'exact outcome logarithm certificate')
    ck(8**5<2*7**5,'original source logarithm certificate')
    ck(6**40<2**11*5**40,'first reset logarithm certificate')
    local=[]
    for w in ([3] if PILOT else [2,3,4,5]):
        for sp in ([[],[2],[1]] if PILOT else [[],[2],[3],[1],[2,1]]):
            for eps in [1,-1]:
                for sign in [1,-1]:local.append(runlocal(w,sp,eps,sign))
    roots=[]
    for m,r in ([(1,3)] if PILOT else [(1,3),(2,2),(2,3),(3,2)]):
        for policy in ['both','a0_only']:roots.append(runroot(m,r,policy))
    out={'status':'PASS','helper_version':'A039-coherent-a-factor-reset-v1','pilot':PILOT,'checks':CHECKS,'runtime_seconds':time.monotonic()-START,'local_parent_count':len(local),'root_policy_count':len(roots),'local':local,'roots':roots,'equality_method':'Exact Fraction pointwise likelihood identities and exact child/erasure probabilities; interval overlap is only a consistency check.','full_FEI':'OPEN'}
    path=R/'out'/('PILOT.json' if PILOT else 'CHECK.json');path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ['local','roots']}))
if __name__=='__main__': main()
