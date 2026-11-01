"""A096 selective-frontier checker v1; stdlib, exact fractions and log intervals."""
import argparse, functools, hashlib, itertools, json, time
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
COUNT=0
POSITIVE_RESETS=0
WITNESS=None
def ck(x):
    global COUNT
    COUNT+=1
    if not x: raise AssertionError(COUNT)
def dump(name,x):
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

@functools.lru_cache(None)
def lg(q):
    """Exact enclosure of log2(q), 18 atanh terms after binary reduction."""
    q=F(q)
    if q==1: return F(0),F(0)
    if q<=0: raise ValueError(q)
    k=0
    while q<1: q*=2; k-=1
    while q>=2: q/=2; k+=1
    def ln(z):
        x=(z-1)/(z+1)
        lo=2*sum((x**(2*j+1)/F(2*j+1) for j in range(18)),F(0))
        er=2*x**37/(37*(1-x*x))
        return lo,lo+er
    a,b=ln(q); u,v=ln(F(2))
    return F(k)+a/v,F(k)+b/u

def add(x,y): return x[0]+y[0],x[1]+y[1]
def scale(a,x): return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def ce(p,q):
    z=(F(0),F(0))
    for u,v in zip(p,q):
        if u:
            ck(v>0)
            z=add(z,scale(-u,lg(v)))
    return z
def spectrum(f):
    x=[F(v) for v in f]; n=len(x)
    h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                a,b=x[j],x[j+h]; x[j],x[j+h]=a+b,a-b
        h*=2
    return [v/n for v in x]
