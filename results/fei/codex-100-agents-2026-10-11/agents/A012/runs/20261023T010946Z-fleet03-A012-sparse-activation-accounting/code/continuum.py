from pathlib import Path
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
S=1<<80;DEN=128;checks=0
M=[[(-1 if s==0 else 1)*(-1)**((s&t).bit_count()%2) for s in range(8)] for t in range(8)]
A=[6]+[-2]*7
def cd(a,b):return -(-a//b)
@lru_cache(maxsize=60000)
def ln(n,d):
    assert d<=n<2*d
    lo=(n-d)*S//(n+d);hi=cd((n-d)*S,n+d)
    tl=lo*lo//S;th=cd(hi*hi,S);pl,ph=lo,hi;L=H=0
    for k in range(24):
        L+=2*pl//(2*k+1);H+=cd(2*ph,2*k+1)
        pl=pl*tl//S;ph=cd(ph*th,S)
    return L,H+cd(18*S,8*49*3**49)
# ln2 is evaluated with a representation strictly below2 for the cached helper.
def ln2():
    u=S//3;v=cd(S,3);pl,ph=u,v;ul=u*u//S;uh=cd(v*v,S);L=H=0
    for k in range(24):
        L+=2*pl//(2*k+1);H+=cd(2*ph,2*k+1);pl=pl*ul//S;ph=cd(ph*uh,S)
    return L,H+cd(18*S,8*49*3**49)
LL,HH=ln2()
@lru_cache(maxsize=60000)
def loghi(n,d):
    assert n>=d>0
    k=0
    while n>=2*d:d*=2;k+=1
    return k*S+cd(ln(n,d)[1]*S,LL)
def slopes(lo,hi):
    out=[];mid=[lo[i]+hi[i] for i in range(8)]
    for t in range(8):
        b=sum(M[t][i]*mid[i] for i in range(8));x=(A[t]*2*DEN-b)**2;y=b*b
        if not y:nu,de=1,4096
        elif not x:nu,de=4095,4096
        else:nu,de=y,x+y
        lam=loghi(de,de-nu);mu=loghi(de,nu)
        assert lam+mu>=2*S
        out.append((lam,mu,lam+mu-2*S))
    return out
def corner_bound(lo,hi):
    sl=slopes(lo,hi);w=[hi[i]-lo[i] for i in range(8)]
    H=[[sum(sl[t][2]*M[t][i]*M[t][j] for t in range(8)) for j in range(8)] for i in range(8)]
    L=[-2*DEN*sum(sl[t][0]*A[t]*M[t][i] for t in range(8))-16*DEN*S for i in range(8)]
    C=sum(sl[t][0]*(A[t]*DEN)**2 for t in range(8))
    val=C+sum(L[i]*lo[i] for i in range(8))+sum(H[i][j]*lo[i]*lo[j] for i in range(8) for j in range(8))
    lin=[w[i]*(L[i]+2*sum(H[i][j]*lo[j] for j in range(8)))+H[i][i]*w[i]*w[i] for i in range(8)]
    pair=[[2*H[i][j]*w[i]*w[j] if i!=j else 0 for j in range(8)] for i in range(8)]
    grad=lin[:];bits=[0]*8;mx=val
    for k in range(1,256):
        bit=(k&-k).bit_length()-1;sgn=1-2*bits[bit];val+=sgn*grad[bit];bits[bit]^=1
        for j in range(8):grad[j]+=sgn*pair[j][bit]
        if val>mx:mx=val
    return -mx
def seed(job):
    lo=[0]*8
    if job in (1,2):lo[1]=DEN//2
    if job==2:lo[2]=DEN//2
    if job in (3,4):lo[0]=DEN//2
    if job==4:lo[1]=DEN//2
    return lo,[x+DEN//2 for x in lo]
def run(job):
    t0=time.perf_counter();stack=[seed(job)];leaves=[];pruned=[];splits=[];unresolved=[];visited=0
    while stack:
        if time.perf_counter()-t0>49 or visited>=50000:
            unresolved+=stack;break
        lo,hi=stack.pop();visited+=1
        if 4*sum(hi)<=DEN:pruned.append([lo,hi,'rare']);continue
        if 3*sum(lo)>=4*DEN:pruned.append([lo,hi,'moderate']);continue
        bound=corner_bound(lo,hi)
        if bound>0:leaves.append([lo,hi,str(bound)]);continue
        width=[hi[i]-lo[i] for i in range(8)];j=max(range(8),key=lambda i:width[i])
        if width[j]<=1:unresolved.append([lo,hi]);continue
        mid=(lo[j]+hi[j])//2;h=hi[:];h[j]=mid;l=lo[:];l[j]=mid
        splits.append([lo,hi,j]);stack.append((l,hi));stack.append((lo,h))
    out={'status':'PASS' if not unresolved else 'UNRESOLVED','job':job,'denominator':DEN,'visited':visited,'leaves':leaves,'pruned':pruned,'splits':splits,'unresolved':unresolved,'seconds':time.perf_counter()-t0,'log_cache':loghi.cache_info()._asdict()}
    (R/'out'/f'CONTINUUM_{job}.json').write_text(json.dumps(out,separators=(',',':'))+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('leaves','pruned','splits','unresolved')}),'counts',len(leaves),len(pruned),len(splits),len(unresolved),flush=True)
    loghi.cache_clear();ln.cache_clear()
if __name__=='__main__':
    for j in map(int,sys.argv[1:]):run(j)
