from pathlib import Path
from fractions import Fraction as Q
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import combinations
import sys,time,json,argparse
sys.dont_write_bytecode=True
import arithmetic as M
R=Path(__file__).resolve().parents[1];checks=0;deadline=0
def ck(c):
    global checks
    checks+=1
    if time.perf_counter()>deadline:raise TimeoutError('Frozen runtime exceeded')
    assert c,checks
def H(p):return M.add(*[(n,M.phi(x)) for x,n in Counter(p.values()).items()])
def sub(a,b):return M.add((1,a),(-1,b))
def bitsign(x):return -1 if x.bit_count()%2 else 1
def seedvals(n,m):return [1 if m>>x&1 else -1 for x in range(1<<n)]
def tensor(seed,n,t):
    out=[]
    for x in range(1<<(n*t)):
        v=1
        for j in range(t):v*=seed[(x>>(j*n))&((1<<n)-1)]
        out.append(v)
    return out
def greedy(D,b,r):
    cols=[1<<i for i in range(r)];tags=[]
    for _ in range(D):
        forbidden={0}
        for j in range(1,b):
            for group in combinations(cols,j):
                z=0
                for c in group:z^=c
                forbidden.add(z)
        ell=next(x for x in range(1<<r) if x not in forbidden)
        tags.append(ell);cols.append(ell)
    return tags
def tagdim(D,b):
    if b==1:return 1
    if b==3:return 3 if D==1 else 4
    return next(r for r in range(2,5) if (1<<r)-r-1>=D)
def code_index(s,D,tags):
    z=0
    for i,c in enumerate(tags):
        if s>>i&1:z^=c
    return s|(z<<D)
@lru_cache(maxsize=2048)
def measure(v):
    N=len(v).bit_length()-1;a=M.fwht(v);p=M.probabilities(a);ds=M.inf(p,N)
    return a,p,H(p),ds,sum(ds)
def physical_child(v,N,A,assignment):
    fixed={i:(assignment>>j)&1 for j,i in enumerate(A)};rest=[i for i in range(N) if i not in fixed];out=[]
    for y in range(1<<len(rest)):
        x=sum(z<<i for i,z in fixed.items())
        for j,i in enumerate(rest):x|=((y>>j)&1)<<i
        out.append(v[x])
    return tuple(out)
def rows(a,N,A):
    rest=[i for i in range(N) if i not in A];out=defaultdict(lambda:[Q(0)]*(1<<len(A)))
    for s,c in a.items():
        u=sum(((s>>i)&1)<<j for j,i in enumerate(A));z=sum(((s>>i)&1)<<j for j,i in enumerate(rest));out[z][u]=c
    return out
@lru_cache(maxsize=4096)
def collision(row):
    q=sum(x*x for x in row)
    if not q:return Q(0)
    physical=[sum(c*bitsign(u&x) for u,c in enumerate(row)) for x in range(len(row))]
    return (sum(x**4 for x in physical)/len(row)-q*q)/q
def frac(x,y):return x/y if y else Q(0)
def quartet(row):
    a,b,c,d=row;q=sum(x*x for x in row)
    if not q:return (Q(0),)*5
    ci=4*frac(a*a*b*b,a*a+b*b)+4*frac(c*c*d*d,c*c+d*d)
    cj=4*frac(a*a*c*c,a*a+c*c)+4*frac(b*b*d*d,b*b+d*d)
    pp=4*(a*d+b*c)**2/q
    mi=ci-4*(a*b+c*d)**2/q;mj=cj-4*(a*c+b*d)**2/q
    ck(mi>=0 and mj>=0)
    ck(collision(row)==ci+cj+pp-mi-mj)
    u=a*a+b*b;v=c*c+d*d
    ck(mi==frac(4*(a*b*v-c*d*u)**2,q*u*v))
    v=a*a+c*c;u=b*b+d*d
    ck(mj==frac(4*(a*c*u-b*d*v)**2,q*u*v))
    return ci,cj,pp,mi,mj