def law(f): return [v*v for v in spectrum(f)]
def marginal(q,j):
    ans=[]
    for k in range(len(q)//2):
        z=(k&((1<<j)-1))|((k>>j)<<(j+1))
        ans.append(q[z]+q[z|(1<<j)])
    return ans
def restrict(f,j,outcome):
    ans=[]
    for k in range(len(f)//2):
        z=(k&((1<<j)-1))|((k>>j)<<(j+1))|(outcome<<j)
        ans.append(f[z])
    return ans
def erase(p,j):
    v=(F(0),F(0))
    for k in range(len(p)//2):
        z=(k&((1<<j)-1))|((k>>j)<<(j+1))
        a,b=p[z],p[z|(1<<j)]; t=a+b
        if t:
            v=add(v,scale(t,lg(t)))
            if a: v=add(v,scale(-a,lg(a)))
            if b: v=add(v,scale(-b,lg(b)))
    return v
def calibrate(q,m):
    if m==1: return [F(1)]+[F(0)]*(len(q)-1)
    ck(q[0]<1)
    return [m]+[v*(1-m)/(1-q[0]) for v in q[1:]]
def reference(p,mode):
    m=p[0]; N=len(p)
    if m==1: return p[:]
    if mode==0: return p[:]
    weights=[F(i+1 if mode==1 else (N*N if i==N-1 else 1)) for i in range(1,N)]
    z=sum(weights)
    return [m]+[(1-m)*w/z for w in weights]

def policy(ids,path,kind):
    # Fixed, not selected by numerical sign. Three genuinely asymmetric trees.
    if not ids: return None
    depth=len(path)
    if kind==0:
        return ids[0] if depth==0 else None
    if kind==1:
        return ids[-1] if depth<2 else None
    if depth==0: return ids[-1]
    if depth==1 and path[-1]==1: return ids[0]
    return None

def tree(f,D,S,Q,ids,path,kind,mask,m,L):
    global POSITIVE_RESETS,WITNESS
    p=law(f); jlabel=policy(ids,path,kind)
    if jlabel is None:
        fresh=(sum(path)+len(path)+mask)%3!=0
        ref=calibrate(S,p[0]) if fresh else Q
        ck(sum(ref)==1)
        ck(all(a>=b for a,b in zip(S,D)))
        u=D[0]-m
        ck(u>=0 and u<=1-m)
        ck(Q[0]>=m) # root floor, independently checked, survives marginalization
        val=ce(p,ref)
        if fresh:
            oldcost=ce(p,Q)
            if val[0]>oldcost[1]:
                POSITIVE_RESETS+=1
                if WITNESS is None:
                    WITNESS={'leaf_function':f,'path':path,'source_marginal':list(map(str,S)),'old_reference':list(map(str,Q)),'new_reference':list(map(str,ref)),'strict_signed_cost_lower_bound':str(val[0]-oldcost[1])}
        penalty=F(0) if fresh else (1-m)+m*(1-p[0])
        return val,penalty,int(fresh),int(not fresh),int(bool(not fresh and p[0]<1))
    j=ids.index(jlabel); rest=ids[:j]+ids[j+1:]
    mp=marginal(p,j)
    childs=[law(restrict(f,j,b)) for b in (0,1)]
    ck(all((x+y)/2==z for x,y,z in zip(*childs,mp)))
    results=[tree(restrict(f,j,b),marginal(D,j),marginal(S,j),marginal(Q,j),rest,path+(b,),kind,mask,m,L) for b in (0,1)]
    value=erase(p,j)
    for t in results: value=add(value,scale(F(1,2),t[0]))
    return value,(results[0][1]+results[1][1])/2,sum(x[2] for x in results),sum(x[3] for x in results),sum(x[4] for x in results)

def check_root(f,R,Q,gamma,kind,mask):
    p=law(f); m=p[0]
    D=[r if z else F(0) for r,z in zip(R,p)]
    ck(D[0]==m and sum(D)<=1 and sum(Q)==1)
    ck(Q[0]>=m and all(q>=gamma*d for q,d in zip(Q[1:],D[1:])))
    L=scale(-1,lg(gamma))
    cost,pen,nf,no,nonconst=tree(f,D,R,Q,list(range(len(f).bit_length()-1)),(),kind,mask,m,L)
    ck(pen<=1-m*m)
    bound=add(ce(p,D),scale(pen,L))
    ck(cost[1]<=bound[0])
    return nf,no,nonconst

def abstract(pilot):
    roots=policies=nonconstant_old=0
    n=2 if pilot else 3
    for bits in range(1<<(1<<n)):
        f=[1 if (bits>>i)&1 else -1 for i in range(1<<n)]
        p=law(f); m=p[0]
        for mode in (0,1,2):
            R=reference(p,mode)
            D=[r if z else F(0) for r,z in zip(R,p)]
            for gamma in (F(1,2),F(1,4)):
                # Delete all reference ghosts except one adversarial destination.
                Q=[gamma*d for d in D]; Q[0]=m
                destination=next((i for i in range(1,len(p)) if not p[i]),len(p)-1)
                Q[destination]+=1-sum(Q)
                roots+=1
                for kind in range(3):
                    for mask in (0,1):
                        nf,no,nc=check_root(f,R,Q,gamma,kind,mask)
                        policies+=1; nonconstant_old+=nc
    return {'dimension':n,'all_boolean_truth_tables':1<<(1<<n),'source_instances':roots,'tree_and_frontier_policies':policies,'nonconstant_old_terminal_occurrences':nonconstant_old}

def negative_cell(pilot):
    cases=policies=0; old_nonconstant=0
    dom=itertools.product((1,2) if pilot else (1,2,3),(0,1),(1,2) if pilot else (1,2,3),range(3))
    for a,b,r,mode in dom:
        if b+r<2: continue
        n=a+b; N=1<<(n+r); s=F(1,1<<a); e=F(2,N); h=e/s
        g=[-1 if k&((1<<a)-1)==0 else 1 for k in range(1<<n)]
        source=reference(law(g),mode)
        edited=[(-1 if k&((1<<a)-1)==0 else 1)+(2 if k==0 else 0) for k in range(N)]
        ck(set(edited)<={-1,1})
        pf=law(edited)
        Rp=[(1-h)*v+(h*(1-2*s) if i==0 else 0)+2*e/F(1<<n) for i,v in enumerate(source)]
        ck(sum(Rp)==1)
        data=[sum(pf[t+(u<<n)] for u in range(1<<r)) for t in range(1<<n)]
        Q=[Rp[k&((1<<n)-1)]*pf[k]/data[k&((1<<n)-1)] for k in range(N)]
        ck(sum(Q)==1)
        for create in (([a] if b else [])+([n] if r>=2 else [])):
            exitf=restrict(edited,create,1)
            old=marginal(Q,create)
            S=[source[k] if k<(1<<n) else F(0) for k in range(N)]
            S=marginal(S,create)
            gamma=(1-h)/(1+h/2)
            # General theorem uses c at the pre-creation source, not enlarged ghost cost.
            p0=law(g); D0=[v if z else F(0) for v,z in zip(source,p0)]
            D0=D0+[F(0)]*(N-(1<<n)); D=marginal(D0,create)
            ck(D[0]==(1-2*s)**2)
            ck(old[0]>=D[0] and all(q>=gamma*d for q,d in zip(old[1:],D[1:])))
            cases+=1
            for kind in range(3):
                for mask in (0,1):
                    L=scale(-1,lg(gamma)); m=D[0]
                    cost,pen,nf,no,nc=tree(exitf,D,S,old,list(range(n+r-1)),(),kind,mask,m,L)
                    bound=add(ce(law(g),source),scale(pen,L))
                    ck(cost[1]<=bound[0])
                    ck((1-m*m)*L[1]<22*e)
                    ck(5*a*(2**(b+r))-13*(b+r-1)>=7)
                    policies+=1; old_nonconstant+=nc
    return {'creating_exit_instances':cases,'tree_and_frontier_policies':policies,'nonconstant_old_terminal_occurrences':old_nonconstant}

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
    start=time.perf_counter()
    result={'helper':'A096-selective-frontier-v1','arithmetic':'exact Fraction plus 18-term atanh rational log2 enclosures','abstract':abstract(args.pilot),'negative_cell':negative_cell(args.pilot),'assertions':COUNT,'positive_signed_reset_occurrences':POSITIVE_RESETS,'runtime_seconds':time.perf_counter()-start,'status':'PASS','independent_review':'PENDING'}
    dump('PILOT.json' if args.pilot else 'VALIDATION.json',result)
    if WITNESS is not None: dump('POSITIVE_RESET_WITNESS.json',WITNESS)
    print(json.dumps(result))