def fixture(seed,n,t,b):
    core=tensor(seed,n,t);D=n*t;r=tagdim(D,b);tags=greedy(D,b,r);N=D+r
    aa,sp,hh,sds,II=measure(tuple(core))
    coded=[]
    for x in range(1<<N):
        data=x&((1<<D)-1);z=x>>D
        for i,l in enumerate(tags):
            if (l&z).bit_count()%2:data^=1<<i
        coded.append(core[data])
    a,p,h,ds,I=measure(tuple(coded));expected={code_index(s,D,tags):c for s,c in aa.items()}
    ck(a==expected);ck(h==hh)
    ck(all(code_index(s,D,tags).bit_count()>b for s in range(1,1<<D)))
    ck(ds[:D]==sds);ck(I-II<=r*(1-sp.get(0,Q(0))))
    edit=list(coded);eta=edit[0];edit[0]*=-1;ea,ep,eh,eds,eI=measure(tuple(edit));epsilon=Q(1,1<<(N-1));pp=Q(1,1<<N)
    ck(all(ea.get(s,Q(0))==a.get(s,Q(0))-eta*epsilon for s in range(1<<N)))
    ck(len(ea)==1<<N);ck(sum(x<0 for x in edit)%2==1);ck(sum(x<0 for x in coded)%2==0)
    for i in range(N):
        ck(abs(eds[i]-ds[i])<=epsilon)
        ck(eds[i]==Q(sum(edit[x]!=edit[x^(1<<i)] for x in range(1<<N)),1<<N))
    ctotal=Q(0);refund_total=Q(0);blocks=0;childcount=0
    for size in range(1,b+1):
        mm=1<<size
        for A in combinations(range(N),size):
            blocks+=1;oldrows=rows(a,N,A);erows=rows(ea,N,A)
            ck(all(sum(v!=0 for v in row)<=1 for row in oldrows.values()))
            cc=Q(0)
            for z,row in erows.items():
                original=oldrows.get(z,[Q(0)]*mm);c=next((v for v in original if v),Q(0));q=c*c-2*eta*c*epsilon+mm*epsilon*epsilon
                exact=(mm-1)*epsilon*epsilon*(mm*epsilon-2*eta*c)**2/q
                ck(collision(tuple(row))==exact);ck(exact<=mm*mm*epsilon*epsilon);cc+=exact
                if size==2:
                    ci,cj,par,mi,mj=quartet(tuple(row));refund_total+=mi+mj
            ck(cc<=(1<<(size+2))*pp);ctotal+=cc
            chs=[]
            for assignment in range(mm):
                ch=measure(physical_child(coded,N,A,assignment));ech=measure(physical_child(edit,N,A,assignment));childcount+=1
                ck(ch[2]==h);ck(ch[4]==I-sum(ds[i] for i in A))
                chs.append(ech)
            avh=M.add(*[(Q(1,mm),ch[2]) for ch in chs]);avi=sum(ch[4] for ch in chs)/mm
            ck(avi==eI-sum(eds[i] for i in A))
            for K in [Q(0),Q(8,3)]:
                delta=sub(eh,((2,K*eI),));reserve=sub(((2,K*avi),),avh)
                ck(reserve==M.add((1,sub(eh,avh)),(-1,((2,K*sum(eds[i] for i in A)),)),(-1,delta)))
    ck(ctotal<=4*pp*sum(__import__('math').comb(N,j)*(1<<j) for j in range(1,b+1)))
    if b>=2:ck(refund_total<=16*__import__('math').comb(N,2)*pp)
    return blocks,childcount,N
def main(pilot):
    global deadline
    start=time.perf_counter();deadline=start+(60 if pilot else 120);fixtures=0;blocks=0;children=0;maxN=0
    for n in ([1] if pilot else [1,2]):
        for mask in range(1<<(1<<n)):
            for t in [1,2]:
                for b in [1,2,3]:
                    q,c,N=fixture(seedvals(n,mask),n,t,b);fixtures+=1;blocks+=q;children+=c;maxN=max(maxN,N)
    out={'helper_version':'A002-growing-block-v1','pilot':pilot,'fixtures':fixtures,'actual_roots':2*fixtures,'blocks':blocks,'physical_child_assignments':children,'exact_assertions':checks,'failures':0,'seconds':time.perf_counter()-start,'max_materialized_dimension':maxN,'arithmetic':'integer truth tables/normalized signed FWHT, Fraction physical edge influence and fourth-moment collisions, formal rational prime-log entropy identities; no floating sign','memory':'peak not measured; frozen estimate100MB'}
    (R/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
